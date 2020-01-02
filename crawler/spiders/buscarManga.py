# -*- coding: utf-8 -*-
import scrapy
import requests
import os
from scrapy.spiders import CrawlSpider, Rule
from scrapy.linkextractors import LinkExtractor
# concurrent
# scrapy crawl buscarManga -s HTTPCACHE_ENABLED=1


class BuscarmangaSpider(CrawlSpider):
    name = 'buscarManga'
    txt = str(input('Digite o nome do manga: '))
    manga = txt.replace(' ', '-').lower()
    allowed_domains = ['unionleitor.top']
    start_urls = [f'https://unionleitor.top/manga/{manga}']
    base_urls = ['https://unionleitor.top/z']

    for url in start_urls:
        r = requests.get(url)
        if r.url in base_urls:
            print('-'*30)
            print('Manga não encontrado!!!')
            print('-'*30)
        else:
            try:
                os.mkdir(manga)
            except:
                pass

            rules = (
                Rule(
                    LinkExtractor(
                        restrict_xpaths=(
                            '//div/div[1]/a[contains(@href,"leitor/")]')
                    ), callback='parse_new'
                ),
            )

    def parse_new(self, response):
        pages = []
        [pages.append(link) for link in response.css('img.img-responsive::attr("src")').getall()]
        for page in pages:
            trt = page.lower().find(self.txt)
            mangaImg = page[trt:].replace('/','-').replace('https:--','')
            import ipdb; ipdb.set_trace()
            with open(self.manga +"/" + mangaImg, 'wb') as f:
                f.write(response.content)