import json

import scrapy

from settings_debug import SEARCH_URL
from settings_debug import ZUIRE_ORDER
from settings_debug import SHORT_COMMENTS_URL
from settings_debug import SEARCH_URL_REQUEST_HEADERS
from settings_debug import COMMNETS_URL_REQUEST_HEADERS
import re

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
            request_url = SEARCH_URL.format(film)
            print(SEARCH_URL_REQUEST_HEADERS)
            SEARCH_URL_REQUEST_HEADERS['Referer'] = request_url
            print(SEARCH_URL_REQUEST_HEADERS)
            yield scrapy.Request(url=SEARCH_URL.format(film),
                                 callback=self.parse,
                                 headers=SEARCH_URL_REQUEST_HEADERS,
                                 meta={"film": film},
                                 dont_filter=True)
    def parse(self,response):
        # page = response.text()
        # a = response.xpath("//div[@class='content']").extract()
        for content_selector in response.xpath("//div[@class='content']"):
            print(content_selector)

            film_name = content_selector.xpath(".//a/text()").extract_first().strip()
            if film_name == response.meta['film']:
                print("获取ID")
                print("抓取基本信息")
                film_id_click = content_selector.xpath(".//a").attrib['onclick']
                film_id = re.findall(r"sid:(.+?),", film_id_click)[0].strip()
                # TODO response.follow中的refer默认为请求 时候的refer,后使用scrapy.spidermiddlewares.referer.RefererMiddlewarec处理
                comments_url = SHORT_COMMENTS_URL.format(str(film_id), ZUIRE_ORDER)
                print(COMMNETS_URL_REQUEST_HEADERS)
                yield scrapy.Request(url=comments_url, headers=COMMNETS_URL_REQUEST_HEADERS, callback=self.parse_comments)
                film_score = ""
                film_comments_number = ""
                film_cast = ""
                film_info = ""
                return
    def parse_comments(self,response):
        print("执行翻页")
        print("完成抓取")
