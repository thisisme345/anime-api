import re
import scrapy

class Stream(scrapy.Spider):
    name = "stream"

    start_urls = ["https://4anime.to/cowboy-bebop-tengoku-no-tobira?id=22944"]

    def parse(self, response):
        data = response.css("section.page-single script::text").get()
        link = re.findall('(?:(?:https?|ftp):\/\/)?[\w/\-?=%.]+\.[\w/\-&?=%.]+', data)

        yield {
            'link': link[1]
        }
