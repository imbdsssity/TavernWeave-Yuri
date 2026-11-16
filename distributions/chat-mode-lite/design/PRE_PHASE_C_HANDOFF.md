# Pre-Phase-C integration handoff

Review date: 2026-11-16. Status: A2/B2 authoring reviewed and merged; this handoff and the CORE navigation refresh are coordinator integration work, not a release or runtime acceptance.

## 1. Immutable review and integration record

| Item | Exact revision / evidence |
| --- | --- |
| A1/B1 foundation | `c57f981e4230be746fe5bdcf3592e2784b8fdbeb` |
| A2 reviewed head, PR #19 | `fdf2456475a588e7cb643eb7a63cfb2482cba700` |
| A2 squash merge | `378aad26074556fb5551cad6352666e9ff3db632` |
| B2 reviewed head, PR #20 | `29c441d19f6cc876c7bfc2018816f682ee0376d8` |
| B2 squash merge / combined workflow tree | `d0c50174f62906f3f049e13148870d96db45d7ad` |
| CORE navigation refresh | `31a28e7958ac3885bf1a59a8513bc7eb56ed8cda`; integration marker `lite-pre-c/1` |
| Shared behavior versions | Core `lite-core/A1.1`; policy `yuri-policy/1.0`; checkpoint `yuri-lite/checkpoint/v1` |
| Workflow versions | Cards `lite-card-workflows/A2.1`; sources `lite-source/B2.1` |

[PR #19](https://github.com/imbdsssity/TavernWeave-Yuri/pull/19) and [PR #20](https://github.com/imbdsssity/TavernWeave-Yuri/pull/20) were reviewed against the same foundation and merged only into `lite-phase-0-design`. Coordinator comments record acceptance and evidence limits. No contributor correction or policy redesign was required.

The only shared integration adjustment is CORE's stale phase-status text and four routing links. Its behavior revision and the checkpoint/profile contracts stay unchanged. The four original design documents remain historical design baselines; this handoff updates implementation status, not their confirmed product decisions.

This document does not attempt to predict the commit containing itself. Phase C must use the final coordinator-confirmed merge commit containing this handoff and CORE's `lite-pre-c/1` marker. Read and record that exact SHA before creating the packaging branch. Do not start from the older design-only or A1/B1 baseline.

## 2. Completion assessment

| Area | Review outcome |
| --- | --- |
| A2 ownership | Exactly seven additions: two card workflows, three authoring/output references and two synthetic illustrations. No Full or cross-owner rewrites. |
| Original creation | Supports a minimal delegated request, independent adult characters, a playable opening and substantive worldbook bodies without a mandatory questionnaire or tool. |
| Inherited-card adaptation | Separates authorized narrative edits from protected technical content; addresses accessible/inspected scope, counterparts, actual target revision and incomplete output. |
| Existing-card output | Complete JSON, field replacements and JSON Patch remain neutral candidates. Application effort, preconditions, escaping, final artifact and observed checks are evaluation requirements; no T1 winner is selected. |
| B2 ownership | Exactly four additions: POST, NOVEL and their illustrations. Existing foundation, fixture and source contracts remain unchanged. |
| Post handling | Poster binds to `{{user}}`; uncertainty, source identity, quoted speakers, fictional additions and current player control stay distinct. |
| Sequential novels | Preserves total authorization across batches; separates upload/access/read/extract/adapt/review; handles missing, overlapping, repeated and revised material and fresh-conversation continuation. |
| Knowledge boundary | Later evidence can revise author records without granting knowledge to an earlier opening or predetermining the player's answer. |
| Shared records | Uses the existing adaptation record, twelve-group checkpoint and resume prompt; no second protocol or source-of-truth store. |
| Examples | Explicitly illustrative, not test transcripts. The two source illustrations reuse the one canonical four-chapter novel fixture. |
| Dependencies | No required CLI, code execution, package installation, automatic skill discovery or design-directory loading for ordinary text drafting. |

The combined tree contains 21 implementation/reference/template/example files: five instruction files, seven references, four templates and five examples, alongside the four design documents. This handoff is an additional maintainer document, not runtime knowledge. Its presence does not make an installable package.

## 3. Checks performed and their limits

The coordinator inspected the actual PR metadata, changed content, immutable branch revisions, discussion state, available foundation contracts and the combined Lite tree. Cross-checked source/player/relationship/default semantics, checkpoint fields, independent chapter coverage, examples versus the existing fixture, and actual companion paths. The retained upstream worldbook planning/loading reference supports A2's stated new-design convention; inherited configuration remains protected.

Observed completed successful repository CI at both reviewed heads:

- A2: [validate run 43866883318](https://github.com/imbdsssity/TavernWeave-Yuri/actions/runs/43866883318).
- B2: [validate run 43866952409](https://github.com/imbdsssity/TavernWeave-Yuri/actions/runs/43866952409).

These results apply to those commits. The final coordinator integration PR has its own CI status; check its actual run rather than transferring either result to a different commit. A merge or file inventory is not conversational acceptance.

Author-reported parser/link checks remain recorded in their PRs. The coordinator did not rerun the Full campaign, perform material/model conversion trials, apply sample patches, test a fresh Chat Mode session, configure a Project/GPT, import into SillyTavern or conduct roleplay. A cloud-container clone attempt failed at DNS resolution; repository inspection and writes used the connected GitHub tools instead. No local checkout/build success is claimed.

## 4. Phase C entry and owned work

Phase C is package preparation, not public release or deployment. Create `lite-docs` from the coordinator-confirmed final integration SHA; submit its PR to `lite-phase-0-design`, without merging or modifying production branches. Reuse the existing common contributor brief and the four design contracts.

Owned outputs under `distributions/chat-mode-lite/`:

- `packages/portable/`: self-contained starting path, reference mapping and checkpoint/resume guidance.
- `packages/chatgpt-projects/`: actual Project instruction text, setup guide, upload map and resume guide.
- `packages/custom-gpt/`: GPT instruction text, configuration/starters, knowledge map, Preview cases and compatibility/migration guidance.
- `README.md`, `README.zh-CN.md`, `PACKAGE_CONTENTS.md`, `LICENSE` and `THIRD_PARTY_NOTICES.md` with accurate material boundaries.

Package from the maintained core/workflows rather than writing independent policies. Core and detailed references may exceed a host's active-instruction budget; do not blindly paste the complete source tree into that field. Verify current limits, keep essential behavior active, and provide explicit reference-content access/fallback. Instruction compression must preserve policy meaning and disclose unavailable material.

The corpus contains maintainer notices/links and illustrative expected outcomes. Make extracted-package paths self-contained and include required notices locally; repository-root links are not a standalone license bundle. Exclude design records, review receipts, test answer keys, private material and real checkpoints from default reusable knowledge. If illustrations are offered separately, identify them clearly and keep future test answers out of clean trial contexts.

Verify current official host documentation and actual account eligibility at packaging time. Earlier lifecycle notes are dated evidence, not an evergreen assumption. Preserve preparation of both requested ChatGPT-tailored packages; mark unavailable deployment checks blocked rather than silently dropping a package or claiming account installation. Do not start a separate plugin architecture.

Canonical workflow files, preferences, source records and Full code are outside Phase C ownership. Report a concrete cross-owner defect to the coordinator; do not silently alter semantics while packaging.

## 5. Remaining evidence gates — not pre-C authoring blockers

| Gate | Current state and required next evidence |
| --- | --- |
| T1 output selection | Not run. Use bounded actual trials and a usable application route before choosing a default or conditional policy. |
| T2 fresh-session recovery | Not run. Use the existing fixture and truly isolated initial/resume conversations; a checkpoint example is not a pass. |
| T3 host-package checks | Not run. Requires the prepared packages and actual available host configuration. |
| SillyTavern import / roleplay | Not observed for Lite. Do not inherit Full acceptance or infer importability from JSON appearance. |
| Publication | Not authorized by pre-C completion. No release, tag or production-channel advancement. |

Packaging may proceed while T1/T2 remain explicitly unperformed; do not freeze support claims or select an output winner in package prose. Independent QA can use the integrated source candidate and later package candidate. Use cost-effective GPT testing instances and the smallest synthetic tests that resolve specific risks; do not launch paid model APIs or repeat historical Full tests.

The proposed Full-edition continuation refinement remains separate follow-up work. Existing multi-chapter selection is not absent, and changing frozen source registration requires its own reviewed design. It is not a dependency or authorization to modify Full during Phase C.

## 6. Protected branches and final handoff

Production/development channel heads observed before integration:

| Branch | SHA |
| --- | --- |
| `main` | `503f2eb5ee252f29140969a9605d67b81983e01a` |
| `yuri-dev` | `e8b00854654f504938e28da98340419cbd83d07e` |
| `yuri-plugin` | `9144c11eeef91eaf7b69e2527c4eb6fb8e41ee9c` |
| `Gemini-plugin` | `626c0823b4063b2930f84d2a57ad73b8e224bf2b` |
| `DSH-plugin` | `95c02b53152fc2b805735b18d0c73d205ad387cf` |

This work does not advance these branches, publish artifacts, install anything in an account or delete development branches. Final completion requires read-back of the integration PR/merge SHA, its actual CI result and the combined file scope. Record that final baseline in the coordinator handoff; the mutable branch name alone is insufficient.
