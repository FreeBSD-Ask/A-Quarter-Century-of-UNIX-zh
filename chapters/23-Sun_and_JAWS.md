# Sun 和 JAWS


真正的 Unix 硬件的首次尝试是 ONYX。正如 Mike O'Dell 和 Neil Groundwater 在 USENIX Association 会议上提到的那样，ONYX 曾被宣布。ONYX 由 Bob Marsh 创立，他后来创办了 /usr/group。John Bass 当时为他工作。他告诉我：

>Z8000 ONYX 几乎算不上是 VAX 或单芯片系统。我们带到 Boulder 的系统由三块大约 15" x 22" 的电路板组成（我不记得确切的尺寸）。它的性能和架构更像是 PDP-11/45 或 70……采用分段内存，没有分页。稍后发布的 LSI 11/73 可能更快且价格更低。LSI 11/23 稍慢一些，价格便宜得多（当时我家用的系统就是 11/23，后来升级成 11/73）。
>
>除此之外，ONYX 是第一款设计成桌面型运行 Unix 的系统。它有 8 个串口（用户），价格低于 2.5 万美元，短期内成为 PDP-11 Unix 系统的替代品。
>
>当时构建系统最大的问题是磁盘驱动技术……体积大且昂贵。ONYX 的真正创新在于采用了 8 英寸 20-60MB 的 IMI 硬盘和 1/4 英寸磁带流式存储……这一组合成就了这款产品。实际上，ONYX 的存在是因为风险投资家 Carl Berg 资助 IMI 设计该硬盘，然后需要一个市场来销售……Carl 不得不资助三家计算机公司使用该硬盘以保护他对 IMI 的投资。ONYX、Corvus 和我记不得的另一家公司。
>
>有趣的是，Carl 的一位拥有计算机商店的朋友一直告诉他 Unix 没有市场，ONYX 应该专注于 CPM/MPM Z80 系统（用于 C8002 的 I/O 控制器和启动资金机器）。1980 年夏天，Carl 解散了 ONYX 创始团队（所有 Unix 成员），将公司重心转向 CPM/MPM……一年后 IBM 发布了带 PCDOS/MSDOS 的 PC，CPM 市场在不到六个月内消亡。Carl/ONYX 被迫重建 Unix 团队并重新聚焦 Unix 以挽救公司……但为时已晚。

与此同时，Xerox 开发了 Alto，一种“个人工作站”，实际上更像是我们今天所理解的工作站。它拥有位图屏幕和鼠标。虽然相对昂贵（从未公开出售，但估计价格在 3 万美元左右），但当 Motorola 68000 CPU 推出后，斯坦福的 Andreas Bechtolsheim 和其他学生能够廉价模拟它。斯坦福授权了一款单板计算机，称为 Stanford University Network 板，简称 SUN。有多家公司获得了授权：Codata、Fortune、Dual、Cyb、Lucasfilm 等。机器——被称为 Just Another Workstation（JAW）——开始出现，有些售价低至 1 万美元；运行的系统多为 4.1BSD 或 System III。大多数公司像大多数创业公司一样经历了兴衰。Sun Microsystems 雇佣了原始板的设计师 Bechtolsheim 和 4.1BSD 的首席架构师 Joy，幸存下来。Boggs 和 Metcalfe 于 1976 年在 Palo Alto 的 Xerox 发明了以太网；他们的文章于当年 7 月发表在 CACM 上；Xerox 于 1980 年 10 月发布了规范。桌面机器和网络的理念在 Palo Alto 生机勃勃。

1982 年 6 月的《;login: 》杂志刊登了以下内容：

>**有趣的发展**
>
>**加州大学伯克利分校的 Bill Joy 加入 Sun Microsystems**
>
>Bill Joy 决定参与一家新创公司，并将在接下来的几个月内逐步退出伯克利的计算机系统研究小组（CSRG）。他将加入 Sun Microsystems, Inc.，这家公司的创始人之一是 Sun 工作站设计师 Andy Bechtolsheim。SMI 是少数几家计划提供基于微处理器的网络工作站、运行 4.2BSD 软件的公司之一……
>
>虽然 SMI 可能需要在某些专业领域开发专有软件，Bill 预计在 SMI 进行的针对 4.2BSD 共享基础程序的修正可以由伯克利分发。目前 CSRG 与各工业集团之间的合作被视为双方关系的典范……

这篇文章署名为“Prof. Bob Fabry”。

1982 年 7 月 6 日星期二，在波士顿举行的 USENIX 会议上，Joy 发表了关于 4.2BSD 和进程间通信的演讲。（Leffler 和 McKusick 则就 4.2 的其他方面进行了演讲。）第二天，Andy Bechtolsheim 介绍了“Sun 工作站”。

他对一千多名听众表示，这款工作站是…

>一台面向图形的个人计算机，运行 Unix 系统。它被设计为在分布式计算环境中用作通用工作站。用户界面包括一块 800x1024 像素的位图显示屏，配备“RasterOP”机制以实现高速显示更新，并可选配鼠标。处理器是运行在 Intel Multibus 上的 Motorola 68000。待 68010 处理器可用时，将进行升级。（68010 将支持完整的虚拟内存功能。）还可选配以太网本地网络。一组工作站可以联网，实现文件系统及外设（如打印机、磁带等）的共享。
>
>该工作站当前运行 UniSoft 的第 7 版 Unix，包含部分伯克利的增强功能。待 4.2BSD 可用时，将进行升级。这将允许联网的工作站无须本地磁盘即可运行……

在同一次会议上，麻省理工学院的 Jack Test 讨论了“NUnix 窗口系统”，BBN 的 Rich Fortier 和 Tony Lake 介绍了 BitGraph——BBN 的智能位图终端，贝尔实验室的 Rob Pike 讲述了“位图图形与 Unix 的融合”。1982 年 12 月，Hewlett-Packard 宣布推出其新一代 9000 系列 32 位工作站。随后宣布，HP 将在基于 Motorola 68000 芯片的 9826 和 9836 桌面机型上支持 Unix。该操作系统（称为 HP-UX）主要源自 System III，但包含许多扩展功能，包括以太网兼容性和伯克利 vi 屏幕编辑器。

1983 年 1 月，在 UNICOM（Software Tools、USENIX 和 /usr/group 联合会议）上，现任 Sun Microsystems 的 Tom Lyon 和 Bill Shannon 讲述了将 4.2BSD 移植到 Sun 上的工作。实际上移植的是 4.1c，但它是 BSD，并且运行在 68000 上。同一会议上，Eric Shienbrood（编写者之一）及其同事介绍了在 Apollo 计算机上运行 Unix 的情况——这是 AUX，System III 的一种模拟。那年晚些时候，IBM 宣布其 PC（基于 16 位 Intel 8088 芯片）上可以使用 Unix（移植工作由 Interactive 完成）。

但最重要的是高速工作站与 Unix 操作系统的诞生。这直接推动了网络的发展，没有运行 Unix 的工作站，网络就不可能以现有的形式出现。例如，Apollo 的 Domain 软件在许多方面优于互联网协议或 Sun 的 NFS 软件，但它并非开放的，所以最终失败了。Unix 不仅在大学校园中发挥作用，还广泛应用于科学和设计实验室以及商业机构。
