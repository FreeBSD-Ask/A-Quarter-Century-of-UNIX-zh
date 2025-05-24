# PWB 和 MERT

回忆 Thompson 和 Ritchie 为 PDP-7 写的第一个系统，第一版是在 1971 年为 PDP-11/20 写的。第四版是贝尔实验室于 1973 年末在第三版的基础上用 C 语言重写的，当它使另一个项目获得成长：程序员的工作台 (PWB)。它的第一版帮助 Charlie Roberts 思考。Bob Morris 说 Rudd Canaday 从来没有得到他提供的贷款。对 Roberts 来说也是这样。MERT(多环境实时) 是 Roberts 的发明，虽然它的大部分是由 Heinz Lycklama 和 Doug Bayer 写的。Roberts 告诉我：

> 1970 年早期，我知道在 PDP-11 上有一个 Unix，它是用 B 语言实现的。但在我看来 Steve Johnson 已经在谈论 C 语言。在 1970 年 10 月我离开莫里山计算机中心回到科研。我作为客户已经意识到专利，并且我回顾思考 1127 将 Unix 视为分时系统来为文档做准备。计算机科学研究就像很多的学术部门：它有两部分。Sam Morgan 领导了包含有 Dennis，Ken，还有 Doug McIlroy 的计算机科学那部分。Hank McDonald 则是系统计算研究部门的总监。我在哪里为 Hank 工作，他想为 80 年代建立下一代的 ESS。

> 我们在 15 楼，正好在 Doug 和其他伙计们的下面。我有 Heinz Lycklama，Dick House 以及 Carl Christensen 为我工作，还有其他一些程序员。Carl 和 Heinz 那时工作于数字数据处理器 DDP516，那是一个小的计算机，它有自己的操作系统和硬件。但我曾经读了 Per Brinch Hansen 的一些文章。他后来把所有的内容都卸载了 *操作系统原理 1973 年* 这本书里，他让我思考像微内核，操作系统层还有其他很多直到 Mach 3 和 Chorus 以及 Windows NT 才真正成熟的东西。在我看来 Unix 作为一个分时系统有些太过于聚焦，我想使用一个专注的自定义系统工作——为交换和大数据库，实时和交易处理。

> 好了，71 年的时候 Hank 帮我搞到买大容量磁盘 11/45 机器的钱，接下来几个月我都在为我的系统工作，它的名字叫 OSKER——**OS KERnel**。在 10 月和圣诞节间的某个时间，我引诱 Heinz Lycklama 离开了 DDP。他和 Carl 看不到我想实现的概念。但 Hank 孤立 Heinz 来和我一起工作并且在 72 年晚期的时候我们得到足够的钱去雇佣一些人，Doug Bayer 在 73 年的时候加入我们，Heinz 真的将 OSKER 开发出来。在那个时候，我和部门的头 Doug McIlroy 又一次谈话，他建议联合起来合作。但是我看不到可能性并且担心这会让我的员工放弃 OSKER 去为 Unix 工作。那时 Heinz 建议我们“将 Unix 构建在 OSKER 上面”，然后那就成了 MERT。我们同时有了 Unix 和实时处理，这很了不起。但是 Heinz 对内核失去了兴趣，Doug 是一个新手。我感到巨大的压力，1973 年我决定搬到霍姆德尔将工作更多的放在通信和图像处理上。

> 当我离开的时候，Heinz 开始开发 Unix MERT: 那是系统实验室 74 年的工作内容，他们从来没有进行过内核方面的工作。MERT 在 Berk Tague 组建 USG 的时候搬到了哥伦布和印第安山。印第安山在 78 年创建了多路复用 MERT——DMERT，它不是一个可移植的微内核，非常依赖硬件。它运行在 3B20D 上，但它今天仍然运行在每个 4ESS 和 5ESS 上。
