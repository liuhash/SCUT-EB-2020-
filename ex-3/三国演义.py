from bs4 import BeautifulSoup
import lxml
import requests
import re
import os

#将本地html文档中的数据加载到对象中
#fp = open('./test.html,'r',encoding = 'utf-8')
#soup = BeautifulSoup(fp,'lxml')
#print(soup)

url = 'http://guoxue.lishichunqiu.com/gdxs/sanguoyanyi/'

headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/103.0.5060.114 Safari/537.36 Edg/103.0.1264.62'
    }
page_text = requests.get(url=url,headers=headers).text

soup = BeautifulSoup(page_text,'lxml')
#select返回一个列表 ’>‘一个层级  ’ ‘多个层级
td_list = soup.select('.news_list ul a')



ex = re.compile(r'(?P<li>.*?)历史春秋网www',re.S)

for td in td_list:
    title = td.string
    detail_url = td['href']

    detail_page_text = requests.get(url=detail_url, headers=headers).text
    detail_soup = BeautifulSoup(detail_page_text, 'lxml')
    div_tag = detail_soup.find('div', id='content')
    content = div_tag.text.replace(u'\xa0',u' ')
    res = ex.finditer(content)
    for i in res:
        # 把每章写在不同的文件里
        dir_name='./三国演义'
        if not os.path.exists(dir_name):
            os.mkdir(dir_name)
        fp = open(dir_name+'/'+title+'.txt', 'w', encoding='utf-8')
        fp.write(title + ":" + i.group('li') + '\n')
        print(title, '成功')
fp.close()