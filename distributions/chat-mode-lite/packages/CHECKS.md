# Phase C checks and remaining evidence

Exact base: `4bdf78f9a8895d8778776e40d2efe8fb1ce6ba95`; branch `lite-docs`; PR target `lite-phase-0-design`. Package marker `lite-packages/C.1` is an unreleased preparation revision, not a published product version.

The requested pre-Phase-C handoff and all four original design documents were read at the exact base, followed by the sixteen integrated runtime/reference/template files and applicable repository/extension terms. The final integration base's own CI was read directly: [validate run 43869743253](https://github.com/imbdsssity/TavernWeave-Yuri/actions/runs/43869743253), with `repository` and `portable-plugin` completed successfully. That is base evidence, not the Phase C candidate's result.

## Static preparation checks

Observed locally on 2026-11-16:

- The checkout started at the exact requested base on `lite-docs`. The package helper compared all sixteen canonical bodies byte-for-byte with Git objects at that base. No canonical instructions, references, templates, examples or design records changed.
- `python -B distributions/chat-mode-lite/packages/build_packages.py --check` passed: generated-byte parity, source/base equality, version mapping, inventories, local links/anchors, same active rules in all three forms and the local text budget. Active entries have **7,895 characters / 7,897 UTF-8 bytes**. The 7,900-character design budget is not a verified host limit.
- Each REFERENCE_PACK.md has sixteen complete source bodies and **121,145 UTF-8 bytes**. Portable has 10 files, Projects 11 and Custom GPT 12 (including each manifest). Complete file inventories and actual source/rendered/file SHA-256 values are included. The upstream root terms and Yuri MIT grant were copied verbatim from the exact base.
- Created the optional three ZIPs twice in temporary QA directories. Each pair was byte-identical. Checked ZIP CRC, extracted every package, independently checked every manifest size/digest and exact file set, and verified that relative links resolve within the extracted folder. No design/example/QA bodies or real user state were included. These temporary archives are inspection artifacts, not a published release.
- Python AST parsing passed for the package helper. Static semantic mapping and bilingual guide review covered the actions, defaults, source/player/relationship rules, checkpoint/resume requirements, output uncertainty and text fallback listed in PARITY.md.
- `git diff --check` passed. A scoped diff confirmed canonical paths unchanged; the final PR file list is limited to Phase C files under `distributions/chat-mode-lite/`. Full code, workflow CI definitions, production metadata and release versions were not edited.

No authored case or static check is conversational evidence. Existing repository CI may run automatically for this PR; inspect the exact candidate check status separately, without transferring the base's successful result. No additional Full campaign was launched locally.

## Unperformed or unavailable

| Gate | State and next evidence |
| --- | --- |
| T1 existing-card delivery selection | Unperformed. Complete JSON, inspected field replacements and guarded machine-readable patches remain candidates without priority/size threshold. Requires the same bounded synthetic target/change, actual application route and resulting artifact checks. |
| T2 isolated recovery | Unperformed. Requires the one existing novel fixture and genuinely separate initial/resume conversations; source examples and static record review cannot pass it. |
| T3 portable/Projects/GPT | Unperformed. Requires actual active-field acceptance, reference access, tools-disabled task and recovery observations. No account configuration was attempted; account eligibility and numerical limits are unverified. A genuinely unavailable GPT route should then be marked blocked, not passed. |
| Lite SillyTavern import / human roleplay | Unperformed. JSON appearance, parsing and Full historical tests do not establish either. |
| Large inputs / new hosts | Unverified; no universal batch size, output threshold or context guarantee. |
| Publication / migration | Not performed or authorized. No release/tag, account installation, migration, production advancement or PR merge. |

The optional package checker is maintainer tooling, not a Lite runtime dependency. No paid model APIs, material/model conversion trials, fresh Chat Mode recovery trials or repeated Full test campaign were run. Public documentation establishes host guidance; only account observations can establish eligibility, field acceptance or actual deployment behavior.
