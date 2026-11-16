# Illustration — one inspected narrative edit

**Synthetic illustration, not a conversion trial, observed model response or import-ready card.** Authored for `lite-card-workflows/A2.1` under `yuri-policy/1.0`. This complete small JSON document is a card-shaped teaching fixture, not a claim of a format-complete export or a T1 result. See [ADAPTATION.md](../instructions/ADAPTATION.md) and [card output](../references/card-output.md).

## Illustrative input and authority

Target: `illustration-input/r1`, supplied below in full. Illustrative request: “Make Lin an adult woman. Keep the name and all other facts; change only the description's identity wording. Preserve the fenced template and all settings.” No player behavior, relationship outcome or technical change is authorized. The source age remains 30; the fictional identity change does not rewrite the evidence of the original wording.

```json
{
  "spec": "chara_card_v2",
  "spec_version": "2.0",
  "data": {
    "name": "Lin",
    "character_version": "illustration-input/r1",
    "description": "Lin is a 30-year-old man who restores harbor maps.\n```text\n{{keep_me}}\n```",
    "first_mes": "Lin points to a blank chart. \"Which coast shall we study?\"",
    "alternate_greetings": [],
    "system_prompt": "<% preserve_this_token(); %>",
    "character_book": {
      "scan_depth": 2,
      "recursive_scanning": false,
      "entries": [{"id": 41, "keys": ["harbor charts"], "content": "Fragile originals stay on their supports.", "enabled": true, "insertion_order": 7}]
    },
    "extensions": {"opaque": {"keep": [2, 1]}, "regex_scripts": [{"id": "rx-1", "findRegex": "Lin", "replaceString": "Lin"}]}
  }
}
```

The intended narrative edit is only `/data/description`, not scripts or worldbook configuration. The greeting contains no gendered identity wording or prescribed player reply. Lin remains Lin; changing the source name or searching/replacing every occurrence is unnecessary. The fixed code span inside the description remains identical.

## Candidate forms — no winner selected

**A — complete JSON:** would reproduce the entire supplied document with only the authorized description string changed. No complete replacement artifact is supplied or claimed applied here. Evaluation would require all other values and structure to survive, complete delivery, and inspection of the actual assembled result.

**B — field replacement:** the target is `/data/description` in `illustration-input/r1`. The following are JSON string literals for editing JSON text, not quoted strings to paste blindly into an unknown UI field. A field editor would need decoded text. Compare the expected old value before replacing; stop if it differs.

Expected old value:

```json
"Lin is a 30-year-old man who restores harbor maps.\n```text\n{{keep_me}}\n```"
```

Proposed replacement:

```json
"Lin is a 30-year-old woman who restores harbor maps.\n```text\n{{keep_me}}\n```"
```

**C — JSON Patch:** an alternative representation of the same proposed edit. These guards check known identity/revision/value fields; they are not a full-document fingerprint. An available practical application route and final artifact would still need evaluation. This patch is not applied here and is not an importable card.

```json
[
  {"op": "test", "path": "/data/name", "value": "Lin"},
  {"op": "test", "path": "/data/character_version", "value": "illustration-input/r1"},
  {"op": "test", "path": "/data/description", "value": "Lin is a 30-year-old man who restores harbor maps.\n```text\n{{keep_me}}\n```"},
  {"op": "replace", "path": "/data/description", "value": "Lin is a 30-year-old woman who restores harbor maps.\n```text\n{{keep_me}}\n```"}
]
```

If the real description is already changed, or the revision/path/value differs, this proposal must be reconciled with the available current text instead of reapplied blindly. Preserve the original and any failed working copy separately.

## Illustrative record and limits

The assistant would record `E1` as the source main character, the description's original claim at `/data/description`, and decision `D1` as the requested fictional identity edit. Source fact and adaptation remain distinct. Use the existing [adaptation record](../templates/adaptation-record.md) for the actual user instruction, preferences, protected anchors, draft/application status and observed checks; the hypothetical request above is not real consent for another card.

Protected scope includes the embedded template, greeting, name, version, worldbook ID/order/settings and unknown extension values. No array index is inferred, technical token executed or relationship change proposed. The constructed change specification demonstrates scope; it provides no observed preservation, application, import or roleplay result.

If only a real card's description were accessible, the same local edit could be proposed with those limits, but complete-document inspection and whole-card preservation would remain unverified. Do not recreate the missing fields from this fixture. At a real batch end/pause/handoff, use all twelve groups of `yuri-lite/checkpoint/v1` in the [continuity record](../templates/continuity-record.md); do not treat these illustration notes as a checkpoint.

Attribution and applicable terms: [CORE provenance](../instructions/CORE.md#provenance-and-a1-differences).

Required Notice: Copyright 2026 LiarMTTT
