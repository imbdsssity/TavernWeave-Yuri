# Yuri Card Workbench 1.2.1

A specialized Yuri product distribution built on the TavernWeave ecosystem, with its own workflows and execution contracts. Native skills-only plugin: original conversation, inherited JSON/PNG, supplied posts and novel TXT/EPUB excerpts. The four yuri entries share the packaged TavernWeave dependencies.

Supports Codex/ChatGPT Work, Claude Code, ZCode and Cursor through this complete portable bundle. The Claude Code adaptation draws on upstream TavernWeave's plugin structure and skill discovery; ZCode uses the Claude-compatible manifest and Cursor uses the root Agent Plugins manifest. See the installation guide for commands and host-specific acceptance limits.

Counting: 4 canonical Yuri workflows, exposed through 4 discovery wrappers, plus 23 upstream dependency entries = 27 discoverable entries. The wrappers bind those workflows; they are not four additional workflows. Internal modules are not discovery entries.

[English guide](extensions/yuri-creation/README.md) · [中文说明](extensions/yuri-creation/README.zh-CN.md) · [Install / 安装](extensions/yuri-creation/docs/NATIVE_HOSTS.md)

Install/enable through your host, then start a new task and ask it to list the four yuri skills. This generated branch is a complete plugin folder, not the editable development source. Do not copy individual wrappers into a standalone skills folder. No hooks, MCP server, keys or global rule changes are installed.

Source revision: `ee8eedc1104deb001160615f14950fb805684484`. See NATIVE_PLUGIN.json for package evidence. Account installation, actual skill discovery and live host execution remain separate checks.

Licensing: original additions are MIT; the unchanged TavernWeave base retains its root LICENSE, Required Notice and third-party terms. See NATIVE_LICENSE_BOUNDARY.md and THIRD_PARTY_NOTICES.md.
