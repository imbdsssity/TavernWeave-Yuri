# Yuri Card Workbench Lite — Project Specification

**Status:** Phase 0/1 design baseline, revised for the user's three decisions  
**Revision date:** 2026-11-14  
**Target release:** Lite 0.1.0  
**Parent product:** TavernWeave-Yuri 1.2.0  
**Implementation status:** Design only; this revision neither runs model trials nor implements or releases the workflows.

## Contents

1. Confirmed decisions
2. Product definition and goals
3. Operating boundary
4. Inputs and output experiments
5. Sequential novel processing
6. Required distributions
7. Relationship to Full
8. Acceptance and release gates
9. Evidence and references

## 1. Confirmed decisions

| ID | User decision | Implementation consequence |
| --- | --- | --- |
| D1 | Determine existing-card output through actual testing. | Compare complete JSON, field-level replacements and machine-readable patches where useful. Do not prescribe patch-first or complete-JSON-first behavior before results exist. |
| D2 | Include sequential, multi-chapter processing with conversational checkpoints. | Treat continuation within and across conversations as a required workflow, not an optional future feature. |
| D3 | Also prepare packages for ChatGPT Projects and Custom GPTs. | Deliver a portable text edition plus distinct Projects and Custom GPT setup packages from the same maintained Lite policy. Check actual host availability separately. |

These choices are settled requirements. Do not reopen them as a questionnaire. The outcome of D1 remains deliberately undecided until observed trials support a selection.

## 2. Product definition and goals

Lite is a conversation-first execution edition of Yuri Card Workbench. Preserve the four workflows, Yuri adaptation rules, causal relationship reasoning, source fidelity, player agency, name review and user-controlled preferences without requiring the CLI/plugin execution environment.

The four workflow identifiers remain `yuri-card-creator`, `adapt-yuri-card`, `post-to-yuri-card` and `novel-excerpt-to-yuri-card`. The novel name does not limit it to one chapter: it also covers a user-declared sequence processed in bounded batches.

The intended users are ordinary roleplay creators, not developers. They provide material and creative decisions; the assistant maintains concise source and continuity records. Do not require users to maintain technical worksheets or silently make them install a patching tool.

Full remains the advanced tool-backed edition. Lite shares behavior, not Full's binary-preservation, automated validation or persistent-storage guarantees. Repository 1 stays frozen; there is no routine backport to it.

## 3. Operating boundary

### Baseline runtime

Require only conversational text input and structured text output. Attachments, file creation, browsing, image tools, persistent storage, code execution and subagents are optional, detected capabilities. A failed Node/AGY/plugin-build check must not block a text-only Lite task: development tooling, host packaging and end-user runtime are separate concerns.

The assistant must distinguish material supplied, actually available, reviewed, not yet processed, and absent. Attachment availability or retrieval of some passages is not evidence of complete reading.

### Excluded from Lite 0.1.0 runtime

- PNG payload decoding/repacking and binary-preservation guarantees.
- EPUB archive extraction; externally extracted text may be supplied.
- Automated source backfilling, indexing, database transactions or arbitrary filesystem operations.
- Required Python, Node.js, shell, package installation, CLI registration or upstream skill invocation.
- Autonomous multi-agent execution, script/regex migration and live runtime debugging.
- Claims of automatic hash/schema verification, guaranteed lossless editing or successful import without the corresponding observed checks.

These are end-user restrictions, not a ban on maintainer tooling. Developers may use available parsers, diffs or CI to inspect trial artifacts and package consistency. Record those checks separately; they must not become hidden Lite runtime dependencies.

## 4. Inputs and output experiments

Accept creative briefs, supplied JSON/text cards and worldbooks, TXT/Markdown posts, and user-declared novel chapters or excerpts. For a PNG card, request decoded card JSON; visual inspection of the portrait does not expose its embedded card data.

Return playable card/worldbook drafts, adaptation notes and source records. Existing-card delivery is subject to D1:

- Candidate A: complete replacement JSON.
- Candidate B: explicit field-level replacement text with inspected locators.
- Candidate C: machine-readable JSON Patch, where its application route is practical.

No candidate is the design default. Test the same bounded synthetic card and authorized change through the viable candidates. Assess unauthorized changes, missing fields, paths/IDs, escaping, truncation, user effort and the final usable artifact. A patch is not itself a finished importable card; account for applying it. A visually plausible JSON block is not parser or import evidence.

The test outcome may support one default, a conditional policy, or a narrower supported scope. Record the tested host/model, input revision and output limitations; do not generalize a single small-card result to arbitrary cards or all hosts. See the feature matrix and shared contracts for the decision gate.

Do not split a JSON string arbitrarily or call numbered fragments a complete export. When output capacity is insufficient, preserve progress and state exactly what remains. Multipart assembly is another delivery path to test, not a guaranteed workaround.

## 5. Sequential novel processing

Process one novel project over successive bounded chapter batches, with explicit conversational checkpoints after each completed batch and before a context/session handoff. This is not a batch service for unrelated books.

Keep three separate scopes:

1. The user's total authorized goal, such as chapters 1–12.
2. Material currently supplied and actually accessible.
3. The current processing batch, such as chapters 1–2.

A smaller batch does not reduce the agreed deliverable. If later chapters are unavailable, checkpoint and request the missing material when needed; do not invent it, mark it reviewed or promise background work.

Each checkpoint must preserve source edition, chapter/segment coverage, next unread location, stable character aliases, chronology, relationship changes, evidence locators, user decisions, adaptation choices, protected anchors, draft revision and unresolved issues. Keep source facts and adapted fiction separate. Distinguish author knowledge from what a character can know at the intended opening stage.

Resuming must reconcile the checkpoint with accessible source material and newer explicit user decisions. Detect missing, overlapping, reordered or revised chapters. Do not silently overwrite conflicts or reopen settled creative choices. A compact checkpoint is a continuity aid, not a replacement for the original evidence. The shared contract defines the required protocol.

Test at least one bounded synthetic multi-chapter source across a fresh conversation, including a later correction or contradiction. Do not describe the feature as verified merely because a checkpoint template exists.

## 6. Required distributions

Maintain one Lite core and three installation/setup forms:

| Distribution | Required deliverables | Boundary |
| --- | --- | --- |
| Portable conversation | Self-contained starter instructions, workflow references, checkpoint template and resume prompt | Works through pasted text; no attachment or plugin loader required. |
| ChatGPT Projects | `PROJECT_INSTRUCTIONS.md`, setup guide, upload map, compact reference pack and checkpoint/resume guide | User applies instructions and adds files in their project; no automatic account setup or guaranteed retrieval of every file. |
| Custom GPT compatibility | `GPT_INSTRUCTIONS.md`, name/description/starters, knowledge upload map, capability settings, setup/Preview guide and migration notes | Preparation is required; deployment depends on current account eligibility, editing availability and platform lifecycle. |

Put essential behavioral rules, routing and checkpoint requirements in the actual host instruction field. Knowledge/reference files hold supporting detail and examples, not the only copy of mandatory rules. Merely uploading a file named `CORE.md` does not establish that its instructions are active.

Project context can assist continuation, but the explicit checkpoint remains the portable state. Custom GPT continuation must work when the next conversation starts without prior history. User-specific chapters/cards and session checkpoints must not be bundled as public GPT knowledge.

Both tailored packages must use the same canonical policy and workflow versions. Provide plain-language setup and text fallback, not a claimed one-click ZIP import. Keep user-facing instructions available in Chinese and English. Avoid hard-coded host limits unless dated and verified during packaging.

### Current platform lifecycle note

Official OpenAI guidance checked on 2026-11-14 announces Custom GPT retirement scheduled for December 11, 2026, with specified exceptions/deferrals, and account-dependent creation/migration restrictions. Therefore retain D3's Custom GPT package as a compatibility/migration deliverable, not a promise that every user can create a new GPT. Projects and the portable text edition provide independent deployment routes. Follow the user's actual workspace notice and recheck before release. This design does not create a plugin, GPT or Project in the user's account.

## 7. Relationship to Full

A read-only review of `yuri-dev` at `e8b00854654f504938e28da98340419cbd83d07e` found that Full already supports repeated `--chapter`, explicit `--all`, and reading source units across checkpoints. Do not describe multi-chapter processing as wholly absent or add a fifth novel skill.

Recommend a separate Full follow-up that formalizes the same continuation semantics: a discoverable resume record, source/scope/profile consistency, stage-bounded knowledge, repeated-resume behavior and later-chapter corrections. Map these onto Full's existing provenance and creative authority; do not create a second authoritative fact store or replace exact evidence bindings with a Lite summary.

The reviewed novel CLI exposes `index` and `init`, not a demonstrated append/resume operation. Existing guidance alone does not prove a tested new-session recovery path. Audit the shared facilities before adding code. Extending an already registered source scope must preserve original bindings through a reviewed revision/registration design rather than silently mutating a frozen source.

This is a recommendation for a separately scoped Full change, not authorization to modify Full in the Lite design branch. Record the latest development commit separately from the released 1.2.0 baseline.

## 8. Acceptance and release gates

Release consideration requires:

1. Four self-contained workflows with no required CLI/runtime dependencies.
2. D1's output decision supported by actual bounded trials, with unsupported formats/hosts explicitly identified.
3. D2's sequential processing, checkpoint restore, source coverage and contradiction handling exercised in a fresh conversation.
4. Portable, Projects and Custom GPT compatibility packages prepared with the same policy; unavailable deployment tests marked blocked/unverified rather than passed.
5. Chinese/English behavior parity, source fidelity, player agency and preservation limits checked.
6. Actual evidence distinguished: static review, model trial, parser/diff check, real host setup, SillyTavern import and human roleplay feedback.
7. Licenses and notices preserved; rewritten or condensed upstream-derived material is not assumed to become MIT automatically.

Use cost-effective GPT testing instances, bounded synthetic fixtures and the smallest changed-surface checks. Do not repeat the prior Full import/roleplay campaign or use this expensive authoring instance for material trials.

The target remains Lite 0.1.0. This design revision changes no Full version, release, production source or installation branch. Implementation, account deployment and release approval are separate from recording the user's decisions.

## 9. Evidence and references

- [Feature decisions](LITE_FEATURE_MATRIX.md), [shared contracts](LITE_SHARED_CONTRACTS.md), [agent assignments](LITE_AGENT_ASSIGNMENTS.md).
- [Full novel workflow at reviewed commit](https://github.com/imbdsssity/TavernWeave-Yuri/blob/e8b00854654f504938e28da98340419cbd83d07e/extensions/yuri-creation/skills/novel-excerpt-to-yuri-card/SKILL.md).
- [Full input/scope guidance](https://github.com/imbdsssity/TavernWeave-Yuri/blob/e8b00854654f504938e28da98340419cbd83d07e/extensions/yuri-creation/references/novel-inputs.md).
- [Full novel CLI](https://github.com/imbdsssity/TavernWeave-Yuri/blob/e8b00854654f504938e28da98340419cbd83d07e/extensions/yuri-creation/scripts/novel_source.py).
- Official host documentation, checked 2026-11-14: [Projects](https://help.openai.com/en/articles/10169521-projects-in-chatgpt), [GPT configuration](https://help.openai.com/en/articles/8554397-creating-and-editing-gpts), [GPT conversation behavior](https://help.openai.com/en/articles/8554407-gpts-in-chatgpt), [retirement/migration FAQ](https://help.openai.com/en/articles/20001519-custom-gpt-retirement-and-migration-faq). These describe host behavior, not a completed Lite deployment test.
