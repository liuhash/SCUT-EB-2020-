import requests
from lxml import etree
import pandas as pd

headers = {
    'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/103.0.5060.114 Safari/537.36 Edg/103.0.1264.62'
}

url = 'https://gz.58.com/ershoufang/'
page_text = requests.get(url=url,headers=headers).text
# print(page_text)
tree = etree.HTML(page_text)
div_list = tree.xpath('//div[@class="property-content"]')
data=[]*7
for i in div_list:
    info = i.xpath('./div[1]/div[1]/h3/text()')[0]
    place = i.xpath('./div[1]/section/div[2]/p[1]/text()')[0]
    # print(place)
    # 使用//text()可以得到所有子标签元素的值。并且过滤掉空格。之后使用join拼接。下面的房型也是这样使用。
    address="-".join(i.xpath('.//p[@class="property-content-info-comm-address"]//text()'))
    # print(address)
    total_price = i.xpath('./div[2]/p/span[1]/text()')[0]+i.xpath('./div[2]/p/span[2]/text()')[0]
    average_price=i.xpath('./div[2]/p[2]/text()')[0]
    area=str(i.xpath('./div[1]/section/div[1]/p[2]/text()')[0]).strip()
    # print(area)
    # print(average_price)
    # room_type=""
    # for j in range(1,7):
    #     print(i.xpath('./div[1]/section/div[1]/p[1]/span['+str(j)+']/text()')[0])
    #     room_type+= i.xpath('./div[1]/section/div[1]/p[1]/span['+str(j)+']/text()')[0]

    # print(type(i.xpath('./div[1]/section/div[1]/p[1]//text()')))
    room_type="".join(filter(lambda x:x!=" ",i.xpath('./div[1]/section/div[1]/p[1]//text()')))
    # print(room_type)
    # print([info,place,address,total_price,average_price,area,room_type])
    data.append([info,place,address,total_price,average_price,area,room_type])
    # print(data)
# 这里使用csv而不是txt做持久化存储。方便进一步的数据分析任务(如果有的话)
print(data)
df=pd.DataFrame(data)
df.columns=["房产信息","小区名称","小区地址","总价","每平米价格","面积","房型"]
df.to_csv("58_广州二手房.csv",index=False)
    # fp.write(name+' '+place+' '+price+'\n')
print('finish')