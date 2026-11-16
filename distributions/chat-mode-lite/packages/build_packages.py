#!/usr/bin/env python3
"""Optional maintainer-only, offline Lite packaging; no end-user dependency."""
import argparse
import hashlib
import json
import posixpath
import re
import subprocess
import sys
import zipfile
from pathlib import Path
from urllib.parse import unquote, urlsplit

ROOT = Path(__file__).resolve().parents[1]
REPO = ROOT.parents[1]
BASE = "4bdf78f9a8895d8778776e40d2efe8fb1ce6ba95"
VERSION = "lite-packages/C.1"
PREFIX = "distributions/chat-mode-lite/"
URL = f"https://github.com/imbdsssity/TavernWeave-Yuri/blob/{BASE}/"
VERSIONS = {
    "package": VERSION, "core": "lite-core/A1.1", "integration": "lite-pre-c/1",
    "policy": "yuri-policy/1.0", "cards": "lite-card-workflows/A2.1",
    "sources": "lite-source/B2.1", "checkpoint": "yuri-lite/checkpoint/v1",
}
SOURCES = (
    "instructions/CORE.md", "instructions/CREATION.md", "instructions/ADAPTATION.md",
    "instructions/POST.md", "instructions/NOVEL.md", "references/yuri-policy.md",
    "references/relationship-rules.md", "references/player-agency.md",
    "references/character-design.md", "references/worldbook-design.md",
    "references/card-output.md", "references/source-evidence.md",
    "templates/preferences.json", "templates/adaptation-record.md",
    "templates/continuity-record.md", "templates/resume-prompt.md",
)
PACKAGES = {
    "portable": ("START_HERE.md", ("USAGE.md",)),
    "chatgpt-projects": ("PROJECT_INSTRUCTIONS.md", ("SETUP.md", "RESUME_GUIDE.md")),
    "custom-gpt": ("GPT_INSTRUCTIONS.md", (
        "CONFIGURATION.md", "PREVIEW_TESTS.md", "COMPATIBILITY_AND_MIGRATION.md")),
}
LINK = re.compile(r"\[([^\]\n]+)\]\(([^)\s]+)\)")


def digest(data):
    return hashlib.sha256(data).hexdigest()


def anchor(path):
    return "source-" + re.sub(r"[^a-z0-9]+", "-", path.lower()).strip("-")


def git_bytes(path):
    return subprocess.check_output(["git", "show", f"{BASE}:{path}"], cwd=REPO)


def rewrite(path, text):
    """Only link destinations/optional-link labels change; policy prose is retained."""
    def convert(match):
        label, target = match.groups()
        if urlsplit(target).scheme or target.startswith("#"):
            return match.group()
        destination = posixpath.normpath(posixpath.join(posixpath.dirname(path), target.split("#")[0]))
        if destination in SOURCES:
            return f"[{label}](#{anchor(destination)})"
        if destination == "../../LICENSE":
            return f"[{label}](LICENSE)"
        if destination == "../../THIRD_PARTY_NOTICES.md":
            return f"[{label}](THIRD_PARTY_NOTICES.md)"
        if destination == "../../extensions/yuri-creation/LICENSE":
            return f"[{label}](licenses/YURI-MIT.txt)"
        if destination == "../../extensions/yuri-creation/LICENSE_BOUNDARY.md":
            return f"[{label}](THIRD_PARTY_NOTICES.md#material-boundary)"
        if destination.startswith("examples/"):
            return f"[{label} — optional illustration excluded from this package]({URL}{PREFIX}{destination})"
        raise ValueError(f"Unmapped package dependency: {path} -> {target} ({destination})")
    return LINK.sub(convert, text)


def make_reference():
    index = []
    sections = []
    records = []
    for path in SOURCES:
        raw = (ROOT / path).read_bytes()
        if raw != git_bytes(PREFIX + path):
            raise ValueError(f"Canonical source differs from exact base: {path}")
        rendered = rewrite(path, raw.decode("utf-8")) if path.endswith(".md") else "```json\n" + raw.decode("utf-8") + "```\n"
        index.append(f"- [{path}](#{anchor(path)})")
        sections.append(f'<a id="{anchor(path)}"></a>\n\n# Source: {path}\n\n{rendered}')
        records.append({
            "canonical_path": path,
            "base_git_blob": subprocess.check_output(
                ["git", "rev-parse", f"{BASE}:{PREFIX}{path}"], cwd=REPO, text=True).strip(),
            "source_sha256": digest(raw), "source_bytes": len(raw),
            "pack_anchor": anchor(path), "rendered_sha256": digest(rendered.encode("utf-8")),
        })
    preface = f"""# Lite reference pack

Package `{VERSION}`; exact source base `{BASE}`. Supporting knowledge, **not a substitute for active instructions**. Apply the companion host instructions first. All sixteen maintained instruction/reference/template bodies are included below; no filesystem or repository fetch is needed for their content. Use only selected sections/companions for a task; do not assume uploading this pack means it was all read.

Source phase/status statements are historical authoring context, not new test results. Current package state: unreleased preparation; T1 output selection, T2 isolated recovery and T3 host setup remain unperformed. Link normalization changes navigation only: source companions point inside this file, licenses point to local copies, optional excluded illustrations point to the pinned repository. Design links remain optional maintainer traceability. No illustration/fixture/answer key, design record, real source or completed checkpoint body is embedded.

For plain copy/paste, locate `Source: <canonical path>` and copy that section through the next Source heading. Templates are blank structures, not observed records. Their Instructions/Source headings are navigation text, not source claims.

## Section index

"""
    return (preface + "\n".join(index) + "\n\n" + "\n\n".join(sections)).encode("utf-8"), records


def map_text(host):
    active = PACKAGES[host][0]
    return f"""# Reference placement / 参考放置

| File | Destination / 用途 |
| --- | --- |
| {active} | Active host instruction field, or portable initial message. Actual rules, not just knowledge. / 实际宿主指令或通用首条消息，不只上传为知识。 |
| REFERENCE_PACK.md | One complete reference source/knowledge file, or pasted selected sections. / 一个完整来源／知识文件，或按需粘贴段落。 |
| SOURCE_MAP.md | Canonical-path index, versions and provenance. Human setup reference; not an extra required upload. / 来源映射，无需另行上传。 |
| LICENSE, THIRD_PARTY_NOTICES.md, licenses/YURI-MIT.txt | Keep locally with the package. No active-instruction/knowledge upload required. / 随包保留，无需作为指令或知识上传。 |
| HOST_REQUIREMENTS.md, MANIFEST.json and setup/Preview guides | Human setup/audit only. Do not add to reusable knowledge. / 仅供设置与审阅，不添加到可复用知识。 |

Find the following canonical labels inside REFERENCE_PACK.md; they are included sections, not separate files you must fetch:

| Request / 请求 | Read or paste / 查阅或粘贴 |
| --- | --- |
| Every task / 所有任务 | instructions/CORE.md; references/yuri-policy.md, relationship-rules.md, player-agency.md; templates/adaptation-record.md |
| Original / 原创 | instructions/CREATION.md; references/character-design.md, worldbook-design.md, card-output.md |
| Existing card/book / 已有卡或世界书 | instructions/ADAPTATION.md; references/character-design.md, worldbook-design.md, card-output.md, source-evidence.md |
| Post / 帖子 | instructions/POST.md; references/source-evidence.md; relevant character/worldbook/output guidance |
| Novel / 小说 | instructions/NOVEL.md; references/source-evidence.md; relevant character/worldbook/output guidance |
| Handoff/resume / 交接恢复 | templates/continuity-record.md and templates/resume-prompt.md; applicable workflow/source guidance and actual checkpoint/current draft/source |
| Optional preferences / 可选偏好 | templates/preferences.json is a sample only, not adopted choices, validation or consent. / 只是样例，不代表采用、校验或授权。 |

If needed sections cannot be retrieved completely, request/paste their text and disclose the limit; no automatic loading is promised. Supply private task sources separately. A retrieved passage does not establish full chapter coverage. Keep design records, all example/answer bodies, private profiles, real checkpoints and PREVIEW_TESTS.md out of reusable knowledge. / 若无法完整访问所需章节，粘贴正文并说明限制；私人任务材料单独提供，检索片段不等于完整章节覆盖。设计、示例／答案、私人偏好、真实检查点及 Preview 方案不进入可复用知识。
"""


def collect():
    active = (ROOT / "packages/ACTIVE_INSTRUCTIONS.md").read_bytes()
    # An intentionally conservative packaging budget, NOT an official host limit.
    if len(active.decode("utf-8")) > 7900:
        raise ValueError("Active instructions exceed local 7,900-character design budget")
    ref, source_records = make_reference()
    notice = (ROOT / "THIRD_PARTY_NOTICES.md").read_bytes()
    terms = git_bytes("LICENSE")
    mit = git_bytes("extensions/yuri-creation/LICENSE")
    outputs = {ROOT / "LICENSE": terms, ROOT / "licenses/YURI-MIT.txt": mit}
    source_map = "# Package source map\n\n" + f"Exact base: `{BASE}`. Package: `{VERSION}` (unreleased).\n\n"
    source_map += " / ".join(f"{key}: `{value}`" for key, value in VERSIONS.items()) + "\n\n"
    source_map += "All rows are sections in the local reference pack. Original UTF-8 source SHA-256 and Git blobs are in MANIFEST.json. Rendered bodies retain source prose; only relative Markdown links and optional illustration link labels are normalized. No source behavior is edited.\n\n"
    source_map += "| Canonical path | Included section |\n| --- | --- |\n"
    source_map += "\n".join(f"| `{p}` | [Read](REFERENCE_PACK.md#{anchor(p)}) |" for p in SOURCES) + "\n"
    for host, (entry, docs) in PACKAGES.items():
        folder = ROOT / "packages" / host
        files = {
            entry: active, "REFERENCE_PACK.md": ref, "SOURCE_MAP.md": source_map.encode("utf-8"),
            "LICENSE": terms, "licenses/YURI-MIT.txt": mit, "THIRD_PARTY_NOTICES.md": notice,
            "HOST_REQUIREMENTS.md": (ROOT / "packages/HOST_REQUIREMENTS.md").read_bytes(),
            ("KNOWLEDGE_MAP.md" if host == "custom-gpt" else "UPLOAD_MAP.md"): map_text(host).encode("utf-8"),
        }
        for doc in docs:
            files[doc] = (folder / doc).read_bytes()
        manifest = {
            "schema": "lite-package-inventory/1", "versions": VERSIONS, "source_base": BASE,
            "host": host, "state": "unreleased-preparation", "active_entry": entry,
            "instruction_characters": len(active.decode("utf-8")), "instruction_utf8_bytes": len(active),
            "local_instruction_design_budget": 7900, "official_instruction_limit_verified": False,
            "reference_upload_files": ["REFERENCE_PACK.md"], "sources": source_records,
            "excluded_content": ["design", "examples", "qa", "private casework", "real checkpoints", "Full runtime"],
            "gates": {"T1": "unperformed; output undecided", "T2": "unperformed", "T3": "unperformed; account eligibility unverified", "SillyTavern_import": "unperformed", "human_roleplay": "unperformed"},
            "inventory_note": "Manifest excludes itself to avoid a recursive digest. Hashes are maintainer-computed packaging checks, not runtime evidence of source reading or host acceptance.",
            "files": {path: {"bytes": len(data), "sha256": digest(data)} for path, data in sorted(files.items())},
        }
        files["MANIFEST.json"] = (json.dumps(manifest, ensure_ascii=False, indent=2) + "\n").encode("utf-8")
        outputs.update({folder / path: data for path, data in files.items()})
    inventory = f"""# Package contents / 包清单

Candidate `{VERSION}`, exact base `{BASE}`. No release or host acceptance is claimed. / 候选准备版本，不代表发布或宿主验收。

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

"""
    for host in PACKAGES:
        folder = ROOT / "packages" / host
        paths = sorted(path.relative_to(folder).as_posix() for path in outputs if path.is_relative_to(folder))
        inventory += f"### packages/{host}/\n\n" + "\n".join(f"- `{p}`" for p in paths) + "\n\n"
    inventory += "Each manifest records byte sizes and actual SHA-256 values for every other file. Copy an entire host folder, retaining notices; no symlinks or parent-folder runtime dependencies are used. Only the reference pack is a knowledge upload. Setup/Preview documents and assessment criteria stay outside clean trial contexts. / 每份清单记录其他全部文件的大小和实际哈希。完整复制宿主目录并保留声明；没有符号链接或父目录运行依赖。仅参考包作为知识上传，设置／Preview 及判断标准不进入干净测试上下文。\n"
    outputs[ROOT / "PACKAGE_CONTENTS.md"] = inventory.encode("utf-8")
    return outputs


def check_links(outputs):
    # Inspect actual delivery text, not repository-relative resolution that could hide omissions.
    for path, data in outputs.items():
        if path.suffix != ".md":
            continue
        for _, target in LINK.findall(data.decode("utf-8")):
            if urlsplit(target).scheme:
                continue
            name, _, fragment = target.partition("#")
            dest = (path.parent / unquote(name)).resolve() if name else path
            if dest not in outputs and not dest.is_file():
                raise ValueError(f"Broken local link: {path} -> {target}")
            if "packages" in path.parts and any(h in path.parts for h in PACKAGES):
                package_root = next(ROOT / "packages" / h for h in PACKAGES if h in path.parts)
                if not dest.is_relative_to(package_root):
                    raise ValueError(f"Standalone link escapes package: {path} -> {target}")
            if fragment:
                text = outputs.get(dest, dest.read_bytes() if dest.exists() else b"").decode("utf-8")
                ids = set(re.findall(r'<a id="([^"]+)">', text))
                ids.update(re.sub(r"[^\w\- ]", "", heading.strip().lower()).replace(" ", "-")
                           for heading in re.findall(r"^#+ (.+)$", text, re.M))
                if fragment not in ids:
                    raise ValueError(f"Missing local anchor: {path} -> {target}")


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--check", action="store_true", help="Verify committed/generated package bytes without changing them")
    parser.add_argument("--archive-dir", type=Path, help="Optional three standalone ZIPs; never imports or deploys anything")
    args = parser.parse_args()
    outputs = collect()
    check_links(outputs)
    for path, data in outputs.items():
        if args.check:
            if not path.is_file() or path.read_bytes() != data:
                raise ValueError(f"Stale/missing generated file: {path.relative_to(ROOT)}")
        else:
            path.parent.mkdir(parents=True, exist_ok=True)
            path.write_bytes(data)
    for host in PACKAGES:
        folder = ROOT / "packages" / host
        actual = {p for p in folder.rglob("*") if p.is_file()}
        expected = {p for p in outputs if p.is_relative_to(folder)}
        if actual != expected:
            raise ValueError(f"Uninventoried/missing package files: {actual ^ expected}")
    if args.archive_dir:
        args.archive_dir.mkdir(parents=True, exist_ok=True)
        for host in PACKAGES:
            folder = ROOT / "packages" / host
            with zipfile.ZipFile(args.archive_dir / f"yuri-lite-{host}-C1.zip", "w", zipfile.ZIP_DEFLATED) as archive:
                for path in sorted(p for p in outputs if p.is_relative_to(folder)):
                    info = zipfile.ZipInfo(f"yuri-lite-{host}/{path.relative_to(folder).as_posix()}", (2026, 11, 16, 0, 0, 0))
                    info.compress_type = zipfile.ZIP_DEFLATED
                    info.external_attr = 0o100644 << 16
                    archive.writestr(info, outputs[path])
    print(f"{'Verified' if args.check else 'Prepared'} three standalone packages; 16 canonical bodies each; active rules identical; source base {BASE}.")


if __name__ == "__main__":
    try:
        main()
    except (ValueError, OSError, subprocess.CalledProcessError) as error:
        print(str(error), file=sys.stderr)
        sys.exit(1)
