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
    film_name = scrapy.Field()
    film_score = scrapy.Field()
    film_comments_number = scrapy.Field()
    film_cast = scrapy.Field()
    film_info = scrapy.Field()

    pass
class DoubanShoutCommentsItem(scrapy.Item):
    pass
