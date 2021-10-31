# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy


class LeruamerlenItem(scrapy.Item):
    title = scrapy.Field()
    price = scrapy.Field()
    href = scrapy.Field()
    photos = scrapy.Field()
    _id = scrapy.Field()
    pass
