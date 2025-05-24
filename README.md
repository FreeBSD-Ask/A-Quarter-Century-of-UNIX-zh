# 翻译项目

本项目《Unix 四分之一世纪》由 FreeBSD 中文社区独立翻译。

---

```c
/* 你不需要看懂这段代码 */
if (rp -> p_flag & SSWAP) {
    rp -> p_flag &= ~SSWAP;
    aretu (u.u_ssav);
}
```

这是第六版 UNIX（Western Electric，第六版）中第 2238 行的注释，以及位于第 2240 至 2243 行的代码。

---

## 更多资源

* 本书由 Addison-Wesley 出版社出版于 1994 年
* 在线阅读：<https://freebsd.gitbook.io/unix-er-shi-wu-nian>
* 翻译源码：<https://github.com/FreeBSD-Ask/A-Quarter-Century-of-UNIX-zh>
* 英文原版：<http://wiki.tuhs.org/lib/exe/fetch.php?media=publications:qcu.pdf>
* Unix 源码：<http://minnie.tuhs.org/cgi-bin/utree.pl>
