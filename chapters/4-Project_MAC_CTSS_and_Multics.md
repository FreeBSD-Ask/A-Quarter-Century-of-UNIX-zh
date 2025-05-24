# MAC项目：CTSS和Multics

MAC 项目是 1963 年春天由 J.C.R. Licklider 建议在 MIT 发起的。他的创始主任是 MIT 的教授 Robert M. Fano。根据 1965 年 Fano 为 MAC 项目进度报告写的前言，MAC 代表机器辅助认知 (Machine Aided Cognition) 和多路访问计算机 (Multiple Access Computer)。事实上，它之所以有名是因为 MIT 计算机科学所在的科技广场五楼。Marvin Minsky 的人工智能实验室位于被称之为人与计算机 (Man and Computer) 的九楼 (最初实验室是属于 Minsky 和 MacCarthy 的，但当 LISP 的发明人 John MacCarthy 去了斯坦福后，他爱的名字被取消了)。

1963 年 MAC 项目主办了一个暑期课程。许多知名的的计算机科学家被带到剑桥，他们使用 IBM 的使用 CTSS(the Compatible Timeshare System，兼容分时系统) 并讨论计算的未来。MAC 项目这时主要的成就是 Fernando J. Corbato 的 CTSS，Victor H. Yngve 的 COMIT，还有 Minsky 的人工智能实验室。

在 50 年代和 60 年代早期是批处理的时代。但这既浪费时间又浪费资源。桌椅浪费是因为机房里无所不在的签名表。除非你很幸运，刚排队没多久就就让你运行一个像 debug 这样预约时间为一小时小任务。你的程序运行了 40 分钟，或者不幸的，你的程序一小时后还没有完成：它将被直接丢弃 (已经完成的部分很可能就完全丢掉了)。然后你又要将来的一个半小时 (通常在下午的 1 点，2 点或者 3 点)。解决这个问题的答案是分时。

兼容分时系统 (CTSS) 是第一个分时系统，它是由 Corbato 带领团队在 MIT 计算中心开发的。CTSS 运行经过修改的的 IBM 7094，它通过添加两块 IBM 720A 增加了 32K 字节存储。另一台 7904 在 1965 年早期加入进来。通过一台连接到拨号调制解调器的 IBM 7750 会话控制器，它最高可以让 30 哥用户通过电话线远程访问 (事实上没有人可以拥有一个小时的 CPU 时间，因为那已经超出了系统失败的时间上限)。

CTSS 作为 MAC 项目的分时部分，既是一台服务设备，又是系统编程员的实验室。这是这个附加功能 (当时 7094 还在调整) 导致了 Multics 的诞生 (Multiplexed Information and Computing Service，多路复用信息和计算服务)。

Multics 是第二代分时系统，目的是成为一个“计算机公用程序”的原型。它在 1964 年作为 MAC 项目，贝尔实验室，以及通用电气的合作项目开始进行。Corbato 是开发计划的主要领导人，项目有九个主要目标：

> * 方便的使用远程终端
>
* 像电话系统一样的连续运行
* 广泛的系统配置
* 可靠的内部文件系统
* 支持选择性的信息分享
* 层次结构的信息分类
* 支持大量的应用程序
* 支持多个环境和接口
* 系统进化的能力

Berkley Tague 在 1962 年加入贝尔实验室，又于 1965 年作为项目三人组的秘书加入 Multics 项目组。他说在 1967 年就可以很明显的看出项目不会成功，因为“三个成员有着互相冲突的目的”。他去新泽西惠帕尼的 AT&T 工作了三年，在那里他工作于一个防护项目。1970 年又重新回到纽约默里山。

MIT 的 Jack Dennis 教授在 Multics 早期贡献了几个很有影响的架构建议。当需要寻找一个计算机厂商支持新的操作系统时，人们说 IBM 将要生产叫做 360/65 的机器。Doug McIlroy 告诉我：

> 这是真的，但是 Amdahl 不会制造虚拟机。最后时刻 IBM 让 Gerry Blaauw 主导 360/67，但是为时已晚。

IBM 的员工对 MAC 项目组关于分页的主意不感兴趣。那时还是 MIT 讲师的 Joseph Weizenbaum 向在通用电气的前同事们介绍了 MAC 项目组，前同事们对于分段分页机制非常热心，在他们的提议下产生了 GE-645(635 的升级版本)。就这样通用电气成为 Multics 项目的一部分。

MIT，贝尔实验室和通用电气一致同意合作。分别来自三个公司的三个人人组成了三人决策组，他们是 MIT 的 Fano，贝尔实验室的 E.E.David，和通用电气的 C.W.Dix。还有三个人负责具体的实际管理，分别是 MIT 的 Corbato，通用电气的 A.L.Dean，贝尔实验室的 Peter G.Neumann。值得注意的特性包括分段内存，虚拟内存，高级语言 (PL/I)，多处理器共享内存，多语言支持，还有在线配置。

1964 年 PL/I 被选为编程语言。其他候选的还有 MAD(the Michigan Algorithm Display) 和 AED-0(an MIT display)。实现完整的 PL/I 比预料的还要困难。贝尔实验室和两个外部人员签订了奖励协议。但是一年过去了，两人没有拿出一个 PL/I 编译器。Bob Morris 和 Doug McIlroy 制定了一个备用计划，在 7094 上使用 McClure 的 TMG 语言，这个语言也被称为 EPL(早期 PL/I)。McIlroy 回忆道：

> 1965 年 5 月 3 号，我们突然发现协议无法按时完成，马上就就开始自己建造它。我们在年前一段时间就有顾客。Morris 的 66 到 67 年的学术休假被完整的使用了。我们雇佣的签约人员没有做出任何有价值的东西。所以 EPL 一直被推迟到 1970 年通用电气一个精湛的团队做出真正的编译器。

> Morris 编写了 TMG 的前端，它输出单路 ASCII 代码。每个地址都注释着“基址，偏移，模式，精度”这些让人不知所云的东西。我用 TMG 语言做了代码生成器，它输出汇编语言。Dolores Leagus 加入进来做数据结构编译。我们排除了占据 PL/I 一半语法的输入输出部分，单精度，属性声明，跨段序列，但实现了一个显著的子集，包括 IBM 早期版本性感的“引用”属性 (“引用”使得序列的大小信息可以保留在数据结构的元素中)。

> Jim Gimpel 加入进来负责数据封装。Multics 有着种类繁多的数据结构，我们将一些三路代码加入的中间语言以消除很少使用的临时变量。编译器缺少某些功能，它只能输出“语法错误”和“多重声明”这两种错误提示，当数据越界时提示“非法数据结构”的警告。

> McClur 将 TMG 的汇编代码从 CDC 1600 翻译为 7090 的编码格式，我在千里之外帮他调试。Clem Pease 随后又通过将 IBM 指令定义为 635 宏将将它移植到 GE 635。

编译器将编译结果送入 EPLBSA(EPL 引导汇编器)。编译过程非常缓慢。

等待 PL/I 编译器最终可用的时候，团队编写了 Multics 系统编程人员手册。它一共有 3000 页，每一节都经过几轮修订，还有几节重写或者大改了几次。

Tom Van Vleck 说：

> 在 68 年到 69 年系统已经延期并且资金紧张有被取消的风险。或许这恰好鼓舞了团队精神 (相比于表面的士气)。1968 年 ARPA(the Advanced  Research Proect Agency of the Department of Defense) 的一次审查是我们最接近被取消的时候，不过他们建议我们继续下去。但为时已晚，贝尔实验室在 1969 年四月正式退出。

直到 1993 年仍有 Multics 机器在运行，它们是稀有物种。Van Vleck 像我提供了下面的清单，标记型号的是未能确认的站点：

> * ACTC (加拿大 亚伯达 卡尔加里)
>
* Air Force Data Service (华盛顿哥伦比亚特区) *
* Bull System-M (亚利桑那州凤凰城)
* Credit Lyonnais (发过巴黎)
* Department of National Defence (加拿大 新斯科舍省 哈里法克斯)
* Ford Motor Company (密歇根州 迪尔伯恩)
* General Motors(密歇根州 沃伦)
* Ministerie van Sociale Zaken en Werkgelegenheid (荷兰 海牙) *
* National Security Agency (马里兰州 林西克姆)
* Societe Europeenne de Propulsion (法国 弗农)

Multics 的重要性在于它持久的影响力。霍尼韦尔公司 (Honeywell) 买下了通用电气的计算机业务，但是它的 GCOS 6 操作系统，Prime 的 Primos，Stratus 的 VOS，还有 Apollo 的 Domain，以及 BBN 创建的 TENEX，TOP-20，都深刻的被 Multics 影响着 (Prime 的创建者 Bill Poduska 曾在通用电气为 Multicsul 工作，然后去了 DEC，Multics 曾经的多语言经理 Bob Freiburghouse 是 Stratus 公司的创始人)。英特尔 386，486 系列的内存管理看起来是来自 Multics 的手册。但最重要影响恐怕是来自贝尔实验室的 Dennis Ritchie 和 Ken Thompson，以及他们的同事 Mcllroy，Morris，Neumann，以及接触了 CTSS 和 Multics 的 Ossanna。Ritchie 告诉我：

> 我们从 Multics 学到了很多重要的事情：
>
> * 树形的文件系统结构
> * 一个命令解释程序，甚至这个程序的名字“shell”也是取自 Multics
> * 更重要的是，文件的结构就是没有结构，之看做字节数组。大多数情况下操作系统对此不作解释
> * 文本文件只是有换行字符分隔的字符序列
> * 读写操作的语义都是针对一个文件句柄，一个缓冲区，一个计数。对上隐藏了底层的磁盘簇块


---
**译者注**

[Multics System Programmers' Manual](http://multicians.org/mspmtoc.html)
