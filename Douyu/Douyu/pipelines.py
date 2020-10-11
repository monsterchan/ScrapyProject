# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html


# useful for handling different item types with a single interface
from itemadapter import ItemAdapter
import scrapy
import os
from Douyu.settings import IMAGES_STORE as images_store
from scrapy.pipelines.images import ImagesPipeline

class DouyuPipeline(ImagesPipeline):

    def get_media_requests(self,item,info):
        images = item["room_src"]
        # vertical_src_images = item["vertical_src"]

        print(images)
        # print(vertical_src_images)
        if "/dy1" in images:
            images = images[0:-4]
            print(images)
            yield scrapy.Request(images)
        else:
            yield scrapy.Request(images)
        # if "/dy1" in vertical_src_images:
        #     vertical_src_images = vertical_src_images[0:-4]
        #     print(vertical_src_images)
        #     yield scrapy.Request(vertical_src_images)
        # else:
        #     yield scrapy.Request(vertical_src_images)
    def item_completed(self, results, item, info):
        print(results)
        print(images_store)
        images_path = [x["path"] for ok,x in results if ok]
        print(images_path[0])

        if os.path.exists(images_store+item["city"]+"-"+item["nickname"]+"-"+item["room_id"]+".jpg")== False:
           os.rename(images_store+images_path[0],images_store+item["city"]+"-"+item["nickname"]+"-"+item["room_id"]+".jpg")
        else:
           os.rename(images_store + images_path[0],
                      images_store + item["city"] + "-" + item["nickname"] + "-" + item["room_id"] + "(1)"+".jpg")

        return item