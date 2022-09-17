import requests
from bs4 import BeautifulSoup

if __name__ == '__main__':
    pass
    # 对首页的数据进行爬取
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/88.0.4324.150 Safari/537.36'
    }
    url = 'https://www.shicimingju.com/book/sanguoyanyi.html'
    page_text = requests.get(url=url, headers=headers).content
    # 在首页中解析出所有章节的标题和详情页的url
    # 实例化BeautifulSoup对象，需要将页面的网页源码加载到该对象中
    soup = BeautifulSoup(page_text, 'lxml')  # 拿到了对象
    # 解析章节标题和详情页的数据
    li_list = soup.select('.book-mulu>ul>li')
    # 层级表达式
    fp = open('./sanguoyanyi.text', 'w', encoding='utf-8')
    for li in li_list:
        title = li.a.string
        detail_url = 'https://www.shicimingju.com' + li.a['href']
        # 对详情页发起请求，并进行解析
        detail_page_text = requests.get(url=detail_url, headers=headers).content

        # 解析详情页面的内容
        detail_soup = BeautifulSoup(detail_page_text, 'lxml')
        div_tag = detail_soup.find('div', class_='chapter_content')
        content = div_tag.text
        fp.write(title + ":" + content + '\n')
        print(title + '爬取成功')

# 作业：58同城 标签标题 房型 价格
# 三国演义乱码
