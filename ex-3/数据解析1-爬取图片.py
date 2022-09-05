import requests
headers = {
    'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64; rv:104.0) Gecko/20100101 Firefox/104.0'
}
url1="https://gimg2.baidu.com/image_search/src=http%3A%2F%2Fimg1.duote.com%2Fduoteimg%2Fdtnew_newsup_img%2F202109%2F20210918174558_54566.jpeg&refer=http%3A%2F%2Fimg1.duote.com&app=2002&size=f9999,10000&q=a80&n=0&g=0n&fmt=auto?sec=1664951194&t=909ea759b9ed34af50bf4ade1440e0f2"
resq=requests.get(url=url1,headers=headers)
img_data=resq.content
resq.close()
with open('mid_autumn.jpg','wb') as fp:
    fp.write(img_data)