# Project state

Current release: **1.2.1**, authorized by the maintainer on 2026-11-19 after multiple rounds of independent character-card conversion testing of 1.2.1-dev.1 with positive results. The exact accepted checkpoint is `e8b00854654f504938e28da98340419cbd83d07e`; its supplied DSH archive has SHA-256 `20790be50ee62d6a35182b062a4933c17edfbd013cfd471164537158f5f49434`. All 550 packaged extension/dependency resource files were compared with that checkpoint and matched before release edits.

`main` holds official source, `yuri-dev` continues development and `yuri-v1.2.1` identifies this release. The official workflow builds portable/Gemini/DSH assets, records exact source and checksums, and advances installation channels with normal ancestry. Separate Lite development remains outside this release.

This release retains the tested V2/V3 mirror and fenced HTML display-copy fixes. Release edits update documentation, version identifiers, inventories and portable host compatibility descriptions; they do not change conversion policies or algorithms. README credits upstream TavernWeave's Claude Code adaptation and documents ZCode through the existing Claude-compatible manifest and Cursor through the root Agent Plugins manifest. Official installation documentation was checked on 2026-11-19; live installation/discovery/conversion acceptance for these three hosts remains pending.

Four canonical Yuri workflows plus 23 unchanged TavernWeave dependencies provide 27 discoverable entries. Portable/Gemini expose four wrappers; DSH registers canonical workflows directly. Keep complete shared resources and existing license boundaries. Upstream TavernWeave remains pinned at `f9863d2b05305457fe9ed8b0c5688d52aca400a5` (2.4.0); no upstream adoption is part of this release.

The maintainer's positive independent conversion trials are user-reported evidence. Release preparation checks package integrity, metadata/resource paths and provenance without repeating model/card/image trials. Historical dated reviews, host acceptance and earlier limitations remain available in their original records. The previous 1.2.0/1.0.0/0.5.0 releases and separate frozen Workbench v1.2.0 remain unchanged.

Earlier implementation and validation records: docs/CARD_LAYOUT_FIX_2026-11-13.md, docs/HOST_ACCEPTANCE_2026-11-13.md, docs/CUSTOM_PROFILE_TRIAL_REVIEW_2026-11-13.md, docs/UPSTREAM_SYNC.md and docs/ARCHITECTURE.md. Private casework is not included in public packages.
