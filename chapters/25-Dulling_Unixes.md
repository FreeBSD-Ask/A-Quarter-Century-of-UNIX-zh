# 互相争斗的 Unix

直到 1978 年，Unix 指的还只是 AT\&T 的操作系统。直到 PWB 2.0、V7、32V 和 3BSD 的出现，混乱才开始出现。但 Unix 并不是 AT\&T 的操作系统产品。它是一款“电信支持工具”。请记住，由于同意令的限制，AT\&T 认为自己不能涉足计算机行业，也无权参与计算机市场的竞争。Unix 在 AT\&T 的未来从研究部门移交给了 USG —— UNIX 支持组，在 1970 年代的大多数时间里由它掌控发展方向。随后在 1979 年，微软和 Santa Cruz Operation 发布了 XENIX，而伯克利则发布了 4BSD，它们都是基于第 7 版的衍生系统。XENIX 是第一款为 Intel 8086 以及许多其他架构实现的 Unix。它仍是一种非常流行的实现，尽管已经日益与其他系统不兼容。自由软件基金会的 Len Tower 曾对我说：“使用 SCO Unix 就像在时间里倒退。”

正如 Andy Tannenbaum 所指出的：“在贝尔实验室内部确实有一个 UNIX 支持组，但你从没听说过 UNIX 开发组。这是因为贝尔系统下的任何机构都没有被授权开发计算机操作系统……”1981 年，Jeff Schriebman 创立的 UniSoft 推出了一款移植版本，称为 UniPlus+，它始终与 System III 兼容，并已发展到兼容 System V。1983 年，一群来自伯克利的人组建了 mt Xinu（即 Unix™ 的反写）来商业化并支持 BSD，其中包括 Bob Kridle、Alan Tobey、Ed Gould 和 Vance Vaughan。不久后，Debbie Scherrer 加入了他们。他们首先销售的是 more/4.2BSD，然后是 more/4.3BSD。（mt Xinu 以客户服务著称：1986 年 Debbie 亲自为我安装了 4.3 磁带。）同样在 1983 年，USG 和 PWB 组合并为 Unix 系统开发实验室。

五年内，Apollo、DEC、Eakins、Gould、Integrated Solutions、Masscomp、mt Xinu、NSC 和 Wollongong 等公司开始销售伯克利 Unix。而销售 AT\&T System III 或 System V 衍生版本的公司包括：AT\&T、Altos、Apollo、Compaq、Convergent、HP、Honeywell、IBM、ITT、英特尔、Interactive、Masscomp、Microport、微软、Motorola、NCR、NUXI、Opus、SCO、Silicon Graphics、Sperry、Sun、Tandy、UniSoft 和 Wollongong。此外，Amdahl、Apollo、苹果、Cray、DEC、Data General、HP、IBM、英特尔、Motorola、Unisys 以及其他众多公司也都提供 Unix 的专有版本，其中有几个是基于 4.2BSD 的。无论是 AT\&T 还是 BSD 衍生系统，它们都需要向 AT\&T 获取许可证。

最近，出现了若干无需此类授权的 Unix 版本。尽管它们还不是成熟的商业产品，但 BSDI、386/BSD 和 NetBSD 都可以运行在任何 386/486 机器上。（这些“免许可”版本全部源自 CSRG 的免费发布，在我写作时仍处于诉讼中；1994 年 2 月 4 日，这一状况发生了变化；见第 29 章。）Linus Torvalds 编写的 Linux 同样可以运行在 386/486 机器上，而且没有使用任何 CSRG 代码。这四个系统都大量使用了由 Richard M. Stallman 创立的自由软件基金会（FSF）为其近乎完成的 GNU（“GNU 不是 Unix”）系统编写的程序。GNU 程序包括对大多数 Unix 软件的原创、可自由再分发的重写版本（这些程序以所谓的“著佐权”协议发布，GNU 项目参与者用这个术语来指代其许可证。这意味着原始版本和所有改进版本都必须保持可分发和可修改状态，而且如果发布的是二进制文件，也必须一并提供源代码）。gcc，也就是 GNU 的 C 语言编译器，可能是 Steve Johnson 的 pcc 最重要的继承者。

最后，这些衍生版和克隆版运行在各种计算机芯片上：DEC、英特尔、MIPS、Motorola、NSC，仅举几例。

这种由一锅字母汤煮成的稠糊状混合物最终带来了用户和潜在购买者的困惑：什么系统能和什么系统兼容？可以肯定的是，尽管有那么多的宣传和喧嚣，所谓的“开放系统”并不存在，标准化过程也没有带来任何实际的互操作性。另一方面，只要你理解了 BSD 或 SVR4、AIX 或 HP/UX、Solaris 或 Ultrix，那么你就已经理解了其他任何变种的 90%。而程序开发的通用语言是 ISO/IEC C。

>Doug McIlroy 反过来问我：
>
>你对这样一个问题有什么见解吗：Unix 明明比 MS-DOS 起步时更小巧、更强大，却从未在 PC 世界中取得成功？还有，为什么 Unix 今天变得如此臃肿？

Armando Stettner 给我的回应是，Unix 从来没有拥有“微软那样的市场营销”，而且“真正需要干活的人，所需的功能远远超过第 6 版和第 7 版所能提供的”。我认为 Unix 没能打入 PC 世界的原因之一，是直到最近，它都没有一个普通人也能轻松使用的用户界面（尽管我的很多程序员朋友会坚持认为 shell 比 MS-DOS 更友好、更灵活）。当 IBM 推出运行 MS-DOS 的 PC，当乔布斯和沃兹尼亚克推出 Apple（以及后来的 Macintosh）时，那些从未坐在计算机前的人开始觉得他们能和这些机器互动了（当然他们并非都成功——请回想 1983 年的 Apple Lisa）。由于这些人并不是在大学校园和研究机构里使用大型计算机工作的人，他们并不知道自己错过了什么，尽管 MS-DOS 的界面在某些方面比任何 Unix shell 都更糟，错误信息也确实更加糟糕。

我不知道微软对 XENIX 的投资是否是为了阻止 Unix 在市场上获得成功的策略，但它确实起到了那样的效果。

至于 Unix 为什么会变得如此臃肿，我觉得原因很简单。如果我们把 Ken 和 Dennis、Bill Joy、Kirk、Sam Leffler 和 Mike Karels 看作“品味的仲裁者” \[Stettner 的说法]，那么现在的 Unix 厂商中已经没有这样的角色了。当 System V 采纳了许多 Berkeley 风格的特性时，AT\&T 的 Unix 系统实验室（1993 年被 Novell 收购）并没有将它们整合进系统中，而只是简单地把这些代码拼接起来。此外，还存在一种“用户要什么我们就给什么”的心态。需要编辑环境？给你 vi（Bill Joy）和 emacs（Richard Stallman）。需要窗口系统？给你 X 视窗系统，以及 Motif 和 OpenLook 两套用户界面。需要 shell？给你 sh、csh 和 ksh。那时还有传言说 USG 被要求在 System V 中加入 BSD 的特性，以示“开放性”。我无法证实这个说法。每个这样的特性都占用空间、都需要内存；每一个都是上千甚至上万行的代码。一款简洁、轻量的系统有更少的选项和工具。
