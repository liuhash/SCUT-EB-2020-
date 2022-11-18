# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy


class DishonestItem(scrapy.Item):
    # 姓名/获取企业名称
    name = scrapy.Field()
    # 证件号
    card_num = scrapy.Field()
    # 地区
    content = scrapy.Field()
    # 失信内容
    area_name = scrapy.Field()
    # 法人
    business_entity = scrapy.Field()
    # 公布单位/执行单位
    publish_unit = scrapy.Field()
    # 公布日期/宣判日期
    publish_date= scrapy.Field()
    # 更新日期, 创建日期
    create_date = scrapy.Field()
    # 更新日期
    update_date = scrapy.Field()
