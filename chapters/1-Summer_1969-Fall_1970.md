# 1969 年夏到 1970 年秋

1987 年，时任多伦多人类计算资源公司的 Mike Tilson 制作了一块纪念牌，牌上刻着 Ken Thompson 和 Dennis Ritchie 两位留着胡子的面孔。这块牌子上写着“我们的创始人”。从广义上讲，这说法没错，但更准确地说，Thompson 是发起人，Ritchie 和 Rudd Canaday 紧随其后，还有一小群贝尔电话实验室的员工组成了团队。他们是个团结而友好的团队。虽然开头的故事是虚构的，但并没有大幅偏离事实。

当我问 Dennis Ritchie 为什么 Ken 要开发《太空旅行》时，他回答：“仅仅是为了好玩。”（实际上，《太空旅行》是一款严肃的天文模拟程序，而不仅是游戏）

在某种程度上，这也是贝尔电话实验室当时普遍的态度。用 Ritchie 的话说，实验室的基本理念是：

>实验室过去和现在的做法都是雇佣那些能自己产生好点子并付诸实践的人……Ken 正在做一些有趣的事情，最终会证明这非常有价值……当一所优秀的大学聘请年轻教授时，他们期望教授们做什么呢？当然，有一定量的琐碎事务和各种服务工作，但真正期待的是他们有好的想法，能够产生一定的影响。学术界和这里的琐事细节和氛围虽有不同，但最终的期望惊人地相似。人们被给予了极大的自由去开辟自己的道路。当然，并不是所有人都能找到这条路，尽管我们在挑选人才方面很幸运。

Ken Thompson 在贝尔公司于 1969 年 3 月退出 Multics 项目时，正在为 Multics 机器 GE645 工作。他继续从事这项工作，“仅仅是为了好玩”。然而，享受乐趣意味着尝试让它运行，这也意味着必须面对硬件和软件的局限性。通用电气机器价格昂贵，而 Multics 还没有准备好作为任何实际生产环境来使用。

Doug Mcllroy 说：“当 Multics 开始运行时，第一个真正运行的地方就是这里……贝尔电话实验室实际上将 645 机器当作 Multics 机器使用。三个人就能使它过载。”

Thompson 在伯克利时接触过 Butler Lampson 编写的 SDS930 操作系统。但在 Multics 失败之后，新泽西的操作系统研究并不受欢迎。

Sandy Fraser 于 1969 年 5 月加入贝尔。他离开 Ferranti 就是因为想参与 Multics 项目，但一到贝尔就得知贝尔电话实验室已经中止了该项目。一天，贝尔研究副总裁 Bill Baker 和 Multics 项目的联络人 Ed David 来到贝尔电话实验室 Murray Hill 五楼，David 读出了一封信，通知员工贝尔将退出该项目。Fraser 回忆说这是一次“痛苦的变革”，人们都很沮丧。“玩具没了……明显缺乏动力，”他说。

在 4 月、5 月和 6 月期间，Thompson 对编写文件系统产生了兴趣。正如他对 Mike Mahoney 所说：

>“从未设计过具体到把地址放哪里，文件如何扩展之类的细节；从未达到那个层面。我想也就开过一两次会。Dennis、\[Rudd] Canaday 和我讨论了这些总体思路，比如如何让文件互不干扰，扩展的细节，真正的实现：块地址放哪里，放在哪儿……我们是在 Canaday 的办公室讨论的，讨论结束时，Canaday 拿起电话；贝尔实验室新开了一个录音服务。你打电话，基本上就是给一台录音机留下笔记，第二天早上会把笔记打出来然后寄给你。第二天这些笔记寄回来了，所有缩写词都被写错了，比如 `inode` 变成了 `eyen...`。于是我们拿到了这些说明，复印的笔记我们每个人都有一份，成为文件系统的工作文档——该文件系统就是在 PDP-7（Digital Equipment Corporation，数字设备公司的一款计算机）上花一两天时间构建出来的。
>
>起初……我们还用它做了别的事，比如著名的《太空旅行》游戏，而它自然成了放置文件系统的理想地方。当我们在 Canaday 的办公室用录音机草拟出这个文件系统的粗略设计后，我就去 PDP-7 上实现了它。”

Bob Morris 于 1960 年加入贝尔实验室，他表示自己认为 Canaday 对 UNIX 的贡献是“最被低估的”原始参与者之一；他说，一开始是“Ken、Dennis 和 Rudd”， “其他人都是一两三年后才加入的……我当时在那里，但并未参与其中。”Steve Bourne 在 1970 年代曾在贝尔实验室工作，他则更正式地表达了这一观点：

>一台废弃的 PDP-7 配备了一台 340 显示器，但 PDP-7 只提供汇编器和加载器。一次只能有一位用户使用这台计算机，每位用户对机器拥有独占使用权。这种环境很粗糙，很快便开发出单用户 UNIX 系统的部分功能。太空旅行程序被改写用于 PDP-7，同时编写了一款汇编器和一款初步的操作系统内核，并在 GECOS（通用电气综合操作系统）上为 PDP-7 交叉汇编……
>
>交叉汇编意味着使用两个计算机系统，每次修改都需要携带纸带在两者之间转换……该系统支持两个人同时工作，UNICS 这一名称显然是由 Peter Neumann，一位惯用双关语的幽默大师，在 1970 年创造的。\[UNiplexed Information and Computing Service，非复用信息和计算机服务，是对“阉割版 Multics”的一个双关；有几个人告诉我 Brian Kernighan 改变了拼写，但 Kernighan 表示没人记得是谁最初把名字改成 UNIX 的。]

PDP-7 属于 Joe Condon 的团队。Condon 回忆说，这台机器是“为了 Bill Ninke 想做的某个图形项目而买的”，“但 Ninke 后来去了 Holmdel（贝尔电话实验室的另一个分部）”，所以当 Thompson 和 Ritchie 想用它时，这台机器并没有被使用。

>Ken Thompson 回忆说：
>
>那是 1969 年夏天。实际上，我妻子去加州我家探望父母；我们刚有了个儿子，他出生于 1968 年 8 月，我的父母还没见过孩子，所以 Bonnie 带着孩子去看望我家人，她在加州呆了一个月。我给操作系统、shell、编辑器和汇编器各分配了一周时间，让它们彼此重写自己。在她离开的那个月，这些程序完全以一种看起来像操作系统的形式重写了，带有一些大家熟悉的工具，比如汇编器、编辑器和 shell——如果说它还没完全能自我维护的话，也已经差不多了，完全切断了与 GECOS 的联系……基本上是一个人工作了一个月。
>
>这确实是一个“人月”（一个人全职工作一个月的工作量）。
>
>Thompson 继续说：
>
>它自己存在的时间并不长。我们做的是——为了运行文件系统，你必须能够创建文件、删除文件、读取和写入文件，并观察它的性能。为此，你需要一个脚本来模拟文件系统上的各种操作，我们用的是写有“读取文件”、“创建文件”、“写入文件”等命令的纸带。你会把脚本从纸带上运行，它会让磁盘嗡嗡作响，但你根本不知道发生了什么。你看不见，也无法干预，完全没法观察。所以我们在文件系统上构建了几个工具，用纸带加载这些工具，然后从文件系统里运行这些工具——这就是所谓的 `exec`（执行）——你向这些工具输入命令，这就是所谓的 shell，通过它驱动文件系统进行我们想要测量的各种操作，观察它的工作表现和反应。文件系统自己单独存在的时间可能只有一两天，之后我们开始开发需要加载的工具。
>
>虽然 Multics 中有一些东西影响了 UNIX，但正如 Ritchie 所说，也存在“深刻的差异”：
>
>“我们有些被大系统思维压制了。Ken 想做一些简单的东西。或许和其他任何因素一样重要的是，我们的资源要小得多——我们只能得到没有任何复杂 Multics 硬件的小型机器。
>
>所以 UNIX 并不完全是对 Multics 的反动，更多的是这些因素的结合。Multics 已经不再属于我们，但我们喜欢它带来的交互式计算体验；Ken 有一些关于如何构建系统的想法需要解决；而可用的硬件和我们的兴趣都倾向于打造精巧的小东西，而不是宏大的系统。Multics 对 UNIX 的方法有影响，但并没有主导它，既不是反 Multics 系统，也不是廉价复制品。”

Thompson“捞到了这台 PDP-7，并且（大部分时间）用它做了这些酷炫的东西，”Ritchie 说。但 Ritchie 有些过于谦虚。Thompson 和他创造了一个新玩具。他们在 1969 年夏末初秋开始的工作，为贝尔电话实验室计算机研究指明了方向，持续了十年，并为之后的十年提供了实验平台。这个玩具启发了全球范围内新系统的开发。不过，一开始他们只有 PDP-7 可用：“硬件是借来的，而且已经非常落伍，”Ritchie 告诉我。

