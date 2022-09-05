import requests
import re
import os
import time
import random
headers = {
    'user-agent': 'Mozilla/5.0 (X11; Linux x86_64; rv:104.0) Gecko/20100101 Firefox/104.0',
    'Cookie':'写你自己的'
}

# 不同的代理IP,代理ip的类型必须和请求url的协议头保持一致
proxy_list = ['122.9.101.6','47.113.90.161','122.152.196.126','114.215.174.227','119.185.30.75']

def get_html(url):
    '''Request a web page and get the source code'''
    try:
        html = requests.get(url, headers=headers,proxies={'http':random.choice(proxy_list)})
        return html.text
    except requests.exceptions.RequestException:
        print(url, '请求失败')

def download_image(html):
    # print(html)
    iter1=re.compile(r'<div class="pic">.*?<img.*?alt="(?P<movie_name>.*?)" src="(?P<img_url>.*?)".*?>.*?</div>',re.DOTALL)
    result1=iter1.finditer(html)
    movie_names=[]
    img_urls=[]
    for i in result1:
        # print(i.group('movie_name'))
        # print(i.group('img_url'))
        movie_names.append(i.group('movie_name'))
        img_urls.append(i.group('img_url'))
    # iter2=re.compile(r'<div class=.*?>(?P<middle>.*?)</div>',re.DOTALL)
    # result2=iter2.finditer(html)
    # for i in result2:
    #     print(i.group("middle"))
    for name,url in zip(movie_names,img_urls):  # 拿到每张图片的下载地址
        time.sleep(1)  # 避免大规模访问   导致网站崩
        response = requests.get(url, headers=headers,proxies={'http':random.choice(proxy_list)})  # 这个是请求图片
        dir_name = './pics'
        if not os.path.exists(dir_name):
            os.mkdir(dir_name)
        with open(dir_name + "/" + name+'.png', "wb") as f:  # 加/是为了体现目录的替换
            f.write(response.content)

if __name__ == '__main__':
    urls = ['https://movie.douban.com/top250?start={}&filter='.format(i * 25) for i in range(0, 10)]
    for url in urls:
        html = get_html(url)
        # print(html)
        datas = download_image(html)
    # 自己测试
    # with open('豆瓣电影 Top 250.html') as fp:
    #     html1=fp.read()
    #  print(html1)
    # download_image(html1)



