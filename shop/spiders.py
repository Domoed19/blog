from decimal import Decimal

import scrapy


class OmaSpider(scrapy.Spider):
    name = "oma.by"
    # allowed_domains = ["https://www.oma.by"]
    start_urls = ["https://www.oma.by/elektroinstrument-c"]

    def parse(self, response, **kwargs):
        for product in response.css(".catalog-grid .product-item"):
            cost = product.css(".product-price-block .price__normal::text").get().strip()
            if cost:
                cost = Decimal(cost.replace(",", "."))
            data = {
                "external_id": product.attrib.get("data-ga-product-id"),
                "title": product.css(".product-title-and-rate-block .wrapper::text").get().strip(),
                "cost": cost,
                "link": f"https://www.oma.by{product.css('a.area-link::attr(href)').get()}",
                "image": product.css(".product-item_image-box .catlg_list_img:first-child::atr(src)").get(),
            }
            yield data

        next_page = response.css(".page-nav_box .btn__nav-right:last-child::attr(href)").get()
        if next_page is not None:
            yield response.follow(next_page, callback=self.parse)
