from concurrent.futures import ThreadPoolExecutor
import requests
import csv

headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/103.0.5060.114 Safari/537.36 Edg/103.0.1264.62'
}


def download_url(page):
    url1 = "http://www.xinfadi.com.cn/getPriceData.html"
    data1 = {
        'limit': '20',
        'current': page
    }
    resp = requests.post(url=url1, data=data1, headers=headers)
    page_json = resp.json()
    print(page_json)
    resp.close()
    fp1 = open('xinfadi.csv', 'a', encoding='utf-8')
    csv1 = csv.writer(fp1)
    for item in page_json['list']:
        csv1.writerow(item.values())
    fp1.close()
    print(page, '页下载完毕')


def main():
    with ThreadPoolExecutor(10) as t:
        for i in range(2, 200):
            t.submit(download_url, f'{i}')
        print("Finished")


main()