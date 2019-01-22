import datetime
import json

import scrapy

from settings_debug import SEARCH_URL
from settings_debug import ZUIRE_ORDER
from settings_debug import SHORT_COMMENTS_URL
from settings_debug import SEARCH_URL_REQUEST_HEADERS
from settings_debug import COMMNETS_URL_REQUEST_HEADERS
import re

from items import DoubanFilmItem

from items import DoubanShoutCommentsItem


class shoutCommentsSpider(scrapy.Spider):
    name = "shoutComment"
    def start_requests(self):
        # urls = [
        #     'https://www.douban.com/search?cat=1002&q=闺蜜'
        #     'https://www.douban.com/search?cat=1002&q=大三儿'
        #     'https://www.douban.com/search?cat=1002&q=闺蜜'
        # ]
        film_list = ["四个春天", "大黄蜂", "大三儿", ""]
            # , "闺蜜2", "闺蜜", "大象席地而坐"]

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
                yield scrapy.Request(url=comments_url,
                                     headers=COMMNETS_URL_REQUEST_HEADERS,
                                     callback=self.parse_comments,
                                     meta={"film_id": film_id,
                                            "ZUIRE_ORDER":ZUIRE_ORDER
                                           })
                dItem = DoubanFilmItem()
                dItem['film_id'] = film_id
                dItem['film_name'] = film_name
                dItem['film_score'] = content_selector.xpath(".//span[@class='rating_nums']/text()").extract_first().strip()
                dItem['film_comments_number'] = content_selector.xpath(".//span[3]/text()").extract_first().strip()
                dItem['film_cast'] = content_selector.xpath(".//span[@class='subject-cast']/text()").extract_first().strip()
                dItem['film_info'] = content_selector.xpath(".//p/text()").extract_first().strip()
                dItem["crawled_time"] = datetime.datetime.now().strftime("%Y/%m/%d %H:%M:%S")

                yield dItem
    def parse_comments(self,response):
        print("执行翻页")
        print("完成抓取")

        url_start = re.findall(r"start=(.+?)&",response.url)[0]
        try:
            if int(url_start) > 199:
                print("翻页完成结束")
                return
            else:
                # 解析当前页面 获取页面
                for comment_selector in response.xpath("//div[@class='comment-item']"):
                    scItem = DoubanShoutCommentsItem()
                    scItem['film_id'] = response.meta['film_id']
                    scItem['comment_id'] = comment_selector.attrib['data-cid']
                    scItem['people_link'] = comment_selector.xpath(".//span[@class='comment-info']/a/@href").extract_first()
                    scItem['people_nickname'] = comment_selector.xpath(".//span[@class='comment-info']/a/text()").extract_first().strip()
                    scItem['comment_score'] = comment_selector.xpath(".//span[@class='comment-info']/span[2]/@class").extract_first()
                    scItem['comment_time'] = comment_selector.xpath(".//span[@class='comment-time ']/@title").extract_first()
                    scItem['comment_info'] = comment_selector.xpath(".//span[@class='short']/text()").extract_first().strip()
                    scItem['comment_vote_number'] = comment_selector.xpath(".//span[@class='votes']/text()").extract_first().strip()
                    scItem["crawled_time"] = datetime.datetime.now().strftime("%Y/%m/%d %H:%M:%S")

                    yield scItem
                next_page_url = response.url.replace("start="+url_start, "start="+str(int(url_start)+20))
                yield response.follow(url=next_page_url, callback=self.parse_comments, meta={"film_id": response.meta['film_id']})
        except Exception as e:
            print(e)


