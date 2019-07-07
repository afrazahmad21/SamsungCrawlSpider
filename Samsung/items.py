# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# http://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class DeviceItem(scrapy.Item):

    device_name = scrapy.Field()
    model = scrapy.Field()
    region = scrapy.Field()
    version = scrapy.Field()
    os = scrapy.Field()
    os_version = scrapy.Field()
    build_date = scrapy.Field()
    file_urls = scrapy.Field()
