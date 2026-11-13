# Yuri Card Workbench 1.0.0 for Gemini

Install this complete bundle as a Gemini CLI extension:

```sh
gemini extensions install https://github.com/imbdsssity/TavernWeave-Yuri --ref Gemini-plugin
gemini extensions list
```

Restart Gemini CLI, then check /skills list for the four yuri workflows. Gemini CLI discovers bundled skills automatically; the agent loads their canonical workflows and dependencies as needed. Task mode retains the individually imported skill route. Keep the complete shared folder available in either case.

[English guide](extensions/yuri-creation/README.md) · [中文说明](extensions/yuri-creation/README.zh-CN.md) · [Installation and limits](extensions/yuri-creation/docs/NATIVE_HOSTS.md)

Built from `5ab97e2dd36cda9cf97e9e131fa5d719be48cf80`. See NATIVE_PLUGIN.json and NATIVE_LICENSE_BOUNDARY.md. The root gemini-extension.json loads GEMINI.md and skills/ contains the discoverable entries. User-reported Gemini CLI extension import/discovery passed; this build does not repeat installation or card conversion.
