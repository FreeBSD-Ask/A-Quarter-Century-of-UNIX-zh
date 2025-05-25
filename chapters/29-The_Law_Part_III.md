# 法律 第三幕

从大约 1986 年起，Keith Bostic 会在半年一度的 USENIX 会议上站起来宣布他——CSRG 项目的进展：大约 35% 的程序不含 AT\&T 代码；大约 55%……；大约 77%…… 不管进展到什么程度——总是有所进步——都会引来欢呼和热烈的掌声。AT\&T 的律师在 1970 年代中期一开始就走错了路。但这并不是欢呼的所有原因。创建一个无许可证 Unix 的主要动机在于 AT\&T 的收费。当 UCSF 获得第 7 版时，许可证费用约为 7,000 美元。“商业”许可证费用则要高得多。Clem Cole 回忆道：

>鉴于当时 Mellon Institute 使用 Unix 是为了商业利益，Dan \[Klein] 和我最终选择了“罢工”，直到 CMU 购买了真正的“工业级”Unix 许可证。CMU 成为第一家购买了 2 万美元许可证的大学。几年后，像 Case Western Reserve 这样的几所学校也效仿了这一政策。

1978 年，那时 Mellon Institute 使用 Unix 是为了商业利益，Dan \[Klein] 和我最终选择了“罢工”，直到 CMU 购买了真正的“工业级”Unix 许可证。CMU 成为第一个购买了 2 万美元许可证的大学。几年后，像 Case Western Reserve 这样的几所学校也效仿了这一政策。

John Gilmore 和其他几位推动 CSRG 生产他们的无许可证版本。AT\&T 并未反对其他 Unix 衍生版本，如 Linux、MINIX 等。

1988 年秋，在 BSD 研讨会上，Keith、Mike Karels 和 Kirk McKusick 宣布完成 BSD Networking Release 1（NET 1），该版本于同年 11 月发布。NET 1 是当时 Berkeley 系统的一个子集，类似于 4.3-Tahoe，包含内核的网络部分、C 库和实用程序的源代码及文档。该版本没有附带任何先前的许可证（无论是 AT\&T 还是 Berkeley），并通过匿名 FTP 重新分发，源文件中包含 Berkeley 的版权声明和允许署名分发的许可说明。

两年半后，1991 年 6 月，在纳什维尔举行的 USENIX 大会上，发布了 BSD Networking Release 2（NET 2）。NET 2 除了包含更多代码外，也同样没有先前许可证。新功能包括基于卡内基梅隆大学 Mach 系统的新虚拟内存系统（由犹他大学移植）和对 Intel 386/486 系统的支持。

NET 2 是一次美俄合作成果，贡献者包括 Bill Jolitz、Donn Seeley、Trent Hein、Vadim Antonov、Mike Karels、Igor Belchinskiy、Pace Willisson、Jeff Polk 和 Tony Sanders。该版本被商业化，形成了 BSDI（Berkeley Software Design, Inc.）。BSDI 于 1991 年底完成，并于 1993 年 4 月 10 日发布，但由于 UNIX Systems Laboratories（USL）提起诉讼阻止 BSDI 发货，发布被延迟。USL 申请禁止分发 BSD/386，理由是 BSD/386 侵犯了其 32V 软件版权并盗用了商业秘密。

1993 年 3 月 3 日，法院拒绝了 USL 的初步禁令请求，裁定 USL 未能证明其版权或商业秘密主张有成功的可能。3 月 30 日，新泽西州联邦地区法院法官 Dickinson Debevoise 重申了对 USL 禁令请求的拒绝，认定 32V 源代码是在没有版权声明的情况下发布的，并且 USL 没有显示能成功维护版权的可能性。法院还认定 BSD/386 并未包含 USL 的商业秘密。

USL 后来提出复议请求，要求重新听审 32V 是否缺乏版权声明的问题，但法院仍予以拒绝，认为分发数量的事实修正并不影响无版权声明发布的裁定。

这距离 Ken 在 SOSP 上发表那篇论文不到 20 年，距离 UNIX NEWS 变成 ;login:，以及 UNIX 用户组变成 USENIX 也有 15 年。然而，AT\&T、西部电气公司（Western Electric）以及现在的 USL，对用户社区几乎一无所知。

BSDI 和其他开发者试图确保 Unix 操作系统的持续发展、成长和使用。USL 的诉讼是为了保护一件已经被发现极具价值的事物，但为时已晚。可能 Ritchie 和 Thompson 在 70 年代中期对系统管理不够谨慎，也可能 BTL 员工曾无意中将 Unix 公开，未加严格限制。

BSDI 已发布了 BSD/386 的测试版本，并开始进行国际分发。完整版源代码价格约为 1000 美元。（1994 年 1-2 月的 ;login: 杂志中 Lou Katz 写道：“它可以用了！它可以用了！”）

由于加州大学获得许可的方式，加州大学理事会也被包括在了 USL 的诉讼中。1993 年 6 月，理事会进行了反击，起诉 USL 未遵守与 CSRG 之间的协议。与此同时，Novell 已经收购了 USL。

当时，无法预见这场通过诉讼进行的市场争斗的最终结果。但遗憾的是，很明显微软等公司利用了 Unix 之争以及各 Unix 厂商制造的各种市场障碍。

到本文印刷时，Novell 为了抵御 Windows NT 的猛烈攻势，可能已经决定终止继承的这场诉讼。

【临时补充：1994 年 2 月 4 日星期五，Novell 与加州大学达成协议，放弃所有相关诉讼和反诉。BSDI 立即宣布发布“4.4BSD-Lite”。BSDI 总裁 Rob Kolstad 对我说：“我们很高兴与 USL 达成和解，这样我们就可以全力投入产品开发和服务客户。”】
