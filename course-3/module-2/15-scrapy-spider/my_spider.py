import scrapy # type: ignore

class MySpider(scrapy.Spider):
    name = 'my_spider'
    start_urls = ['https://www.yahoo.com/']

    def parse(self, response):
        # extract the title of the page using css selectors
        title = response.css('title::text').get()

        # extract all the paragraphs of the page using css selectors
        paragraphs = response.css('p::text').getall()

        # print the extracted data
        print("Title:", title)
        print("Paragraphs:", paragraphs)
        
    
