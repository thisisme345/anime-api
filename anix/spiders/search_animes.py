import scrapy
from anix.utils.anime import parse_anime

class SearchAnimes(scrapy.Spider):
    name = 'search_animes'
    start_urls = ['https://4anime.to/?s=cowboy+bebop']

    def parse(self, response):
        links = response.css("#headerDIV_2 a::attr('href')").getall()

        for link in links[0:3]:
            yield scrapy.Request(url=link, callback=self.anime)

    def anime(self, response):
        return parse_anime(response)

