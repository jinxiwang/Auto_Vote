# Auto_Vote
歌手打榜，自动投票，python实例讲解

最近学习了一下爬虫的基础知识，想找个投票网站练练手。刚好在朋友圈发现了一个音乐打榜网站，由于该网站不需要登录即可投票，这就给了脚本刷票可乘之机。<br>

在浏览该网站的民歌榜单时，无意间发现了一位得票数为0的兵哥哥，点进去后觉得《崛起的中国》这歌唱的相当好听，于是激起了我的爱国情怀，投票目标决定了：让他上榜。
![images](https://github.com/jinxiwang/Auto_Vote/blob/master/images/111.png)

首先记录手动投票过程，通过F12查看网页提交的请求头和数据，找到兵哥哥的作品id和提交post请求的网址。
![images](https://github.com/jinxiwang/Auto_Vote/blob/master/images/222.png)

实验过程还发现，每个IP每天最多投票5次，这就需要代理IP或其他方法构建。幸运的是，通过对post请求头中的X-Real-Ip和X-Forwarded-For参数赋值，即可构建出虚拟ip并能通过网站的重复ip检测。

程序运行情况和最后展示结果如下，兵哥哥成功登顶，这下爱国歌曲包揽民歌榜top2，赞赞赞。
![images](https://github.com/jinxiwang/Auto_Vote/blob/master/images/333.PNG)
![images](https://github.com/jinxiwang/Auto_Vote/blob/master/images/444.png)

[我的CSDN博客](https://blog.csdn.net/wangjinxile/article/details/105183383)

