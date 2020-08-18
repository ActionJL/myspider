import scrapy


class TencentSpider(scrapy.Spider):
    name = 'tencent'
    allowed_domains = ['tencent.com']
    start_urls = ['http://tencent.com/']

    # https://careers.tencent.com/search.html
    # https://careers.tencent.com/search.html?index=2
    baseURL = 'https://careers.tencent.com/search.html?index='

    offset = 0
    start_urls = [baseURL + str(offset)]

    def parse(self, response):
        pass
        response.xpath("//tr[@class='even']")

