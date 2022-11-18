import requests


url = 'http://www.gsxt.gov.cn/affiche-query-area-info-paperall.html?noticeType=21&areaid=100000&noticeTitle=&regOrg=110000'

data = {
    # 'draw': '0',
    'start': '0',
    'length': '10'
}

# 准备请求头
headers = {
    'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_14_2) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/70.0.3538.110 Safari/537.36',
    # 'User-Agent': 'Mozilla/4.0 (compatible; MSIE 6.0; Windows NT 5.1; SV1; AcooBrowser; .NET CLR 1.1.4322; .NET CLR 2.0.50727)',
    # 'Referer': 'http://www.gsxt.gov.cn/corp-query-entprise-info-xxgg-100000.html',
    'Cookie': '__jsluid=fb0718dce34ccf53c4b94d15e9ab13d5; SECTOKEN=7178252594204902863; __jsl_clearance=1546475343.133|0|QZ7AOWMecndqD4CZG4hqoBAHtVw%3D;'
}

proxies = {
    'http':'http://110.52.235.85:9999'
}

response =  requests.post(url, data=data, headers=headers)
print(response.status_code)
print(response.content.decode())