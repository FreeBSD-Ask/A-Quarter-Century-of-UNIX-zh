# 互相争斗的 Unix 系统

直到 1978 年，Unix 都意味着 AT&T 的操作系统。随着 PWB 2.0，V7，32V，和 3BSD 的出现，它加入了更多东西。但是 Unix 不只是 AT&T 的产品，它是一个“电话通讯支持工具”。因为和解协 AT&T 议被迫离开计算机商业，不允许继续在计算机市场参与竞争。没有了 AT&T 的支持，Unix 的未来命运从科研界转手到了 Unix 支持小组 (USG)。USG 在 70 年代大部分时间掌握着 Unix 的命运，然后到了 1979 年，微软和圣克鲁斯操作公司 (SCO) 推出了 XENIX2，伯克利推出了 4BSD，这两个系统都是 V7 的衍生版本。XENIX 是 Unix 针对 Intel 8086 和其他很多硬件架构的第一个移植版本。虽然它变得和其他版本不再兼容，但它也是一个非常流行的版本。自由软件基金会的 Len Tower 向我评论说“SCO Unix 用起来就像是在向前穿越时间”。

正如 Andy Tannenbaum 指出的，“贝尔实验室有一个 Unix 支持小组，但是你从没听说过 Unix 开发小组。这是因为贝尔公司没有权限开发计算机操作系统...”。1981 年 Jeff Schriebman 创建的 UniSoft 推出了一个名为 UniPlus+ 的移植版本，它与 System III 和现在的 System V 保持兼容。1983 年伯克利的一个小组成立了 mt Xinu 来支持和商业化 BSD，其中的成员有 Bob Kridle，Alan Tobey，Ed Gould，还有 Vance Vaughan。Debbie Scherrer 不久后也加入了他们。他们先是销售了更多的 4.2BSD，然后是 4.3BSD(mt Xinu 擅长于客户服务：1986 年 Debbie 自己安装了我的 4.3 纸带)。

5 年的时间中，Apollo，DEC，Eakins，Gould，Integrated Solutions，Masscomp，mt Xinu，NSC，和 Wollongong 是众多 Unix 销售公司中的一部分。这些销售 AT&T System III 或者 System V 衍生版本的公司有：AT&T，Altos，Apollo，Compaq，Convergent，HP，Honeywell，IBM，ITT，Intel，Interactive，Masscomp，Microport，Microsoft，Motorola，NCR，NUXI，Opus，SCO，Silicon Graphics，Sperry，Sun，Tandy，UniSoft，Wollongong。此外，Amdahl，Apollo，Apple，Cray，DEC，Data General，HP，IBM，Inter，Motorola，Unisys 和许多其他的公司提供私有的 Unix 版本，其中一部分是基于 4.2BSD 的。

所有的这些版本，不管是 AT&T 还是 BSD 的衍生版本，都需要 AT&T 的授权。最近几个 Unix 的版本可以不需要这种授权。虽然没有一个商业产品是真正强健的，但 BSDI，386/BSD，还有 NetBSD 都已经可以在任何 386/486 机器上运行。这些“自由授权”版本都衍生自自由的 CSRG 发行版，当我写这些的时候它仍然在诉讼中。详细信息可以参见 29 章。Linus Torvalds 写的 Linux 也运行在 386/486 机器上，不过没有使用 CSRG 的代码。这四个系统都使用了大量自由软件基金会的软件。Ritchard M. Stallman 创建了自由软件基金会，并为他几近完成的 GNU 系统写了那些软件。GNU 软件包括大多数 Unix 软件可以自由分发的重制版本 (它们在 GNU 项目中一个叫做‘copyleft’的授权下发行，这意味着原始和改进后的版本必须可以让其他人自由修改和分发源码。如果发布了二进制版本，源码也必须一起发布出来)。**gcc** 是 GNU 的 C 语言编译器，可能是 Steve Johnson 的 pcc 最好的继任者。

最终，这些衍生和克隆版本可以运行在一系列的处理器上：DEC，Intel，MIPS，Motorola，NSC，更多的就不再一一列出。

这些长长的名字列表让用户和准用户们感到疑惑：这些都是做什么的？当然，尽管名字们看起来很混乱，但没有“开放系统”就没有任何标准化，就会导致无法协同工作。换句话说，如果你理解了 BSD 或者 SVR4，又或者 AIX，HP/UX，Solaris，Ultrix，那么你对其他的变种就已经理解了 90%。程序开发的编程语言是 ISO/IEC C。

Doug Mcllroy 问我：

> 你有没有想过，为什么 Unix 在刚开始的时候那么小巧，又有着比 MS-DOS 强大的多的能力，但它却没有进入个人计算机的世界？还有为什么现在的 Unix 这么臃肿？

Armando Stettner 给我的答案是 Unix 从来没有进入“微软的市场”，并“人们工作中真正的需求要比 V6 和 V7 提供的多很多”。我想 Unix 没能进入个人计算机市场的一个原因是它没有一个让普通人可以很容易使用的界面。虽然我很多编程的朋友都声明命令行比 MS-DOS 更加友好更加灵活。当 IBM 退出了运行 MS-DOS 的 PC，当乔布斯和沃兹尼亚克推出了苹果，从来没有坐到计算机前面的人们感到他们可以和这些机器交互。回忆一下 1983 年苹果的 Lisa，他们也没有特别成功。这些从来没有在大学校园和科研协会使用过大型机器的人们，他们不知道自己错过了什么。虽然 MS-DOS 比任何一个 Unix 命令行都要差劲，还有着差强人意的错误消息。

我不知道微软投资 XENIX 是不是想要阻止 Unix 在市场上的成功，但是它显然有这样的效果。

关于 Unix 为什么变得臃肿了，我觉得这很简单。如果我们想象 Ken 和 Dennis，Bill Joy 和 Kirk 以及 Sam Leffler，Mike Karels 去做“品位裁决”，就不会有现在这么多的 Unix 厂商。当 System V 采用了大量的伯克利增强修改，将它们整合进系统，AT&T 的 Unix 系统实验室 (1993 年被 Novell 收购) 仅仅将将代码收录在一起。这是一种满足用户所有要求的态度。想要一个编辑环境？这有 Bill Joy 的 vi 和 Richard Stallman 的 emacs。想要一个窗口系统？这有 X Window 系统和 Motif 以及 OpenLook 两种用户接口。想要一个命令行？这有 sh，csh，还有 ksh。在那时，USG 被告知为了证明开放性，要讲大量 BSD 的特性添加到 System V 中去。我不能确认这一点。这些特性每一个都增加了空间占用，分配了更多的内存。每一个特性都是几千上万行的代码。一个苗条的系统应该有更少的选择和更少的实用工具。
