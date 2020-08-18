# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html


# useful for handling different item types with a single interface
import os

import scrapy
from itemadapter import ItemAdapter
from scrapy.pipelines.images import ImagesPipeline

from settings import IMAGES_STORE as images_store

class DouyuPipeline(ImagesPipeline):
    def process_item(self, item, spider):
        return item

    def get_media_requests(self, item, info):
        image_link = item['imagelink']
        yield scrapy.Request(image_link)

    def item_completed(self, results, item, info):

        # 取出results里图片信息中 图片路径的值
        image_path = [x['path'] for ok, x in results if ok]

        os.rename(images_store + image_path[0], image_store + item['nickname'] + '.jpg')
