# 用户 第一幕

AT\&T 律师决定允许教育机构获得 Unix，但拒绝提供支持和修复补丁，这一决定当即产生了影响：它迫使用户相互共享。他们分享想法、信息、程序、错误修复和硬件修复。一些潜在用户已经听说过 Unix：哥伦比亚大学生物科学系负责人 Cyrus Levinthal 就是其中之一（“但他当时认为它不可用，”Lou Katz 告诉我），而普林斯顿的 Richard Langridge 也是。

但在 1973 年 10 月第一篇论文发表后，你就可以把数据放到你的 RK05 磁盘上。1974 年早春，Lou Katz（当时在哥伦比亚大学）组织了一次 Unix 用户会议。哥伦比亚大学是第一批收到 Unix 发行版的单位——先是磁盘版本，然后是九轨磁带版本——发生在秋季（“Cy 为系里弄来了 RK05 磁盘，”Katz 告诉我，“但我们没有驱动器，所以我开车去了 Murray Hill，Ken 给我制作了一套九轨磁带。”）会议于 1974 年 5 月 15 日在哥伦比亚医学院（P\&S）三楼的 Merritt 会议室举行，Katz 当时已从生物系调到医学院。以下是 Reidar Bornholdt 提供给我的会议日程：

| 时间    | 议程内容                    |
| ----- | ----------------------- |
| 10:30 | 开始                     |
| 11:30 | 简要介绍几位用户及其 Unix 使用情况    |
| 12:00 | 午餐                      |
| 13:00 | Ken Thompson 演讲         |
| 14:00 | 交流 Unix 使用技巧、问题、解决方案、错误 |
| 15:00 | 交流 DEC 使用技巧、问题、解决方案、错误  |
| 16:00 | 自由讨论                    |

大约有二十多人，来自近十个机构出席了会议。回想起来，Thompson 和 Ritchie 的第一篇文章将在 1974 年 7 月发表在 CACM 上——比这次首次会议晚两个月。到第二年春天（1975 年），Mel Ferentz（当时在布鲁克林学院）向三十多个从贝尔电话实验室收到软件的站点发送了一封“邀请函”，邀请他们加入 Unix 邮件列表（Thompson 在这些早期年份多次向 Ferentz 提供了收到 RKOS 和磁带的名单）。随后，Unix 用户会议通知发出，会议定于 1975 年 6 月 18 日在纽约市立大学（CUNY）举行，通知发送给了回复者及“20 个新安装点”。第三次通知则于 6 月 16 日发给 Ferentz 修订后的 37 个回复名单，内容是关于“Unix 新版本”（第六版）的消息。到那时，哥伦比亚、布鲁克林和 CUNY 的计算中心都已安装了 Unix。

Ferentz、Katz 和 Bornholdt 组织了这次会议，Ira Fuchs 负责具体安排。用 Ferentz 的话来说（摘自《UNIX NEWS》，第 1 期，1975 年 7 月 30 日；发行量 37）：

>1975 年 6 月 18 日在纽约市立大学举行的会议，有来自 20 个机构的 40 多人参加。每个机构简要介绍了其功能和特点。我们不打算在这里复述这些内容，因为预计之后每个安装点都会提交一页的介绍以供收录（本期中包含了若干这样的介绍）。与会者一致认为，应尽可能保持用户组及其通讯的非正式性质。

那期 11 页的《UNIX NEWS》包括了来自波士顿儿童博物馆和多伦多大学的介绍。它还包含一篇题为《MUNIX—一种多处理器 Unix》的简短文章，以及一个邮件列表。

这个邮件列表非常有趣，因为它反映了 Unix 的传播情况——这是一款未经宣布、没有支持的操作系统。

>**首次邮件列表中的机构**
>
>* 贝尔电话实验室 Bell Telephone Laboratories
>* 布鲁克林学院 Brooklyn College
>* 卡尔顿学院 Carleton College
>* 凯斯西储大学 Case Western Reserve University
>* 儿童博物馆 The Children's Museum
>* 纽约市立大学 City University of New York
>* 哥伦比亚大学 Columbia University
>* 杜克医学院 Duke Medical Center
>* 东布伦瑞克高中 East Brunswick High School
>* 哈佛大学 Harvard University
>* 耶路撒冷希伯来大学 Hebrew University of Jerusalem
>* 赫瑞 - 瓦特大学 Heriot-Watt University
>* 约翰斯·霍普金斯大学 Johns Hopkins University
>* 诺克斯学院 Knox College
>* 海军研究生院 Naval Postgraduate School
>* 俄勒冈科学与工业博物馆 Oregon Museum of Science and Industry
>* 纽约理工学院 Polytechnic Institute of New York
>* 普林斯顿大学 Princeton University
>* 兰德公司 The Rand Corporation
>* 圣奥拉夫学院 St. Olaf College
>* 斯坦福大学 Stanford University
>* 斯宾塞学校 The Spence School
>* 鲁汶天主教大学 Universite Catholique de Louvain
>* 阿尔伯塔大学 University of Alberta
>* 加州大学伯克利分校 University of California, Berkeley
>* 曼尼托巴大学 University of Manitoba
>* 北卡罗来纳大学 University of North Carolina
>* 萨斯喀彻温大学 University of Saskatchewan
>* 德克萨斯大学达拉斯分校 University of Texas at Dallas
>* 多伦多大学 University of Toronto
>* 犹他大学 University of Utah
>* 滑铁卢大学 University of Waterloo
>* 威斯康星大学 University of Wisconsin

《UNIX NEWS》第 2 期（1975 年 10 月 8 日，发行量 60）刊登了通知：“西部的第一次会议将于 10 月 31 日星期五在海军研究生院举行。”第 3 期（1976 年 2 月 10 日）刊登了来自加州大学伯克利分校电气工程与计算机科学系 Robert S. Fabry 教授和哈佛科学中心技术服务主任 Lewis A. Law 的信件，宣布西部（2 月 27 日和 28 日）及东部（4 月 1 日和 2 日）的下一次会议。第 4 期（1976 年 3 月 19 日）刊登了 John Lions 博士关于新南威尔士大学安装情况的第一封信件，以及一个新的邮件列表，现有 80 个名字。到 1976 年 9 月，名单已增至 138 条目。其中十三个在加拿大，十个在英国，四个在澳大利亚，三个在以色列和荷兰，奥地利、比利时、德国和委内瑞拉各一个。其余 101 个在美国。

《UNIX NEWS》1977 年 5-6 月刊是最后一期。从 1977 年 7 月起，该刊物改名为《; login: 》。Mel Ferentz 曾接到 AT\&T 律师的电话，告知该小组（当时仍无名称）不能使用 UNIX 一词，因为他们未从西部电气获得使用许可。1978 年 5 月 24-27 日在哥伦比亚医学院举行的 UNIX 用户会议上，选举产生了一个五人委员会，目的是提出 UNIX\* 安装用户组织的章程草案。被选举的人是：

>* Mel Ferentz  洛克菲勒大学
>* Mars Gralia  约翰斯·霍普金斯大学
>* Lou Katz  哥伦比亚大学
>* Lew Law  哈佛大学
>* Peter Weiner  交互系统公司 Interactive Systems Corp.
>
>Law 被选为主席……委员会的名称定为 USENIX\*\* 委员会……

令人欣慰的是看到这两个脚注：它们揭示了 1970 年代团结 Unix 用户的精神，这种精神延续至今，其根源在于一种“我们对抗他们”的态度，结合了幽默感。两次名称变更引发了贝尔实验室专利律师 Stephen J. Phillips 写给 Ferentz 的一封信。Phillips 的信开头写道：

>我怀着浓厚兴趣阅读了 1978 年 6/7 月第 3 卷第 6 期。你们选择“USENIX”这个名字，是避免在委员会名称中使用 UNIX\* 商标的一种颇具灵感的方式。

Phillips 详细阐述了对 UNIX 商标“稀释”的担忧，他希望 USENIX“今后不会在任何名称中包含”这一点。Ferentz 以一种讽刺的态度将这封信刊登在《; login: 》杂志上。

USENIX 这一名称由 Margaret Law 创造，她曾是哈佛和拉德克利夫的教职员工；而《; login: 》杂志更具趣味性。Dennis Ritchie 解释道：

`;login: ` 的“;”是实用主义的。在七十年代早期，大多数人使用的终端是 Teletype 37 型。序列 `<esc>;` 会将终端设置为全双工模式，这样终端不会本地打印字符，而是让系统回显它们。因此，这个序列被放进了欢迎消息中。当然，当你使用该终端时它不会打印，但后来出现的其他终端不理解这条消息，于是就打印出了这个“;”符号。

1978 年 5 月在哥伦比亚举行的会议有来自克利夫兰凯斯西储大学的 Bill Shannon 和其他几位参加。Shannon 是 Sam Leffler 的同事，Leffler 于次年参加了多伦多会议（1979 年 6 月 20-23 日）。Leffler 回忆道：“我们那次都去看了《异形》；走回多伦多宿舍的路上，我们回头张望——你知道，是怕‘异形’。”

课外活动在早期 USENIX 会议中非常突出：Leffler 和其他几位回忆道，“我们在 1980 年 6 月的特拉华会议上打了排球。”这对 Leffler 的未来以及 Unix 的未来都非常重要。（我稍后讨论伯克利 Unix 时会再提到这一点。）

从最初的 Unix 用户名单中可以看出，他们的分布远非地域限制。因此，得知以下情况也就不足为奇了：

>澳大利亚 Unix 系统用户组（AUUG）于 1984 年 8 月 27 日在墨尔本大学校园举行的 Unix 用户会议上正式成立，此前已非正式存在九年……AUUG 的第一次会议于 1975 年在新南威尔士大学举行。（Peter Barnes，AUUG 秘书）

新南威尔士大学是加利福尼亚以西首个获得 Unix 的地点——发生在 1974 年。

英国于 1973 年获得 Unix，组织用户的步伐也紧随其后。1976 年 9 月的大学间计算机委员会会议上，阿伯丁大学的 P. M. D. Gray 与几位同事讨论了英国日益增多的 Unix 安装情况。

同年 12 月，英国大学 Unix 通讯（UK UNIVERSITIES UNIX NEWSLETTER）第 1 卷第 1 期问世，刊载了 11 个安装点名单：阿伯丁、达勒姆、埃塞克斯、格拉斯哥、赫瑞瓦特（爱丁堡）、肯特（坎特伯雷）、拉夫堡、伦敦玛丽女王学院、伦敦韦斯特菲尔德学院、圣安德鲁斯和萨塞克斯——其中苏格兰有四个，英格兰有七个。

1977 年 3 月 4 日，格拉斯哥大学的 Alistair C. Kilgour 发出一封信，建议成立英国 Unix 用户组，作为 DECUS 特别兴趣小组（SIG），并计划于 4 月 15 日星期五 DECUS 英国年会后召开感兴趣人员会议。他还提议在 1977 年 5 月底于格拉斯哥举办一次 Unix 研讨会。接下来的几期通讯页首均标注 DECUS U.K.，标题为英国 Unix 用户组通讯（UK UNIX USERS GROUP NEWSLETTER）。DECUS 英国负责复印和邮寄费用。

1977 年 5 月 27 日，格拉斯哥确实举办了一次研讨会，“大约有 40 人参加”。不到一年时间，英国 Unix 用户组（UKUUG）便与北海彼岸的荷兰联手，在阿姆斯特丹自由大学举行了一次会议。数学中心（Mathematische Centrum）很早就获得了 Unix。Teus Hagen 告诉我：

>我看到了 Ken Thompson 在《CACM》上的文章，立刻给他写了封信，询问更多细节以及获取软件的可能性，他马上就把软件寄给了我（通过 DEC RK05 磁带盒），且完全没有任何许可限制。那是 Unix 第五版。
>
>我们之前一直在用 PDP-11/45 和 RTL 或 RSX11 做一个图形项目。在收到 Unix 后，我们立即扔掉了 DEC 的东西，改用了贝尔电话实验室的版本。随后我们又用了第六版、6.1 版、6.2 版、第七版，然后我们的 DEC VAX-11/780（序列号 10）到货。我们订购时没有申请 VMS 许可（当时 DEC 对此感到惊讶），最初使用实验室的 Unix VAX 版本（部分以 PDP-11 模式运行），后来转用了伯克利的版本。\[VAX 代表虚拟地址扩展（Virtual Address Extension）。]

NLUUG 于 1978 年 11 月成立。随着 Unix 在欧洲的传播，其他国家的组织也相继成立，1981 年 4 月，欧洲 Unix 系统用户组（EUUG，现为 EurOpen）召开了首次会议（同样在阿姆斯特丹）。有趣的是，日本 Unix 的出现比澳大利亚晚不到两年，因此日本的 Unix 用户会议也紧随欧洲和澳大利亚之后开始举办。

1976 年，当东京大学的石田治久引进 Unix 到日本后，不久由村井纯、岸田浩一和斋藤信雄成立了日本 Unix 协会（JAS）。起初，它只是一个 Unix 学习小组，但发展迅速。十年后的 Unix，真正实现了全球范围内的使用。
