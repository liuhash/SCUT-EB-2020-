import requests
import json

cityName = input('请输入你想爬取的肯德基餐厅的城市: ')
url = "http://www.kfc.com.cn/kfccda/ashx/GetStoreList.ashx?op=keyword"
pageIndex = '1'
data = {
    'cname': '',
    'pid': '',
    'keyword': cityName,
    'pageIndex': pageIndex,
    'pageSize': '20'
}
headers = {
    'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64; rv:104.0) Gecko/20100101 Firefox/104.0'
}
try:
    data_list=[]
    print('肯德基在'+cityName)
    response = requests.post(url=url, data=data, headers=headers)
    json_data = response.json()['Table1']
    print(json_data)
    for j in json_data:
        if j['cityName']==cityName+"市":
            print(j["addressDetail"])
            data_list.append(j["addressDetail"])
    path =cityName + "KFC.txt"
    fp=open(path, 'w', encoding='utf-8')
    json.dump(json_data,fp=fp,ensure_ascii=False)
    with open(cityName+'pure_store.txt', 'w', encoding='utf-8') as file:
        file.write(str(data_list))
except IOError:
    print("写入异常！")