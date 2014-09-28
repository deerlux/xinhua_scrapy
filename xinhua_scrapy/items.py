# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# http://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class XinhuaScrapyItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    title = scrapy.Field()
    source = scrapy.Field()
    body = scrapy.Field()
    public_time = scrapy.Field()
    url = scrapy.Field()
    crawl_time = scrapy.Field()

    domain = scrapy.Field()
    keywords = scrapy.Field()

