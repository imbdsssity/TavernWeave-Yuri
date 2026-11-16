# Package contents / 包清单

Candidate `lite-packages/C.1`, exact base `4bdf78f9a8895d8778776e40d2efe8fb1ce6ba95`. No release or host acceptance is claimed. / 候选准备版本，不代表发布或宿主验收。

## Maintained source and generated delivery

Five instruction files, seven references and four templates remain canonical outside packages. All sixteen bodies ship in each REFERENCE_PACK.md, with navigation-only link rewrites. Their Git blobs, source/rendered hashes and versions appear in each MANIFEST.json. Source files are unchanged. / 五个指令、七个参考、四个模板仍为规范来源；每包包含全部正文，仅重写导航链接。

| Area | Treatment / 处理 |
| --- | --- |
| packages/ACTIVE_INSTRUCTIONS.md | One maintained host-adapter condensation; byte-identical copies in all three active entries. / 唯一有效指令适配源，三包逐字相同。 |
| packages/HOST_REQUIREMENTS.md | Dated official findings, copied into each standalone folder. / 带日期的官方资料核查，随包复制。 |
| packages/build_packages.py | Optional maintainer regeneration/check/archive helper. Never a chat-runtime requirement. / 可选维护工具，普通使用不需要。 |
| packages/PARITY.md and CHECKS.md | Maintainer mapping and observed checks/evidence gaps; not reusable knowledge. / 维护映射与检查记录，不作为知识上传。 |
| README.md and README.zh-CN.md | English/Chinese entry guides with identical behavioral scope. / 双语入口指南，行为范围一致。 |
| LICENSE and licenses/YURI-MIT.txt | Verbatim root/extension terms, also in every folder. / 原样许可，同时随每个包提供。 |
| THIRD_PARTY_NOTICES.md | Applicable material boundaries, copied locally into each folder. / 适用材料边界，随包提供。 |
| design/, examples/ | Remain in source repository, excluded from reusable packs and optional package archives. / 仅保留在来源仓库，默认包和归档不包含正文。 |
| Real material/records and Full | No private source/checkpoint or Full runtime is packaged or modified. / 不打包私人材料或 Full 运行时。 |

## Standalone file inventory

### packages/portable/

- `HOST_REQUIREMENTS.md`
- `LICENSE`
- `MANIFEST.json`
- `REFERENCE_PACK.md`
- `SOURCE_MAP.md`
- `START_HERE.md`
- `THIRD_PARTY_NOTICES.md`
- `UPLOAD_MAP.md`
- `USAGE.md`
- `licenses/YURI-MIT.txt`

### packages/chatgpt-projects/

- `HOST_REQUIREMENTS.md`
- `LICENSE`
- `MANIFEST.json`
- `PROJECT_INSTRUCTIONS.md`
- `REFERENCE_PACK.md`
- `RESUME_GUIDE.md`
- `SETUP.md`
- `SOURCE_MAP.md`
- `THIRD_PARTY_NOTICES.md`
- `UPLOAD_MAP.md`
- `licenses/YURI-MIT.txt`

### packages/custom-gpt/

- `COMPATIBILITY_AND_MIGRATION.md`
- `CONFIGURATION.md`
- `GPT_INSTRUCTIONS.md`
- `HOST_REQUIREMENTS.md`
- `KNOWLEDGE_MAP.md`
- `LICENSE`
- `MANIFEST.json`
- `PREVIEW_TESTS.md`
- `REFERENCE_PACK.md`
- `SOURCE_MAP.md`
- `THIRD_PARTY_NOTICES.md`
- `licenses/YURI-MIT.txt`

Each manifest records byte sizes and actual SHA-256 values for every other file. Copy an entire host folder, retaining notices; no symlinks or parent-folder runtime dependencies are used. Only the reference pack is a knowledge upload. Setup/Preview documents and assessment criteria stay outside clean trial contexts. / 每份清单记录其他全部文件的大小和实际哈希。完整复制宿主目录并保留声明；没有符号链接或父目录运行依赖。仅参考包作为知识上传，设置／Preview 及判断标准不进入干净测试上下文。
