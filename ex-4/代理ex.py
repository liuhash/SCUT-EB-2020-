import requests
url="http://www.baidu.com"
session1=requests.session()
resp=session1.get(url=url,proxies="http://122.9.101.6:80")

print(resp.status_code)