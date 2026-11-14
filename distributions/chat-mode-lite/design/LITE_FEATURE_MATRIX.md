# Yuri Card Workbench Lite — Feature Retention Matrix

**Status:** Phase 0 scope revised for confirmed user decisions D1–D3  
**Revision date:** 2026-11-14  
**Baseline:** Full 1.2.0; read-only novel audit additionally examined `yuri-dev` at `e8b00854654f504938e28da98340419cbd83d07e`  
**Evidence status:** Design decisions and source inspection only; no Lite output or host trial has run in this revision.

## Contents

1. Decision labels and fixed scope
2. Workflows and shared policies
3. Source handling and sequential novels
4. Card operations and output candidates
5. Distribution and runtime dependencies
6. Required actual tests
7. Full-edition follow-up
8. Remaining implementation questions

## 1. Decision labels and fixed scope

- **Retain:** Preserve user-facing behavior and essential policy.
- **Simplify/replace:** Preserve the purpose through a conversational mechanism, with narrower guarantees.
- **Exclude:** Outside the required Lite 0.1.0 runtime.
- **Optional:** Depend on an actually available host capability.
- **Required:** Must be prepared/implemented for the scoped release.
- **Test-gated:** Choose or claim support only after observed trials.

D1: existing-card output is test-gated; neither JSON Patch nor complete JSON is preferred in advance. D2: sequential multi-chapter processing with checkpoints is required. D3: portable, ChatGPT Projects and Custom GPT compatibility packages are required. These are not open product-choice questions.

## 2. Workflows and shared policies

| Capability | Decision | Lite behavior and boundary |
| --- | --- | --- |
| Original Yuri creation | Retain | Conversation-only, text-first; unspecified ordinary choices may be delegated. |
| Existing-card adaptation | Simplify; output test-gated | Inspect supplied JSON/text, identify protected fields and make authorized narrative changes. No binary/lossless claim. |
| Post adaptation | Retain/simplify | Read supplied text; preserve uncertainty; consistently bind the poster's runtime role to `{{user}}`. |
| Novel adaptation | Required | One excerpt or a user-declared chapter sequence, processed in batches with checkpoints. No EPUB decoder. |
| Custom preferences | Retain/simplify | Conversation or optional profile JSON; disclose unsupported/contradictory choices instead of silently defaulting. |
| Main-cast and inclusive identity rules | Retain | Adult-main-cast defaults, author-defined women and user exclusions; background identities protected. |
| Relationship policies | Retain | Preserve existing outcomes absent an authorized causal reason; obey explicit preserve/rederive/pairing policies. |
| Player agency | Retain | No unauthorized current actions, thoughts or replies; keep source identity separate from runtime player binding. |
| Name review | Retain | Contextual options; no automatic renaming from gender stereotypes. |
| Protected anchors | Retain | Assistant-maintained review; user gives decisions in conversation. |
| Source fact/inference/invention separation | Retain | Concise evidence and adaptation records with inspectable locators. |
| Profile hashes/programmatic enforcement | Replace | Stated preference revision and semantic review; no false machine-enforcement claim. |
| Artwork and browsing | Optional | Use real host tools when present; unavailable tools do not block text-only work. |

## 3. Source handling and sequential novels

| Capability | Decision | Lite treatment |
| --- | --- | --- |
| Frozen binary/text hashes | Replace | Source title/edition/user-declared revision and visible segment IDs; do not invent hashes. |
| Per-claim evidence | Retain/simplify | Concise real quotes or chapter/paragraph labels; identify whether evidence is accessible on resume. |
| Exact quote-offset checking | Exclude as requirement | Only claim computational checking when it actually ran. |
| Database indexing/backfilling/promotion | Exclude | Assistant maintains conversational records; no pretend database transaction. |
| TXT/Markdown and pasted prose | Retain | Work only from accessible content; retrieval snippets do not prove chapter completeness. |
| EPUB/PNG extraction | Exclude | User may supply separately decoded text/JSON. |
| Chapter selection | Retain | Preserve user's total scope separately from current batch. |
| Sequential chapters within a conversation | Required | Process in declared order; update coverage and continuity after each batch. |
| Fresh-conversation continuation | Required | Restore from explicit checkpoint plus necessary source; do not rely exclusively on platform memory. |
| Later corrections/reveals | Required | Record superseded claims, chronology and knowledge boundaries; review affected adaptation choices. |
| Scope expansion or changed source edition | Required explicit handling | Record a new declared source/scope revision; do not silently reuse stale facts. |
| Whole-novel goal | Supported through bounded progress | No fixed universal chapter/token cap and no claim to read everything at once. Completion means all agreed portions actually processed. |
| Independent multi-book batch service | Exclude | A single novel's sequential batches are not this excluded capability. |

The checkpoint protocol in `LITE_SHARED_CONTRACTS.md` is normative for Lite. Records are continuity aids, not source substitutes or a guarantee of unlimited effective context.

## 4. Card operations and output candidates

| Capability/output | Decision | Constraint |
| --- | --- | --- |
| Supplied JSON cards/worldbooks | Retain/simplify | Inspect only available content; standalone worldbook edits use the existing adaptation entry, not a fifth workflow. |
| Unknown fields, scripts, IDs/order/settings | Preserve within declared scope | Do not rewrite technical content. If preservation cannot be assessed, narrow the supported operation and report the gap. |
| PNG decode/repack/payload parity | Exclude | Portrait pixels are not embedded card data. |
| Cross-version migration and runtime script fixes | Exclude | Leave to Full or separately scoped specialist work. |
| Folder inventory and automatic grouping | Exclude | User identifies target and related material. |
| A: complete replacement JSON | Test-gated candidate | Check all unrelated fields, escaping, schema/wrapper and complete delivery; not automatically safest. |
| B: field-level replacements | Test-gated candidate | Use inspected locations and expected old content; test application effort and ambiguity. |
| C: machine-readable JSON Patch | Test-gated candidate | Test exact target revision, paths, preconditions and a usable application route. A patch alone is not an importable card. |
| Review draft in Markdown | Retain | A creative review artifact, not evidence of an importable card. |
| Multipart JSON | Test-gated transport | Test assembly, escaping and missing parts; never assume fragmentation solves an output limit. |
| Downloadable files | Optional | Real file generation only; text fallback remains available. |
| Final import-ready artifact | Conditional claim | Require a complete assembled artifact; distinguish parser checking and actual SillyTavern import. |

No size-based routing rule is final until supported by evidence. The release may select one mode or a host/task-dependent policy. Failure of every candidate for a class of input reduces the claimed scope rather than forcing unsafe output.

## 5. Distribution and runtime dependencies

| Capability | Decision | Treatment |
| --- | --- | --- |
| Portable instruction package | Required | Host-neutral copy/paste path, workflow references and resume prompt. |
| ChatGPT Projects setup package | Required | Actual Project instructions, file/upload map, compact references, checkpoint guide and setup smoke test. |
| Custom GPT compatibility package | Required preparation; deployment conditional | Actual GPT instructions, configuration fields, knowledge map, capability settings, Preview cases and lifecycle/migration notes. |
| CLI/AGY/Gemini/Codex plugin manifests | Exclude | Lite chat setup is not CLI plugin installation. |
| Python/Node/shell/installations | Exclude as user requirements | Maintainer validation remains allowed and separately reported. |
| Upstream's 23 skills as runtime dependency | Exclude | Replace required calls with self-contained scoped guidance; retain applicable attribution. |
| Automatic loading of uploaded instruction files | Do not assume | Put mandatory rules in the active host instruction field and test actual use of references. |
| Host memory | Optional convenience | Explicit checkpoint remains the recovery authority; never assume exact recall. |
| Native subagent orchestration | Exclude at runtime | Independent developer instances may collaborate using the agent assignments. |
| Parser/diff/schema checks in development | Allowed | Run only in available tooling; record evidence without claiming the user needs that tooling. |
| Production source or installation-branch edits | Outside current design scope | No Full behavior, plugin channel or release mutation. |

Host lifecycle and official documentation links are recorded in `LITE_PROJECT_SPEC.md`. The Custom GPT preparation requirement is retained despite platform transition restrictions; blocked account setup is not a passed test and is not permission to drop the package silently.

## 6. Required actual tests

These are planned tests, not completed results. Use a cost-effective GPT testing instance and small synthetic inputs; do not run a broad model comparison or repeat historical Full trials. Estimate the sample budget first and do not silently shrink the user's total processing scope.

### T1 — Existing-card output selection

Agents 3 and 6 use one bounded synthetic JSON fixture with a greeting, worldbook IDs/settings, an unknown field and protected technical text. Apply the same authorized narrative change through viable candidates A/B/C under comparable prompts and host conditions. Avoid gratuitous variants; extend coverage only to answer a specific failure.

Record:
- Source/fixture revision, Lite instruction revision, host/model and enabled tools.
- Output completeness, syntax observations and actual parser result if available.
- Allowed changes versus actual changes; missing/extra fields and preservation failures.
- Path/precondition accuracy and whether a nontechnical user can apply the result.
- Output/truncation cost, manual steps and recoverability.
- Whether a final card was assembled and whether import was actually observed.

Undeclared protected-field changes, silent omissions, wrong-target edits and false validation claims fail the candidate. Choose a default or conditional rule only from the recorded findings. Do not report a statistical success rate from a single example. Mark large-card/unseen-host support unverified.

### T2 — Sequential reading and checkpoint recovery

Use one short synthetic novel fixture containing several labeled chapters. Read a first batch, emit a checkpoint, then start a fresh test conversation with only that checkpoint and the necessary next material. Include an alias, a source uncertainty and a later correction/reveal.

Check that the model preserves accepted user choices, distinguishes earlier-source evidence from the summary, resumes at the right location, notices a missing/overlapping segment and does not duplicate or silently overwrite reviewed state. Check that later knowledge does not leak into a deliberately earlier opening. Exercise repeated resume and revised-source handling with small targeted variations only where needed.

### T3 — Distribution setup and parity

Run a minimal task through the portable package, a Project configured with the supplied instructions, and a Custom GPT only where the account can create/edit/use the relevant configuration. Reuse T1/T2 fixtures; no new test campaign is necessary.

Verify the active policy/version, reference discoverability, tools-disabled text route and checkpoint recovery. Keep static package readiness distinct from observed account setup. A platform-retired or inaccessible Custom GPT route is recorded as blocked, with a prepared compatibility package and Projects/portable fallback, not fabricated acceptance.

## 7. Full-edition follow-up

**Already present:** the reviewed Full novel skill and input guide explicitly support multiple `--chapter` values, explicit `--all`, bounded reading units and checkpoints. `scripts/novel_source.py` confirms the selection options.

**Recommended refinement:** audit whether those existing facilities provide a stable, tested resume record for new sessions, corrections, scope/source revisions and knowledge-stage boundaries. Reuse them before introducing any helper. A separate follow-up may strengthen the existing novel workflow, not duplicate the extraction engine or add a fifth skill.

**Important distinction:** continuing unread units inside an existing registration is different from appending later chapters to a frozen registered source. The latter needs a reviewed revision design to preserve evidence bindings. This design records the requirement but does not implement it or claim the append path exists.

## 8. Remaining implementation questions

Only evidence-dependent details remain: the output mode selected by T1, empirically practical batch sizes, package instruction/file budgets, and actual host eligibility. Sequential processing and both ChatGPT-tailored package preparations are settled requirements, not decisions to ask the user again.

See [project scope](LITE_PROJECT_SPEC.md), [shared contracts](LITE_SHARED_CONTRACTS.md) and [agent responsibilities](LITE_AGENT_ASSIGNMENTS.md).
