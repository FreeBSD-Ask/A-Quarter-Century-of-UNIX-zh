# 用户 第二幕

在我看来，Unix 故事中最吸引人的方面之一，就是它以飞速传播到了加拿大、欧洲、澳大利亚和日本。由于详细追踪过程会非常冗长，我选择了几个国家，让实际参与者来讲述他们的经历。我之前提到过其中一些用户，但现在你可以听到他们自己的声音。

首先，这是玛丽女王学院（Queen Mary College，QMC。现为玛丽女王和韦斯特菲尔德学院）的 George Coulouris 教授。我问他 QMC 是如何在 1973 年末获得第 4 版的。

>William Newman 是我们实验室的访问研究员，大约从 1971 年 10 月开始，待了一年多（后来他去了 Xerox PARC，现在在剑桥的 Rank Xerox EuroPARC 工作）。在他的指导下，我们发现了交互式小型机系统的价值。他和 Mike Cole 在玛丽女王学院开发了一款单用户交互式操作系统（称为 MIFS）。MIFS 运行在 Interdata 计算机上，松散地模仿了 TENEX。它是为支持两个研究项目而开发的：一个是 William 设计图形编程语言的研究，另一个是我们一组人利用微程序仿真研究新机器架构的设计。像 Unix 一样，MIFS 包含了广泛的组件和工具——文件系统、系统编程语言、编译器 - 编译器、带有单字符交互的行编辑器、调试器等等。几乎所有这些都是由 William 和 Mike 开发的。
>
>在 MIFS 开发期间，我们还没听说过 Unix，但 William 还在我们这里时，他去过贝尔实验室访问。回来后他说：“他们似乎在 Murray Hill 开发了类似 MIFS 的东西，但它支持多用户，并且运行在 PDP-11 上。”Mike Cole 获得了一些文档，研究后得出结论，这确实能给我们带来很大好处——它提供了我们在 MIFS 中发现非常有用的大部分功能，且远远超出了 MIFS 的范围。
>
>我们没有九轨磁带驱动器，只有 DECtape 和一台 System Industries 的 10 兆字节可交换硬盘。真正的问题是 Ken 没有为 SI 控制器写驱动程序（全世界没人有）。显然，我们不能用只有 DECtape 作为外设的 Unix 系统来开发新驱动程序——交换操作会使整个过程极其缓慢！Mike Cole 是我们的系统专家，他解决了这个问题。1973 年夏天，他在去 Xerox PARC 访问几个月的路上，从 Ken 那里用 DECtape 拿到了 V4 版本。在 PARC 时，他去了伯克利，写并编译了一款简单的 SI 控制器驱动程序，并构建了包含该驱动的内核。但伯克利没有 SI 磁盘，所以他没法在那里测试！回到玛丽女王学院后，DECtape 顺利安装，好家伙——幸运的是 Mike 是个非常优秀的程序员。
>
>令人惊讶的是，（a）我们竟然敢买一台磁盘与贝尔实验室系统不兼容的机器，而当时我们本打算运行 Unix；（b）Mike 居然能在第一次尝试时就写出一款能工作的磁盘驱动，尽管他从未写过 Unix 驱动，从未用过 C 语言，亦从未使用过 Unix。

Mike Cole 补充说：

>George 的说法大体正确，但有几个细节不幸地削弱了我那看似传奇的编程技能。我的记忆有些模糊，但我认为以下才是 73 年夏天的真实经过。
>
>我并没有在去西海岸的路上从贝尔实验室拿到磁带。相反，在 PARC 的时候，我花了几个下午时间在伯克利的 Mike Stonebraker 小组，并从他们那里（经过 AT\&T 的必要许可）拿到了一份 Unix 和相关文档。我随后开始学习足够的 C 语言来编写 SI 磁盘驱动程序，并用他们的 11/45 机器配合 LA30 DECwriters 构建系统（那是个痛苦的经历）。据我记得，他们当时正忙于开发 Ingres。
>
>因为系统必须在我回到 QMC 后第一次就能正常工作，我决定在回英国的路上先去贝尔实验室一趟。Ken Thompson 检查了我的代码，发现了一两个错误（几乎肯定是因为在 C 语言中错误使用指针），然后把整个 Unix 软件装到了 7 到 8 盘 DECtape 上。Unix 就这样第一次装进了英国，装在一只 PanAm 行李袋里！
>
>作为英国首个使用 Unix 的地方，我记得 74 年时受邀到 Edinburgh 和 Cambridge 介绍我们使用这个叫 Unix 的奇怪操作系统。让我印象深刻的是 Cambridge 的 Neil Wiseman 和 Charles Lang 的团队非常反感，根本不考虑采纳一款没有供应商支持的系统（据我记得他们当时使用的是 RSX-11）。这就是早期推广者的失望啊！

不久之后，Nigel Martin 是玛丽女王学院的一名学生，当城市学院的 Sunil Das 获得了西部电气许可后，就不必再等新泽西去处理向英国运送软件的问题了：Sunil 从 Nigel 那里拿到了第 5 版 + 版本。

与此同时，多伦多大学也获得了 Unix。在详细介绍历史之前，必须强调 Unix 与加拿大的紧密联系。Brian Kernighan 是多伦多大学的本科生；Al Aho 也在那里获得了学位；Heinz Lycklama 在安大略省汉密尔顿的 McMaster 大学接受教育；Morven Gentleman 曾在蒙特利尔的 McGill 大学就读，并在安大略省滑铁卢大学任教 15 年；Tom Duff 是滑铁卢大学的本科生，后来加入了多伦多大学的 Rob Pike、David Tilbrook、Howard Trickey 和 Mike Tilson 团队；Tom Cargill 在滑铁卢大学获得博士学位。还有许多其他人可以列举（甚至我自己也曾在多伦多大学任教 11 年）。

多伦多大学于 1974 年中购买了一台 PDP 11/45，运行的是第 5 版。10 月 1 日，它获得了第 6 版的许可。其他大学就没那么耐心了。Tom Duff 曾告诉我：

>1974 年，在滑铁卢大学。Steve Johnson 当时正在休学年（我那时也是那里的本科生），他从实验室打电话连接到了 Unix 机器。有人在他身边偷看了号码，后来用这个号码打电话，拿走了系统源代码。

Doug McIlroy 告诉我，传说是错的：是他的实验室电话号码被偷了。“我在滑铁卢做了一个演讲，Unix 的电话号码出现在学生计算机俱乐部的电话账单上。等到教职工发现并绝望地叫我去问时，我们的代码和他们的代码已经纠缠在一起，无法分开了。”

翌年，Duff 成为多伦多的研究生。（Rob Pike 是 1975 年夏天的实习生；Dave Galloway 是 1976 年夏天的实习生。）Duff 说：

>这台 45 机在 9 月到达，12 月开始运行第五版。我记得六版开始运行是在稍晚一些的时候……1975 年初可能是对的。那时我正在写论文，还没到第六版引入的分离指令和数据（split I\&D）阶段。\[Mike] Tilson、\[Bill] Reeves 和我组成了那个冷加载第五版磁带的团队。
>
>我们遇到了一些问题，给 Ken 打电话寻求帮助，虽然显然他接到的电话比他想象中还多。大约二十个运行第五版的站点，这个分发规模远大于他之前遇到的。mkfs 的说明中提到，如何在 RKO5 上用 4000 个块制作根文件系统，剩下 872 个块（几乎半兆字节！）用作交换空间。Bill 在第二个 RK 上敲入了同样的公式来制作文件系统，觉得浪费的几千字节不值得花时间去查 RKO5 文档了解它到底有多大。一个星期后我们遇到了瓶颈，我花了几个小时阅读 check 程序中 `-s` 选项的代码，发现实际上可以修改超级块里的文件系统大小，然后运行 `check -s` 来回收这些块。

Duff 还因为使用系里的 Xerox 复印机打印 yacc 手册而惹上麻烦——在那个年代，官僚体系严格把持着复印权力。

>Mike Tilson 修改了 Duff 的版本。
>
>第一款系统是 PDP-11/40，这是一台临时机器，在等待 11/45 交付期间使用。我相信我们能够验证 Unix 仅用 64KB 内存就能启动的说法！这盘磁带是 Ken 亲自制作的，他在贝尔实验室亲手交给我的（当时和现在一样，AT\&T 发货很慢，但不像现在，你能绕过繁琐的手续，自己拿到磁带）。
>
>11/40 配备了 GT-40 显示器：它的驱动程序是多伦多大学最早的“定制破解”之一。


1977 年 2 月 11 日星期五，位于多伦多校园 Sanford Fleming 工程大楼东北角发生火灾。尽管多伦多消防队全力扑救，建筑几乎被烧毁，剩余部分（除立面外，现为新楼的正面）也被拆除。根据 Tilson 所述，11/45 计算机整夜运行，直到……

>大约在上午 9 点左右，消防队终于理清了大楼内错综复杂的电线，成功切断了电源。还有一点值得注意：火灾发生前一周，实验室经理曾讨论过异地备份的问题，结论是这是过于紧张的想法，可能没必要。火灾过后，我们返回时，首要任务之一就是建立异地备份程序。

1977 年 11 月 1 日，多伦多获得了 Phototypesetter V7（照相排字机）的许可。稍后我会回到多伦多的情况。现在，我们先去欧洲。Teus Hagen 在第 10 章讲述了 Unix 在荷兰的故事。Hagen 认为，“Unix 中的技术（字符串表达式、yacc、行编辑器、文本处理、awk、字节流哲学、管道）在早期推动了欧洲计算机科学的巨大进步。仅仅几个月内，欧洲这边的成果就大幅领先。”他还告诉我：

>我认为我们（阿姆斯特丹数学中心）大约在伦敦的玛丽女王学院获得 Unix 的差不多同时也收到了它。大约过了一年，其他人才拿到了第 6 版。我手里还保留着最初的手册。奈梅亨大学（Hendrik Jan Thomassen）是下一个安装 Unix 的，经过一番讨论，弗里大学的 Andy Tanenbaum 也获得了它（当时 Andy 正忙于自己的操作系统开发）。
>
>我们面临的一个问题是计算机设备价格极高：磁带单元大约要 4.5 万美元，一台磁盘驱动器（DEC RM05）要 5.5 万美元（我们的其中一台设备曾经一次差点“飞”出机房）。
>
>我们曾经在与 DEC 的维修人员打交道时遇到麻烦，因为他们要求系统必须运行 RSX 或 VMS，否则就无法修复我们的硬件问题。然而，由于我们的 Unix 下的报错信息要清楚得多，我们最终还是说服了他们。但问题是：你怎么能在一台有故障的计算机系统上安装 VMS 或 RSX 呢？

Hagen 并不是唯一一个遇到 DEC 麻烦的人，Lou Katz 告诉我：“基本上，DEC 的维修人员会运行他们的诊断程序，然后说是我们的软件有问题，因为他们的诊断程序没问题。特别是，事实证明没有任何 DEC 诊断程序测试过 PDP-11 的 Supervisor 模式，而 Unix 就使用了这个模式。”Armando Stettner 说：“Unix 在 PDP-11 上做了很多事情，是 DEC 的操作系统和诊断程序都没有做过和测试过的。”

>DEC 无法相信所有东西都是用 C 语言写成的（C 语言是什么？）并且以大约 500 页的代码清单形式提供。更令人难以置信的是，你可以随时更改源代码。相比之下，DEC 提供了一大堆手册和文件，堆得几乎和计算机房一样高。
>
>起初，我们有一台 PDP-11/45（带有磁芯存储器；是个很好的取暖设备！），但只有一个容量为 1.5 兆字节的 RKO5 磁盘驱动器作为交换介质。我们不确定公共交通工具对磁盘盘片磁场的影响（阿姆斯特丹有很多有轨电车）。因此，我们不敢冒险，会步行从数学中心走到自由大学（大约七英里）。后来我们逐渐放心了，Unix 用户就因为会在有轨电车上提着装满 RKO5 磁带盒的大箱子而被认出来。

正是 Hagen 在欧洲启动了第一个 Unix 网络，并开始了欧洲 Unix 用户组的正规化。正如他所说，在欧洲启动网络比美国的 UUCP 和 ARPANET 更为复杂。

>欧洲邮电局（PTT）不允许使用拨号器和调制解调器，所以我们在建立 Unix 网络时遇到了很多麻烦。邮电局的人根本无法理解 UUCP 的功能（我们讲的完全是另一种语言）。于是我们使用了一种办公桌面半自动拨号器，并把它装进一个盒子里（和 110/300 波特的调制解调器是分开的）。一家小公司生产了更多这样的设备，并把它们作为无线放大器走私穿越边境。我的好朋友、DEC 的 Armando Stettner 帮助我建立了与美国的连接（当时只有邮件，因为新闻还不存在）。压缩技术还不为人知，因此由于速度缓慢，我们花了不少钱。这就是为什么欧洲网络至今仍实行严格计费制度的原因。因为夜间资费低，我们把与美国的通信时间调整到了夜间。有一天早上，我发现与美国的调制解调器线路宕机了：不断交换错误和重启信息，这种情况已经持续了大约 10 小时。一次 10 小时的电话费非常昂贵，所以我被叫去见主任（他是数学家，对计算机一窍不通，也不想管这些）。结果我惹了不少麻烦……
>
>我们过了好几年才开始收到新闻。我还记得自己在网络上发表的第一篇文章，因为美国那边的人会对我大喊，问我到底是怎么回事，怎么能在他们写文章前几个小时就回复他们的文章！他们刚刚发现美国以外的世界。
>
>【我问过 Teus 关于 Kremvax 的事】
>
>那是愚人节。我们从数学中心发了一篇带有路径追踪的文章到莫斯科，说克里姆林宫的 VAX 正在宣布它首次登上网络。除了在网络上引发了一阵喧嚣，很多人互相大喊之外，我还听说美国政府的一次安全会议因此变得紧张起来。官员们试图立刻切断通往欧洲的通信线路。但幸运的是，很快他们发现这样的做法是徒劳的，网络的“无政府状态”依旧继续。

Kremvax 的真正起源者是 Piet Beertema；该消息发布于 1984 年 4 月 1 日。6 年后，当 demos.su 加入 USENET 时，Demos 的高级程序员 Vadim Antonov 必须说服大家这不只是另一个恶作剧。Armando Stettner 的故事与 Hagen 的略有不同，他告诉我：

>我们（DEC）当时和很多地方通过 UUCP 通信，但我们还没有传送 NETNEWS。而 Teus 和我在一个会议上，谈到了传送 NETNEWS 的想法。我说：“听着，跨越大西洋传送 NETNEWS 的问题在于连接时间。如果你那一端和我这边都加上压缩，我就给你发 news。”我并不知道会发生什么。但后来 Teus 给我发了封邮件说：“把这些东西从我们的机器上拷走。”于是我们成功跑起来了……不久之后，我就开始通过 Teus 的机器和欧洲交换 NETNEWS。几周顺利运行后，我又通过 Robert Elz 的机器，把澳大利亚也接入了网络。

有一段时间，Stettner 的机器 decvax 的电话费每月高达将近 25 万美元。DEC 的一位财务人员问他，他们只有四条线路，怎么可能产生这么高的账单。Stettner 回答说：“哦，那是我们高端机器在交换信息。”

Stettner 向澳大利亚发送 news，其实并不像听起来那么奇怪。1974 年夏天，当新南威尔士大学（UNSW）准备接收一台 PDP-11/40 时，John Lions 在《ACM 通讯》上读到了那篇文章，随后学校在年底前就与西部电气商定了许可证。以下是 Lions 的叙述：

>1974 年，新南威尔士大学（UNSW）用一台运行 KRONOS 的 CDC Cyber 72-26 计算机替代了 1965 年的 IBM 360/50。
>
>这台 Cyber 计算机服务于大约 100 台类电传终端（300 波特率），以及 12 台 PDP-11/40 计算机……其中 7 台 PDP-11/40 购入时仅为最简配置（16 KB 内存），而另外 5 台配置了 128 KB 核心内存、一个 DJ11 终端多路复用器以及各 3 个 RK05 磁盘单元……
>
>于是，一切都为我们收到 Unix 软件的那一刻做好了准备。仅仅两个晚上的试验，就足以让我们意识到我们偶然发现了一件相当有趣的事物，而且 Unix 系统相较于 RSX-11D 将带来显著优势……
>
>我们的问题变成了：“如何安排在白天也能运行 Unix，而不仅仅是在夜间远程批处理服务不需要的时候？”答案显然是开发一个可在 Unix 系统下运行的 U-200 仿真器。由 Ian Johnstone 领导的四人爱好者小组接受了这个挑战，并在两周内开发出原型系统。又过了四周，RSX-11D 被彻底取代，永不复返。

Greg Rose 是 1974 年新南威尔士大学（UNSW）的一名本科生。我和他聊了聊这段历史。

>我那时是名完全没有经验的本科生，而学校正处于动荡时期。原先是 IBM 系统……那台 360/50 正在退役。实际上，它只是从教学和科研中退出，被彻底移交给了行政部门——毕竟他们可不想重写所有的 PL/I 程序。
>
>当时的想法是转向使用 Cyber……所以学校买了五台 PDP-11/40 和七台 PDP-11/10。Cyber 系统预计在 1975 年 1 月投入使用，而在 1974 年中，恰好有两篇很有意思的论文发表：一篇是关于 Unix 的，另一篇是关于 Pascal 的。所以 John Lions 跑去搞到了 Pascal，而 Ken Robinson 则搞来了 Unix……
>
>教学必须继续进行。二年级的一门必修课是汇编编程，而汇编器必须在 PDP-11 上运行。于是安排了一张非常复杂的时间表，以便我们能为 PDP 系统准备一个批处理汇编器。而我们还得支持学生完成作业并进行调试，否则我们就无法在这台机器上运行 Unix。所以 Ian Johnstone、Greg James、Ian Hayes、Peter Ivanov 和 John Wainwright 这帮人就决定在这台机器上运行 Unix，因此他们必须编写所有这些 U-200 设备驱动程序和仿真器，以便系里能够继续运行 RSX-11，同时机器运行 Unix……
>
>但总得有人来维护系统、确保它能运行。于是 Ken Robinson 说：“我们有两个学生现在没有被好好利用，不如交给他们吧。”我就是其中之一，Chris Maltby 是另一位。
>
>我的第一个任务是为汇编课程写一个批处理支持程序，而那门课程我自己还是个学生！在 1975 到 1976 年间，Unix 在校园里大获成功。我们拥有了一台 PDP-11/70 和另一台 PDP-11/45，而新成立的管理学院也决定他们需要 Unix。然后到了 1976 年，伍伦贡大学（University of Wollongong）成立了。它原先是 UNSW 的一个学院，但后来独立了。那时候 Interdata 几乎是在“白送”机器，为了打入市场，他们给了伍伦贡一个无法拒绝的报价。
>
>我们以前常会有一些非正式的聚会，大概十来个人围坐一圈喝咖啡。在其中一次聚会上，Rich Miller 说：“你们知道我们有一台机器，搭载了一个简直糟透了的操作系统。但我们不明白，既然 Unix 是用一种相对高级的语言编写的，为什么不能让它在这台机器上运行呢？”
>
>于是我们坐下来花了几天时间，主要是我和 Ian Johnstone，讨论体系结构以及我们需要如何修改编译器来生成代码。而 Rich 则离开了一段时间——他是个非常厉害的人——我想他现在应该在牛津。他回来之后说：“我想我搞出一个编译器了。”于是他和 Ian 就一起去交叉编译这个编译器，然后带着它回到伍伦贡。
>
>我们就这样来来回回地驱车奔波——单程一百公里——带着 9-track 磁带。当我们到达伍伦贡时，由于 Interdata 没有磁带机，我们就会在一台 Univac 11-某某的机器上读取这些磁带，并把内容写到与 Interdata 兼容的磁盘包中。
>
>但其实总共只去了三趟：第一次是带去编译器，第二次是操作系统的初步移植版本，最后一次是升级版，因为我们起初使用的是第 5 版，当我们拿到第 6 版时，Rich 说：“好吧，现在给我一卷最新的源代码磁带。”
>
>与此同时，Steve Johnson 和 Dennis（Ritchie）也在进行他们自己的移植工作。

这确实是一项非常了不起的努力，正如 Steve Johnson 回忆的那样。Rich Miller 在 1977 年 2 月的第二届澳大利亚 Unix 用户组会议上谈到了这件事。

在 1976 年 3 月的《UNIX NEWS》上，刊登了一封长信，信件日期为 1975 年 10 月 10 日，寄信人是 John Lions，收信人是 Mel Ferentz。这封信的开头写道：

>我们最近才看到您最初的两期《UNIX NEWS》，因此之前无法参与投稿。不过，我们非常感谢您创办这份通讯的努力，并希望它能够取得成功。

Lions 于 1976 年 6 月 21 日再次写信给 Ferentz，宣布将于 1976 年 8 月 29 日在新南威尔士大学举行首届“东海岸”Unix 用户会议，并通知用户，纽卡斯尔大学和悉尼大学也已加入 Unix 社区。

9 月 17 日，Lions 写信报告了会议情况：“有 30 多人聚集。”会议非常成功，于是又安排了下一次会议，定于 1977 年 2 月 18 日举行。更重要的是：

>大家一致认为，鉴于 Unix 支持的非常规性质，Unix 用户之间确实有合作的必要。

1977 年，John Lions 完成了他的《UNIX 操作系统评注》，这是他复刻第 6 版源代码的配套著作。这两本薄薄的小册子，可能是计算机史上最重要的未正式出版的著作。我问他关于源码和评注的事，他说：

>我当时在教授操作系统课程；我和一位教授编译器课程的同事竞争，他让学生们编写真正的编译器；所以代码阅读练习看起来是个不错的主意。而且我们的 Unix 许可证并没有明确禁止这种活动。为什么选择 Unix？别无选择。正如你所知，它非常强大，而且远胜于竞争对手（我们当时也获得了 Brinch Hansen 的 SOLO 系统）。

1977 年 3 月的 UNIX NEWS（第 2 卷第 3 期）宣布，该书已提供给许可证持有者，同时 Ferentz 发表了备注：Ken Thompson 已经看过该书的第一个版本，评价很高。价格包括空运费为 17.70 澳元（当时不到 20 美元）。UKUUG 通讯宣布代码和注释本已可获得，但下一期声明未来的订单应直接向贝尔实验室下单，到 1978 年，已不再提供这些版本。它们可能是计算机科学领域中被复印最多的书籍。书中附有适当的版权声明及对许可证持有者的限制，但西部电气依然无法阻止这类极具价值资料的传播。我承认自己既有一份多代复印件，也有一份由 John Lions 亲笔题字、封面为鲜橙红色的版本。Mike Cole 曾问我是否有...

>确认了 Jim Curry 是首位将 Unix 引入欧洲的人，他在奥地利的 IIASA 安装了 Unix。据我回忆，Jim 在 William 前往 PARC 后不久也离开了 PARC。Jim 在 72/73 年冬天访问了我们位于 QMC 的实验室，并帮助说服我，我们将新的教学系统基于 Unix 并非完全疯狂。

Curry 曾（并且仍然）在位于维也纳以南拉克森堡的国际应用系统与分析研究所工作。他从 1974 年到 1978 年担任那里的计算机服务主管；他告诉我：

>我于 1975 年 1 月在我们的 PDP-11/45 上安装了 UNIX（版本 5）。据我所知，这是欧洲的首次 UNIX 安装。
>
>到了 1978 年中期，我招募了 Jim Kulp 接替我担任计算机服务主管，从那时起直到 1982 年，我与计算机系的直接联系不多，所以这段时间的细节我有些模糊。但我确实知道 Jim 在 1979 年初买了我们的 VAX/780。我不确定这是否是奥地利的第一台 VAX，但这肯定是第一台运行 UNIX 的机器；Jim 当时运行的是一款非常早期的 BSD 系统——很可能是 3BSD，或者是 4BSD 的预发布版本（还未成为 4.0BSD）。
>
>至于网络接入，IIASA 在历史上没有特别的位置。早在 1975 年，我们就尝试过各种临时的电信链接（主要是与东欧），但我们的第一个真正的国际邮件接入是通过一条 2400 波特的租用 UUCP 线路连接到维也纳技术大学（tuvie）。我不太记得具体时间，但因为这晚于 tuvie 的设施，我想这可能不算特别重要。

Herb Hasler（来自 IIASA）说：“我相信 IIASA 是奥地利第一台拥有 VAX 的机构。”更重要的是，IIASA 的 Jim Kulp 编写了 Unix 作业控制的第一个版本，这个版本被包含进了 4.1BSD（1980）。

这再次体现了远程用户的工作被纳入了主要版本中。

正如 John Lions 与 Mel Ferentz 的通信所表明的那样，分散在各地的 Unix 爱好者之间的大部分交流——正如计算中心的支持者所看待他们那样——是通过 UNIX NEWS 及其继任者 login: 实现的。例如，AT\&T/西部电气的律师对可能允许或不允许的行为态度犹豫不决，导致了 1976 年 4 月 30 日的公告，当时哈佛科学中心的 Lew Law…

>愿意承担复制和分发 UNIX 手册的任务。……《UNIX 程序员手册》第六版，日期为 1975 年 5 月，将被完整复制。大多数安装点会选择删除几页，大多数用户无需了解这些内容。
>
>《UNIX 分时系统使用文档》第六版将被复制，但会省略第 1 节（UNIX 的安装）和第 13 节（关于 UNIX 的安全性）……


同一期还刊登了波士顿儿童博物馆的 Bill Mayhew 关于“如何用 49 美分（加税）修复你的 PDP-11/40 静电问题”的文章。下一期（1976 年 5-6 月）宣布了“软件交换的首次邮寄”。第一盘软件包含哈佛的软件，复制和邮寄由当时在芝加哥伊利诺伊大学分校的 Mike O’Brien 负责。1976 年 8 月的 UNIX NEWS 包含了 Alan Nemeth 的首次投稿，内容涉及分离的 1\&D 空间中浮点模拟器的问题。1976 年 11 月宣布了第二次软件发行，并附有 O’Brien 的以下说明：

>我得到了 Bell UNIX 正式系统相对于“标准”第 6 版的所有更改的“diff”清单……总之，我列出了大约 50 项更改，并已将清单发送给 Ken 进行核实和评论。这些更改可以通过中心特别请求获得。

第二次发行包含了来自 RAND 公司、海军研究生院、加利福尼亚大学圣地亚哥分校、耶鲁大学和伊利诺伊大学厄巴纳 - 香槟分校的贡献。UNIX NEWS 还刊登了来自多伦多大学的图形软件可用性的公告。

第三次软件发行在 1977 年 5-6 月刊中宣布，内容还包括“超过 150 人”参加了 1977 年 5 月在厄巴纳召开的会议的消息。

>Mini-UNIX 已经发布，LSI-UNIX 和 Mert 可能会在稍后的某个时间跟进发布。

记住：没有广告，没有支持。Urbana 会议还举办了第一次编程比赛，由 Steve Holmgren 组织。所有用户都得自力更生。

其中一位自力更生的用户是东京大学的石田晴久。他告诉我：“我是日本首位 UNIX 用户和持证者。1976 年我与 AT\&T 贝尔实验室签署了协议。Unix 是第六版，我在一台经过轻微修改的 LSI-11 上实现了它。”LSI-11 是 DEC 自己在微芯片上模拟 PDP-11 的产品，发布于 1974 年。最早的版本没有内存管理，内存管理是由另一颗芯片提供的。东京很可能购买了这个版本的 LSI-11，因为没有内存管理的话 V6 版本是无法运行的。

1980 年，独立软件公司 SRA 的岸田孝一买了一台 VAX，并请 Bob Schulman 到日本安装 Unix。Schulman 告诉我：

>我在 1980 年夏天去安装了第一版的 32V，随后在 VAX 11/780 上安装了 BSD 3.0。
>
>他们买 VAX 的原因，当然是因为他们想要 Unix。他们想要 Unix 的原因是，当时岸田孝一是个爱社交的人，常去欧洲和美国参加各种会议。那时，他遇到的几乎每个研究人员都告诉他他们在用 Unix。所以他决定自己也必须用 Unix。基本上，就是为了能和那些顶尖研究人员拥有相同的工作环境。我很喜欢他的这个想法。
>
>我 1980 年夏天到那里时，780 刚装好，但他们没怎么用，因为还需要 32V 的磁带。安装完成后，这么大一笔投资自然得有点“天助”，所以他们请来了一位神道教牧师，在机房里做了某种祝福仪式。仪式中挥舞着棕榈叶，牧师用某种古老的日语方言念诵（估计没人听懂）。当然也敬了清酒，不过我觉得 780 应该没喝多少。出于安全考虑，建筑物晚上被锁住了，我从没搞清楚具体原因。所以，如果你想熬夜工作超过晚上十一点四十五分，必须等到早上六点以后才能离开，这在一定程度上阻碍了深夜编程。
>
>我的工作职责之一（也就是职责）是教 SRA“Unix 的方法”。我觉得如果“Unix 的方法”有社会层面，我还得试着解释什么是“黑客”和“书呆子”（nerd）。因为语言和文化障碍（我的日语从来没学好），花了很久他们才真正理解。黑客这个概念对他们来说非常有吸引力。至于书呆子，他们理解得比较困难，我觉得他们没能像我那样对书呆子产生负面反应。大概是因为他们认为书呆子的执着也没什么坏处。

日本 UNIX 协会（jus）由岸田浩一、村井淳和斋藤信雄创建。我稍后会回到 jus 的话题，但现在我想回到 USENIX。1977 年 9 月的《;login: 》通知会员 PWB 已发布，并且有关它的论文可向 Ted Dolotta 申请获取。下一期（第 2 卷，第 9 期）声明“用户组的会员人数现已逾 250 人。”1977 年 11 月的《;login: 》包含两个公告：一是 Joseph F. Ossanna 的逝世；二是即将出版的《C 程序语言设计》。

>还用多说吗？

1978 年 3 月，Lew Law 宣布哈佛科学中心提供 PWB 手册，分为四卷，总价 26.50 美元。同年 8 月，Ferentz 将《;login: 》整个头版 dedicated 给了《Bell System Technical Journal》（第 57 卷，第 6 期，第 2 部分）关于 Unix 的特刊公告。

漏洞修复、硬件修复、新软件、巧妙的 hack——这正是 USENIX、AUUG 和 UKUUG 致力的方向。我最喜欢的贡献是 Tom Ferrin 的一篇文章，他当时和现在都在加利福尼亚大学旧金山分校。他给《;login: 》寄来了一封两页的信（1977 年 12 月 9 日），附带一些代码和示意图。信中部分内容写道：

>PDP-11/45 和 11/70 计算机中的内存管理单元相比于其他 PDP-11 系列计算机提供了若干优势。其中一个更强大的功能是能够将程序分离成指令段和数据段……
>
>有四条 PDP-11 指令便于程序在不同寻址模式以及内存中的指令/数据区域之间进行通信。这些指令是“在之前的指令/数据内存空间间移动”（mtpi，mfpi，mtpd，mfpd）……
>
>由于 DEC 希望“……维护专有程序的完整性”，当进程状态字等于 17xxxx（即当前模式和之前模式均为 USER）时，‘mfpi’指令执行不正确。这个事实导致 C 子程序‘nargs.s’无法按预期运行……
>
>针对这个缺陷，有几种解决方案……
>
>第四种：修改硬件，使其“更正确”地工作。
>
>经过几次与 DEC 代表的电话沟通以及几个小时查看微代码后……我们提出了对 PDP-11/70 CPU 的一个简单修改，使‘mfpi’指令能够正常工作。这个修改对于有经验的人来说大约需要 15 分钟，包括切断一条电路铜箔并在 M8138-YA 内存管理板上添加一根跳线……


Tom Ferrin 的电路图如下所示：

 ![](/assets/mfpi_fix.jpg) 

