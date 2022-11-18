import requests
import json
from jsonpath import jsonpath
from _datetime import datetime
import aiohttp
import asyncio
import pandas as pd

url='https://sp1.baidu.com/8aQDcjqpAAV3otqbppnN2DJv/api.php?resource_id=6899&query=%E5%A4%B1%E4%BF%A1%E4%BA%BA%E5%90%8D%E5%8D%95&pn=0&rn=10&from_mid=1&ie=utf-8&oe=utf-8&format=json&t=1666540446008&cb=jQuery110207412315952203221_1666540395462&_=1666540395465'
head={'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/103.0.5060.66 Safari/537.36 Edg/103.0.1264.44',
      'Referer': 'https://www.baidu.com/s?ie=UTF-8&wd=%E5%A4%B1%E4%BF%A1%E4%BA%BA'}

async def get_dishonest():
    tasks=[]
    resp = requests.get(url=url, headers=head).text.strip('/**/jQuery110207412315952203221_1666540395462(').strip(');')
    datas = json.loads(resp)
    disp_num = jsonpath(datas, '$..dispNum')[0]
    print(disp_num)
    data=[]*10
    data.append(['name', 'card_num', 'age', 'area', 'business_entity', 'content', 'publish_date', 'publish_unit', 'create_date','update_date'])
    df=pd.DataFrame(data)
    df.to_csv('dishonest.csv', mode='a',header=False, encoding='utf-8-sig', index=False)
    for i in range(0,disp_num,10):
        tasks.append(asyncio.create_task(get_detail(i)))
    await asyncio.wait(tasks)

async def get_detail(page_num):
    url=f'https://sp1.baidu.com/8aQDcjqpAAV3otqbppnN2DJv/api.php?resource_id=6899&query=%E5%A4%B1%E4%BF%A1%E4%BA%BA%E5%90%8D%E5%8D%95&pn={page_num}&rn=10&from_mid=1&ie=utf-8&oe=utf-8&format=json&t=1666540446008&cb=jQuery110207412315952203221_1666540395462&_=1666540395465'
    async with aiohttp.ClientSession() as session:
        async with session.get(url=url) as f:
            page =await f.text()
            pagetext=page.strip('/**/jQuery110207412315952203221_1666540395462(').strip(');')
            datas=json.loads(pagetext)
            results = jsonpath(datas, '$..disp_data')[0]

            # data=pd.DataFrame(columns=['name','card_num','age','area','business_entity','content','publish_date','publish_unit','create_date','update_date'])
            data = [] * 10
            for result in results:
                data.append([result['iname'],result['cardNum'],result['age'],result['areaName'],result['businessEntity'],result['duty'],result['publishDate'],result['courtName'],datetime.now().strftime('%Y-%m-%d %H:%M:%S'),datetime.now().strftime('%Y-%m-%d %H:%M:%S')])
            dataframe=pd.DataFrame(data)
            dataframe.columns=('name','card_num','age','area','business_entity','content','publish_date','publish_unit','create_date','update_date')
            dataframe.to_csv('dishonest.csv', mode='a',header=False,encoding='utf-8-sig', index=False)

if __name__ == '__main__':
    asyncio.get_event_loop().run_until_complete(get_dishonest()) #使用get_event_loop()执行异步爬虫防止报错
    print('over!') #结束




