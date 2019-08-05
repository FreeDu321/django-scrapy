import scrapy
# from testscrapy
from scrapy.selector import Selector
# import items
class DmozSpider(scrapy.Spider):
    name = "test"
    allowed_domains = ["dmoz.org"]
    start_urls = [
        "https://yq.aliyun.com"
    ]

    def parse(self, response):
        selector = Selector(response)
        # print("===============================================================================\n%s" % response.body)
        print("ttttttttttttttttttttt")

        # print(selector.xpath('//title').extract())
        # print(selector.xpath('//div[contains@class,"item-box"]/a/@href').extract())
        print(selector.xpath('//div[@class="item-info"]/div[@class="main-info"]/h3').extract())
        print("ttttttttttttttttttttt")

        # with open("a.txt", 'wb') as f:
        #     f.write(response.body)
        # print(selector.xpath('//title[@*]'))
