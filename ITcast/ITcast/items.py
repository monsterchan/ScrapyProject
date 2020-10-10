# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy

# ItcastItem 继承了 scrapy.Item
class ItcastItem(scrapy.Item):
    # define the fields for your item here like:
    # 创建一个item字段
    # name = scrapy.Field()

    #试题题目
    name = scrapy.Field()
    #试题选项
    option = scrapy.Field()
    # 试题答案
    answer = scrapy.Field()
    pass
