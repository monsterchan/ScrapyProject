import scrapy
import json
from Douyu.items import DouyuItem
class DouyuSpider(scrapy.Spider):
    name = 'douyu'
    allowed_domains = ['douyucdn.cn']
    base_urls = "http://api.douyucdn.cn/api/v1/getVerticalRoom?limit=20&offset="
    offsetUp = 0
    UpOver = False
    offsetDo = -1
    start_urls = [base_urls+str(offsetUp)]

    def parse(self, response):
        data_list = json.loads(response.body)["data"]
        print("len(data_list)"+str(len(data_list)))
        if len(data_list)==0 and self.UpOver == False:
            return
        elif len(data_list)==0 and self.UpOver == True:
            self.UpOver = False

        for data in data_list:
             item = DouyuItem()
             item["nickname"] = data["nickname"]
             item["room_id"] = data["room_id"]
             item["room_src"] = data["room_src"]
             item["vertical_src"] = data["vertical_src"]
             item["city"] = data["anchor_city"]
             print(item)
             yield item
        # print("*"*40)


        if not self.UpOver:
            self.offsetUp += 1
            yield scrapy.Request(self.base_urls+str(self.offsetUp),callback=self.parse)
        else:
            self.offsetDo -= 1
            yield scrapy.Request(self.base_urls+str(self.offsetDo),callback=self.parse)
