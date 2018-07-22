# -*- coding: utf-8 -*-
import scrapy


class MobilspiderSpider(scrapy.Spider):
    name = 'mobilspider'
    allowed_domains = ['https://www.olx.co.id']
    start_urls = ['https://www.olx.co.id/motor/bekas/magelang-kab/']

    def parse(self, response):
        title =  response.css('.marginright5.link span::text').extract()
        gambar = response.css('img').xpath('@src').extract()
        url = response.css('a.marginright5.link.linkWithHash.detailsLink::attr(href)').extract()
        harga = response.css('p strong.c000::text').extract()
        for item in zip(title, gambar,url,harga):
            scraped_info = {
                'title' : item[0],
                'gambar' : item[1],
                'url' : item[2],
                'harga': item[3]
            }
            yield scraped_info
