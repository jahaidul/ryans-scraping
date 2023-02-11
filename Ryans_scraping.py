import scrapy


class LaptopSpider(scrapy.Spider):
    name = "laptop"
    allowed_domains = ["ryans.com"]
    start_urls = ["https://www.ryanscomputers.com/category/laptop-all-laptop?limit=100&osp=0"]

    def parse(self, response):
        for product in response.xpath('//div[@class="card-body text-center"]'):
            title = product.xpath('. //p[@class="card-text p-0 m-0 list-view-text"]/a/text()').get()
            Ram = product.xpath('.//li[contains(text(), "RAM")]/text()').get()
            Gen = product.xpath('.//li[contains(text(), "Generation")]/text()').get()
            Graphics = product.xpath('.//li[contains(text(), "Graphics Memory")]/text()').get()
            Storage = product.xpath('.//li[contains(text(), "Storage")]/text()').get()
            Price = product.xpath('.//p[@class="pr-text cat-sp-text pb-1"]/text()').get()
            Image =product.xpath('.//div[@class="image-box"]/a/@href').get()
            
            
            yield {
                "title": title,
                "Ram" : Ram,
                "Gen": Gen,
                "Graphics": Graphics,
                "Storage": Storage,
                "Price": Price,
                "Image": Image
                }
