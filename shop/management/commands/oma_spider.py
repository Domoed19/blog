from django.core.management.base import BaseCommand
#Почитать про signals отдельно
from scrapy import signals
from scrapy.signalmanager import dispatcher

from shop.models import Product
from shop.spiders import OmaSpider
from scrapy.crawler import CrawlerProcess
from scrapy.utils.project import get_project_settings


class Command(BaseCommand):
    help = "Crawl OMA catalog"

    def handle(self, *args, **options):
        Product.objects.all().delete()
        def crawler_results(signal, sender, item, response, spider):
            Product.objects.update_or_create(external_id=item["external_id"], defaults=item)

        dispatcher.connect(crawler_results, signal=signals.item_scraped)

        process = CrawlerProcess(get_project_settings())
        process.crawl(OmaSpider)
        process.start()
