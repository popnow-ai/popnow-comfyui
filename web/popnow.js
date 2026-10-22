// PopNow for ComfyUI: the settings panel entries and the credit price badge on every model node.
import { app } from "../../scripts/app.js";
import { api } from "../../scripts/api.js";

const KEY_SETTING = "PopNow.ApiKey";
const LIMIT_SETTING = "PopNow.MaxCreditsPerRun";
const MASK = "•".repeat(4);
const NODE_PREFIX = "PopNow_";
const MODEL_DEFAULT = "model default";
const UNIT_SHORT = { second: "s", image: "image", run: "run", "1k characters": "1k chars", "1k tokens": "1k tokens" };

let prices = null;

function toast(severity, summary, detail, life = 6000) {
  try {
    app.extensionManager.toast.add({ severity, summary, detail, life });
  } catch {
    console[severity === "error" ? "error" : "log"](`[PopNow] ${summary}: ${detail ?? ""}`);
  }
}

function setSetting(id, value) {
  try {
    return app.extensionManager.setting.set(id, value);
  } catch {
    return app.ui?.settings?.setSettingValue?.(id, value);
  }
}

function getSetting(id) {
  try {
    return app.extensionManager.setting.get(id);
  } catch {
    return app.ui?.settings?.getSettingValue?.(id);
  }
}

// The settings field only ever keeps a masked marker. The key itself lives in the ComfyUI user
// directory on the server, never in comfy.settings.json and never in a workflow.
function maskedLabel(status) {
  if (!status?.configured) return "";
  const where = status.keySource === "env" ? "from POPNOW_API_KEY" : "saved";
  return `${MASK} ${status.keyHint.replace("...", "")} (${where})`;
}

async function readJson(response) {
  try {
    return await response.json();
  } catch {
    return {};
  }
}

async function onKeyChange(value, previous) {
  // The settings store calls this once on load with no previous value; that is not an edit.
  if (previous === undefined || value === previous) return;
  const text = String(value ?? "").trim();
  if (text.startsWith(MASK)) return;
  if (!text) {
    const response = await api.fetchApi("/popnow/api-key", { method: "DELETE" });
    const status = await readJson(response);
    if (status.configured) {
      toast("warn", "PopNow", "The key set through POPNOW_API_KEY stays in use.");
      setSetting(KEY_SETTING, maskedLabel(status));
    } else {
      toast("info", "PopNow", "API key removed.");
    }
    return;
  }
  const response = await api.fetchApi("/popnow/api-key", {
    method: "POST",
    headers: { "Content-Type": "application/json" },
    body: JSON.stringify({ apiKey: text }),
  });
  const result = await readJson(response);
  if (!response.ok || !result.ok) {
    toast("error", "PopNow key not saved", result.message || `HTTP ${response.status}`);
    // Whatever key was in use before is still in use; show that rather than an empty field.
    setSetting(KEY_SETTING, String(previous ?? "").startsWith(MASK) ? previous : "");
    return;
  }
  setSetting(KEY_SETTING, maskedLabel(result));
  const credits = result.balance?.availableCredits;
  toast(
    "success",
    "PopNow connected",
    credits !== undefined && credits !== null
      ? `Available: ${credits} credits`
      : "Key saved. It could not be checked right now.",
  );
  const refresh = result.catalogRefresh;
  if (refresh?.restartNeeded) {
    const added = refresh.added?.length ?? 0;
    toast(
      "info",
      "PopNow",
      added > 0
        ? `Restart ComfyUI to load the full model list (${added} more models).`
        : "Restart ComfyUI to load the latest model list.",
      12000,
    );
  }
}

async function onLimitChange(value) {
  const amount = Math.max(0, Math.floor(Number(value) || 0));
  const response = await api.fetchApi("/popnow/settings", {
    method: "POST",
    headers: { "Content-Type": "application/json" },
    body: JSON.stringify({ maxCreditsPerRun: amount }),
  });
  if (!response.ok) {
    const result = await readJson(response);
    toast("error", "PopNow", result.message || "Could not save the spending limit.");
  }
}

// -- Price badge -----------------------------------------------------------

function keyValue(value) {
  if (typeof value === "boolean") return value ? "true" : "false";
  if (typeof value === "number" && Number.isInteger(value)) return String(value);
  return String(value);
}

// Mirrors pricing.current_values and pricing.match_rule in Python.
function currentValues(spec, node) {
  const widgets = Object.fromEntries((node.widgets ?? []).map((w) => [w.name, w.value]));
  const values = {};
  for (const name of spec.fields ?? []) {
    const target = spec.presence?.[name];
    if (target !== undefined) {
      const connected = (node.inputs ?? []).some(
        (input) => input.link != null && (input.name === target || input.name.startsWith(`${target}.`)),
      );
      values[name] = keyValue(connected);
    } else if (name in widgets && widgets[name] !== MODEL_DEFAULT && widgets[name] !== -1) {
      const shown = keyValue(widgets[name]);
      values[name] = spec.labels?.[name]?.[shown] ?? shown;
    } else if (spec.defaults && name in spec.defaults) {
      values[name] = spec.defaults[name];
    }
  }
  return values;
}

function matchRule(spec, node) {
  const rules = spec.rules ?? [];
  if (!rules.length) return spec.from;
  const values = currentValues(spec, node);
  let best = null;
  for (const rule of rules) {
    const entries = Object.entries(rule.when);
    if (entries.every(([name, value]) => values[name] === value)) {
      if (!best || entries.length > Object.keys(best.when).length) best = rule;
    }
  }
  return best ? best.credits : null;
}

function priceText(node) {
  const spec = prices?.[node.comfyClass ?? node.type];
  if (!spec) return "";
  const unit = UNIT_SHORT[spec.unit] ?? spec.unit;
  const credits = matchRule(spec, node);
  if (credits !== null && credits !== undefined) return `${spec.approximate ? "~" : ""}${credits} cr/${unit}`;
  return `from ${spec.from} cr/${unit}`;
}

function attachBadge(node) {
  const type = node.comfyClass ?? node.type ?? "";
  if (!type.startsWith(NODE_PREFIX) || node.__popnowBadge) return;
  const Badge = window.LGraphBadge;
  if (!Badge || !Array.isArray(node.badges)) return;
  node.__popnowBadge = true;
  node.badges.push(() => new Badge({ text: priceText(node), fgColor: "#FFF4E8", bgColor: "#B23D1A" }));
}

app.registerExtension({
  name: "PopNow.Comfy",
  settings: [
    {
      id: KEY_SETTING,
      category: ["PopNow", "Account", "API key"],
      name: "API key",
      tooltip:
        "Paste a key from popnow.ai/api/console/keys. It is stored in the ComfyUI user folder on " +
        "this machine, never in workflows or image metadata. Clear the field to remove it.",
      type: "text",
      defaultValue: "",
      attrs: { placeholder: "sk-popnow-..." },
      onChange: (value, previous) => {
        onKeyChange(value, previous).catch((error) => toast("error", "PopNow", String(error)));
      },
    },
    {
      id: LIMIT_SETTING,
      category: ["PopNow", "Spending", "Max credits per run"],
      name: "Max credits per run (0 = no limit)",
      tooltip:
        "A node whose quote is above this many credits stops before anything is held. " +
        "1 credit = $0.001. The quote is the most a run can cost.",
      type: "number",
      defaultValue: 0,
      attrs: { min: 0, step: 10 },
      onChange: (value) => {
        onLimitChange(value).catch((error) => toast("error", "PopNow", String(error)));
      },
    },
  ],

  async setup() {
    try {
      const response = await api.fetchApi("/popnow/prices");
      prices = await readJson(response);
      app.graph?.setDirtyCanvas?.(true, true);
    } catch (error) {
      console.warn("[PopNow] price list unavailable", error);
    }
    try {
      const status = await readJson(await api.fetchApi("/popnow/status"));
      const shown = String(getSetting(KEY_SETTING) ?? "");
      const expected = maskedLabel(status);
      if (shown !== expected && (status.configured || shown.startsWith(MASK))) {
        await setSetting(KEY_SETTING, expected);
      }
    } catch (error) {
      console.warn("[PopNow] status unavailable", error);
    }
  },

  nodeCreated(node) {
    attachBadge(node);
  },

  loadedGraphNode(node) {
    attachBadge(node);
  },
});
