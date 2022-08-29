import requests
url="https://www.baidu.com"
headers={
'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; WOW64; rv:34.0) Gecko/20100101 Firefox/34.0'
}
page=requests.get(url=url,headers=headers)
# print(page)
# print(page.text)
with open("baidu.html",'w',encoding="utf-8") as f:
    f.write(page.text)

