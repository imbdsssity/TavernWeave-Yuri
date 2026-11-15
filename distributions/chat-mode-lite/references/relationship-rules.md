# Relationship policy

Reference revision: `lite-core/A1.1` · Policy: `yuri-policy/1.0`

Apply [CORE.md](../instructions/CORE.md)'s authority order and protected scope. An identity change does not itself change orientation, motives, history, pairing or outcome. Friendship, rivalry, hostility, dependence, kinship and power do not establish romance or consent. `allowed_dynamics` permits a kind of outcome; it does not request one.

| `relationships.outcome_policy` | Required behavior |
| --- | --- |
| `rederive_if_causal` — default | Retain each source outcome unless a specific authorized change in circumstances gives a reasoned causal basis to rederive it. Without that basis, preserve the outcome. |
| `preserve_outcomes` | Keep relationship outcomes fixed. Changed circumstances do not waive this policy. If the user requests an incompatible change, resolve and record the explicit policy override before that edit. |
| `explicit_pairing_targets` | Honor every requested `{a, b, target_dynamic}` using distinct known stable IDs and an allowed dynamic. Change no additional pairs. Preserve source facts and explain the fictional causal changes needed for each altered outcome. |

Pairing targets are nonempty only with `explicit_pairing_targets`. Detect unknown IDs, self-pairs, duplicate/conflicting pairs, disallowed dynamics and conflicts with exclusions or anchors. A pairing request does not silently authorize altering an excluded identity, player persona or protected anchor. Resolve material conflicts rather than selecting whichever policy is easiest. Under other policies, keep `pairing_targets` empty. Preserve source uncertainty under every policy.

For each changed outcome, keep a concise record of the prior source outcome or uncertainty, the actual authorization, specific changed circumstance, causal reason, affected characters/locators and chosen fictional result. Distinguish observed facts from inference and additions. Generic claims such as “they are women now, so they fall in love” provide no causal support. Retained outcomes can be noted as preserved; do not invent a change just to populate a record.

For original creation there is no extracted source outcome to preserve. Choose ordinary initial relationships within the delegated brief; `preserve_outcomes` protects the agreed authored design on revision. Explicit pairing targets still require all requested pairs without additional changed pairs. Do not fabricate a source history or male before-card. Adult women may have independent goals and nonromantic relationships.

Later source revelations may correct a factual claim or viewpoint. Record the prior locator as superseded/viewpoint-limited and review affected adaptation choices; this is not automatic permission to alter an approved pairing or leak future knowledge into an earlier opening. Use `yuri-lite/checkpoint/v1` under [shared contracts §§5–7](../design/LITE_SHARED_CONTRACTS.md#5-sequential-chapter-protocol); the dedicated continuity template remains pending Conversation B.

Review relationship policy in the actual draft, including greetings and worldbook entries. A structured declaration does not prove causal quality, compliance or consent. The `rederive_if_causal` default must never be described as either mandatory relationship change or the stricter `preserve_outcomes` option.

Derived from Full's `references/custom-profiles.md` and `shared/profiles.py` at the A1 base. See [CORE provenance](../instructions/CORE.md#provenance-and-a1-differences) for attribution, terms and the replacement of tool enforcement with conversational review.
