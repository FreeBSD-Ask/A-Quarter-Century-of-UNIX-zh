# AGENTS.md

本文件为 AI 编码代理（Claude Code、ZCode 等）在本仓库工作时提供指导。

## 仓库概览

这是 Peter H. Salus 所著《Unix 四分之一世纪》（*A Quarter Century of UNIX*，Addison-Wesley，1994）的简体中文翻译项目，由 FreeBSD 中文社区（CFC）译制与维护。基于 GitBook 格式（`SUMMARY.md` 驱动目录），由 GitBook 平台在线发布，无需本地构建步骤。

- 本项目仓库：<https://github.com/FreeBSD-Ask/A-Quarter-Century-of-UNIX-zh>
- 在线阅读：<https://freebsd.gitbook.io/unix-er-shi-wu-nian>
- 早期译本（`upstream`远程）：<https://github.com/zhangyangjing/A-Quarter-Century-of-UNIX-zh>。本仓库早期 fork 自该译本，此后逐句精校，并补齐了原译本缺失的"进一步阅读""人物与术语表"两篇附文。
- 英文原版（TUHS）：<http://wiki.tuhs.org/lib/exe/fetch.php?media=publications:qcu.pdf>，即仓库根目录的 `qcu.pdf`（已被 `.gitignore` 忽略，不入库）
- Unix 源码树：<http://minnie.tuhs.org/cgi-bin/utree.pl>
- 授权：本仓库自有内容（译文、目录、脚本）采用 BSD 2-Clause 许可（见 `LICENSE`，Copyright © 2025 FreeBSD 中文社区）。原著正文与插图的著作权归 Peter H. Salus 及出版方所有。

**重要：现有译稿源自两年前的旧译本，并不是全书的完整翻译。** 30 个正文章节文件与 7 篇附文虽然齐备，但每章内部存在大量漏译段落（相对 278 页英文原版）。校对与补全时必须与英文原文**逐段比对**，不能以"章节文件齐全"推断"翻译完整"。详见"翻译校对工作流（AI 代理）"。

**注意：本仓库有完整的 `.github/` 目录与多条 CI 工作流**（目录自动生成、H1 自动同步、格式检查、图片与链接检查、PDF/EPUB 发布）。不要把其他翻译项目（如 FreeBSD 手册 handbook.bsdcn.org、树莓派文档 rpicn）的 CI 假设、目录命名（`qian-yan/`、`shu-mei-pai/` 等拼音板块）与术语规则套用到本仓库。

## 原文与版本

- 本书 1994 年出版，内容固定，**不存在"跟随上游滚动同步"的概念**；本仓库与早期译本之间也无同步义务，只作参考与致谢。
- 英文原版 `qcu.pdf` 是**扫描件，没有文本层**（`pdftotext`、PyMuPDF `get_text()` 均返回空），用于逐段比对时须先 OCR。
- 本机可用的 OCR 方案：`rapidocr-onnxruntime`（推荐，约 6～10 秒/页）、`easyocr`；`pytesseract` 已安装但系统无 `tesseract` 二进制。渲染用 PyMuPDF（`get_pixmap(dpi=300, colorspace=fitz.csGRAY)`）。
- OCR 结果仅作校对底稿，**不能直接入库**；扫描件 OCR 有错字（漏字、误认），引用前须结合上下文判断。
- `CHANGELOG.md` 不入库：由 `create-pdf.yml` 在发布时用 changelog 生成器即时产出并写入 Release 说明。

## 内容架构

### 目录结构

| 路径 | 内容 |
| ---- | ---- |
| `chapters/` | 全书正文 30 章，文件名形如 `<序号>-<英文原名>.md`（`0-Prelude_to_Space.md` 至 `29-The_Law_Part_III.md`） |
| `mix/` | 正文之外的前后附文 7 篇：`Preface.md`、`Acknowledgements.md`、`Introduction.md`、`What_Made_It_work.md`（结语）、`book.md`（进一步阅读）、`who.md`（人物与术语表）、`Attached_Photos.md`（附图） |
| `assets/` | 正文插图，13 个 `.jpg`。正文以 **`/assets/xxx.jpg`** 绝对路径引用（不是 `.gitbook/assets/`，也不是相对路径） |
| `.github/` | CI 工作流、markdownlint 与 lychee 配置、图片检查脚本、Issue 模板 |
| `README.md` | 书名页：简介、作者、内容特色、译者注与资源链接 |
| `SUMMARY.md` | 全书唯一目录数据源，GitBook 据此生成侧边栏。**第一行必须是 `# Table of contents`** |
| `mu-lu.md` | 目录的副本，**由 CI 从 `SUMMARY.md` 自动生成**（见 `mulu.yml`），不要手工编辑 |
| `qcu.pdf` | 英文原版扫描件（`.gitignore` 忽略） |
| `LICENSE` / `AGENTS.md` | 授权协议 / 本文件 |

### 标题管理（由 CI 自动完成，不要手工改 H1）

- `sync-headers.yml`：任何 push 都会按 `SUMMARY.md` 逐条同步各文件的 H1 —— **`SUMMARY.md` 是标题的唯一来源**。
- `mulu.yml`：`SUMMARY.md` 变更时，删除并重新复制生成为 `mu-lu.md`，自动提交。
- `file-name-check.yml`：校验 `SUMMARY.md` 中每个条目对应的文件是否存在，缺失则开 issue（标签 `summary-check`）。
- 因此**修改章节标题只需改 `SUMMARY.md`**；各文件 H1 与 `mu-lu.md` 会由 CI 跟上，人工改这两处反而会被覆盖。

### 新增/调整页面

- 新增正文页：在 `chapters/` 按 `<序号>-<英文原名>.md` 命名（不得含空格、中文、英文冒号 `:`，须兼容 Windows 文件名），在 `SUMMARY.md` 对应位置插入条目（用 `##` 分组标题 + `* [标题](路径)`），首行写与条目一致的 H1。
- 新增附文：放入 `mix/`，文件名用英文原名（与现有风格一致），同样登记进 `SUMMARY.md`。
- 图片：本地化放入 `assets/`，正文以 `/assets/xxx.jpg` 引用。

## 编写规范

### 格式

- **列表：** 全仓库统一使用 `*` 作为无序列表标记（markdownlint 配置 `MD004`/`MD049`/`MD050` 要求 asterisk），不得使用 `-` 或 `+`。
- **引号：** 使用中文双引号“”，**禁止出现「」**。逐个手动修改，禁止机械替换。
- **第二人称：** 一律用"你"，不用"您"。
- **引用块：** 访谈原话、书信、清单用 `>` 引用。同一条引文内的分段用单独一行 `>` 隔开。书中的方框/边栏小标题写成 `>**标题**`（如 `>**Unix 哲学**`）。
- **转义：** 正文中的特殊字符按现有写法转义，如 `AT\&T`、`\[LA36]`、`\[基于 1976 年会议]`。
- **代码块：** 保留原文内容，禁止篡改命令、参数、版本号；代码内英文注释译为中文，代码结构不变。shell 用 `bash`/`sh` 围栏，其余按语言标注（如 `c`），无法判断用无标注围栏，禁止用 `text`。
- **图片：** `![说明](/assets/xxx.jpg)`，说明可留空（`![]()`）。
- **CJK 空格：** 中文与英文、数字之间必须加半角空格；文件名、命令、选项、路径用反引号包裹（如 `config.txt`）。可用 AutoCorrect 检查（见"本地工具"）。
- **禁止篡改：** 人名、机构名、产品名、URL、版本号、页码/脚注标记、带圈数字（①②③）必须与原文对应，不得增删或移位。
- **禁止机械替换：** 统一批量替换会破坏上下文（如"硬拷贝"不能改成"硬复制"、"一份拷贝"与"拷贝命令"语境不同）。任何改动逐个手动完成。
- **避免滥用"已"字：** "已新增"应写"新增"，"已修复"应写"修复完成"，禁止机械替换。
- **避免机翻腔与欧化汉语：** 不用"将被自动安装"这类生硬被动句，不用后置、倒装、偷换主语的句式；译文应当是可读的中文。
- **避免硬编码交叉引用：** 不写"参见第 X 章"式的编号引用；站内引用用相对 markdown 链接，指向英文原书内容可直接给出 TUHS 上的 `qcu.pdf` 链接。
- **段落内联：** 一个段落写在一行内，不要在行尾用 `+` 之类的软换行拼接，也不要残留 AsciiDoc 语法（`xref:`、`link:`）。

### 术语

- **术语表即 `mix/who.md`（人物与术语表）**，按字母顺序收录人名、机构缩写与专有名词，格式为 `* 词条：释义`。新出现的人名、机构、专有名词先查该表，确定译法后补录进表内再在正文使用。
- 本书常用译法：Bell Labs/Bell Telephone Laboratories → 贝尔电话实验室（或贝尔实验室）；Project MAC → MAC 项目；Computer Systems Research Group → 计算机系统研究组；Programmer's Workbench → 程序员工作台；Multi-Environment Real Time → 多环境实时系统；time-sharing → 分时；Shell → shell（小写）。
- 产品名、型号、软件名、组缩写保持英文原样：Raspberry Pi 之外如 Unix/UNIX、Multics、CTSS、PDP-7/11、PWB、USG、CSRG、BSD、SVR2/SVR3、USENIX、AUUG/UKUUG/EUUG、ARPANET、Usenet、uucp、troff/nroff、ed、sh、C、awk、RJE、SCCS 等。人名一般保留英文原名（Salus、Ritchie、Thompson、McIlroy…），历史上已有通行中文名的（`mix/Preface.md`、`mix/who.md` 中如"石田晴久（Haruhisa Ishida）"）按现有写法保留。
- 关于 UNIX/Unix 的拼写：原著在致谢中说明采用 Unix 拼法（`mix/Acknowledgements.md` 有说明），正文以现有译文为准，不要整篇统一替换大小写。

### 表格与标题层级

- 表格风格与所在文件既有表格一致（内容列左对齐，短枚举列居中）；表头声明几列，数据行就必须有几列，缺的补空单元格。
- 标题层级：`SUMMARY.md` 的一级条目对应各文件 H1；文件内部小节用 `##`、`###`、`####`（如 `mix/who.md`、索引类页面先用 `##` 分组，条目再用列表）。

## 翻译校对工作流（AI 代理）

对译文进行质量审校与补全时，遵循以下步骤：

1. **获取原文**：以根目录 `qcu.pdf`（英文原版扫描件）为唯一权威源。先用 OCR 提取英文（见"原文与版本"），校对时不得以中文译文或早期译本 `upstream` 作为修改依据，避免错误沿袭。

2. **逐段比对**（本仓库最关键的检查项）：把中文每一段与英文原文对应段落逐一对照，特别标记**漏译**——英文有、中文整段或整句缺失的内容。由于"文件齐全 ≠ 翻译完整"，每章都要实际比对，不能只看有没有文件。

3. **重点检查项** ：

   | 问题类型 | 说明 |
   | -------- | ---- |
   | 漏译 | 英文原文整段、整句缺失，尤以访谈引文、脚注旁白为多 |
   | 事实性错误 | 数字、人名、年份、机构、型号译错 |
   | 机翻腔/欧化汉语 | 生硬被动句、倒装、后置、偷换主语 |
   | 用词不当 | 术语与 `mix/who.md` 不一致 |
   | 语法/文字错误 | 重复字词、错别字、多余"地"、"已"字滥用 |
   | 标点与格式 | 出现「」、列表用了 `-`、CJK 未加空格 |

4. **补译**：新译段落风格须与上下文一致，术语与 `mix/who.md` 对齐；插入位置对准英文原文的段落顺序。

5. **提交修改**：
   - 基于 `master` 创建分支（如 `fix/<章节名>`）
   - 仅提交修改的 `.md` 文件，不含无关文件（OCR 结果、临时脚本不入库）
   - 提交信息用中文简述变更（现有风格如"更新 12-Style_and_Tools.md""更新 README.md"）
   - PR 目标分支为 `master`

6. **逐句校对递归工作流**（核心约束）：
   - **逐行逐句**遍历内容，检查逻辑一致性，联网复核后修改
   - **三轮 + 一轮复查**：完整执行三轮逐句校对，然后严格、完整地复查一轮；若仍有问题，继续执行三轮，递归直至无问题
   - **逐个修改**：禁止机械修改、禁止批量；必须逐个手动修改，禁止用软件工具批量替换或批量逐个复核
   - **修改前后复核**：修改前确认问题真实存在，修改后确认改动准确且未引入新错误
   - **不复查旧错**：已做过三轮的错误不再复查；每轮内容必须是新的（与之前重复的跳过不改，只看有无新增内容）
   - **联网复查**：涉及实际可访问对象（失效链接、版本号、API 端点等）须联网复查三次后再改
   - **禁止绕过审查**：不得以任何方式搜索、批量或绕过逐句审查流程

## CI 工作流

| 工作流 | 触发 | 作用 |
| ------ | ---- | ---- |
| `mulu.yml` | `SUMMARY.md` 变更 / 手动 | 复制 `SUMMARY.md` 为 `mu-lu.md` 并自动提交 |
| `sync-headers.yml` | push / `mulu.yml` 完成后 / 手动 | 按 `SUMMARY.md` 同步各文件 H1 |
| `file-name-check.yml` | push（含 `*.md`） | 校验 `SUMMARY.md` 条目文件是否存在，缺失开 issue |
| `Markdown-lint2-pr.yml` | pull_request | 对改动的 `.md` 跑 markdownlint（`continue-on-error`，不阻断） |
| `markdown-lint2.yml` | 手动 | 全仓库 markdownlint 修复，失败时开 PR |
| `AutoCorrect.yml` | `repository_dispatch` / 手动 | autocorrect 加 CJK 空格后开 PR |
| `md-padding.yml` | `repository_dispatch` / 手动 | md-padding 加空格后开 PR |
| `links.yml` | 手动 / 每月 15 日 | lychee 链接检查，失败开 issue |
| `check-images.yml` | `.gitbook/assets/**` 变更 / 手动 | 跑 `check_images.py` 报告缺失/未使用图片，开 issue |
| `create-pdf.yml` | 手动 | 用 `FreeBSD-Ask/gitbook-pdf-export` 生成 PDF/EPUB，打日期标签、生成 CHANGELOG、发 Release |
| `dependabot.yml` | 每日 | 更新 GitHub Actions 版本 |

已知不一致（改动时注意）：

- `check-images.yml` 与 `links.yml` 只在手动/定时触发时真正有效：`check-images.yml` 的触发路径写的是 `.gitbook/assets/**`，而实际图片目录是 `assets/`；`links.yml`（lychee）只按手动和定时跑。
- `AutoCorrect.yml` 引用 `--config .autocorrectrc`，但仓库里**没有** `.autocorrectrc` 文件，该工作流实际按默认规则运行。
- markdownlint 配置见 `.github/.markdownlint.json`（`MD013` 行长度、`MD033` 内联 HTML、`MD034` 裸 URL 等均关闭）；lychee 配置见 `.github/lychee.toml`；图片检查脚本 `.github/scripts/check_images.py` 以 `/assets/*` 前缀解析图片路径。

## 本地工具

- **OCR**：`rapidocr-onnxruntime`（推荐）、`easyocr`；配 PyMuPDF 渲染页面。用于提取 `qcu.pdf` 原文，产物不要入库。
- **AutoCorrect**（`.github/workflows/AutoCorrect.yml` 所用）：仅用于检查/补全 CJK 空格，运行后必须逐文件核对 diff 再提交，禁止盲目批量应用。
- **markdownlint**：配置在 `.github/.markdownlint.json`，可本地用 `markdownlint-cli2` 按该配置检查。
- **PDF/EPUB 导出**：`create-pdf.yml` 调用 [gitbook-pdf-export](https://github.com/FreeBSD-Ask/gitbook-pdf-export)（脚本 `mdconv.py`），本地导出可参照 `README.md`。
