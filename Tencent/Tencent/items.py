# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy


class TencentItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()

    # 职位名称
    positionName = scrapy.Field()
    # 详情链接
    positionLink = scrapy.Field()
    # 职位类别
    positionType = scrapy.Field()
    # 人数
    peopleNumber = scrapy.Field()
    # 工作地点
    workLocation = scrapy.Field()
    # 发布时间
    publishTime = scrapy.Field()



