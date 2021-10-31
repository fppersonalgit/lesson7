import scrapy
from scrapy.http import HtmlResponse
import pymongo
from scrapy.pipelines.images import ImagesPipeline
from leruamerlen import items
from leruamerlen.items import LeruamerlenItem



class LeruaSpider(scrapy.Spider):
    name = 'lerua'
    allowed_domains = ['leroymerlin.ru']
    start_urls = ['https://leroymerlin.ru/catalogue/vygodnaya-pokupka']

    def parse(self, response: HtmlResponse):
        products_links = response.xpath("//div[@class = 'phytpj4_plp largeCard']/a/@href").extract()

        for link in products_links:
            yield response.follow(link, callback=self.product_parsing)

    print()

    def product_parsing(self, response: HtmlResponse):
        title = response.xpath("//h1/text()").extract_first()
        price = response.xpath("//span[@slot = 'price']/text()").extract_first()
        href = response.xpath(
            "/html/body/div[3]/div[2]/uc-regions-overlay/uc-region-list/uc-multicolumn/uc-regions-overlay-item["
            "2]/a/@href").extract_first()
        photos_p1 = response.xpath("//img[@slot='thumbs']/@src").extract()
        photos_changed = photos_p1
        photos = []
        for photo in photos_changed:
            big_size_image = photo.replace('w_82', 'w_2000')
            bit_size_image_corrected = big_size_image.replace('h_82', 'h_2000')
            photos.append(bit_size_image_corrected)

        yield LeruamerlenItem(title=title, price=price, href= href, photos= photos)

        print()
