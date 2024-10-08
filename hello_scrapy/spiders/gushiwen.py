import scrapy


class GushiwenSpider(scrapy.Spider):
    name = "gushiwen"
    allowed_domains = ["gushiwen.cn"]
    start_urls = ["https://gushiwen.cn"]

    def parse(self, response):
        pass
