# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy


class Order(scrapy.Item):
    exchange_rate = scrapy.Field()
    volume = scrapy.Field()
    value = scrapy.Field()
    count = scrapy.Field()
    share = scrapy.Field()

