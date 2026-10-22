"""Price tables for the badge each model node shows.

PopNow prices every model in credits (1 credit = $0.001). Each catalog entry carries
``credits = {unit, perUnit, rules}``: ``unit`` is how the price scales (``per_image``,
``per_second``...), ``perUnit`` is the starting price, and each rule applies when the request
matches its ``when`` values. ``"*"`` in ``when`` stands for the one field that sets the tier
(the single entry of the schema's ``x-pricing.variantFields``).

The badge is a rate, never a total: "37 cr/s", not "185 credits". A total depends on things
the node cannot know before it runs (how long an uploaded clip is, how many images come back),
and an estimate shown as a fact is worse than none. The authoritative amount is the quote taken
when the node runs, and the charged amount is printed on the node afterwards.

Matching: a value missing from the node takes its schema default, a field listed in
``x-pricing.presenceFields`` is ``true`` when the input it names has something connected, and
when several rules match, the one naming the most fields wins (a rule with an empty ``when``
is the fallback).
"""

from __future__ import annotations

from decimal import Decimal, InvalidOperation
from typing import Any

UNIT_LABELS = {
    "per_second": "second",
    "per_image": "image",
    "per_request": "run",
    "per_1k_characters": "1k characters",
    "per_1k_tokens": "1k tokens",
}
CREDIT_USD = Decimal("0.001")


def _decimal(value: Any) -> Decimal | None:
    if isinstance(value, bool):
        return None
    try:
        return Decimal(str(value))
    except (InvalidOperation, ValueError):
        return None


def format_credits(value: Any) -> str:
    """5.55, 8, 0.27: as many digits as the price has, no trailing zeros."""
    amount = _decimal(value)
    if amount is None:
        return str(value)
    text = format(amount.normalize(), "f")
    return text


def format_usd(credits: Any) -> str:
    """The dollar equivalent of a credit amount: 37 credits -> $0.037."""
    amount = _decimal(credits)
    if amount is None:
        return ""
    text = format((amount * CREDIT_USD).normalize(), "f")
    if "." in text:
        whole, fraction = text.split(".", 1)
        text = f"{whole}.{fraction.ljust(2, '0')}"
    else:
        text = f"{text}.00"
    return f"${text}"


def key_value(value: Any) -> str:
    """How a value appears in a rule's ``when``: booleans lower-case, whole numbers bare."""
    if isinstance(value, bool):
        return "true" if value else "false"
    if isinstance(value, float) and value.is_integer():
        return str(int(value))
    return str(value)


def _resolve_when(when: dict[str, Any], star: str | None) -> dict[str, str] | None:
    """Spell out ``"*"`` as the field it stands for; None when it cannot be resolved."""
    resolved: dict[str, str] = {}
    for name, value in when.items():
        if name == "*":
            if star is None:
                return None
            name = star
        resolved[str(name)] = key_value(value)
    return resolved


def badge_for(model: dict[str, Any]) -> dict[str, Any] | None:
    credits = model.get("credits")
    if not isinstance(credits, dict):
        return None
    unit = str(credits.get("unit") or "")
    start = _decimal(credits.get("perUnit"))
    schema = model.get("inputSchema") or {}
    x_pricing = schema.get("x-pricing") or {}
    properties = schema.get("properties") or {}
    fields = [str(f) for f in x_pricing.get("variantFields") or []]
    star = fields[0] if len(fields) == 1 else None
    rules: list[dict[str, Any]] = []
    lowest = start
    for rule in credits.get("rules") or []:
        if not isinstance(rule, dict) or not isinstance(rule.get("when"), dict):
            continue
        if str(rule.get("unit") or unit) != unit:
            continue  # a rule in another unit cannot share one badge
        amount = _decimal(rule.get("perUnit"))
        if amount is None:
            continue
        when = _resolve_when(rule["when"], star)
        if when is None:
            continue
        rules.append({"when": when, "credits": format_credits(amount)})
        if lowest is None or amount < lowest:
            lowest = amount
    if lowest is None:
        return None
    names = sorted({name for rule in rules for name in rule["when"]} | set(fields))
    defaults = {
        name: key_value(properties[name]["default"])
        for name in names
        if isinstance(properties.get(name), dict) and "default" in properties[name]
    }
    presence = {str(k): str(v) for k, v in (x_pricing.get("presenceFields") or {}).items()}
    return {
        "unit": UNIT_LABELS.get(unit, unit.replace("per_", "").replace("_", " ")),
        "fields": names,
        "defaults": defaults,
        "presence": presence,
        "rules": rules,
        "from": format_credits(lowest),
        "approximate": x_pricing.get("billingMode") == "formula",
    }


def current_values(badge: dict[str, Any], values: dict[str, Any], connected: set[str]) -> dict[str, str]:
    """The value of each pricing field for this node, as rules spell them."""
    current: dict[str, str] = {}
    for name in badge.get("fields") or []:
        target = (badge.get("presence") or {}).get(name)
        if target is not None:
            current[name] = key_value(target in connected)
        elif name in values and values[name] is not None:
            current[name] = key_value(values[name])
        elif name in (badge.get("defaults") or {}):
            current[name] = badge["defaults"][name]
    return current


def match_rule(badge: dict[str, Any], values: dict[str, Any], connected: set[str]) -> str | None:
    """The per-unit credits for these settings, or None when no rule matches.

    The same rule the JavaScript badge follows; it is kept here so it is tested in one place.
    """
    rules = badge.get("rules") or []
    if not rules:
        return badge.get("from")
    current = current_values(badge, values, connected)
    best: dict[str, Any] | None = None
    for rule in rules:
        when = rule["when"]
        matches = all(current.get(name) == value for name, value in when.items())
        if matches and (best is None or len(when) > len(best["when"])):
            best = rule
    return best["credits"] if best else None


def describe_price(badge: dict[str, Any] | None) -> str:
    if not badge:
        return ""
    prefix = "about " if badge.get("approximate") else ""
    amount = badge["from"]
    text = f"{prefix}{format_credits(amount)} credits ({format_usd(amount)}) per {badge['unit']}."
    if len({rule["credits"] for rule in badge.get("rules") or []}) > 1:
        return f"From {text}"
    return text[0].upper() + text[1:]
