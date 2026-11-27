# Yuri Card Workbench Lite — Agent Assignments and Integration Plan

**Status:** Revised design work packages; no agents or trials launched by this document  
**Revision date:** 2026-11-14  
**Coordinator:** Agent 0, Architect / Integration Lead  
**Repository:** `imbdsssity/TavernWeave-Yuri`  
**Development integration:** `yuri-dev`  
**Current design branch:** `lite-phase-0-design`

## Contents

1. Decisions and authorization boundary
2. Roles and deliverables
3. File ownership and package layout
4. Branch coordination
5. Execution order and acceptance gates
6. Test cost and evidence rules
7. Full-edition follow-up
8. Handoff and current status

## 1. Decisions and authorization boundary

The user has resolved the three design choices:

- **D1:** Existing-card output is decided by actual tests, not an architectural preference.
- **D2:** Sequential multi-chapter processing with conversational checkpoints is required.
- **D3:** Prepare portable, ChatGPT Projects and Custom GPT compatibility packages.

Do not ask the user to choose these again. Output-mode selection and host eligibility remain evidence questions. Do not label a package or workflow accepted before relevant observations exist.

This revision updates four planning documents only. It does not start specialist agents, spend a model-test budget, alter Full runtime code, merge branches, configure the user's ChatGPT account or publish a release. GitHub write access does not create shared execution, account-admin authority or subagent capabilities.

Use one integration lead and bounded ownership. The seven roles may be performed by fewer independent instances in sequence; seven simultaneous sessions are not required. User-controlled handoffs are acceptable when automatic delegation is unavailable.

## 2. Roles and deliverables

| Agent | Scope | Required deliverables and dependencies |
| --- | --- | --- |
| 0 | Architecture/integration | Maintain design decisions and policy compatibility; resolve conflicts; approve bounded work packages; integrate reviewed work and report remaining evidence gaps. |
| 1 | Shared policy/core | `CORE.md`, Yuri/relationship/player-agency references and preference template; align the causal-relationship default across all forms. |
| 2 | Original creation | `CREATION.md`, character/worldbook methodology and a synthetic example; depend on Agent 1's contract. |
| 3 | Existing-card workflow | `ADAPTATION.md`, output candidates, preservation limits and application instructions; co-own T1 with Agent 6, without choosing patch-first or full-first beforehand. |
| 4 | Sources/continuity | `POST.md`, `NOVEL.md`, evidence and checkpoint templates, fresh-session resume prompt, source-revision handling and bounded novel fixture; co-own T2 with Agent 6. |
| 5 | Distribution/setup | Portable starter plus separate Projects and Custom GPT compatibility setup packages, upload maps, lifecycle notes, bilingual guides and licensing review; depend on stable core/checkpoint contracts. |
| 6 | Independent QA | Static consistency review and actual T1/T2/T3 evidence; assess output/application and fresh-session behavior; report unavailable tests honestly. |

Agent 0 reviews shared-policy changes rather than rewriting specialist prose for stylistic preference. Agent 6 may propose a patch, but does not silently alter another agent's owned instructions.

## 3. File ownership and package layout

The following is a target layout, not a claim these implementation files exist:

```text
distributions/chat-mode-lite/
  design/                         # Four design documents; Agent 0
  instructions/
    CORE.md                       # Agent 1, Agent 0 contract review
    CREATION.md                   # Agent 2
    ADAPTATION.md                 # Agent 3
    POST.md                       # Agent 4
    NOVEL.md                      # Agent 4
  references/
    yuri-policy.md                # Agent 1
    relationship-rules.md         # Agent 1
    player-agency.md              # Agent 1
    character-design.md           # Agent 2
    worldbook-design.md            # Agent 2
    card-output.md                # Agent 3
    source-evidence.md            # Agent 4
  templates/
    preferences.json              # Agent 1
    adaptation-record.md          # Agent 4; Agent 3 reviews card use
    continuity-record.md          # Agent 4
    resume-prompt.md              # Agent 4
  packages/
    portable/                     # Agent 5
      START_HERE.md
      UPLOAD_MAP.md
    chatgpt-projects/             # Agent 5
      PROJECT_INSTRUCTIONS.md
      SETUP.md
      UPLOAD_MAP.md
      RESUME_GUIDE.md
    custom-gpt/                   # Agent 5
      GPT_INSTRUCTIONS.md
      CONFIGURATION.md
      KNOWLEDGE_MAP.md
      PREVIEW_TESTS.md
      COMPATIBILITY_AND_MIGRATION.md
  examples/                       # Each workflow author owns its example
  qa/                             # Agent 6
    fixtures/
    OUTPUT_TRIALS.md
    CHECKPOINT_TRIALS.md
    HOST_PACKAGE_CHECKS.md
  README.md                       # Agent 5
  README.zh-CN.md                  # Agent 5
  PACKAGE_CONTENTS.md              # Agent 5; Agent 0 release review
  LICENSE                         # Agent 5; preserve actual boundaries
  THIRD_PARTY_NOTICES.md           # Agent 5
```

Any optional schemas describe data; they do not imply runtime validation. Agent 1 owns preference-schema proposals, Agent 3 card-output proposals and Agent 4 source/checkpoint proposals. Coordinate edits to shared templates rather than concurrent writes.

Package adaptations must derive their required rules from the same canonical Lite files. Use version mapping and a content/parity checklist; do not maintain three independent policies. A build helper is optional maintainer tooling, never an end-user prerequisite. Every produced package must include the referenced content, not links requiring access to the Full checkout.

Agent 5 places mandatory behavior in actual host instruction fields, not only uploaded knowledge. Keep design documents, QA transcripts, private sources and real user checkpoints out of default runtime knowledge bundles. Prepare plain-text setup instructions and a fallback; do not claim one-click archive import or automatic account creation.

## 4. Branch coordination

Continue design edits on `lite-phase-0-design`. Before specialist implementation, Agent 0 selects one immutable shared baseline containing the agreed contracts. The live `yuri-dev` audit head was `e8b00854654f504938e28da98340419cbd83d07e`; re-read branch heads at execution time, because this is not a promise they remain unchanged.

Use focused feature branches such as `lite-policy`, `lite-creation`, `lite-adaptation`, `lite-source`, `lite-docs` and `lite-qa`. Create them only when the work starts. Do not create parallel permanent source histories or treat generated host packages as editable canonical source.

Each agent confirms the base SHA, owner/path scope and contract revision; reads current content; makes focused commits on its branch; and opens a PR to the coordinator-designated development target, not `main`. The coordinator alone integrates after review within the user's actual authorization.

Do not force-push, overwrite concurrent work, reset `yuri-dev` to this older design branch or merge an entire generated distribution into source. Re-read changed files/SHAs before writes and resolve conflicts explicitly. Preserve the newer Full development fixes while integrating only the intended Lite paths.

A design or integration PR is not release authorization. `main`, Full installation branches and public release metadata remain protected by separate scope/approval. Multiple instances sharing GitHub credentials do not gain independent authority to publish.

## 5. Execution order and acceptance gates

### G0 — Contract baseline

Record D1–D3 as settled. Confirm the same causal relationship default, source fidelity and player-agency rules. Identify upstream-derived text and notices. Remove stale patch-first instructions and obsolete questions asking whether sequential reading or ChatGPT packages are required.

### G1 — Core and checkpoint contract

Agent 1 prepares the compact core. Agent 4 defines the checkpoint template and resume prompt against `yuri-lite/checkpoint/v1`. Agent 0 verifies source/profile revisions, lineage, coverage, gaps, correction handling and separation of read-through progress from story knowledge.

### G2 — Workflow drafts

Agents 2–4 draft self-contained workflows. Existing-card output remains experimental until T1. Novel processing must carry the user's total scope across smaller batches rather than silently reducing the task. Reuse the same post/narrator player-binding and evidence vocabulary.

### G3 — Actual bounded trials

Agent 6 performs or coordinates only the approved small trials in suitable host sessions:

- **T1 with Agent 3:** same synthetic JSON card/change through viable output candidates; measure preservation, completeness, application effort and resulting artifact. Record the final evidence-backed output policy or unsupported cases.
- **T2 with Agent 4:** one short synthetic multi-chapter fixture; checkpoint, new conversation, next chapter, source uncertainty/correction and knowledge-stage constraints. Record repeated-resume/missing-source behavior without a large test campaign.

Test design or model self-review does not complete either gate. Do not use this expensive design-authoring instance for inference-heavy sample trials.

### G4 — Three distribution preparations and host checks

Agent 5 prepares all three packages. Agent 6 reuses existing fixtures for T3: check active instructions, required-rule presence, reference mapping, tools-disabled operation and checkpoint recovery. Test actual Project setup where available. Test Custom GPT configuration/Preview only where the user's account can support it.

Custom GPT creation, editing and retirement restrictions are live constraints. Use the dated official guidance linked in `LITE_PROJECT_SPEC.md`, verify the workspace notice and recheck before release. A blocked Custom GPT deployment remains blocked/unverified; preparation of its compatibility package is still required. Projects/portable delivery must not depend on Custom GPT access.

### G5 — Readiness and release

Agent 0 checks parity, evidence scope, remaining blockers and license notices, then reports readiness. No universal host or large-input compatibility claim follows from one successful sample. Public release/version/tag changes require their own authorization. User feedback stays in conversation; the agents maintain the records.

## 6. Test cost and evidence rules

Use cost-effective GPT instances for model-based tests, a small synthetic sample per relevant test, and bounded variations that address an identified risk. Reuse prior evidence when the tested surface is unchanged. Do not repeat the Full host-import, image-generation or roleplay campaign, revive excluded cases, or silently call paid APIs.

Estimate sample size/cost before starting. Shrink a test fixture rather than a user's already authorized real-project scope. No broad model competition is required to decide D1.

Keep these evidence classes separate: static inspection; model semantic review; actual conversational trial; parser/diff/schema check; real host setup; SillyTavern import; human roleplay observation. Developer tooling may verify artifacts but must not become a Lite runtime dependency. A tool-disabled baseline should remain usable.

For every trial record instruction/package version, source fixture revision, host/model and enabled capabilities, inputs/outputs, exact observed failures, checks run, checks unavailable and decision limits. No fabricated percentages, hashes, commands, tests or import results.

## 7. Full-edition follow-up

Agent 4 supplies a short gap assessment to Agent 0, based on the reviewed Full novel workflow, input reference and CLI. Those files already provide multi-chapter selection and checkpointed reading, so the question is reliable continuation semantics and evidence, not whether to build another ingestion engine.

Recommend a separately scoped Full task to reuse the existing provenance/creative authority for explicit checkpoint/resume, revision consistency, corrections, knowledge stages and repeat-resume safety. Audit existing shared/upstream facilities before adding files or commands.

Do not equate resuming unread registered units with appending newly supplied chapters. A later append/revision design must preserve frozen-source hashes and evidence bindings. This follow-up is not implemented or authorized merely by the Lite assignment document, and must not delay the independent Lite design unless an actual contract dependency emerges.

## 8. Handoff and current status

Every handoff states role/scope, base commit, changed paths, contract/package version, decisions, assumptions, checks performed, checks not performed, known limitations, evidence locations and PR/patch. A proposed role is not proof that a subagent was invoked.

**Current state after this revision:** the user's three choices are incorporated in all four design documents. The source audit supports refining Full rather than inventing a new novel skill. No output winner is selected; no Lite model/host trial, implementation, account installation, PR merge or release is claimed.

The design is ready for bounded work-package assignment without another round of the same three product-choice questions. See [scope](LITE_PROJECT_SPEC.md), [feature/tests](LITE_FEATURE_MATRIX.md) and [shared contracts](LITE_SHARED_CONTRACTS.md).
