# 《Unix 四分之一世纪》翻译项目

本项目《Unix 四分之一世纪》由 FreeBSD 中文社区独立翻译。

---

1972 年 6 月 12 日，Ken Thompson 和 Dennis Ritchie 写道：“UNIX 的安装数量已增长到 10，预计还会更多。”两年后，这个数字变成了 50。据估计，如今已有超过 300 万套 UNIX 系统在运行……

《UNIX 四分之一世纪》

Peter H. Salus 著

UNIX 是一款简单、优雅、可移植、功能强大的软件系统。它的流行是在没有庞大市场营销组织支持的情况下自然增长起来的。程序员持续使用它；大公司则不断抗拒它。十年后，用户的胜利已经非常明显。《UNIX 四分之一世纪》是第一本解释这种惊人成就的著作，借助它的创造者、开发者和用户的原话来展示：一个技术群体的社会结构如何足以压倒数十亿美元企业的意图。

在撰写本书过程中，Peter Salus 采访了 100 多位 UNIX 社群的重要人物，并收集了从澳大利亚到奥地利的大量相关资料。这就是那本将 UNIX 民间传说转化为 UNIX 历史的书。

---

**内容特色**

* 提供 UNIX 操作系统发展历程的首部文献性记录
* 采访 100 余位 UNIX 社群的关键人物
* 收录经典照片和插图
* 阐释 UNIX 成功的原因

---

**关于作者**

Peter H. Salus 是一位在国际上享有盛誉的 UNIX 爱好者。他是季刊《Computing Systems》的主编，定期为计算机出版物撰稿，并在 USENIX 通讯《;login: 》中主持“The Bookworm”栏目。他著有多部书籍、文章和评论。

Salus 拥有化学本科学位、日耳曼语言学硕士学位，以及纽约大学语言学博士学位。


---

```c
/* 你不需要看懂这段代码 */
if (rp -> p_flag & SSWAP) {
    rp -> p_flag &= ~SSWAP;
    aretu (u.u_ssav);
}
```

这是第六版 UNIX（西部电气，第六版）中第 2238 行的注释，以及位于第 2240 至 2243 行的代码。

---

## 更多资源

* 本书由 Addison-Wesley 出版社于 1994 年出版
* 在线阅读：<https://freebsd.gitbook.io/unix-er-shi-wu-nian>
* 翻译源码：<https://github.com/FreeBSD-Ask/A-Quarter-Century-of-UNIX-zh>
* 英文原版：<http://wiki.tuhs.org/lib/exe/fetch.php?media=publications:qcu.pdf>
* Unix 源码：<http://minnie.tuhs.org/cgi-bin/utree.pl>
