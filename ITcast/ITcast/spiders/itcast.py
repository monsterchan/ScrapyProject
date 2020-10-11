
# import sys
# import io
# import importlib
# importlib.reload(sys)
# sys.stdout = io.TextIOWrapper(sys.stdout.buffer,encoding='utf8')


import scrapy
from ITcast.items import ItcastItem

class ItcastSpider(scrapy.Spider):
    # 爬虫名称#
    name = 'itcast'
    # 检查域名进行筛选（可选参数）爬取范围
    allowed_domains = ['sysaqks.snnu.edu.cn']
    # 开始请求列表（可以为元组）
    # start_urls = ['http://sysaqks.snnu.edu.cn/redir.php?catalog_id=6&cmd=learning&tikubh=1471']
    exam_list = ['tongshi','huaxue','yixue','jixie','dianqi','fushe','tezhong','xiaofang']
    examLib = {'tongshi':[1471,76],'huaxue':[1436,77],'yixue':[1467,40],'jixie':[1484,27],'dianqi':[1485,19],'fushe':[1486,12],'tezhong':[4199,10],'xiaofang':[4200,31]}
    KuNumber = 0

# 实现翻页爬取
    baseURL = "http://sysaqks.snnu.edu.cn/redir.php?catalog_id=6&cmd=learning&"
    # offset = 1
    # start_urls = [baseURL+'tikubh='+str(examLib[exam_list[KuNumber]][0])+'&page='+str(offset)]

    start_urls = [baseURL+'tikubh='+str(examLib[exam_list[KuNumber]][0])+'&page=1']

# 解析响应参数
    def parse(self, response):
       item_list = []

       node_list = response.xpath("//div[@id='shiti-content']/div[@class='shiti']")
       # print("hello world!")
       # print(response.xpath("//div[@class='shiti-content']/div[@class='shiti']"))
       answer_list = response.xpath("//div[@class='shiti-content']/span/text()").extract()
       # print(len(node_list))
       # print(len(answer_list))
       for i in range(len(node_list)):
           item = ItcastItem()
           option = {}
           # .extract()将xpath对象转化为Unicode字符串
           name = node_list[i].xpath("./h3/text()").extract()[0]
           option_list = node_list[i].xpath("./ul/li/label/text()").extract()
           # print(type(option_list))
           for op in range(len(option_list)):
              option[op] = option_list[op]
           # print(type(option))
           answer = answer_list[i]
           # print(name)
           item["name"] = name
           # print(option)
           item["option"] = option
           # print(answer)
           item["answer"] = answer
           # return item
           # item_list.append(item)
       # 获取url传给调度器
       # return scrapy.Request(url)
       #将获取数据交给 pipelines        避免把所有数据item放入item_list占用大量内存的情况
           #返回数据给管道，处理完毕后再回来取数据
           yield item
        # 返回值就传给引擎
       # return item_list
       #单库爬寻
       # if self.offset < 76:
       #      self.offset += 1
       #      url = self.baseURL+str(self.offset)
       #      print(url)
       #      yield scrapy.Request(url,callback = self.parse)

       #拼接方式：多库爬寻
       #当第一个库爬寻完毕，爬寻下一个库
       # print(self.examLib[self.exam_list[self.KuNumber]][1])
       # print(len(self.exam_list))
       # print(self.KuNumber)
       # if (self.offset < self.examLib[self.exam_list[self.KuNumber]][1] and self.KuNumber < len(self.exam_list)):
       #     self.offset +=1
       #     url = self.baseURL+'tikubh='+str(self.examLib[self.exam_list[self.KuNumber]][0])+'&page='+str(self.offset)
       #     print(url)
       #     yield scrapy.Request(url,callback = self.parse)
       # elif self.KuNumber < len(self.exam_list):
       #     self.offset = 1
       #     self.KuNumber += 1
       #     url = self.baseURL+'tikubh='+str(self.examLib[self.exam_list[self.KuNumber]][0])+'&page='+str(self.offset)
       #     print(url)
       #     yield scrapy.Request(url,callback = self.parse)

       #方式二：筛选url
       # print(type(str(response.xpath("//div[@class='fy']/a/text()").extract()[0].encode("utf-8"))))
       #
       # print("000"+response.xpath("//div[@class='fy']/a/text()").extract()[0])
       #
       # print("111"+response.xpath("//div[@class='fy']/a/text()").extract()[1])
       # print("222"+response.xpath("//div[@class='fy']/a/text()").extract()[2])
       # print(str(response.xpath("//div[@class='fy']/a/text()").extract()[1].encode("utf-8")).find('下一页'))
       #
       # print(response.xpath("//div[@class='fy']/a/text()").extract()[1])
       # print("下一页" in response.xpath("//div[@class='fy']/a/text()").extract()[1])
       # print(response.xpath("//div[@class='fy']/a/text()").extract()[2])
       # print("下一页" in response.xpath("//div[@class='fy']/a/text()").extract()[2])
       # print(" 下一页".find("下一页"))
       # print("下一页".find("下一页"))
       if "下一页" in response.xpath("//div[@class='fy']/a/text()").extract()[1] and self.KuNumber < len(self.exam_list):
           url = response.xpath("//div[@class='fy']/a/@href").extract()[1]
           # print("1---------"+url)
           nextUrl = "http://sysaqks.snnu.edu.cn/"+url
           yield scrapy.Request(nextUrl,callback=self.parse)
       elif "下一页" in response.xpath("//div[@class='fy']/a/text()").extract()[2] and self.KuNumber < len(self.exam_list):
           url = response.xpath("//div[@class='fy']/a/@href").extract()[2]
           # print("2---------"+url)
           nextUrl = "http://sysaqks.snnu.edu.cn/" + url
           yield scrapy.Request(nextUrl, callback=self.parse)
       elif self.KuNumber<len(self.exam_list):
           self.KuNumber += 1
           nextUrl = self.baseURL+'tikubh='+str(self.examLib[self.exam_list[self.KuNumber]][0])+'&page=1'
           yield scrapy.Request(nextUrl,callback=self.parse)
