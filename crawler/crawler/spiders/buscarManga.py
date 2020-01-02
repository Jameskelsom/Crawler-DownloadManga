# -*- coding: utf-8 -*-
import scrapy
from scrapy.spiders import CrawlSpider, Rule
from scrapy.linkextractors import LinkExtractor
#concurrent 
# scrapy crawl buscarManga -s HTTPCACHE_ENABLED=1

class BuscarmangaSpider(CrawlSpider):
    name = 'buscarManga'
    manga =(input('Digite o nome do manga: ')).replace(' ','-').lower()
    allowed_domains = ['unionleitor.top']
    start_urls = [f'https://unionleitor.top/manga/{manga}']

    rules = (
        Rule(
            LinkExtractor(
                restrict_xpaths=('//div/div[1]/a[contains(@href,"leitor/")]')
            ),callback='parse_new'
        ),
    )

    def parse_new(self, response):
        import ipdb; ipdb.set_trace()
        print(response.url)
        pass
