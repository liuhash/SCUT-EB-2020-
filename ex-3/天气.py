import requests
from lxml import etree
headers = {
    'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/103.0.5060.114 Safari/537.36 Edg/103.0.1264.62'
}
url="https://www.aqistudy.cn/historydata"
page_text=requests.get(url=url,headers=headers).text
tree=etree.HTML(page_text)
