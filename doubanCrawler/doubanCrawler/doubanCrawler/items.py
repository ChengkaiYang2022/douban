# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class DoubancrawlerItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    pass
class DoubanFilmItem(scrapy.Item):
    film_id = scrapy.Field()
    film_name = scrapy.Field()
    film_score = scrapy.Field()
    film_comments_number = scrapy.Field()
    film_cast = scrapy.Field()
    film_info = scrapy.Field()
    crawled_time = scrapy.Field()
    pass
class DoubanShoutCommentsItem(scrapy.Item):
    film_id = scrapy.Field()
    comment_id = scrapy.Field()
    people_link = scrapy.Field()
    people_nickname = scrapy.Field()
    comment_score = scrapy.Field()
    comment_time = scrapy.Field()
    comment_info = scrapy.Field()
    comment_vote_number = scrapy.Field()
    crawled_time = scrapy.Field()
    pass
class DoubanFilmSubjectItem(scrapy.Item):
    pass
class DoubanCelebrityItem(scrapy.Item):
    pass
