# Yuri Card Workbench 1.2.0 for Gemini

A specialized Yuri product distribution built on TavernWeave. Four canonical workflows are exposed through four wrappers; with 23 upstream dependencies this gives 27 discoverable entries. Internal implementation modules are not additional entries.

Install this complete bundle as a Gemini CLI extension:

```sh
gemini extensions install https://github.com/imbdsssity/TavernWeave-Yuri --ref Gemini-plugin
gemini extensions list
```

Restart Gemini CLI, then check /skills list for the four yuri workflows. Gemini CLI discovers bundled skills automatically; the agent loads their canonical workflows and dependencies as needed. Task mode retains the individually imported skill route. Keep the complete shared folder available in either case.

[English guide](extensions/yuri-creation/README.md) · [中文说明](extensions/yuri-creation/README.zh-CN.md) · [Installation and limits](extensions/yuri-creation/docs/NATIVE_HOSTS.md)

Built from `503f2eb5ee252f29140969a9605d67b81983e01a`. See NATIVE_PLUGIN.json and NATIVE_LICENSE_BOUNDARY.md. The root gemini-extension.json loads GEMINI.md and skills/ contains the discoverable entries. User-reported Gemini CLI extension import/discovery passed; this build does not repeat installation or card conversion.
