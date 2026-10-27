# -*- coding: utf-8 -*-
"""项目 → 课程 同步脚本。

主仓库（enterprise-travel-agent）每次更新后，在本课程仓库运行：
    python tools/sync_from_project.py
会把以下内容复制到 09-项目同步资料/ 并记录来源 commit 到 SYNCLOG.md：
- docs/ 关键文档（ roadmap、fourth-round 方案、局域网指南 等）
- stress/ 关键报告（fourth_round_test_report、staging_retest_report 等）
- platform/deploy/k8s/*.yaml（部署清单）
- data-contracts/graphql/schema.graphql
"""
import os
import shutil
import subprocess
from datetime import datetime

PROJECT = r"D:\移动云盘同步盘\enterprise-travel-agent"
COURSE = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
DEST = os.path.join(COURSE, "09-项目同步资料")

SYNC_FILES = [
    "docs/fourth-round-review-and-refactor-plan.md",
    "docs/lan-manual-testing-guide.md",
    "docs/expert-review-and-refactoring-roadmap-2026-09.md",
    "docs/staging-retest-runbook.md",
    "stress/fourth_round_test_report.md",
    "stress/staging_retest_report.md",
    "data-contracts/graphql/schema.graphql",
]
SYNC_GLOBS = [
    "platform/deploy/k8s/*.yaml",
]


def git_head() -> str:
    try:
        return subprocess.run(
            ["git", "log", "-1", "--format=%h %ad %s", "--date=short"],
            cwd=PROJECT, capture_output=True, text=True, encoding="utf-8", check=True,
        ).stdout.strip()
    except Exception:
        return "unknown（本地未取到 git 信息）"


def main():
    os.makedirs(DEST, exist_ok=True)
    copied = []
    for rel in SYNC_FILES:
        src = os.path.join(PROJECT, rel.replace("/", os.sep))
        if os.path.exists(src):
            dst = os.path.join(DEST, os.path.basename(rel))
            shutil.copy2(src, dst)
            copied.append(rel)
    for pat in SYNC_GLOBS:
        full = os.path.join(PROJECT, pat.replace("/", os.sep))
        import glob
        for src in glob.glob(full):
            dst = os.path.join(DEST, "k8s-" + os.path.basename(src))
            shutil.copy2(src, dst)
            copied.append("platform/deploy/k8s/" + os.path.basename(src))
    head = git_head()
    log_path = os.path.join(COURSE, "09-项目同步资料", "SYNCLOG.md")
    with open(log_path, "a", encoding="utf-8") as f:
        f.write(f"\n## 同步 {datetime.now().isoformat(timespec='seconds')}\n")
        f.write(f"- 来源 commit：{head}\n")
        for rel in copied:
            f.write(f"- {rel}\n")
    print(f"synced {len(copied)} files from {head}")
    print("log:", log_path)


if __name__ == "__main__":
    main()
