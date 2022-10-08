import asyncio
import json
import aiohttp
import aiofiles
import requests
import os

#创建一个文件夹储存小说的章节
if not os.path.exists('./西游记/'):
    os.makedirs('./西游记/')

#获取所需要的书的网址以及每个章节的网址
book_url='https://dushu.baidu.com/api/pc/getCatalog?data={%22book_id%22:%224306063500%22}'
page_url='https://dushu.baidu.com/api/pc/getChapterContent?data='
head={'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/103.0.5060.66 Safari/537.36 Edg/103.0.1264.44'}

#定义获取书的方法
async def get_book():
    resp=requests.get(book_url).json() #通过requests请求获取书的页面并进行json解析
    tasks=[] #创建一个任务列表以供接下来协程使用
    for item in resp['data']['novel']['items']: #使用for循环解析并获取页面中包含的每个章节的标题和id
        title=item['title']
        id=item['cid']
        tasks.append(asyncio.create_task(get_page(book_id,id,title))) #为爬取每个章节创建协程的任务并添加进入任务列表
    await asyncio.wait(tasks) #将任务列表加入协程等待执行

#定义获取每个章节内容的方法
async def get_page(bookid,id,title):
    data={  #通过获取书的页面得到每个章节页面的数据
        "book_id":bookid,
        "cid":f"{bookid}|{id}",
        "need_bookinfo":1
    }
    data=json.dumps(data) #将json形式转换为字符串形式
    url=page_url+data #拼接得到每个章节的网址
    async with aiohttp.ClientSession() as session: #使用异步http每个章节的页面并解析
        async with session.get(url) as f:
            dic= await f.json() #将每个页面数据转换成字典
            async with aiofiles.open('./西游记/'+title+'.txt',mode='w',encoding='utf-8') as fp: #使用异步文件储存每个章节文本
                await fp.write(dic['data']['novel']['content']) #写入每个章节内容

#主程序执行
if __name__ == '__main__':
    book_id='4306063500' #书的id
    asyncio.get_event_loop().run_until_complete(get_book()) #使用get_event_loop()执行异步爬虫防止报错
    print('over!') #结束

