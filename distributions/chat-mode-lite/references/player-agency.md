# Player binding and agency

Reference revision: `lite-core/A1.1` · Policy: `yuri-policy/1.0`

Apply [CORE.md](../instructions/CORE.md)'s authority order. Keep the source person's identity, the fictional player persona and permission to portray the player's behavior separate. A creative brief, transformation scope or profile flag alone does not delegate current player control.

## Runtime bindings

- **Post:** the poster is the player and consistently becomes `{{user}}` in runtime prose, greetings and worldbook titles/keys/content. Keep the source name/gender/age, exact quotations and evidence IDs separately; never infer unstated identity from voice or stereotypes.
- **Novel:** a selected first-person narrator/player uses `{{user}}`, not a literal “narrator” placeholder. Do not infer an unstated narrator identity. A user-selected source character may also be the player. Third-person material without a source player may use an explicitly invented adult fictional woman; label her as an addition, with no fabricated source dossier.
- **Original or inherited card:** preserve the supplied player persona unless the user authorizes a specific change. Use `{{user}}` for the runtime player, and an NPC name for card `name` when `{{char}}` denotes that NPC. Do not blindly rewrite technical template tokens.

Binding is separate from transformation eligibility: an excluded source player still binds to `{{user}}` without becoming an identity-change target. Source records may identify the poster/narrator analytically; runtime player references must not leave those labels as substitutes for the binding. Named NPCs and other narrators retain their identities.

## Portrayal permission

Without scoped delegation, do not decide the player's current actions, dialogue, thoughts, feelings, decisions or consent. An established persona or source event can inform background without forcing a present response. Do not invent player anger, attraction, agreement or past actions as extracted facts. Treat authorized fictional additions as additions.

Openings can describe the setting, NPC behavior and an opportunity or question while leaving meaningful player choice. Example dialogue must not turn an illustrative player line into binding present behavior. An NPC may misread the player; label the viewpoint rather than declaring the player's inner state true.

Record actual delegated scope, such as a particular scripted scene; do not extend it into later turns or unrelated choices. Current user decisions can revise prior persona choices, with a recorded revision. Renaming a fictional persona never renames the real user.

## Inherited issues and knowledge

Inspect every accessible greeting and relevant worldbook passage. A retained line may already prescribe player thoughts or actions. Record its location and limitation; “unchanged” is not an agency pass. If authorization includes a repair, make the smallest scoped edit and review it. Otherwise preserve protected content, explain the unresolved defect and avoid claiming full compliance.

Keep read-through progress separate from the intended opening stage and each character's knowledge. Later revelations or checkpoint summaries do not grant player knowledge. On resume, restore the accepted persona, binding, agency permissions and knowledge boundary using `yuri-lite/checkpoint/v1`; see [shared contracts §§3, 5–7](../design/LITE_SHARED_CONTRACTS.md#3-source-fidelity-and-player-agency). Dedicated checkpoint/resume files remain pending Conversation B.

Derived from Full's creator/post/novel entries and `references/custom-profiles.md` at the A1 base. See [CORE provenance](../instructions/CORE.md#provenance-and-a1-differences) for attribution and terms.
