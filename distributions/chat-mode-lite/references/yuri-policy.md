# Yuri identity, scope and preferences

Reference revision: `lite-core/A1.1` · Policy: `yuri-policy/1.0`

Apply [CORE.md](../instructions/CORE.md)'s authority order. This reference expands the core; it does not override the user's applicable decisions or host rules.

## Identity and scope

The default `author_defined_inclusive` recognizes author-defined women, including virtual and nonhuman women. Womanhood is not determined by a name, appearance, body, occupation or personality stereotype. Keep source identity evidence separate from the adapted portrayal.

Use adult main characters. In `main_cast`, consider main/player roles while preserving a supplied player persona; scope selection is not permission to alter that persona. Background identities remain unchanged. In `named_characters`, select exactly the resolved `selected_character_ids`; `entire_cast` explicitly broadens selection to backgrounds. Apply exclusions without losing their source records. Unknown IDs, overlapping selection/exclusion or ambiguous roles require resolution before affected edits. Stable internal IDs are assistant-maintained labels, not fabricated source identifiers.

For selected targets, review the adult-woman requirement and any explicit human/custom criteria. `human_explicitly_female` additionally requires explicitly human women. `custom` requires nonempty `custom_criteria` and a specific reasoned review of each selected target; other identity policies leave that field empty. Do not certify free-text compliance from a checkbox.

Preserve source ages and uncertainty. Known minors are outside this adult transformation-target route; do not silently age them up or claim the target scope is satisfied. Explain the affected limitation and resolve the scope conflict. For unknown ages, an adult fictional choice must be labeled as an addition. Newly invented main/player characters are adults; do not invent source evidence for them. Keep prose non-graphic, do not sexualize minors, and do not add erotic detail to conflicting anatomy. Posts about real people remain supplied accounts and fictional adaptations, not verified biographies.

## Optional preference vocabulary

[preferences.json](../templates/preferences.json) uses Full's `schema_version: 1.0` vocabulary for semantic compatibility; Lite does not run Full's validator. It is a sample, not evidence of adopted preferences or completed review. Accept ordinary language and maintain the profile yourself. Its `status: ready` is declarative. Keep the human-readable revision, actual authorizations and overrides in the conversational record/checkpoint rather than adding unsupported keys to a Full profile.

| Field | Meaning |
| --- | --- |
| `definition.womanhood_policy`, `custom_criteria` | Inclusive default, explicitly human women, or reviewed custom criteria as above. |
| `definition.allowed_dynamics` | Nonempty subset of `romance`, `friendship`, `neutral`, `rivalry`, `hostility`, `kinship`; permits outcomes without requiring any of them. |
| `transformation.scope`, selected/excluded IDs | `main_cast`, `named_characters` or `entire_cast`; selected IDs are used only for `named_characters`. |
| `transformation.player_persona` | `preserve`, or `explicitly_authorized` with the actual scoped user instruction; neither delegates current player behavior. |
| `transformation.protected_anchors` | Story/identity constraints to review individually in the actual output. |
| `relationships` | Outcome policy, pairing targets and uncertainty safeguards; see [relationship rules](relationship-rules.md). |
| `workflow` | `minimal-change`, `pairing-focused`, `character-focused` or `world-focused`; a creative emphasis, not a fifth workflow or broader edit permission. |
| `narrative_language` | Requested prose language or `preserve_source`; interaction language is resolved separately in CORE. |

Keep `infer_gender_from_stereotypes: false`, `infer_romance_from_hostility: false` and `preserve_uncertainty: true`. Unknown fields, malformed values and incompatible policies must be reported, not discarded. Missing optional fields use Full's published defaults: all six dynamics, empty selections/exclusions/anchors/pairings, preserved uncertainty and `minimal-change`. Do not fill missing required saved-profile decisions from the sample without acknowledging the gap. Fresh tasks without a profile use the core defaults without a questionnaire. Explain unsupported requests and continue unaffected work.

## Contextual names

Assess the name's owner, culture, language, era, setting and confirmed user wishes. A masculine-sounding name, alias or nonhuman designation can fit a woman. Do not invent etymology. Offer two or three contextual alternatives plus keeping the original only when useful; retain the current name provisionally and keep drafting. A delegated rename needs no extra confirmation. Preserve settled choices, source names/quotes and IDs. Apply a chosen output name consistently in authorized prose and worldbook references without replacing technical strings. The real user is never renamed.

Derived from Full's preference, creator and name-review guidance at the A1 base. Attribution and applicable terms are retained in [CORE provenance](../instructions/CORE.md#provenance-and-a1-differences); this condensation does not change them.
