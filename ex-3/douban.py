import requests
from bs4 import BeautifulSoup


def save_img(url, title):
    res = requests.get(url, headers=headers)
    if res.status_code == 200:
        print('抓取成功')
        with open('电影海报\%s.jpg' % title, 'wb') as f:  # 创建一个title.jpg的文件  '%s' %XXX
            f.write(res.content)
    else:
        print('抓取失败')


def parse_data(html):
    soup = BeautifulSoup(html, 'lxml')
    movie_img = []
    ol = soup.find('ol', class_='grid_view')
    li_list = ol.find_all('li')
    for li in li_list:
        img = li.find('img')
        title = img['alt']  # 把电影名字也抓取出来
        img_url = img['src']  # 根据字典里的键取值
        save_img(img_url, title)


def get_imgs(url):  # 这里的url是页面的url
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 6.2; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/85.0.4183.121 Safari/537.36'}
    res = requests.get(url, headers=headers)
    if res.status_code == 200:
        html = res.text
        parse_data(html)


for i in range(10):
    url = 'https://movie.douban.com/top250?start=%d&filter=' % (i * 25)
    get_imgs(url)


