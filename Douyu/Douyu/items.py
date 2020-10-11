# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy


class DouyuItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()

    #主播名
    nickname = scrapy.Field()
    #房间号
    room_id = scrapy.Field()

    vertical_src = scrapy.Field()
    #房间截图图片
    room_src = scrapy.Field()

    #城市
    city = scrapy.Field()

