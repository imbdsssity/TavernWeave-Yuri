# Card output, application and evidence

Reference revision: `lite-card-workflows/A2.1` · Policy: `yuri-policy/1.0`

Apply [CORE](../instructions/CORE.md) and the [adaptation workflow](../instructions/ADAPTATION.md). This reference specifies candidates and review criteria. **T1 is unperformed in A2; no winner, priority order, size threshold or universal supported mode is selected.** A user's request for a particular candidate is not a release-policy decision or trial evidence.

## State what is being delivered

| Status | Meaning |
| --- | --- |
| Review draft / change specification | Copyable narrative or proposed old/new edits, not an applied card. A complete original text draft can include a playable greeting and substantive worldbook without being an importable export. |
| Candidate JSON / replacements / patch | A proposed delivery in one of the forms below, with target assumptions and unverified limits stated. |
| Assembled revised document | A separate complete artifact after an application route actually produced it; identify the revision and any visibility gaps. |
| Observed check | A named semantic/static review, parser/diff check, format check, actual host import or human roleplay observation. One does not imply the next. |

Keep machine payloads separate from explanations, part labels and reasons. Do not fabricate a downloadable file, hash, applied edit or import result. Tools/file creation are optional; ordinary text review and scoped replacement instructions remain available. A JSON-looking block has no automatic schema, preservation or import guarantee.

For a new original JSON export, establish the requested format from an available specification or inspected example; do not invent a wrapper/schema. Keep character identity, greeting and substantive worldbook represented. Review-format headings are not a serializer. This original-output route does not settle inherited-card D1.

## Three existing-card candidates

The letters identify candidates only, not preference or execution order. Compare viable candidates on the same target revision and authorized change, with the same protected scope.

| Candidate | How it would be used | What must be evaluated |
| --- | --- | --- |
| A — complete JSON | Work on a copy. Supply the entire document with only authorized edits; replace that copy's contents and retain the original. Inspect the complete assembled result before any import claim. | Entire relevant input accessible; complete output; unchanged wrappers/unknown fields/settings, IDs, array order and protected code; correct values/escaping; truncation and practical copy/save effort. |
| B — field replacements | Give each inspected path or unique text anchor, exact expected old value and replacement. The user or an actually available editor changes only those locations on a copy, then supplies/inspects the resulting document. Stop at a mismatch or ambiguous anchor. | Correct target revision and occurrence, clear old/new boundaries, counterparts, JSON escaping where applicable, manual error/effort and whether the final document preserves protected scope. A list of replacements is not itself the final card. |
| C — machine-readable patch | Supply a named standard, exact target/revision, guarded operations and a practical available application route. For JSON Patch, give a JSON operation array; apply to a copy and inspect the result. | Paths/preconditions, preserved technical content, correct standard semantics, failed-target handling, actual availability/usability of the application route and final artifact. A patch alone is not importable card JSON. |

For B, specify whether a value is a JSON literal for a text editor or decoded text for a field editor. A quoted JSON string contains its escapes; a UI field normally receives the decoded text. Do not tell a user to paste JSON quoting blindly into an unknown editor. For prose, use the heading plus unique surrounding text, exact old passage and full replacement. Never replace every matching name globally. An unseen counterpart cannot be marked updated.

For C, JSON Patch uses [RFC 6902](https://www.rfc-editor.org/rfc/rfc6902) with [JSON Pointer](https://www.rfc-editor.org/rfc/rfc6901) paths. For existing narrative-value edits, use `test` guards for expected values and applicable inspected identity/version fields before `replace` operations. Test all relevant guards before changing values. Escape `~` as `~0` and `/` as `~1` within a pointer token; array indices are zero-based and must come from inspection. JSON string escaping is separate from pointer escaping. The replacement target must exist. Do not invent a revision property, path or array index to make a guard appear exact. These limited operations do not authorize adding/removing/reordering entries or replacing protected parent objects.

If a guard/path or document assumption fails, stop that application; do not retry blindly, skip the guard or report partial application as success. Keep the original copy so a failed application cannot overwrite it; do not promise every local patch tool performs rollback. Preconditions cover only what they actually test and do not establish full revision identity or preservation of unseen material. Record the actual application route. If no usable route exists, mark C unavailable/unverified in that context and continue useful review work; do not require a CLI patcher, shell, Python, Node.js, package installation or a new service account.

## Visibility and evidence limits

Preserve accessible, inspected content outside the authorized edit scope. Incomplete input/output visibility prevents complete-document or lossless-preservation claims. Full-document visibility is necessary for A but alone does not prove preservation. Do not reconstruct omitted settings or drop fields to fit. Narrow to an inspected operation or request missing material, without silently reducing the user's total goal.

Record whether a candidate is merely proposed, delivered, applied to a known copy, or checked against an accessible result. If the result is unavailable, application and whole-document preservation stay unverified. With an available parser/diff, compare actual changes with the authorized set and inspect unknown fields and embedded code; report exactly what ran. Without one, label the check semantic/manual inspection. Successful parsing proves neither format compatibility nor actual import. Report actual import and roleplay only when observed for that artifact.

Multipart transport is also test-gated, not an automatic workaround for length. Preserve JSON boundaries/escaping and keep assembly instructions outside payloads; never call missing fragments complete. On capacity limits, mark exact omissions and checkpoint progress rather than truncate protected material.

## T1 handoff — planned evaluation, no results

In a separately authorized bounded trial, QA and the workflow owner use one small synthetic JSON fixture/change through viable A/B/C candidates under comparable host/model/capability conditions. Record fixture and instruction revisions, exact inputs/outputs, actual application route, final artifact and checks. Reuse the same fixture; extend only for a specific unresolved failure. The [edit illustration](../examples/existing-card-edit.md) explains the forms but is not a trial transcript or selected QA fixture.

Evaluate unauthorized changes/omissions, output completeness, old-value/path/ID accuracy, escaping, application effort, recovery, and the assembled artifact. Missing/extra protected fields, wrong-target edits and false validation claims fail the candidate. A route that cannot be applied remains unavailable for that context. Keep parser/diff findings separate from actual host import and human feedback. Record failures as well as successful observations, with their scope.

Choose a default, conditional rule or reduced supported scope only after observed evidence. A small-card result does not prove arbitrary-size or other-host support. Do not invent a success rate, model result or import outcome. A2 runs none of these material trials. Use the existing [adaptation record](../templates/adaptation-record.md) and `yuri-lite/checkpoint/v1` [continuity record](../templates/continuity-record.md) for actual project decisions and handoff, leaving output form undecided/test-gated unless an explicitly requested candidate is being described as such.

Derived from the shared Lite output contract and Full's inherited-card limitations at the A2 base. This is a conversational replacement for Full tool-backed application, not its lossless or binary guarantee. Attribution and applicable terms: [CORE provenance](../instructions/CORE.md#provenance-and-a1-differences).

Required Notice: Copyright 2026 LiarMTTT
