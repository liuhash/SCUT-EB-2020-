import scrapy
import json
from jsonpath import jsonpath
import re
from dishonest.items import DishonestItem
class BaiduSpider(scrapy.Spider):
    name = 'baidu'
    allowed_domains = ['baidu.com']
    start_urls = [
        'https://sp1.baidu.com/8aQDcjqpAAV3otqbppnN2DJv/api.php?resource_id=6899&query=%E5%A4%B1%E4%BF%A1%E4%BA%BA&pn=0&rn=10&from_mid=1&ie=utf-8&oe=utf-8&format=json&t=1666546246932'
    ]
    url_pattern='https://sp1.baidu.com/8aQDcjqpAAV3otqbppnN2DJv/api.php?resource_id=6899&query=%E5%A4%B1%E4%BF%A1%E4%BA%BA&pn={}&rn=10&from_mid=1&ie=utf-8&oe=utf-8&format=json&t=1666546246932'
    def parse(self, response):
        for num in range(10, 10030, 10):
            # 根据URL模板, 生成URL
            url = self.url_pattern.format(num)
            yield scrapy.Request(url, callback=self.parse_data)

    def parse_data(self, response):
        """解析数据"""
        # 把json字符串转换为python的字典
        data = json.loads(response.text)
        # 获取失信人信息
        results = jsonpath(data, '$..disp_data')[0]
        for result in results:
            # print(result)
            item = DishonestItem()
            # 把抓取到数据, 交给引擎
            item['name'] = result['iname']
            item['card_num'] = result['cardNum']
            item['area_name'] = result['areaName']
            item['content'] = re.sub('%s+', '', result['duty'])
            item['business_entity'] = result['businessEntity']
            item['publish_unit'] = result['courtName']
            item['publish_date'] = result['publishDate']

            # 把数据交给引擎
            yield item
