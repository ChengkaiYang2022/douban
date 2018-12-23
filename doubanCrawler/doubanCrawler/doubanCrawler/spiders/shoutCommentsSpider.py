import scrapy
class shoutCommentsSpider(scrapy.Spider):
    name = "shoutComment"
    def start_requests(self):
        urls = [
            'https://movie.douban.com/subject_search?search_text=闺密&cat=1002'
        ]
        for url in urls:
            yield scrapy.Request(url=url, callback=self.parse)
    def parse(self,response):
        page = response.text()

