# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class VideoItem(scrapy.Item):
    collection = 'videos'

    rank = scrapy .Field()
    title = scrapy .Field()
    src = scrapy.Field()
    img = scrapy .Field()
    play = scrapy .Field()
    comment = scrapy .Field()
    author = scrapy .Field()
    score = scrapy .Field()
    video_url = scrapy.Field()

class DanmusItem(scrapy.Item):
    collection = 'danmus'

    title = scrapy.Field()
    danmus = scrapy.Field()

class CommentItem(scrapy.Item):
    collection = 'comments'

    title = scrapy.Field()
    user_info = scrapy.Field()
    content = scrapy.Field()
    time = scrapy.Field()
    like = scrapy.Field()

