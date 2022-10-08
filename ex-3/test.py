import requests
from lxml import etree

headers = {
    'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/103.0.5060.114 Safari/537.36 Edg/103.0.1264.62'
}

url = 'https://gz.58.com/ershoufang/'
page_text = requests.get(url=url,headers=headers).text

tree = etree.HTML(page_text)
div_list = tree.xpath('//div[@class="property-content"]')
print(div_list)
# fp = open('58.txt','w',encoding='utf-8')

for i in div_list:
    print(i)
    name = i.xpath('./div[1]/div[1]/h3/text()')[0]
    place = i.xpath('./div[1]/section/div[2]/p[1]/text()')[0]
    price = i.xpath('./div[2]/p/span[1]/text()')[0]+i.xpath('./div[2]/p/span[2]/text()')[0]
    print(name)
    print(place)
    print(price)
    # fp.write(name+' '+place+' '+price+'\n')
print('finish')
