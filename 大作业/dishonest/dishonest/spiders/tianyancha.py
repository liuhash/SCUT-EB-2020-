import bs4
import scrapy
from dishonest.items import DishonestItem

class TianyanchaSpider(scrapy.Spider):
    name = 'tianyancha'
    allowed_domains = ['shixin.tianyancha.com']
    start_urls = ['http://shixin.tianyancha.com/']
    url_patterns= "https://shixin.tianyancha.com/search/gs_{}"
    def parse(self, response):
        for i in ["供应链","物流","电商","电子","空调"]:
            url_pattern=self.url_patterns.format(i)
            yield scrapy.Request(url_pattern,callback=self.parse_data)

    def parse_data(self, response):
        for r in results:
            result = soup.find_all("div", class_="detail")
            card_nums = r.find_all("span", class_="value")
            card_num = card_nums[3].text
            area = r.find("span", class_="site").text
            content = r.find("div", class_="results text-ellipsis").text
            publish_date = r.find("span", class_="result").text
            publish_units = r.find_all("span", class_="result")
            publish_unit = publish_units[3].text
            item = DishonestItem()
            item['name'] = name
            item['card_num'] = card_num
            item['area_name'] = area
            item['content'] = content
            item['business_entity'] = business_entity
            item['publish_unit'] = publish_unit
            item['publish_date'] = publish_date

