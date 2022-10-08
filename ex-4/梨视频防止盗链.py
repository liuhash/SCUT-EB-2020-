import requests

url1="https://www.pearvideo.com/video_1723156"

url2="https://www.pearvideo.com/videoStatus.jsp?contId=1723156&mrd=0.6052657320136278"
headers={
    'user-agent':'Mozilla/5.0 (X11; Linux x86_64; rv:104.0) Gecko/20100101 Firefox/104.0',
    'Referer':url1
}
real_url_split='cont-'+url1.split("_")[-1]
session=requests.session()
resp1=session.get(url=url2,headers=headers)
json1=resp1.json()
print(json1)
fake_url=json1['videoInfo']['videos']['srcUrl']


