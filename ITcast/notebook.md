

使用的命令：
执行爬虫： 
scrapy crawl itcast
执行并输出文件： 输出json（默认Unicode)
scrapy crawl itcast -o exam.json
scrapy crawl itcast -o exam.csv
可以输出4中文件格式 csv  xml jsoni

常用报文头：
headers={
    "Accept":"text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8",
    "Accept-Encoding": "gzip, deflate, br",
    "Accept-Language": "zh-CN,zh;q=0.8,en-US;q=0.5,en;q=0.3",
    "Connection":"keep-alive",
    "Host":    "36kr.com/newsflashes",
    "Upgrade-Insecure-Requests":"1",
    "User-Agent":"Mozilla/5.0 (Macintosh; Intel Mac OS X 10.13; rv:55.0) Gecko/20100101 Firefox/55.0"
}

获取元素
试题：
//div[@class='shiti-content']/div[@class='shiti']/h3
选项：
//div[@class='shiti-content']/div[@class='shiti']/ul
//标准答案
//div[@class='shiti-content']/span




"Accept":"text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9",
    "Accept-Encoding": "gzip, deflate",
    "Accept-Language": "zh-CN,zh;q=0.9",
    "Cache-Control": "max-age=0",
    "Connection": "keep-alive",
    "Cookie": "PHPSESSID=g9uvnb72ok8rh0f5ifcak4pho0",
    "Host": "sysaqks.snnu.edu.cn",
    "Upgrade-Insecure-Requests": "1",
    "User-Agent" :"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/85.0.4183.83 Safari/537.36"
}


通识类（76
http://sysaqks.snnu.edu.cn/redir.php?catalog_id=6&cmd=learning&tikubh=1471&page=1
化学类  77
http://sysaqks.snnu.edu.cn/redir.php?catalog_id=6&cmd=learning&tikubh=1436&page=1
医学生物类安全题  40（
http://sysaqks.snnu.edu.cn/redir.php?catalog_id=6&cmd=learning&tikubh=1467&page=1
机械建筑类安全题 27
http://sysaqks.snnu.edu.cn/redir.php?catalog_id=6&cmd=learning&tikubh=1484&page=1
电气类安全题 19
http://sysaqks.snnu.edu.cn/redir.php?catalog_id=6&cmd=learning&tikubh=1485&page=1
辐射类安全题  12
http://sysaqks.snnu.edu.cn/redir.php?catalog_id=6&cmd=learning&tikubh=1486&page=1
特种设备安全题  10
http://sysaqks.snnu.edu.cn/redir.php?catalog_id=6&cmd=learning&tikubh=4199&page=1
消防安全题 31
http://sysaqks.snnu.edu.cn/redir.php?catalog_id=6&cmd=learning&tikubh=4200&page=1