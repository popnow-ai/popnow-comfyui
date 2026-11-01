"""Price tables for the badge each model node shows.

The PopNow API prices every model in US dollars, paid from the API balance. Each catalog entry
carries ``usd = {unit, perUnit, rules, currency}``: amounts are exact decimal strings, ``unit`` is
how the price scales (``per_image``, ``per_second``...), ``perUnit`` is the starting price, and
each rule applies when the request matches its ``when`` values. ``"*"`` in ``when`` stands for the
one field that sets the tier (the single entry of the schema's ``x-pricing.variantFields``).

Catalog copies saved by version 0.1 only carry the deprecated ``credits`` table (1 credit =
$0.001). It is converted to the same USD shape, so an old cache still shows a price.

The badge is a rate, never a total: "$0.037/s", not "$0.185". A total depends on things the node
cannot know before it runs (how long an uploaded clip is, how many images come back), and an
estimate shown as a fact is worse than none. The authoritative amount is the quote taken when the
node runs (``maxChargeUsd``), and the charged amount is printed on the node afterwards.

Matching: a value missing from the node takes its schema default, a field listed in
``x-pricing.presenceFields`` is ``true`` when the input it names has something connected, and
when several rules match, the one naming the most fields wins (a rule with an empty ``when``
is the fallback).

Money is handled as ``Decimal`` or decimal strings throughout, never as binary floats.
"""

from __future__ import annotations

from decimal import ROUND_HALF_UP, Decimal, InvalidOperation
from typing import Any

UNIT_LABELS = {
    "per_second": "second",
    "per_image": "image",
    "per_request": "run",
    "per_1k_characters": "1k characters",
    "per_1k_tokens": "1k tokens",
}
# Deprecated: the fixed rate of the legacy credit projection, used only to read old catalogs and settings.
CREDIT_USD = Decimal("0.001")
# USD amounts carry at most nine decimal places.
USD_STEP = Decimal("0.000000001")
# Keys of a rate table that hold money (the rest are units, conditions and thresholds).
MONEY_KEYS = ("perUnit", "input", "output", "cachedInput", "cacheWrite")


def _decimal(value: Any) -> Decimal | None:
    if isinstance(value, bool) or value is None:
        return None
    try:
        amount = Decimal(str(value).strip())
    except (InvalidOperation, ValueError):
        return None
    return amount if amount.is_finite() else None


def decimal_text(value: Any) -> str:
    """5.55, 8, 0.037: as many digits as the amount has, no trailing zeros, never an exponent."""
    amount = _decimal(value)
    if amount is None:
        return str(value)
    if amount == 0:
        return "0"
    return format(amount.normalize(), "f")


def parse_usd(value: Any) -> Decimal | None:
    """An exact USD amount from a decimal string (or number), or None when it is not one."""
    return _decimal(value)


def usd_text(value: Any) -> str:
    """How a USD amount is shown: $0.037, $0.10, $1.00. Every significant digit is kept."""
    amount = _decimal(value)
    if amount is None:
        return ""
    text = decimal_text(amount)
    sign = ""
    if text.startswith("-"):
        sign, text = "-", text[1:]
    if "." in text:
        whole, fraction = text.split(".", 1)
        text = f"{whole}.{fraction.ljust(2, '0')}"
    else:
        text = f"{text}.00"
    return f"{sign}${text}"


def credits_to_usd(value: Any) -> str | None:
    """Deprecated credit amount (1 credit = $0.001) as an exact USD decimal string."""
    amount = _decimal(value)
    if amount is None:
        return None
    return decimal_text((amount * CREDIT_USD).quantize(USD_STEP, rounding=ROUND_HALF_UP))


def _convert_money(table: dict[str, Any]) -> dict[str, Any]:
    converted: dict[str, Any] = {}
    for key, value in table.items():
        if key in MONEY_KEYS:
            usd = credits_to_usd(value)
            if usd is not None:
                converted[key] = usd
        elif key in ("rules", "assets") and isinstance(value, list):
            converted[key] = [_convert_money(item) if isinstance(item, dict) else item for item in value]
        elif key == "longContext" and isinstance(value, dict):
            converted[key] = _convert_money(value)
        else:
            converted[key] = value
    return converted


def usd_from_credits(table: dict[str, Any]) -> dict[str, Any]:
    """The USD shape of a deprecated ``credits`` rate table: same units and rules, amounts in dollars."""
    converted = _convert_money(table)
    converted["currency"] = "USD"
    return converted


def usd_rates(model: dict[str, Any]) -> dict[str, Any] | None:
    """The model's USD rate table: ``usd`` when the catalog has it, else the converted ``credits``."""
    usd = model.get("usd")
    if isinstance(usd, dict):
        return usd
    credits = model.get("credits")
    if isinstance(credits, dict):
        return usd_from_credits(credits)
    return None


def format_credits(value: Any) -> str:
    """Deprecated: prices are in USD now; use ``decimal_text`` or ``usd_text``."""
    return decimal_text(value)


def format_usd(credits: Any) -> str:
    """Deprecated: the dollar text of a credit amount (37 credits -> $0.037). Use ``usd_text``."""
    return usd_text(credits_to_usd(credits))


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
    """The badge table for a model node: USD rates per unit, keyed by the settings they apply to."""
    rates = usd_rates(model)
    if not isinstance(rates, dict):
        return None
    unit = str(rates.get("unit") or "")
    start = _decimal(rates.get("perUnit"))
    schema = model.get("inputSchema") or {}
    x_pricing = schema.get("x-pricing") or {}
    properties = schema.get("properties") or {}
    fields = [str(f) for f in x_pricing.get("variantFields") or []]
    star = fields[0] if len(fields) == 1 else None
    rules: list[dict[str, Any]] = []
    lowest = start
    for rule in rates.get("rules") or []:
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
        rules.append({"when": when, "usd": decimal_text(amount)})
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
        "currency": "USD",
        "unit": UNIT_LABELS.get(unit, unit.replace("per_", "").replace("_", " ")),
        "fields": names,
        "defaults": defaults,
        "presence": presence,
        "rules": rules,
        "from": decimal_text(lowest),
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
    """The USD per unit for these settings (a decimal string), or None when no rule matches.

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
    return best["usd"] if best else None


def describe_price(badge: dict[str, Any] | None) -> str:
    if not badge:
        return ""
    prefix = "about " if badge.get("approximate") else ""
    text = f"{prefix}{usd_text(badge['from'])} per {badge['unit']}."
    if len({rule["usd"] for rule in badge.get("rules") or []}) > 1:
        return f"From {text}"
    return text[0].upper() + text[1:]
