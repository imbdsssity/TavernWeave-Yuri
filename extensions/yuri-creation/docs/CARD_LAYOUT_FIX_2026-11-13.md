# V3 mirrors and fenced-menu development fix

The user supplied an agent issue against 1.2.0, describing stale top-level/data
prose and an htm-fenced opening menu. The private source card was not attached;
its filename or narrative is not copied into public test fixtures. Regressions
use one small synthetic V3 layout through a cost-effective GPT testing agent.

The released source already refuses one-sided edits when original top/data values
are exactly equal. The reported equal-copy explanation is therefore not reproduced
by the synthetic baseline. Its actual gap is the conditional guard: pre-existing
divergent copies skip validation. The new check requires explicit edits on both
sides of an affected mirror and equal final values regardless of prior equality.
It also handles nested greetings and tags. Unedited divergence stays untouched.
Inspection returns mirrors, divergent mirror names and related renderer copies,
so the agent can plan against the actual layout. Errors name exact missing paths.

Default code/fence protection remains in force. The explicit per-change html_text
mode permits text-node changes inside HTML and html/htm fences, with inert token
comparison preserving tags/attributes, scripts/styles, comments, macro expressions
and structural slots, fence delimiters, and other language-fence bodies. It never
renders HTML or executes code. An acknowledgment alone cannot bypass the checks.

Exact opening/greeting copies in known regex replaceString fields are included
in inspection and coordinated validation. Only such identified display copies
can use the same text-only mode; findRegex, flags, enablement, IDs, arbitrary
replacement strings and unknown extension data remain protected. All copies are
recorded in the normal plan and output receipt; no post-export patch is needed.
Template/JavaScript/CSS/attribute changes beyond this mode still require the
existing scoped UI/regex engineering route and cannot be claimed as completed
by a display-text edit.

The regression verifies container/layout and deterministic edit guarantees. It
does not establish a fresh native installation, private-card conversion, actual
HTML rendering or SillyTavern import/roleplay success. This development checkpoint
is merged into yuri-dev and supplied as a test TGZ; main, official release tags
and public installation channels are not advanced.

Focused regression evidence: GPT-6 Luna passed five stdlib unittest cases in tests/test_card_layout.py. They cover equal/divergent source mirrors, nested greetings/tags, coordinated HTML/regex display copies, immutable code/attributes/macro slots/fences, rejected outputs and preserved unknown configuration/worldbook data. The equal-versus-divergent baseline comparison used the same synthetic fixture. No real/private card or live import was repeated.
