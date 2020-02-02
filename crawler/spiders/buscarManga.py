# -*- coding: utf-8 -*-
import scrapy
import requests
import os
from scrapy.spiders import CrawlSpider, Rule
from scrapy.linkextractors import LinkExtractor
# concurrent
# scrapy crawl buscarManga -s HTTPCACHE_ENABLED=1

class BuscarmangaSpider(CrawlSpider):
    name = 'buscarManga' #nome da spider
    txt = str(input('Digite o nome do manga: ')) 
    manga = txt.replace(' ', '-').lower() #tratamento da string
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
            except FileExistsError:
                pass

            rules = ( #regras
                Rule(
                    LinkExtractor(
                        restrict_xpaths=(
                            '//div/div[1]/a[contains(@href,"leitor/")]')
                    ), callback='parse_new'
                ),
            )

    def parse_new(self, response):
        img_urls = []
        [img_urls.append(link) for link in response.css('img.img-responsive::attr("src")').getall()]
        for img in img_urls:
            img = img.replace('>','').replace('<','')
            yield scrapy.Request(
                response.urljoin(img),
                callback=self.download #Função de download das imagens
            )
    def download(self,response):
        trt = response.url.lower().find(self.txt.replace(' ','%20')) #tratamento de dados
        mangaImg = response.url[trt:].replace('/','-').replace('https:--','').replace('%20','_')
        with open(self.manga +"/" + mangaImg, 'wb') as f:
            f.write(response.body)
