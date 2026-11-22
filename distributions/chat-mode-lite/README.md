# Yuri Card Workbench Lite

[简体中文](README.zh-CN.md)

Create an original yuri roleplay card, adapt a supplied JSON/text card or worldbook, or turn a supplied post or novel passage into a playable card and worldbook draft through conversation. Novel work can span declared chapter batches with explicit checkpoints.

This is an **unreleased package preparation candidate** (`lite-packages/C.2`), based on `4bdf78f9a8895d8778776e40d2efe8fb1ce6ba95`. The integrated workflows are included; bounded agent trials found defects; output selection, recovery acceptance and real-host acceptance remain open. It does not inherit Full's binary editing or lossless-preservation guarantees.

## Choose a starting path

| Package | Start here | How to use it |
| --- | --- | --- |
| Portable | [Usage](packages/portable/USAGE.md) | Paste START_HERE.md, then the selected reference sections and your request. No tools or attachments are required. |
| ChatGPT Projects | [Setup](packages/chatgpt-projects/SETUP.md) | Apply PROJECT_INSTRUCTIONS.md in the project instruction setting; add the one REFERENCE_PACK.md source. |
| Custom GPT compatibility | [Configuration](packages/custom-gpt/CONFIGURATION.md) | Where an editable GPT is available, apply GPT_INSTRUCTIONS.md and add REFERENCE_PACK.md as knowledge. Check lifecycle/eligibility first. |

Each folder contains complete references, a source map, a package manifest, dated host notes and local licenses/notices. You can copy one folder independently of the rest of the repository. These are manual text setup packages; a ZIP is not an automatic host installer. No script or plugin installation is needed to use them.

The instructions and reasoning guidance stay in English; speak with the assistant in Chinese or English and specify the desired draft language. Defaults recognize author-defined adult women, including virtual/nonhuman women, focus on the main cast, preserve background identities, and change relationship outcomes only when an authorized circumstance supplies a specific causal reason. You can state preferences in ordinary language.

## Begin or continue

- Original: “Create an original yuri card. You decide ordinary details; include a playable opening and useful worldbook.”
- Existing card: supply JSON/text, identify the intended revision and authorized changes. Output is still experimental: complete JSON, exact field replacements and guarded patches have no selected default. A review draft is usable for discussion; it is not an applied or imported card.
- Post: paste the account and identify whether comments/updates are included. The poster's runtime role stays `{{user}}`; reported claims and invented fiction stay distinct.
- Novel: give title/edition if known, the total chapter/excerpt goal, current text and any opening-stage constraint. Supply the next batch as needed; a smaller batch does not reduce the total goal.

At a pause or handoff, ask for the current checkpoint. Copy the assistant's complete twelve-group `yuri-lite/checkpoint/v1` record, current draft where needed, and relevant source text. In a new conversation, make the package active again, paste the resume prompt from REFERENCE_PACK.md and the checkpoint, then provide the next material and any changed decisions. Project history is a convenience; explicit accepted state remains necessary. Never add real checkpoints or private chapters to reusable shared GPT knowledge.

For PNG cards supply decoded JSON; for EPUB supply extracted text. Lite does not decode/repack those containers. Attachments, web/images, code, downloads and saving are optional capabilities; pasted text remains the fallback. A whole chapter is reviewed only after its entire required work is actually reviewed, not because it was uploaded, indexed or summarized.

## Readiness and terms

See [package inventory](PACKAGE_CONTENTS.md), [current host findings](packages/HOST_REQUIREMENTS.md), [policy mapping](packages/PARITY.md) and [checks/remaining gates](packages/CHECKS.md). T1 selection and T2 recovery acceptance remain open after bounded agent trials; T3, Lite SillyTavern import and human roleplay remain unperformed. No output winner, general size limit or host compatibility guarantee is selected.

Official host guidance was rechecked on 2026-11-16. It describes a Custom GPT transition; the compatibility package remains prepared, with portable/Projects fallback. Account creation/editing rights and numerical limits were not verified in an account. Follow the dated host notes and owning workspace notice before setup; preparation does not deploy or publish anything.

Retain [LICENSE](LICENSE), [THIRD_PARTY_NOTICES.md](THIRD_PARTY_NOTICES.md) and [the original Yuri MIT grant](licenses/YURI-MIT.txt) when redistributing. This combined distribution is not all-MIT.
