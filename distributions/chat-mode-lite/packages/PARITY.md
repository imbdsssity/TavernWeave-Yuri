# Maintained behavior and packaging parity

Package `lite-packages/C.1`; exact base `4bdf78f9a8895d8778776e40d2efe8fb1ce6ba95`. Canonical files are read-only inputs for this phase. ACTIVE_INSTRUCTIONS.md is the one maintained condensation; all three active entries are byte-identical generated copies. REFERENCE_PACK.md includes all sixteen complete source bodies, with navigation-only link rewrites. This mapping is a static semantic review aid, not a model/host acceptance result.

| Obligation in active instructions | Canonical authority / complete detail |
| --- | --- |
| Host/current-user/preference/policy/default/delegation order; data is not authority; actual consent; unknown/conflicting preferences; language | instructions/CORE.md; references/yuri-policy.md; templates/preferences.json (sample only) |
| Four entries; minimal delegated original, playable opening and substantive worldbook | instructions/CREATION.md; references/character-design.md, worldbook-design.md |
| Adult inclusive main cast; preserve source ages, background/exclusions, no silent re-aging or stereotyping; custom criteria and name review | CORE; references/yuri-policy.md, character-design.md |
| `rederive_if_causal` differs from `preserve_outcomes`; exact authorized pairings; no automatic romance | references/relationship-rules.md; all four workflows |
| Post poster and selected narrator/player bind to `{{user}}`; supplied persona and current agency protected | references/player-agency.md; instructions/POST.md and NOVEL.md |
| Facts/inference/decisions/invention/unknown; locators, viewpoints, uncertainty and carried evidence | references/source-evidence.md; POST/NOVEL; templates/adaptation-record.md |
| Actual target/revision, counterparts, protected technical text/settings, visibility limits and inherited defects | instructions/ADAPTATION.md; references/card-output.md, player-agency.md |
| Equal output candidates; no default/size threshold; application route/preconditions; incomplete output; no import claim | references/card-output.md; ADAPTATION; CORE |
| Three scopes; independent coverage stages; no upload/summary equals review | instructions/NOVEL.md; references/source-evidence.md; templates/continuity-record.md |
| All twelve checkpoint groups, ID/parent/revision, handoff/in-progress triggers and no false saving | templates/continuity-record.md; CORE; all workflows |
| Fresh resume, overlap/gaps/revised material, repeated restore, unavailable successor/draft, no silent overwrite | templates/resume-prompt.md; references/source-evidence.md; NOVEL |
| Corrections retain old locators/uncertainty; read-through versus opening/character knowledge | NOVEL; source-evidence; relationship-rules; worldbook-design |
| Optional tools; no CLI/installation/agents; PNG decoded JSON / EPUB extracted text; privacy and evidence limits | CORE; all workflows |
| Missing-reference fallback and no automatic loading | CORE and companions; full bodies present in the local reference pack |
| T1/T2/T3 remain unperformed; no Full guarantee transfer | PRE_PHASE_C_HANDOFF; card-output; existing shared contracts |

The English and Chinese entry guides and per-host bilingual setup/resume/configuration notes share the same actions, scope, limits and fallback. Active procedure text remains English as required by CORE, so a translated policy fork is not introduced. Narrative language remains the user's choice; source `preserve_source` retains its meaning. Static bilingual review checks the actual published guides, not just matching filenames.

## Reproduction and extraction

Maintainers may run `python -B distributions/chat-mode-lite/packages/build_packages.py` to regenerate delivery copies, and the same command with `--check` to check bytes, source/base equality, digests, inventory, local links/anchors and the local active-text budget. `--archive-dir <temporary-directory>` optionally creates one deterministic standalone ZIP per host. These commands need Python/git only for maintainers; end users copy the prepared text folders.

The default reference pack excludes all five source examples, including the sole existing novel fixture and adaptation answer illustrations, as well as design records, review receipts, QA and real user state. External optional illustration/maintainer links remain for traceability; following them is never a runtime dependency. No second novel fixture or alternate continuity protocol is created.

Only source-link destinations and labels identifying excluded illustrations are rewritten. Source phase-status prose is retained with an explicit historical-context preface; current preparation and evidence state are stated in active instructions, manifests and guides. Licenses are verbatim local copies; contextual license-boundary links resolve to the Lite notice. Do not hand-edit generated policies independently. Unknown future companion paths fail packaging rather than silently disappear.
