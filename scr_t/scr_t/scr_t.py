import scrapy
import scr_t
from scrapy.selector import Selector
class scr_t(scrapy.Spider):
    name = "scr_t"
    allowed_domains = ["aliyun.com"]
    start_urls = [
        "https://yq.aliyun.com/"
    ]

    def parse(self, response):
        item = scr_t.ScrTItem()
        selector = Selector(response)
        item['name'] = selector.xpath('//div][@class="item-info"]/div[@class="main-info"]/h3').extract()
        print(item['name'])