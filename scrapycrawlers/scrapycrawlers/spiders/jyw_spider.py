import scrapy


class JywSpiderSpider(scrapy.Spider):
    name = "jyw_spider"
    allowed_domains = ["jyw-pokeca.com"]
    jyw_urls = ["https://jyw-pokeca.com/products/new-pokemon-card-game-sword-and-shield-high-class-pack-shiny-star-v-box-2020-pokemon-japan",
                "https://jyw-pokeca.com/products/new-pokemon-card-game-deck-shield-chien-pao-apr-2023-pokemon-japan"]
    start_urls = [jyw_urls[1]]

    def parse(self, response):
        pass
