# Yuri Card Workbench Lite — Agent Assignments and Integration Plan

**Status:** Proposed execution plan  
**Coordinator:** Agent 0 — Architect / Integration Lead  
**Repository:** `imbdsssity/TavernWeave-Yuri`  
**Development baseline:** `yuri-dev`  
**Design branch:** `lite-phase-0-design`

## 1. Coordination model

Use a hub-and-spoke model. Agent 0 owns architecture, shared contracts, integration decisions and release readiness. Specialist agents own bounded deliverables and must not independently redefine shared policy.

Multiple ChatGPT instances may contribute through GitHub, but write access is not a shared execution environment. Each instance must inspect the current branch state, work only within its assigned paths and report exactly what it changed.

No agent may merge into `yuri-dev`, modify `main`, publish a release or update Full-edition distribution branches without explicit release authorization.

## 2. Work packages

| Agent | Role | Owned deliverables | Dependencies |
|---|---|---|---|
| 0 | Architect / Integration Lead | Architecture decisions, shared contract changes, integration, PR review, final acceptance report | All packages |
| 1 | Yuri Policy Specialist | Policy wording, preference semantics, character/relationship/player-agency references | Shared contracts |
| 2 | Original Creation Specialist | `CREATION.md`, creation examples and worldbook guidance for conversation-only use | Policy contracts |
| 3 | Existing-Card Specialist | `ADAPTATION.md`, JSON/JSON Patch guidance, preservation limitations and examples | Policy + output contracts |
| 4 | Source Adaptation Specialist | `POST.md`, `NOVEL.md`, evidence records, scope/continuity templates | Policy + source contracts |
| 5 | Packaging / Documentation Specialist | Lite README files, package instructions, localization and licensing/notice review | Stable workflow interfaces |
| 6 | Independent QA Specialist | Static audit, cross-workflow review, conversational test plan, findings and evidence ledger | Candidate package |

Agents 1–4 may draft in parallel after Agent 0 freezes the initial contracts. Agent 5 may prepare documentation scaffolding earlier, but must not promise unfinished capabilities. Agent 6 reviews merged candidates and does not silently rewrite specialist deliverables.

## 3. File ownership

Suggested final Lite package layout:

```text
distributions/chat-mode-lite/
  README.md
  README.zh-CN.md
  LICENSE
  THIRD_PARTY_NOTICES.md
  instructions/
    CORE.md
    CREATION.md
    ADAPTATION.md
    POST.md
    NOVEL.md
  references/
    yuri-policy.md
    character-design.md
    relationship-rules.md
    source-evidence.md
    player-agency.md
    worldbook-design.md
    card-output.md
  schemas/
    preferences.schema.json
    source-record.schema.json
    card-output.schema.json
  templates/
    preferences.json
    continuity-record.md
    adaptation-record.md
  examples/
    original-card.md
    post-adaptation.md
    novel-adaptation.md
```

Ownership:
- Agent 0: `design/` and any shared-contract changes.
- Agent 1: `references/yuri-policy.md`, `relationship-rules.md`, `player-agency.md`, preference template/schema proposals.
- Agent 2: `instructions/CREATION.md`, `references/character-design.md`, `worldbook-design.md`, original example.
- Agent 3: `instructions/ADAPTATION.md`, `references/card-output.md`, card-output schema proposal and adaptation example.
- Agent 4: `instructions/POST.md`, `instructions/NOVEL.md`, `references/source-evidence.md`, continuity/adaptation templates and source examples.
- Agent 5: root README files, LICENSE/third-party notice proposal and final package navigation.
- Agent 6: QA reports under `qa/`; may propose fixes but does not edit another agent's owned files without coordination.

Agent 0 resolves conflicts and owns final integration. Schema files are optional descriptive contracts; their presence must not imply that Lite can execute a validator.

## 4. Branch and PR protocol

Use one feature branch per work package, created from the agreed `yuri-dev` baseline after the architecture branch is integrated or explicitly designated as the shared base.

Suggested branches:
- `lite-policy`
- `lite-creation`
- `lite-adaptation`
- `lite-source`
- `lite-docs`
- `lite-qa`

Each agent:
1. Confirms the repository, base branch and assigned file paths.
2. Creates or uses only its assigned branch.
3. Reads the current shared contracts before drafting.
4. Makes focused commits with descriptive messages.
5. Opens a PR targeting the agreed Lite integration branch (not `main`).
6. Reports changed paths, design decisions, limitations and checks actually performed.

If multiple agents cannot create branches or PRs, Agent 0 may collect their proposed content and perform the GitHub writes. Do not have multiple agents write concurrently to the same path.

## 5. Integration order and gates

### Gate 0 — Architecture baseline
- Approve project scope, feature matrix and shared contracts.
- Confirm the Full edition and existing host branches remain untouched.
- Confirm licensing approach for any reused upstream material.

### Gate 1 — Policy foundation
- Integrate Agent 1's policy references.
- Verify semantic alignment with `LITE_SHARED_CONTRACTS.md`.
- Resolve conflicting defaults before workflow work proceeds.

### Gate 2 — Workflow implementation
- Integrate creation, adaptation and source workflows.
- Check every workflow uses the same terms for source fact, inference, user decision and creative addition.
- Check all workflows respect player agency and protected content.

### Gate 3 — Package and documentation
- Verify all required instructions are self-contained.
- Remove broken links and mandatory references to Full scripts/upstream skill routing.
- Ensure Chinese and English documentation describe the same scope.

### Gate 4 — Independent QA
- Static inspection for unavailable runtime/tool assumptions.
- Cross-workflow policy consistency review.
- Conversational trials with fixed synthetic inputs.
- Artifact inspection where the host actually exposes the output.
- Record untested claims and host-specific limitations.

### Gate 5 — Release decision
- Agent 0 prepares a release-readiness report.
- User reviews the Lite candidate and authorizes publication.
- Only then may a release PR target `main` and a Lite-specific tag/artifact be created.

## 6. Required agent handoff format

Every specialist handoff must state:

- **Role and assigned scope**
- **Base commit/branch**
- **Files created or changed**
- **Policy version used**
- **Decisions made**
- **Assumptions and unresolved questions**
- **Capabilities assumed from the host**
- **Checks actually performed**
- **Checks not performed**
- **Known limitations**
- **PR link or proposed patch**

Do not report a test as passed unless it was actually executed or directly observed. Static inspection, model self-review, conversational trials, JSON inspection and real SillyTavern import are distinct evidence types.

## 7. Conflict and safety rules

- Shared policy conflicts are escalated to Agent 0; workflow agents do not invent local exceptions.
- User-specific preferences and private card/source material must not be committed as public examples.
- Use synthetic fixtures unless a user explicitly authorizes a private sample.
- Do not reintroduce withdrawn or excluded private samples from prior work.
- Never place secrets, account tokens, private casework or generated user cards in the public Lite package.
- Preserve applicable upstream licenses and notices. Do not assume that co-location makes upstream material MIT-licensed.
- No agent may claim lossless card preservation, successful import, image generation, web retrieval or code execution without corresponding evidence.

## 8. Current status

The four design documents are the Phase 0/1 starting baseline. No Lite workflow has yet been migrated, no Full capability has been removed, and no release has been authorized.

Next action: Agent 0 reviews the four documents with the user, resolves the open decisions in the feature matrix, then authorizes specialist work packages.
