# PWB 和 MERT

回忆一下，Thompson 和 Ritchie 写的第一个系统是为 PDP-7 设计的。第一版是在 PDP-11/20（1971 年）上开发的。第四版基本上是第三版用 C 语言重写的，它于 1973 年底从贝尔实验室发布，同时催生了另一个项目：程序员工作台（Programmer's Workbench，简称 PWB）。但第一版已经让 Charlie Roberts 开始思考。Bob Morris 说过，Rudd Canaday 从未得到应有的认可，Roberts 也是如此。MERT（多环境实时系统，Multi-Environment Real Time）是 Roberts 的创意，尽管它主要由 Heinz Lycklama 和 Doug Bayer 编写。Roberts 告诉我：

>到 1970 年初，我知道 PDP-11 上有一个用 B 语言实现的 Unix。但 Steve Johnson 似乎已经开始谈论 C 语言了。1970 年 10 月，我离开了 Murray Hill 计算中心，回到了研究部门。我知道专利部门（Patents）是客户，并记得当时想着 1127 组在推广 Unix 作为文档准备的分时系统。计算机科学研究就像许多学术部门一样，有两个部分。Sam Morgan 负责 Dennis、Ken 和 Doug McIlroy 所在的计算机科学部分；而 Hank McDonald 则是系统计算研究的主管，也就是电子工程部分。我开始为 Hank 工作，他希望为下一个十年（80 年代）构建下一代 ESS。
>
>我们在五楼，正好在 Doug 和其他人下面。我手下有 Heinz Lycklama、Dick House 和 Carl Christensen，还有一些程序员。Carl 和 Heinz 正在研究这台 DDP516——数字数据处理器，一台带有自己操作系统和硬件的小型计算机。但我一直在阅读 Per Brinch Hansen 的一些文章；他后来把这些内容整理成一本书《操作系统原理》（1973），让我开始思考微内核、分层操作系统这些概念，而这些直到 Mach 3、Chorus 和 Windows NT 时代才真正成熟。在我看来，Unix 过于专注于分时系统，而我想做一个专用的定制系统——用于交换机和大型数据库、实时处理和事务处理。
>
>嗯，Hank 帮我在 71 年拿到了买一台带大硬盘的 11/45 的资金，接下来的几个月我一直在开发我们称之为 OSKER（OS KERnel）的系统。在十月到圣诞节之间的某个时候，我把 Heinz Lycklama 从 DDP 上挖了过来。他和 Carl 实在看不到我想实现的概念步骤。但 Hank 鼓励 Heinz 和我一起工作，我们又拿到了资金，在 72 年底雇了人——Doug Bayer 于 73 年加入，Heinz 真正让 OSKER 启动起来。那时，我和我的系主任同事 Doug McIlroy 进行过一次谈话，他建议我们把项目结合起来。但我当时没看到其中的可能性，而且害怕这只是让我的团队放弃 OSKER，转去做 Unix 的借口。后来 Heinz 提议“把 Unix 放在 OSKER 之上”，这就是后来诞生的 MERT。我们既有 Unix 又有实时处理，真是太棒了。但 Heinz 对内核失去了兴趣，而 Doug 还是个新手。我感觉压力很大，于是 73 年决定搬到 Holmdel，更多地投入到通信和图像处理的工作中去。
>
>当我离开时，Heinz 开始开发 Unix MERT：到了 74 年，这成了系统实验室的主要工作——他们再也没继续推进内核的开发。MERT 在 Berk Tague 创建 USG 的时候，被部署到了 Columbus 和 Indian Hill。Indian Hill 在 78 年左右创建了 Duplex MERT-DMERT。它不是一个可移植的微内核，而是高度依赖硬件，运行在 3B20D 上。但它至今仍存在于每一个 4ESS 和 5ESS 系统中。

我稍后会回到 Roberts 的叙述；但首先让我继续讲述 Programmer’s Workbench（PWB）。PWB 由贝尔实验室一个与 1127 无关的小组开发。该项目于 1973 年中期由 Evan Ivie 发起，小组由 Rudd Canaday 领导，最初支持面向大型软件开发项目的 Unix 版本。虽然它起初是 Third Edition 的一个分支，实际上 PWB 是 Sixth Edition 的衍生版本。正如将要看到的，Sixth Edition（1976 年）有大量的后续版本。到 1977 年 6 月，当 T. C. Dolotta 和 R. C. Haight 撰写《PWB/UNIX 概述与功能摘要》时，PWB 支持“超过 1,000 名用户”。一年后，这个数字增长到了 1,100，几乎全部是 AT\&T 内部用户。

该系统运行在 DEC PDP-11/45 和 11/70 机器上。“一个典型的 PWB/UNIX 系统大约花费 120,000 美元，能够轻松支持 24 个同时用户。更大的系统可以支持两倍数量的用户。”
除了当时已成为标准的 Unix 功能外，PWB 还做出了两个真正的贡献：RJE（远程作业输入），它“提供了从 IBM 主机系统提交和检索作业的功能”，以及 SCCS（源码控制系统），这是“一套集成的命令，旨在帮助软件开发项目控制对源代码和文本文件（例如手册）更改的管理”。

这里值得指出的是，Ted Dolotta 曾任 PWB/Unix 组的主管直到 1978 年，之后成为支持组的主管，他负责了由 John Mashey 主要编写的 troff 的 -mm（备忘录）宏包。John Mashey 还编写了一个对 Bourne shell 有影响但长期与其竞争的 shell。Dick Haight 除了其他工作外，还编写了 find、cpio 和 expr。


