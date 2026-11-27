# Phase C checks and remaining evidence

Exact base: `4bdf78f9a8895d8778776e40d2efe8fb1ce6ba95`; branch `lite-docs`; PR target `lite-phase-0-design`. Package marker `lite-packages/C.2` is an unreleased preparation revision, not a published product version.

The requested pre-Phase-C handoff and all four original design documents were read at the exact base, followed by the sixteen integrated runtime/reference/template files and applicable repository/extension terms. The final integration base's own CI was read directly: [validate run 43869743253](https://github.com/imbdsssity/TavernWeave-Yuri/actions/runs/43869743253), with `repository` and `portable-plugin` completed successfully. That is base evidence, not the Phase C candidate's result.

## Conversation D follow-up — 2026-11-22

The private QA package tested C.1 candidate `45b8fa54db4b2c59b8950e0f135d5787a0ee426a`. Bounded agent trials passed small complete-JSON and field-replacement artifact checks, but found incorrect Unicode in the guarded patch, inconsistent player binding in post/novel drafts, later-event leakage, an unclear original yuri premise and a depth-prompt scope error. The supplied-card result remained partial because protected status content conflicted with the adaptation. T1 has no selected winner; T2 was not accepted. Private inputs and outputs are not part of this repository.

The follow-up strengthens actual-output review in the active instructions without changing the sixteen canonical sources, deciding an output format, or migrating protected status code. These are instruction changes, not proof the model will comply. The 2026-11-22 ChatGPT Project attempt ended at the sign-in screen. The subsequent signed-in run is recorded below. The 2026-11-16 observations in Static preparation checks describe the pre-QA candidate.

## Signed-in C.2 validation

On 2026-11-27 the tester set up a signed-in ChatGPT Project with C.2 instructions and `REFERENCE_PACK.md` as the sole project source. They confirmed that the saved instructions retained the C.2 marker and ending. Both smoke prompts ran in separate fresh chats with **GPT-6.2 Sol High**. The tested package is [C.2 at `259e091`](https://github.com/imbdsssity/TavernWeave-Yuri/commit/259e0915841260443edba8b35c87489549d7213a). The package commit's [GitHub Actions validation](https://github.com/imbdsssity/TavernWeave-Yuri/actions/runs/45035299148) also passed.

| Check | Result | Evidence |
| --- | --- | --- |
| `manual/reference-probe.txt` | Passed | The reply quoted the failure rule from `references/card-output.md` and described the assembled card as the complete JSON produced by applying a patch to the specified source revision. |
| `prompts/smoke-original.txt` | Passed | The Markdown draft established a clear yuri premise, left the player's choices open, and included a playable greeting and three substantive worldbook entries. |
| SillyTavern import and live play | Verified by the tester | The tester confirmed successful import and live play. The Project smoke response was Markdown. The imported artifact, the steps used to prepare it, and the SillyTavern version are unspecified. |

## Static preparation checks

Observed locally on 2026-11-16:

- The checkout started at the exact requested base on `lite-docs`. The package helper compared all sixteen canonical bodies byte-for-byte with Git objects at that base. No canonical instructions, references, templates, examples or design records changed.
- `python -B distributions/chat-mode-lite/packages/build_packages.py --check` passed: generated-byte parity, source/base equality, version mapping, inventories, local links/anchors, same active rules in all three forms and the local text budget. Active entries have **7,895 characters / 7,897 UTF-8 bytes**. The 7,900-character design budget is not a verified host limit.
- Each REFERENCE_PACK.md has sixteen complete source bodies and **121,145 UTF-8 bytes**. Portable has 10 files, Projects 11 and Custom GPT 12 (including each manifest). Complete file inventories and actual source/rendered/file SHA-256 values are included. The upstream root terms and Yuri MIT grant were copied verbatim from the exact base.
- Created the optional three ZIPs twice in temporary QA directories. Each pair was byte-identical. Checked ZIP CRC, extracted every package, independently checked every manifest size/digest and exact file set, and verified that relative links resolve within the extracted folder. No design/example/QA bodies or real user state were included. These temporary archives are inspection artifacts, not a published release.
- Python AST parsing passed for the package helper. Static semantic mapping and bilingual guide review covered the actions, defaults, source/player/relationship rules, checkpoint/resume requirements, output uncertainty and text fallback listed in PARITY.md.
- `git diff --check` passed. A scoped diff confirmed canonical paths unchanged; the final PR file list is limited to Phase C files under `distributions/chat-mode-lite/`. Full code, workflow CI definitions, production metadata and release versions were not edited.

No authored case or static check is conversational evidence. Existing repository CI may run automatically for this PR; inspect the exact candidate check status separately, without transferring the base's successful result. No additional Full campaign was launched locally.

## Remaining checks

| Gate | State and next evidence |
| --- | --- |
| T1 existing-card delivery selection | Open after bounded agent trials. Complete JSON, inspected field replacements and guarded machine-readable patches remain candidates without priority/size threshold. Requires the same bounded synthetic target/change, actual application route and resulting artifact checks. |
| T2 isolated recovery | Not accepted after a bounded fresh-agent trial. Requires the one existing novel fixture and genuinely separate initial/resume conversations; source examples and static record review cannot pass it. |
| T3 portable/Projects/GPT | The signed-in ChatGPT Project setup, reference probe, and original-card smoke test passed on one account. Project recovery, the portable path, Custom GPT compatibility, and broader account eligibility and limits remain open. |
| Additional C.2 workflow tests | Post and novel player binding, opening-stage knowledge, and exact edits still need targeted retests. |
| Large inputs / new hosts | Unverified; no universal batch size, output threshold or context guarantee. |
| Publication / migration | Not performed or authorized. No release/tag, account installation, migration, production advancement or PR merge. |

The optional package checker is maintainer tooling, not a Lite runtime dependency. In the original Phase C preparation, no paid model APIs, material/model conversion trials, fresh Chat Mode recovery trials or repeated Full test campaign were run. Public documentation establishes host guidance; only account observations can establish eligibility, field acceptance or actual deployment behavior.
