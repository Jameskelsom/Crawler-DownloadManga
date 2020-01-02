# -*- coding: utf-8 -*-
import scrapy
import requests
from scrapy.spiders import CrawlSpider, Rule
from scrapy.linkextractors import LinkExtractor
#concurrent 
# scrapy crawl buscarManga -s HTTPCACHE_ENABLED=1

class BuscarmangaSpider(CrawlSpider):
    name = 'buscarManga'
    manga =(input('Digite o nome do manga: ')).replace(' ','-').lower()
    allowed_domains = ['unionleitor.top']
    start_urls = [f'https://unionleitor.top/manga/{manga}']
    base_urls = ['https://unionleitor.top/z']

    for url in start_urls:
        r = requests.get(url)
        if r.url in base_urls:
            print('-'*20)
            print('Manga não encontrado!!!')
            print('-'*20)
        else:
            rules = (
                Rule(
                    LinkExtractor(
                        restrict_xpaths=('//div/div[1]/a[contains(@href,"leitor/")]')
                    ),callback='parse_new'
                ),
            )

    def parse_new(self, response):
        print(response.css('img.img-responsive'))
        pass
