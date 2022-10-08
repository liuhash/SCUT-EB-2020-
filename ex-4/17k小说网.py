import requests
from lxml import etree
session=requests.session()
headers = {
    'user-agent': 'Mozilla/5.0 (X11; Linux x86_64; rv:104.0) Gecko/20100101 Firefox/104.0',
}
resp=session.post()
print(resp.json())
print(resp.cookies)
resp.close()
url2="https://user.17k.com/www/bookshelf/"
resp2=session.get(url=url2,headers=headers)
print(resp2.json())