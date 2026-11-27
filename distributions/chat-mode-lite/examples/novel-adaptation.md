# Illustrative novel adaptation — The Lantern Archive

**Status: Authored illustration, not observed test evidence.** These are staged inputs, a draft sketch and expected reconciliation examples, not a transcript, model trial, measured recovery result or completed whole-novel adaptation. Use [NOVEL.md](../instructions/NOVEL.md) and the existing [continuity template](../templates/continuity-record.md); this example adds no checkpoint protocol or source ledger.

## One canonical fixture, two scope choices

The only source is [The Lantern Archive, revision 1, V1](novel-continuation-source.md), ordered C1 → C2 → C3 → C4, with its original paragraph labels. Do not duplicate or rewrite the fixture. Although its file contains all four chapters, the availability described below is hypothetical staged input, not evidence that a host read every chapter.

| Hypothetical request | Authorized scope and completion meaning |
| --- | --- |
| “Use C1 only; open before the tea answer.” | A bounded excerpt: C1.P1–C1.P3. C2–C4 are outside scope; finishing C1 is not finishing the novel. |
| “Use C1–C4 in order, in small batches; keep the opening at C1.P3.” | Sequential project: all ten paragraphs through C4.P2. A C1–C2 reading/extraction batch cannot silently reduce that goal or establish completed adaptation/review. |

The following illustration uses the second request. The hypothetical requester selects Iris as the player, Nera as the card NPC, English prose, an unanswered Monday invitation and continued uncertainty at that opening. Ordinary atmosphere/voice details are delegated. No pairing outcome, name change or current player response is delegated.

## Initial batch: C1–C2 only

Assume only C1.P1–C2.P2 is supplied in the initial session. The assistant maintains `lantern-archive` as source ID and stable local labels `e-iris`, `e-nera` and `e-rook-candidate`. The last is an unresolved identity candidate, not evidence of a separate courier.

| Claim ID | Initial source basis | Uncertainty retained |
| --- | --- | --- |
| `n-cast` | C1.P1: Iris, 27-year-old woman restoring notebooks; Nera, 30-year-old woman maintaining the archive. | Explicit within the fiction; source identity stays separate from player binding. |
| `n-key` | C1.P2: note signed Rook; Nera pockets a key. | The observer cannot identify that key or Rook. |
| `n-tea` | C1.P3: tea invitation, narrator wants to accept but has not answered. | No confirmed date; no scripted current player response. |
| `n-visit-estimate` | C2.P1: gatekeeper reports dawn, then doubts the time; she heard footsteps, not a face. | An uncertain witness estimate, not established timing or identity. |
| `n-courier-guess` | C2.P2: Iris imagines Rook is a separate courier. | Explicit inference, not a confirmed person. |
| `n-sale-rumor` | C2.P2: a rumor says notebooks were sold; Nera denies selling them. | The rumor/denial are reported; neither proves the underlying event. |

The initial batch's goal is reading/extraction, not final adaptation. Its illustrative checkpoint therefore leaves adaptation/review incomplete. Later evidence and early-stage runtime knowledge remain separate.

## Illustrative provisional draft — novel-card/r1

This small review sketch is authored example content, not a validated card. The manner, lamplight and exact speech are delegated creative additions `n-voice`. Both main characters are already adult women; no fictitious before-transformation history is needed.

**Name:** Nera Moss

**Description/voice:** The thirty-year-old archive maintainer, speaking with practical warmth. She has introduced `{{user}}` to the workroom. Her private motives are not established by the initial source account.

**Scenario:** Monday afternoon at C1.P3, before `{{user}}` answers the tea invitation.

**First message:**

> Nera pauses at the workroom door, a little lamplight catching its frame. “Would you like tea after work?” She waits, leaving the invitation unanswered.

**Worldbook sketch:**

| Title / keys | Content at the Monday opening |
| --- | --- |
| Lantern archive / lantern archive; north cabinet | Notebook-restoration workplace; north cabinet locked. No later explanation is included. |
| `{{user}}` / `{{user}}` | A 27-year-old woman newly hired to restore the notebooks and newly acquainted with Nera. Her current answer is the player's choice. |
| Tea invitation / Nera; tea | Nera has invited `{{user}}` for tea; no romantic intent or accepted invitation is established at this stage. |

Neither Tuesday's witness/rumor nor later answers belong in this active Monday worldbook. The draft is provisional and does not establish that C1–C4 has been adapted or reviewed.

## Illustrative checkpoint after the reading/extraction batch

This is a compact rendering of `yuri-lite/checkpoint/v1` with all twelve existing groups. Progress below is assumed for illustration, **not observed progress or a completed trial**. Nothing is claimed saved.

### 1. Identity

Project `illustrative-novel`; workflow `novel-excerpt-to-yuri-card`; protocol `yuri-lite/checkpoint/v1`; checkpoint `illustrative-novel-cp1`, revision 1, parent none. Policy `yuri-policy/1.0`, core `lite-core/A1.1`, workflow `lite-source/B2.1`; package unreleased. State: reading/extraction batch complete, paused with adaptation/review incomplete.

### 2. Source

`lantern-archive`, The Lantern Archive, revision 1, V1; order C1, C2, C3, C4. Stable fixture paragraph labels C1.P1–C4.P2, ten paragraphs total. No measured offsets, hash or second edition asserted.

### 3. Scope

Scope revision 1: adapt all C1–C4 in order; opening remains C1.P3. No excluded source portions. Supplied/accessible now: C1.P1–C2.P2 only. Current batch: read/extract C1–C2; illustrative provisional draft limited to the Monday opening.

### 4. Coverage

| Portion, revision 1/V1 | Supplied | Accessible now | Read | Extracted | Adapted | Reviewed |
| --- | --- | --- | --- | --- | --- | --- |
| C1.P1–C1.P3 | Full | Full | Complete | Complete | Partial: opening sketch | Not started |
| C2.P1–C2.P2 | Full | Full | Complete | Complete | Not started | Not started |
| C3.P1–C4.P2 | No | No | Not started | Not started | Not started | Not started |

These are illustrative states. Completed reading/extraction: C1–C2; fully adapted/reviewed coverage: none. Pending adaptation/review starts with C1; first unread authorized location and exact next source request: C3.P1 onward, preferably C3 as the next bounded batch. Next available later portion: none. No chapter or whole-project review completion is claimed.

### 5. Preferences

`example-pref/1`: English; adult main cast; author-defined inclusive women; preserve player persona, backgrounds and uncertainty; `rederive_if_causal`; no pairing targets, overrides or renaming. Anchors: C1.P3 opening, unanswered invitation, mystery retained there and current player agency. All four chapters remain authorized.

### 6. Entities

`e-iris`: Iris Vale, first-person narrator/player, 27-year-old woman; runtime `{{user}}`. `e-nera`: Nera Moss, main NPC, 30-year-old woman (C1.P1). `e-rook-candidate`: signature/identity candidate from C1.P2/C2.P2; may or may not be another person. Gatekeeper remains a background witness, not a transformation target. Names and source IDs are retained.

### 7. Story

Monday arrival/note/key/tea (C1); Tuesday witness estimate and rumor/denial (C2). New colleagues; romantic meaning unresolved. Open threads: Rook, key, notebooks' disposition, unreliable visitor time/identity, invitation and player answer.

### 8. Evidence

`n-cast` C1.P1 explicit; `n-key` C1.P2 unresolved; `n-tea` C1.P3 viewpoint with unanswered invitation; `n-visit-estimate` C2.P1 uncertain report; `n-courier-guess` C2.P2 inference; `n-sale-rumor` C2.P2 reported rumor/denial with underlying event unknown. Initial input contains those passages. If resumed without them, retain these claims/locators as carried context, not reverified.

### 9. Adaptation

`n-bind`: accepted hypothetical request, Iris binds to `{{user}}`; source identity unchanged. `n-stage`: accepted, Monday C1.P3 before the answer. `n-voice`: delegated practical warmth/lamplight/new dialogue in `novel-card/r1`, explicitly invented. No altered source relationship outcome; retain uncertainty and player agency. Adaptation record `example-adaptation/1`; essential choices are included here.

### 10. Knowledge boundary

Read-through C2.P2; opening C1.P3. Player knows the Monday observations and invitation, not Tuesday's testimony/rumor or any later answers. Nera's detailed private knowledge is not established by the initial text; do not infer she lacks knowledge of her own actions. Later discoveries do not advance the opening.

### 11. Output

`novel-card/r1`: provisional Markdown description/scenario/opening/worldbook sketch; not a completed or importable card. Its text is outside this compact checkpoint; supply it too for exact edits in a fresh chat. `n-bind`, `n-stage`, `n-voice` are illustrated as applied; full adaptation/source-to-draft review pending for C1–C4. No observed model/recovery trial, parser check, host setup, import or human roleplay result.

### 12. Handoff

Blocker: C3–C4 not supplied; no contested checkpoint lineage in this illustration. Next action: request C3 text, starting C3.P1. Draft text is also needed before exact draft edits if not carried. Use the [resume prompt](../templates/resume-prompt.md); the checkpoint aids continuity but proves no source reading and substitutes for no unavailable evidence.

## Fresh conversation and later revelations — expected reconciliation

Assume a new conversation receives active CORE/NOVEL instructions, the checkpoint above and the actual revision-1 text of C3–C4. C1–C2 passages and the draft are not assumed available unless also copied. Earlier claims are carried context, not newly reverified. The next reading batch can be C3; C4 remains available but unread until inspected. Do not request the entire earlier fixture for unrelated continuation.

After actually inspecting the relevant later passages, the expected record changes would be:

| New locator | Expected source-record reconciliation | Earlier-opening consequence |
| --- | --- | --- |
| C3.P1 | Add `n-alias-reveal`: Nera uses Rook. Map `e-rook-candidate` to canonical `e-nera`, retaining the provisional ID/history. Mark `n-courier-guess` superseded as a separate-courier theory. | Player at C1.P3 still does not know the alias. Nera's own longstanding use of it does not mean the player knows it. |
| C3.P2 | Add `n-notebooks-loan` and `n-key-explained`: receipts/inventory show a repair loan; the pocketed key was Nera's workroom key. Retain the old uncertainty and rumor reports with correction links; do not pretend the earlier rumor never occurred. | Do not add these explanations to the active Monday opening/worldbook. |
| C3.P3 | Add `n-visit-correction`: shift notes place footsteps Monday evening. Supersede `n-visit-estimate` as a timing estimate; visitor identity remains unproved. | Do not invent an identified visitor or give Monday's player later testimony. |
| C4.P1–C4.P2 | Add `n-friday-date`: Friday's invitation is explicitly romantic and accepted in the source. Monday's invitation was a colleague welcome; record that later clarification without rewriting the earlier evidence as always certain. | Preserve the unanswered Monday player choice. A later accepted source date is not present player consent or authorization to move the opening to Friday. |

These are expected authored mappings to the canonical fixture, not observed recovery results. Review affected inferences, relationship understanding and adaptation choices explicitly. Keep new source understanding separate from the accepted opening and creative design. Do not claim an exact draft edit while `novel-card/r1` text is unavailable.

After a completed C3 batch, emit an illustrative successor such as `illustrative-novel-cp2`, revision 2, parent `illustrative-novel-cp1`, retaining all twelve groups. If C4 was supplied but not read, its read/extract/adapt/review states remain not started and next unread is C4.P1. After a later completed C4 reading batch, reading/extraction may be complete; adaptation/review and full output delivery must still finish before project completion. Those successor records are not asserted to have been produced or saved here.

## Missing, repeated and revised input — expected boundaries

| Hypothetical next input | Required behavior, not a reported test outcome |
| --- | --- |
| Checkpoint plus C4, with C3 missing | Keep total scope C1–C4 and next unread C3.P1. Ask for C3. Read C4 out of order only if explicitly directed; retain the hole and never mark C3 reviewed. |
| Same checkpoint and C3 supplied again | Compare available lineage/claim/decision/draft state. Do not create another Nera, apply `n-bind` twice or count C3 twice. If a newer successor is unavailable, disclose that limit. |
| C2.P2 overlaps a previous batch | Compare revision and boundaries. Retain established unchanged coverage, inspect the unprocessed or changed part and avoid duplicate claims. |
| A declared revised chapter | No revised fixture is invented here. When actual replacement text is supplied, record its edition/revision, preserve old locators/claims and mark affected coverage/drafts for re-review. Unchanged status transfers only where correspondence is established. |
| Only a chapter summary or checkpoint mention | Treat it as summary/carried context. Request relevant original prose for material evidence; do not mark the underlying chapter read or fully reviewed. |

The user gives decisions in ordinary conversation; the assistant updates the same [adaptation record](../templates/adaptation-record.md) and checkpoint lineage. Fresh-session restoration, repeated-resume safety and runtime behavior still need a separately authorized bounded trial. No second fixture, new source-of-truth system or QA result file is created by this illustration.
