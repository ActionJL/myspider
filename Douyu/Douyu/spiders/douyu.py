import json

import scrapy

from Douyu.Douyu.items import DouyuItem


class DouyuSpider(scrapy.Spider):
    name = 'douyu'
    allowed_domains = ["capi.douyucdn.cn"]

    offset = 0
    url = "http://capi.douyucdn.cn/api/v1/getVerticalRoom?limit=20&offset=10"
    start_urls = [url + str(offset)]



    def parse(self, response):
        # 从json里获取data段数据集合
        data_list = json.loads(response.body)['data']
        print(data_list)
        #
        if len(data_list) == 0:
            return
        for each in data_list:
            item = DouyuItem()
            item['name'] = each['nickname']
            item['imagesUrls'] = each['vertical_src']

            yield item

        self.offset += 20
        yield scrapy.Request(self.url + str(self.offset), callback=self.parse)


