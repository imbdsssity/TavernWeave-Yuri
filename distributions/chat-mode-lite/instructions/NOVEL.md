# Novel excerpt and sequential chapters to Yuri card

Workflow: `novel-excerpt-to-yuri-card` · Revision: `lite-source/B2.1` · Core: `lite-core/A1.1` · Policy: `yuri-policy/1.0` · Checkpoint: `yuri-lite/checkpoint/v1`

Use this procedure with the active [shared core](CORE.md) for one bounded excerpt or one novel's declared sequence of chapters across batches and conversations. Both use the same workflow, records and checkpoint protocol. Maintain records from ordinary conversation in the user's language; the user supplies prose and decisions, not technical forms. Pasted TXT/Markdown text is sufficient. Do not require a CLI, indexer, database, code execution, persistent memory or upstream skill invocation.

Companions: [source evidence](../references/source-evidence.md), [Yuri preferences](../references/yuri-policy.md), [relationships](../references/relationship-rules.md), [player agency](../references/player-agency.md), [optional preference sample](../templates/preferences.json), [adaptation record](../templates/adaptation-record.md), [continuity record](../templates/continuity-record.md) and [resume prompt](../templates/resume-prompt.md). Use their actual available text; a link is not proof of loading. No design-directory file is required at runtime.

## 1. Establish source, scope and the first batch

Reuse an explicit project scope. For a bounded excerpt, identify its beginning/end using supplied headings, paragraph labels or explained local segment boundaries; completion concerns that excerpt, not the whole book. For sequential work, preserve the total authorized chapter/segment order across every smaller batch. If no scope is stated, propose a manageable starting excerpt/batch and proceed with available material, making clear that it is not the entire novel. Do not impose a universal chapter/token cap or silently shrink an agreed goal to fit the current context.

Identify source title, stable source/volume IDs, edition/declared revision or unknown, and chapter titles/order. Preserve supplied identifiers. Chapter numbers may repeat across volumes; locally assigned labels are not publisher IDs. Do not invent measured offsets or hashes. Record these separately:

| Item | Required distinction |
| --- | --- |
| Total authorized scope | The agreed excerpt or complete ordered sequence, scope revision and exclusions. |
| Supplied material | Portions provided or identified, even if their text is inaccessible. |
| Available source | Exact full/partial text that can be inspected now, separated by edition and segment. |
| Current batch | A bounded portion and processing goal within the total task. |
| Completed coverage | Actual stage states by source revision and segment; partial coverage stays partial. |
| Gaps and next locations | First unfinished stage, first unread authorized location, exact missing input and next available portion. These can differ. |

An uploaded book, index/catalog, chapter summary or checkpoint mention does not mean the prose was read, extracted, adapted or reviewed. Reading a later chapter does not establish earlier coverage. Host retrieval may expose only passages. For EPUB or inaccessible attachments, request separately extracted text or the relevant pasted passage; Lite does not decode archives, perform OCR or reconstruct missing prose. Optional tools may provide actual text, but report their limits and retain a text-only route.

## 2. Restore preferences, player and opening boundary

Use the user's actual conversational/profile choices, exclusions, protected anchors and prior approvals. Maintain a human-readable preference revision and explicit overrides; the optional sample does not grant consent. Resolve consequential conflicts before affected edits and continue independent work. Apply the shared inclusive adult-main-cast defaults, preserve background identities and source age facts, and do contextual name review without automatic renaming. Known minors remain outside the adult transformation-target route; an adult fictional choice for an unknown age is an identified addition.

Keep source identity, selected player role and permission over player behavior separate. A selected first-person narrator or source player binds to `{{user}}` throughout runtime prose, greetings and worldbook titles/keys/content, while source names/quotes/IDs stay in evidence. Do not infer an unstated narrator identity. For third-person material, use the user's selected role or an explicitly invented adult female player with no fabricated source dossier. Preserve an existing player persona unless a specific change was authorized. Do not script present player thoughts, replies, actions or consent without scoped delegation.

Record the intended opening at a specific event/time boundary independently of read-through progress. If it is unspecified, choose a useful playable stage within the supplied scope and state that choice as delegated design. For each relevant character/player, distinguish what is known, believed, disputed or unknown there. Later discoveries can update author-level evidence without changing that stage or granting earlier characters knowledge.

## 3. Read and extract one available batch

Read available portions in declared source order, retaining actual segment boundaries. Update stable entities/aliases/roles, story chronology as well as source order, relationship stages, open questions and important claim locators in the existing records. Distinguish source fact, inference, user decision, creative addition and unknown/not supplied. A narrator's guess, witness report or accusation stays viewpoint-limited; a quotation establishes only what its context supports.

Maintain supplied, read, extracted, adapted and reviewed states independently. Mark a whole chapter fully read only when its entire prose was actually inspected. A selected passage establishes only passage coverage, even when it is the full authorized excerpt. Mark whole-chapter review complete only after the required source, adaptation and draft review covers the whole chapter; otherwise report the exact reviewed segments. A read/extract batch can finish while adaptation/review remains pending. Use not started, partial, complete or not applicable with a reason. Preserve the exact partial position when interrupted; do not promote the whole chapter based on its summary or highest processed paragraph.

Never interpolate a missing chapter. If the next unread portion is unavailable, checkpoint the gap and request that portion. Do useful unrelated work where possible. Process later available chapters out of the declared order only under explicit user direction, with gaps and provisional chronology visible; this does not establish contiguous completion.

## 4. Adapt and draft without changing the evidence

Record accepted/delegated choices, their authority, source basis, causal reasons and affected draft fields in the adaptation record. Keep proposed/deferred choices distinct. Under `rederive_if_causal`, retain outcomes unless a specific authorized changed circumstance supports rederivation; gender transformation alone supplies no cause. `preserve_outcomes` fixes outcomes even under changed circumstances, unless explicitly overridden. Honor explicit pairing targets without changing additional pairs. Later factual correction is not automatic permission to alter a settled creative choice.

Build an NPC-centered character draft with independent goals, a recognizable voice, relationship tension and a playable opportunity for `{{user}}`. Identify new motives, dialogue and setting details as additions. A source already about women needs no invented gender transformation. Preserve selected exclusions and anchors; source quotes and identities do not change retroactively.

Provide a labeled text review draft with character description/personality, scenario, opening and useful worldbook entries. The opening describes NPC/setting behavior and leaves the player's current response open. Review all supplied alternative greetings. Worldbook titles/keys/content must use the player binding consistently and contain only information appropriate to the chosen stage. Keep future reveals, author-only claims and private evidence outside active runtime entries; a “spoiler” label does not reliably prevent model access. Do not rely on an untested runtime trigger to hide future knowledge. If a future stage is requested later, version that choice and update the relevant knowledge boundaries explicitly.

Do not depend on pending character-design, export or host-package files to produce a usable review draft. Label a provisional draft with its exact source/knowledge scope and remaining work. Markdown is not an importable card. For any requested structured output, report actual form/completeness and observed checks; existing-card delivery remains test-gated. If inherited card/worldbook content is also edited, follow CORE's inspected-scope protection and incomplete-visibility limits. Do not rewrite unrelated technical content or claim lossless preservation.

## 5. Review and emit the existing checkpoint

Review source support and uncertainty, current preferences and causal choices, stable names/aliases, exclusions, protected anchors, player agency, every greeting and worldbook entry, story-stage knowledge and output completeness. Record only work actually performed. If a newly extracted fact is not yet reconciled into the draft, leave adaptation/review pending and identify affected fields.

Emit copyable `yuri-lite/checkpoint/v1` text after every completed batch, when paused and before a planned context/session handoff. Emit an in-progress checkpoint when a batch cannot finish. Use the continuity template's existing twelve groups without substituting a second record protocol:

1. Identity — project/workflow, checkpoint ID/revision/parent and actual policy/core/workflow/package versions.
2. Source — title, edition/revision, source/volume IDs and declared order.
3. Scope — total authorized task, exclusions, supplied/available text and current batch.
4. Coverage — independent stage states, completed/partial portions, gaps, first unfinished/unread locations and next requested/available input.
5. Preferences — effective choices/revision, explicit overrides and protected anchors.
6. Entities — stable IDs/aliases, roles, player binding and unresolved identity candidates.
7. Story — chronology, relationships, viewpoints and open threads.
8. Evidence — important claims/locators, uncertainty, correction links and current evidence accessibility.
9. Adaptation — accepted/delegated/proposed choices, authority, causal reasons and essential decisions.
10. Knowledge boundary — read-through progress versus target opening and each character/player's knowledge.
11. Output — actual draft/card/worldbook revisions, available text, pending edits, output form/completeness and observed checks.
12. Handoff — conflicts, blockers, next available input and one concrete action.

Use advancing revisions and a distinct snapshot ID/parent in the same lineage; keep intentional alternatives separate. Compact older detail without losing consequential uncertainty, decisions or locators. Essential state must be in the checkpoint, not only behind companion links. A saved file is optional and can be claimed only after actual persistence. This portable aid is not proof of reading, a replacement for source evidence or a promise of unlimited recall/background processing.

## 6. Resume and reconcile before advancing coverage

For a fresh conversation, supply the active Lite instructions, user-designated checkpoint and necessary next source/draft material, using the resume prompt. Do not assume prior-chat access, exact platform memory or automatic retrieval of uploaded files. Briefly restore total scope, current source access, gaps, opening stage and next action before proceeding. Older claims whose passages are unavailable here remain carried context, not reverified; request the relevant passage when a contested claim materially affects the adaptation, not the entire earlier novel for routine work.

| Condition | Required action |
| --- | --- |
| Repeated checkpoint/batch | Compare lineage, IDs, source revision/segments, accepted decisions and draft revision with state actually available here. Reuse accepted work; do not duplicate facts, reapply a change or advance coverage twice. Disclose an unavailable newer successor rather than claiming cross-chat deduplication. |
| Missing/reordered chapters | Keep the first unread authorized location distinct from the next available chapter. Request the gap, or retain an explicitly authorized deferral; never infer missing events or silently reduce scope. |
| Partial/overlapping chapters | Compare edition and visible boundaries. Retain established coverage of unchanged overlap and process the unprocessed remainder; uncertain boundaries or conflicting text need reconciliation before new completion claims. |
| Revised text/edition | Record the new revision and changed portions. Preserve old claims/locators, mark affected coverage and drafts for re-review, and retain unchanged status only where correspondence is established. Do not merge editions silently or let an old reviewed state validate new text. |
| Scope expansion/reduction | Record the user's actual change and a scope revision; preserve prior work and exclusions. A smaller batch or missing chapter is not authorization to reduce the total task. |
| Later reveal/correction | Retain the earlier claim/locator as superseded or viewpoint-limited; add the new evidence and explicitly review affected identity mappings, chronology, relationships, inferences and adaptation choices. Resolve aliases without erasing provisional IDs or prior uncertainty. Preserve the opening's stage and character knowledge. |
| Conflicting checkpoint/preference/draft | Reconcile newer explicit user decisions and material conflicts. Do not choose merely by filename or revision numbers across unrelated lineages, reopen settled choices gratuitously or overwrite a newer draft. Request actual current draft text before an exact edit if it is unavailable. |

Emit a successor checkpoint with honest stage states and outstanding gaps. Continuing already registered Full units is not permission to append to frozen Full sources; Lite records neither replace Full's evidence store nor introduce another novel engine.

## 7. Completion and feedback

Call the project complete only when every authorized segment has reached the required review stage and the scoped output is fully delivered. An excluded portion is not a gap; an unavailable or deferred authorized portion is. If only an excerpt is complete, name it. If later chapters or output sections are missing, state them and preserve progress. Never equate upload, indexing, summary, checkpoint presence or a provisional card with whole-chapter/whole-novel review.

Take feedback conversationally and update the same adaptation/checkpoint/draft lineage. Separate static review, conversational recovery trials, parser/diff checks, host setup/import and human roleplay observations; an unperformed check is not a pass. The [novel adaptation example](../examples/novel-adaptation.md) reuses the [existing synthetic fixture](../examples/novel-continuation-source.md) and illustrates expected behavior only. No model trial or recovery guarantee follows from authored examples.

## Attribution

Based on the integrated Lite core and source guidance at `c57f981e4230be746fe5bdcf3592e2784b8fdbeb`. Retain applicable attribution and terms described in [CORE provenance](CORE.md#provenance-and-a1-differences) when distributing this material.

Required Notice: Copyright 2026 LiarMTTT
