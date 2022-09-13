import requests
import re
import os
import time
import random
headers = {
    'user-agent': 'Mozilla/5.0 (X11; Linux x86_64; rv:104.0) Gecko/20100101 Firefox/104.0',
    'Cookie':'bid=uVCFCfRVxyU; douban-fav-remind=1; _pk_ref.100001.8cb4=%5B%22%22%2C%22%22%2C1662375928%2C%22https%3A%2F%2Fmovie.douban.com%2Ftop250%3Fstart%3D0%26amp%3Bfilter%3D%22%5D; _pk_id.100001.8cb4=6f498f7e135ec15c.1661648117.2.1662375937.1661648117.; __gads=ID=90347103ece56c1e-22f7331a0ad600d4:T=1661648119:RT=1661648119:S=ALNI_Maa3BiDefHQajU-1m-p5Y1iR-nomw; __gpi=UID=0000092563cc11d5:T=1661648119:RT=1662360877:S=ALNI_MaE82R6KkwgLCXrbdd8in_zDQRMzg; __utma=30149280.491179232.1661648120.1662373962.1662375799.5; __utmz=30149280.1662375799.5.4.utmcsr=accounts.douban.com|utmccn=(referral)|utmcmd=referral|utmcct=/; __utmc=30149280; ap_v=0,6.0; dbcl2="219156133:iUxxJVBd6NI"; ck=MU1f; __utmb=30149280.8.10.1662375799; push_noty_num=0; push_doumail_num=0; _pk_ses.100001.8cb4=*; __utmt=1; __utmv=30149280.21915; ct=y'
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
        download_image(html)
    # 自己测试
    # with open('豆瓣电影 Top 250.html') as fp:
    #     html1=fp.read()
    #  print(html1)
    # download_image(html1)



