# 新闻爬虫抓取

丰富平台内容，甚至做一个资讯聚合平台，甚至是满足自己的阅读需要，抓取各大网站的资讯成为必须。        
一直想搞一个这样的平台，但是没有时间精力搞，现在来试试看。  

项目二开自 [基于scrapy的新闻爬虫](https://github.com/yinzishao/NewsScrapy)      



# 百度贴吧爬取说明
贴吧网页版好像直接把帖子的html数据给注释掉了，

需要代理服务器才行，网上抓取的免费代理没啥卵用。    


# IP扫描抓取
分享一个实用的扫描代理ip的方式 https://liaobu.de/share-a-practical-way-to-scan-proxy-ip 
基于扫描建立的ip池 https://github.com/bjjdkp/Proxies-Pool       
zmap https://github.com/zmap/zmap 

使用 `python-masscan` 这个库       


A类：(1.0.0.0-126.0.0.0)
B类：(128.0.0.0-191.255.0.0)
C类：(192.0.0.0-223.255.255.0)


私有地址
A类地址：10.0.0.0～10.255.255.255 
B类地址：172.16.0.0～172.31.255.255 
C类地址：192.168.0.0～192.168.255.255



sudo masscan -p80,3306,22,8080,3389,443,1080,9098,8081,3128,21,69,25 223.0.0.0/8 -oG test2.txt --rate=1000000 -v 


80
83 
3129	
3128	
6969
8060	
8080 
8090
8118
8888 
9000
9091
52024
60808	