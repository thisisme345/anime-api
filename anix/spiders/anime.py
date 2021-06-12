import scrapy
import requests
from anix.utils.anime import parse_anime

class AnimeSpider(scrapy.Spider):
    name = "anime"

    start_urls = ["https://4anime.to/anime/sakamichi-no-apollon"]

    def parse(self, response):
        return parse_anime(response)
