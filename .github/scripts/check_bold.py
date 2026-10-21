#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""检查 Markdown 加粗标记两侧的空格是否符合仓库规则。

规则：
* 开头的 ``**`` 前恰好一个半角空格，段首（行首、列表标记或标题标记之后）可省略；
* 结尾的 ``**`` 后恰好一个半角空格，行尾（段落结束）可省略；
* 不得出现两个及以上连续空格，加粗标记内侧也不得有空格；
* 围栏代码块与行内代码中的 ``**`` 不参与检查。

有违规时以非零状态退出，输出格式为 ``文件:行号: 说明``。
"""

import re
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent.parent
FENCE = re.compile(r"^\s*(```|~~~)")
INLINE_CODE = re.compile(r"`+[^`]*`+")
BOLD = re.compile(r"\*\*(?=\S)(.+?)(?<=\S)\*\*")
# 段首：行首、标题标记之后、列表标记之后（可嵌套在引用块内）
PARA_START = re.compile(
    r"^\s*(?:>\s*)*(?:#{1,6}\s+|(?:[*+-]|\d+\.)\s+)$"
)


def mask_inline_code(line: str) -> str:
    """用等长占位符替换行内代码，保持列位置不变。"""
    return INLINE_CODE.sub(lambda m: "x" * len(m.group(0)), line)


def check_line(line: str):
    """返回该行的违规说明列表。"""
    masked = mask_inline_code(line)
    problems = []
    spans = list(BOLD.finditer(masked))

    for match in spans:
        start, end = match.span()
        prefix = masked[: start]
        suffix = masked[end:]
        before_spaces = len(prefix) - len(prefix.rstrip(" "))
        after_spaces = len(suffix) - len(suffix.lstrip(" "))
        at_start = prefix.strip() == "" or bool(PARA_START.fullmatch(prefix))
        at_end = suffix.strip() == ""

        if not at_start and before_spaces != 1:
            problems.append(
                f"开头 ** 前应有且只有一个空格，实际 {before_spaces} 个"
            )
        if not at_end and after_spaces != 1:
            problems.append(
                f"结尾 ** 后应有且只有一个空格，实际 {after_spaces} 个"
            )

    # 加粗标记内侧的空格会导致加粗无法渲染
    for match in re.finditer(r"\*\*(.+?)\*\*", masked):
        content = match.group(1)
        if content[:1].isspace() or content[-1:].isspace():
            problems.append("加粗标记内侧不得有空格")

    # 未配对的加粗标记
    if masked.count("**") % 2 == 1:
        problems.append("加粗标记 ** 未配对")

    return problems


def check_file(path: Path):
    issues = []
    in_fence = False
    for lineno, raw in enumerate(
        path.read_text(encoding="utf-8").splitlines(), 1
    ):
        if FENCE.match(raw):
            in_fence = not in_fence
            continue
        if in_fence:
            continue
        for problem in check_line(raw):
            issues.append((lineno, problem, raw.strip()))
    return issues


def main():
    total = 0
    for path in sorted(ROOT.glob("**/*.md")):
        if ".git" in path.parts:
            continue
        for lineno, problem, text in check_file(path):
            total += 1
            rel = path.relative_to(ROOT).as_posix()
            print(f"{rel}:{lineno}: {problem}")
            print(f"    {text}")
    if total:
        print(f"\n共发现 {total} 处加粗标记空格问题。")
        return 1
    print("加粗标记空格检查通过。")
    return 0


if __name__ == "__main__":
    sys.exit(main())
