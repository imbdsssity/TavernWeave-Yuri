# Yuri Card Workbench Lite — Project Specification

**Status:** Phase 0/1 design baseline  
**Target release:** 0.1.0  
**Parent product:** TavernWeave-Yuri 1.2.0  
**Implementation status:** Design only; no workflow migration is authorized by this document.

## 1. Product definition

Yuri Card Workbench Lite is a lightweight, conversation-first edition of the Yuri Card Workbench. It preserves the product's Yuri adaptation methodology while removing mandatory dependence on CLI agents, local runtimes, package installation, shell commands, databases, binary processing and automated filesystem workflows.

Its primary target is ordinary client-facing LLM conversations, including ChatGPT Chat Mode and comparable non-CLI interfaces. It should also remain usable when the host has no Python, Node.js, network access, plugin loader, persistent workspace or sub-agent facility.

Lite is a separate execution edition, not a replacement for the Full edition. Full remains the advanced CLI/plugin distribution. The two editions share behavioral policy and product intent, not necessarily implementation or technical guarantees.

## 2. Product goals

1. Preserve the four user-facing workflows:
   - `yuri-card-creator`: create an original card from conversation.
   - `adapt-yuri-card`: adapt a supplied existing card.
   - `post-to-yuri-card`: adapt a user-supplied post.
   - `novel-excerpt-to-yuri-card`: adapt explicitly supplied novel chapters or excerpts.
2. Preserve core Yuri policies: eligible-character criteria, main-cast scope, background-character treatment, relationship causality, source fidelity, player agency and user authorization.
3. Keep source facts, inference, user decisions and creative additions distinguishable.
4. Produce useful text-based SillyTavern card/worldbook content and transparent adaptation records.
5. Make unsupported capabilities and incomplete processing visible rather than silently substituting or claiming success.
6. Keep the package understandable and usable without requiring the user to complete technical worksheets.

## 3. Non-goals for Lite 0.1.0

Lite does not aim to reproduce Full's execution infrastructure. The initial release excludes:

- PNG card-payload decoding, encoding or repacking.
- Binary-preservation guarantees or byte-identical round trips.
- EPUB archive extraction; users may supply extracted text.
- Automated backfilling, database indexing or persistent source-library transactions.
- Mandatory Python, Node.js, shell, CLI, package installation or network access.
- Native CLI plugin registration, host-specific build systems or generated plugin bundles.
- Autonomous multi-agent orchestration.
- Automated cryptographic hashes, schema validation or programmatic regression tests.
- Arbitrary card-schema migration, executable script modification or runtime debugging.
- Claims of guaranteed lossless preservation when editing a large or partially visible document.

Image generation and web research are optional host capabilities, never required workflow steps.

## 4. Target operating assumptions

The baseline host can:
- exchange conversational text;
- accept user-supplied text and, where supported, file attachments;
- reason over the material actually made available to it;
- return structured text, including JSON and Markdown.

The baseline host is not assumed to:
- expose an editable filesystem or downloadable-file generator;
- read every byte of a large attachment;
- retain state across conversations;
- execute code or validate JSON;
- browse the web or call image tools;
- delegate to other agents.

Every workflow must declare what it actually received and processed. A host feature may improve convenience, but cannot be a prerequisite for the Lite core.

## 5. Supported input and output

### Inputs for 0.1.0

- Conversation-only creative briefs.
- User-supplied JSON character cards and JSON worldbooks, within practical context and output limits.
- Pasted or attached TXT/Markdown text.
- Explicitly selected novel chapters or excerpts supplied as text.

PNG and EPUB files are not directly supported in the first release. If a host can extract their text externally, the user may provide that extracted text, but Lite must not claim to have decoded the original container.

### Outputs for 0.1.0

- SillyTavern-oriented character-card JSON, when the host can return the complete document.
- Standalone worldbook JSON or clearly delimited worldbook entries.
- Markdown source/evidence and adaptation records.
- A field-level change summary.
- Optional JSON Patch-style operations for narrow edits, with explicit paths and preconditions.

If the output exceeds the host's reliable response capacity, Lite must split it into numbered, clearly bounded parts and explain how to assemble them. It must not silently omit fields or claim a complete export when only a partial response was produced.

## 6. Product principles

### 6.1 Preserve the shared Yuri policy

The Full and Lite editions should align on:
- the user's selected definition of women and eligible characters;
- main-cast and background-character scope;
- relationship changes only when supported by the authorized adaptation policy and causal circumstances;
- no inference of romance from hostility or kinship;
- preservation of source uncertainty;
- explicit distinction between source fact, inference and invention;
- player agency and authorization boundaries;
- user control over protected anchors and material changes.

The canonical policy wording and version identifier will be defined in `LITE_SHARED_CONTRACTS.md`. A change to a shared policy requires review for both editions.

### 6.2 Conversational-first, not form-first

Users should be able to express goals in ordinary language. Structured profiles and records are optional aids, not mandatory forms. Ask only for a decision that materially affects the result and cannot safely be inferred.

### 6.3 Honest capability reporting

A workflow must distinguish:
- material supplied;
- material actually visible/read;
- material processed;
- material not supplied or not processed;
- output generated;
- output independently validated (if any).

Model self-review is not a substitute for parser validation or real SillyTavern import.

### 6.4 Conservative editing

For existing cards, preserve supplied content outside the authorized edit scope as far as the host's visible document and output limits permit. When complete input or output cannot be handled reliably, stop and offer a smaller explicit scope or a patch rather than inventing a lossless result.

## 7. Relationship to Full and upstream TavernWeave

- Repository 2 remains the canonical home for Full and Lite product development.
- Lite has its own self-contained instructions and references under `distributions/chat-mode-lite/`.
- Lite must not require loading Full scripts or the 23 upstream skill dependencies at runtime.
- Upstream TavernWeave methods may inform the design, but reused text/assets must retain applicable licensing and notices. Prefer original concise instructions that express the required behavior.
- Generated Full host distributions must not include Lite unless explicitly designed and released to do so.
- The frozen standalone Repository 1 is historical reference material, not a source to synchronize automatically.

## 8. Initial acceptance criteria

Lite 0.1.0 is ready for release consideration when:
1. All four workflows can be followed from their Lite instructions without CLI/runtime dependencies.
2. Each workflow uses the same shared Yuri policy and evidence conventions.
3. No mandatory instruction calls unavailable scripts, tools, upstream skills or host-specific commands.
4. JSON adaptation explicitly states its best-effort preservation boundary.
5. Post and novel workflows accurately identify the supplied/processed scope.
6. Large inputs and outputs have an explicit continuation/partial-output protocol.
7. Chinese and English user-facing instructions agree on behavior and limitations.
8. Static review and conversational acceptance results are recorded separately from actual SillyTavern import evidence.
9. Licensing and third-party notices are complete.

## 9. Release boundary

The initial target is **Lite 0.1.0**, an independently identifiable edition. It does not change the Full product version, Full source, existing plugin branches or existing releases. Release authorization and publication remain a separate human-controlled step.
