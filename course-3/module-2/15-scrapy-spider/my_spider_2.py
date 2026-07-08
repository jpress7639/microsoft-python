import scrapy # type: ignore

class MySpider(scrapy.Spider):
    name = 'my_spider'
    start_urls = ['https://www.w3schools.com']

    def parse(self, response):
        yield{
            'title': response.css('title::text').get(),
            'paragraphs': response.css('p::text').getall()
        }