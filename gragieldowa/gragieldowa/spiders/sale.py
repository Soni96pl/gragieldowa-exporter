# -*- coding: utf-8 -*-
import scrapy
from gragieldowa.items import Order


class SaleSpider(scrapy.Spider):
    name = 'sale'
    allowed_domains = ['gragieldowa.pl']

    def __init__(self, stock=None):
        self.stock = stock or 'FW20U2020'
        self.start_urls = ['https://gragieldowa.pl/spolka_arkusz_zl/spolka/%s/typ/0' % stock]

    def parse(self, response):
        table = response.selector.xpath("//table[contains(@class, 'data maintable')]")[1]
        rows = table.xpath(".//tr[position()>1 and position()<last()]")
        for row in rows:
            exchange_rate, volume, value, count, share = row.xpath(".//td/text()").getall()
            order = Order(
                exchange_rate=exchange_rate,
                volume=volume,
                value=value,
                count=count,
                share=share,
            )
            yield order
