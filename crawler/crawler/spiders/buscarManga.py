# -*- coding: utf-8 -*-
import scrapy
from scrapy.spiders import CrawlSpider,Rule
from scrpay.linkextractors import LinkExtractor

class BuscarmangaSpider(scrapy.Spider):
    name = 'buscarManga'
    allowed_domains = ['unionleitor.top']
    start_urls = ['https://unionleitor.top/']

    def parse(self, response):
        pass
