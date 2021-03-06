from scrapy.crawler import CrawlerProcess
from scrapy.settings import Settings
from leruamerlen import settings
from leruamerlen.spiders.lerua import LeruaSpider

if __name__ == '__main__':
    crawler_settings = Settings()
    crawler_settings.setmodule(settings)

    process = CrawlerProcess(settings=crawler_settings)
    process.crawl(LeruaSpider)

    process.start()