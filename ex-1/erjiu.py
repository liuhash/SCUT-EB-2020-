import requests
url="https://cn.bing.com/search?form=MOZLBR&pc=MOZI&q=%E4%BA%8C%E8%88%85"
headers={
'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; WOW64; rv:34.0) Gecko/20100101 Firefox/34.0'
}
page=requests.get(url=url,headers=headers)
# print(page)
# print(page.text)
with open("erjiu.html",'w',encoding="utf-8") as f:
    f.write(page.text)