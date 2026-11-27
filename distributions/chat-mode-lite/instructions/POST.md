# Post to Yuri card

Workflow: `post-to-yuri-card` · Revision: `lite-source/B2.1` · Core: `lite-core/A1.1` · Policy: `yuri-policy/1.0` · Checkpoint: `yuri-lite/checkpoint/v1`

Use this procedure with the active [shared core](CORE.md). It turns supplied forum/social-post text into a source-grounded fictional card and worldbook draft. Work through ordinary conversation in the user's language; maintain the records yourself. Pasted text is sufficient. No browser, attachment reader, CLI, database or upstream skill invocation is required, and this instruction file does not establish tested host compatibility.

Companion guidance: [source evidence](../references/source-evidence.md), [Yuri preferences](../references/yuri-policy.md), [relationships](../references/relationship-rules.md), [player agency](../references/player-agency.md), [optional preference sample](../templates/preferences.json), [adaptation record](../templates/adaptation-record.md), [continuity record](../templates/continuity-record.md) and [resume prompt](../templates/resume-prompt.md). Use available text, not an assumption that a link was loaded. Runtime use does not require the design directory.

## 1. Establish the available account and intended adaptation

Reuse the user's supplied scope, preferences, exclusions and prior decisions. If no scope is stated, begin with the supplied main post; comments, quoted posts and follow-up updates are separate portions, not silently included. Identify the source title/handle only if supplied, its declared revision or unknown revision, and visible paragraph boundaries. Assign explained local labels when needed. A supplied URL, screenshot filename or thread title does not establish access to the account's full text; request the relevant pasted text if unavailable.

Keep total authorized scope, supplied portions, accessible text and current batch separate. Preserve the total task if only part of a long thread is available. For multiple accounts, record who says what and whether they concern the same person/event; do not merge identities or corroborate a claim merely because it is repeated. Do not fetch further posts or publish private material by implication.

State a useful starting interpretation briefly and proceed with delegated details. Resolve only consequential ambiguity, such as a missing passage needed for an exact change or a preference conflicting with a protected anchor. Do not require the user to fill JSON or a source worksheet. Use the actual preference choices and a human-readable revision; the optional sample is neither adoption nor consent.

## 2. Extract without turning reports into facts

Read the accessible account before adapting it. Maintain stable entity and claim IDs, names/aliases, main/player/background roles, source age/identity facts, chronology, relationship stages, relevant events, open questions and evidence locators using the existing source-evidence guidance. Label source fact, inference, user decision, creative addition and unknown/not supplied separately. An accusation, a reported message or the poster's interpretation is evidence of that account or viewpoint, not independent proof about another person's motives or conduct.

Preserve uncertainty, conflicting versions and missing context. Do not infer unstated gender, age, orientation, attraction or consent from voice, occupation or behavior. Keep source people and real user identity distinct from fictional personas. Posts about real people are supplied accounts, not verified biographies; use fictionalized details only as identified adaptation choices. Preserve real source facts in the records rather than retroactively changing them to fit a fictional cast. Known minors remain outside the adult transformation-target route; do not silently re-age them. An unknown-age adult fictional portrayal is an addition, not evidence of source age.

Quotes and locators must come from accessible text. A paraphrase is not a quotation. Preserve original quotations and evidence IDs even when the output uses different names or pronouns. Summaries and carried checkpoints do not establish that omitted portions were inspected.

## 3. Bind the poster and record authorized choices

The source poster is the player. Map that runtime role consistently to `{{user}}` in descriptions, scenario, every greeting, example dialogue and worldbook titles/keys/content. Keep the source name and stable entity ID in the analytical record. Do not leave “poster,” “OP,” “narrator” or the source name as a substitute for the player's runtime binding. Named NPCs retain their own roles; a quoted speaker is not automatically the poster. Do not rename the real user or fabricate player identity facts.

Binding does not authorize changing a supplied player persona, even if main-cast selection includes that person. Preserve the persona unless a specific change was authorized. It also grants no control over present player actions, dialogue, feelings, decisions or consent. Source events may inform background; an opening at an earlier unresolved moment must leave the response open. Preserve an explicitly chosen story stage and what each participant knows then, even if the post reports later outcomes.

Apply the shared adult-main-cast and author-defined inclusive-womanhood defaults, exclusions, background protection and contextual name review. Do not automatically rename or turn every relationship romantic. Under `rederive_if_causal`, retain source outcomes unless an authorized changed circumstance gives a specific causal reason for rederivation. `preserve_outcomes` is stricter. Honor explicit pairing targets within their exact scope; permitted dynamics are not requested outcomes.

Use the adaptation record for accepted choices, delegated additions, proposed/deferred choices and their authority. Record the original claim/uncertainty, specific changed circumstance, causal reason, affected characters and draft fields. New dialogue, motives, setting details and adult fictional choices are additions even when plausible. A request to adapt a post does not authorize unsupported biographical claims or unrelated changes.

## 4. Write a playable draft

Build from the extracted account and recorded choices; keep source records separate from runtime fiction. Unless the brief selects otherwise, center the card on an NPC interacting with `{{user}}`, with that NPC's name as the card name. Give her an independent goal, recognizable voice and a situation that offers meaningful player choice. Mark unsupported characterization as creative design in the adaptation notes. Choose ordinary details within delegation instead of asking a long design questionnaire.

Deliver a clearly labeled text review draft containing:

- Character description and personality/voice, with the player's binding used consistently.
- Scenario and intended opening stage; the first message describes setting/NPC behavior and leaves `{{user}}` free to respond.
- Useful worldbook entries for setting, people and relationships within that stage. Keep author-only evidence, future revelations and private source identifiers outside active runtime entries. A player entry uses `{{user}}` in its title/keys/content.
- Brief adaptation notes identifying creative additions, retained uncertainty, protected anchors and source/coverage limits. If alternative greetings are supplied, review every one.

Do not require a future character-design or output helper to produce this draft. A Markdown draft is not an importable card. If structured delivery is requested, identify its actual form and completeness; do not infer parser success, importability or binary preservation. Existing-card output selection remains test-gated. If also editing an inherited card/worldbook, apply CORE's inspected-scope protection and visibility limits; report inaccessible portions and offer a narrower operation when needed.

## 5. Review, checkpoint and continue

Inspect the actual draft against the source and effective profile: source/invention separation, causal relationship reasoning, names, exclusions, player persona and agency, all greetings, worldbook bindings, story-stage knowledge and protected anchors. Revise unsupported certainty or accidental player scripting. State exactly what was inspected and any incomplete material; a declaration of compliance is not a check.

Track supplied/read/extracted/adapted/reviewed states independently for the authorized post portions. A batch completes only its declared work; project completion requires every authorized portion to reach the required review stage. If only the main post was processed from an authorized full thread, name the remaining comments/updates. An upload, thread summary or checkpoint mention cannot mark them reviewed.

After each completed batch, on pause and before a planned context handoff, emit copyable `yuri-lite/checkpoint/v1` text using the continuity template's twelve groups: identity, source, scope, coverage, preferences, entities, story, evidence, adaptation, knowledge boundary, output and handoff. Include essential decisions and locators rather than only links. Use an in-progress checkpoint when unfinished, with exact remaining position and one next action. Files and saving are optional; claim persistence only when observed, and promise no background reading.

For a later update or fresh conversation, use the existing resume prompt and source-evidence reconciliation rules. Restore the user-designated checkpoint, source revision, preferences, player binding and draft revision; inventory text actually accessible now. Earlier evidence unavailable here stays carried context, not reverified. Compare overlapping or revised paragraphs before advancing coverage; repeated input must not duplicate facts or apply a decision twice. Retain corrected claims and locators as superseded/viewpoint-limited, review affected drafts and preserve the intended opening. Request only the relevant missing evidence or draft text when needed.

Take feedback in conversation and update the same records and draft lineage. Report static review, conversational trials, parser checks, host setup/import and human feedback separately. See the [illustrative adaptation](../examples/post-adaptation.md); it is not trial evidence.

## Attribution

Based on the integrated Lite core and source guidance at `c57f981e4230be746fe5bdcf3592e2784b8fdbeb`. Retain applicable attribution and terms described in [CORE provenance](CORE.md#provenance-and-a1-differences) when distributing this material.

Required Notice: Copyright 2026 LiarMTTT
