import scrapy

from settings_debug import SEARCH_URL


class shoutCommentsSpider(scrapy.Spider):
    name = "shoutComment"
    def start_requests(self):
        urls = [
            # 'https://movie.douban.com/subject_search?search_text=闺密&cat=1002'
            'https://www.douban.com/search?cat=1002&q=闺蜜'

            'https://www.douban.com/search?cat=1002&q=大三儿'
            'https://www.douban.com/search?cat=1002&q=闺蜜'
        ]
        film_list = ["大三儿", "闺蜜2", "闺蜜", "大象席地而坐"]

        for film in film_list:
            yield scrapy.Request(url=SEARCH_URL.format(film), callback=self.parse, meta={"film":film}, dont_filter=True)
    def parse(self,response):
        # page = response.text()
        # a = response.xpath("//div[@class='content']").extract()
        for content_selector in response.xpath("//div[@class='content']"):
            print(content_selector)
            film_name = content_selector.xpath(".//a/text()").extract_first().strip()
            if film_name == response.meta['film']:
                print("获取ID")
                print("抓取基本信息")

