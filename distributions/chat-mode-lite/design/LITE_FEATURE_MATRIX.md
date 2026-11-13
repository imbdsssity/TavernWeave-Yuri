# Yuri Card Workbench Lite — Feature Retention Matrix

**Status:** Proposed Phase 0 scope  
**Baseline:** TavernWeave-Yuri 1.2.0  
**Purpose:** Decide what Lite retains, simplifies, replaces or excludes before workflow migration.

## Decision labels

- **Retain:** Keep the user-facing behavior and essential policy.
- **Simplify:** Preserve the outcome but remove automated or advanced implementation.
- **Replace:** Provide a different conversational mechanism.
- **Exclude:** Do not claim or implement this capability in Lite 0.1.0.
- **Optional:** Use only when the current host demonstrably provides the capability.

## 1. Canonical workflows

| Full capability | Decision | Lite 0.1.0 behavior | Boundary |
|---|---|---|---|
| Original Yuri card creation | Retain | Create from conversation, with delegated creative choices when requested | Text-first; no mandatory research or image tools |
| Existing-card adaptation | Simplify | Read supplied JSON, plan scoped edits, return a patch or complete JSON | No PNG, binary container or lossless round-trip claim |
| Post-to-Yuri-card | Retain / simplify | Adapt supplied post text with source facts separated from inventions | No scraping, automated indexing or evidence backfilling |
| Novel-excerpt-to-Yuri-card | Simplify | Process explicitly supplied TXT/Markdown text or selected chapters | No EPUB extraction; no claim about unseen chapters |
| Saved custom preferences | Retain / simplify | Accept conversational preferences or optional JSON profile | No profile database or mandatory profile file |
| Character/name review | Retain | Offer contextual alternatives and wait for user choice/authorization | No automated name classifier |
| Image adaptation | Optional | Draft prompts and review visible references if host supports images | Image generation and embedding are not required |
| Web research | Optional | Use native browsing only when available and requested/appropriate | No custom crawler or retrieval service |

## 2. Shared Yuri policy and narrative behavior

| Full capability | Decision | Lite treatment |
|---|---|---|
| Inclusive, user-defined eligibility policy | Retain | Same policy semantics; do not infer identity from stereotypes |
| Main-cast transformation | Retain | Preserve background identities by default |
| Relationship outcome policy | Retain | Preserve or rederive only according to user-selected policy and causal evidence |
| Explicit pairing targets | Retain | Apply only when authorized and compatible with declared policy |
| Distinguish romance, friendship, hostility, rivalry and kinship | Retain | Never infer romance merely from hostility or kinship |
| Player persona and agency | Retain | Do not invent player actions, thoughts or replies without authorization |
| Protected anchors | Retain | Track in a concise conversational checklist |
| Source fact / inference / invention separation | Retain | Use compact evidence/adaptation records |
| Profile fingerprint and cryptographic binding | Exclude | State the selected preferences in the conversation/checkpoint; no hash guarantee |
| Programmatic policy enforcement | Replace | Explicit model-facing checklist and final review; describe as conversational review, not machine enforcement |
| Custom-profile schema validation | Simplify | Optional example JSON; unsupported fields are reported, not silently discarded |

## 3. Source evidence and long-input handling

| Full capability | Decision | Lite treatment |
|---|---|---|
| Frozen source snapshots and hashes | Replace | Identify supplied source by title/name and user-provided locator; no cryptographic immutability claim |
| Per-claim quotation/evidence | Retain / simplify | Quote concise relevant passages and label their source location when available |
| Exact quote-offset verification | Exclude | Do not claim programmatic quote validation |
| Source-library indexing and reindexing | Exclude | Keep a compact in-conversation source register |
| Automated backfilling/promotion | Exclude | User supplies and reviews the evidence record; no database write |
| Chapter/section selection | Retain | User explicitly selects or confirms the scope |
| TXT/Markdown reading | Retain | Only content actually available to the model |
| EPUB parsing/spine extraction | Exclude | User may extract text externally and supply it |
| Full-novel processing | Simplify | Process selected, bounded portions and carry forward continuity checkpoints |
| Coverage/gap checking | Replace | State supplied, processed and unprocessed ranges explicitly |
| Batch source conversion | Exclude | One bounded source/workflow at a time in the MVP |

## 4. Existing-card and worldbook operations

| Full capability | Decision | Lite treatment |
|---|---|---|
| JSON card reading | Retain / simplify | Accept supplied JSON within host context limits |
| JSON worldbook reading | Retain / simplify | Edit supplied entries or standalone JSON |
| PNG tEXt/zTXt/iTXt decoding | Exclude | Ask user to provide decoded JSON/text externally |
| PNG repacking and payload parity | Exclude | No embedded-image output |
| Original-byte/document binding | Exclude | No byte-preservation guarantee |
| Pointer-based guarded editing | Replace | Human-readable field/path change plan and optional JSON Patch |
| Unknown-field preservation | Simplify | Preserve visible supplied fields in output where feasible; disclose limits |
| Script/regex edits | Exclude by default | Identify and leave untouched; refer to Full/specialist tools for technical changes |
| Arbitrary schema migration | Exclude | No cross-version conversion claim |
| Folder inventory and component grouping | Exclude | User identifies the target file and related components |
| Worldbook IDs/order/settings | Simplify | Preserve visible values when returning a complete document; avoid unrequested restructuring |

## 5. Build, packaging, host and validation infrastructure

| Full capability | Decision | Lite treatment |
|---|---|---|
| Python scripts and shared modules | Exclude | No execution dependency |
| Node-based builders and validators | Exclude | No execution dependency |
| CLI plugin registration | Exclude | Distribute instructions as text/document package |
| Host-specific manifests and wrappers | Exclude | One host-neutral core; optional host-specific import notes |
| Native multi-agent orchestration | Replace | Human-coordinated independent conversations, shared briefs and review |
| Automated JSON/schema tests | Exclude | Optional host-native checks; never claim they ran if unavailable |
| Automated hashes/checksums | Exclude | No integrity assertion |
| Conversational consistency review | Retain | Explicit checklist, with model review labeled as such |
| Actual SillyTavern import | External acceptance | User performs import; record result separately |
| Roleplay quality evaluation | External acceptance | User feedback remains separate from static output review |

## 6. Output modes

| Output | Decision | Rule |
|---|---|---|
| Complete character-card JSON | Retain, bounded | Return only when the complete document can fit reliably |
| Complete worldbook JSON | Retain, bounded | Same complete-output rule |
| Markdown card draft | Retain | Useful review format, not automatically an importable card |
| JSON Patch-style operations | Replace / add | Preferred for narrow edits to large existing JSON |
| Adaptation/evidence record | Retain / simplify | Concise Markdown or JSON |
| Multi-part output | Retain | Number parts, mark boundaries and state assembly instructions |
| Downloadable files | Optional | Depend on host facility; never required |
| PNG card | Exclude | No binary encoder or embedded payload |

## 7. Migration priorities

1. Extract and stabilize shared Yuri policies and conversational output contracts.
2. Rewrite original creation as the simplest reference workflow.
3. Rewrite post and novel workflows using the same evidence vocabulary.
4. Rewrite JSON adaptation with conservative patch-first behavior.
5. Remove all mandatory references to Full scripts, upstream skills and CLI tools.
6. Add examples, static review and conversational acceptance cases.
7. Review licensing, Chinese/English parity and release packaging.

## 8. Decisions requiring explicit review before 0.1.0

The following are not silently decided by the matrix:
- Maximum practical input/output size and the exact continuation protocol.
- Whether complete JSON output is a release requirement or JSON Patch is sufficient for large cards.
- Whether the first release should accept standalone JSON worldbooks as a separate workflow.
- Which host-native file-generation facilities, if any, receive optional documentation.
- Whether image generation belongs in the first release or a later optional add-on.

These decisions should be resolved by the Architect using the shared contracts and the actual conversational trials.
