import requests as rqs
import bs4
import re
import webbrowser
import time
import datetime
import random

# 失信url的合成
root_url = "https://shixin.tianyancha.com/"
search_target = "gs_" + "供应链"
search_target2 = "gs_" + "物流"
search_target3 = "gs_" + "电商"
search_target4 = "gs_" + "电子"
search_target5 = "gs_" + "空调"
divide_sign = "/"
operator = "search"
number_pane =5
start_pane = 1

url = root_url + operator + divide_sign + search_target + divide_sign + "p" + "{:d}"
url2 = root_url + operator + divide_sign + search_target2 + divide_sign + "p" + "{:d}"
url3 = root_url + operator + divide_sign + search_target3 + divide_sign + "p" + "{:d}"
url4 = root_url + operator + divide_sign + search_target4 + divide_sign + "p" + "{:d}"
url5 = root_url + operator + divide_sign + search_target5 + divide_sign + "p" + "{:d}"
#爬取的数据保存在什么文件里面
save_file_name = "shixin2.txt"
# 请求头的设立
headers = {
    'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/106.0.0.0 Safari/537.36',
    'cookie': 'HWWAFSESID=5d5697cf4b12cef1e9; HWWAFSESTIME=1666600310503; csrfToken=fWoKx4S7qqw3AdRDfUv7H37Z; TYCID=50036700537611edaa87b74af6f25341; ssuid=5030977400; sajssdk_2015_cross_new_user=1; sensorsdata2015jssdkcross=%7B%22distinct_id%22%3A%22184091ea980c3-0d8abdbddc77f-26021f51-1327104-184091ea981b2d%22%2C%22first_id%22%3A%22%22%2C%22props%22%3A%7B%22%24latest_traffic_source_type%22%3A%22%E7%9B%B4%E6%8E%A5%E6%B5%81%E9%87%8F%22%2C%22%24latest_search_keyword%22%3A%22%E6%9C%AA%E5%8F%96%E5%88%B0%E5%80%BC_%E7%9B%B4%E6%8E%A5%E6%89%93%E5%BC%80%22%2C%22%24latest_referrer%22%3A%22%22%7D%2C%22%24device_id%22%3A%22184091ea980c3-0d8abdbddc77f-26021f51-1327104-184091ea981b2d%22%7D; bannerFlag=true; Hm_lvt_2acec3d3ec1827cad3f546d97f1050a5=1666600317; token=482c158c06b64cfeb5542cb40b74fbe8; _utm=63938b3970614cafa7230946446d0af9; _ga=GA1.2.2052375872.1666600318; _gid=GA1.2.1334032379.1666600318; _gat_gtag_UA_123487620_1=1; tyc-user-info={%22anonymityLogo%22:%22https://static.tianyancha.com/design/anonymity/anonymity2.png%22%2C%22personalClaimType%22:%22none%22%2C%22explainPoint%22:%220%22%2C%22isValidEnterpriseVip%22:%220%22%2C%22onum%22:%220%22%2C%22companyName%22:%22%22%2C%22messageBubbleCount%22:%220%22%2C%22monitorUnreadCount%22:%220%22%2C%22yellowDiamondEndTime%22:%220%22%2C%22isShowClaimCompany%22:%220%22%2C%22signUp%22:%220%22%2C%22score%22:%220%22%2C%22integrity%22:%2230%25%22%2C%22scoreUnit%22:%22%22%2C%22myQuestionCount%22:%220%22%2C%22pleaseAnswerCount%22:%220%22%2C%22headPicUrl%22:%22https://cdn.tianyancha.com/design/avatar/v3/man3.png%22%2C%22claimPoint%22:%220%22%2C%22nickname%22:%22tycv9291994233%22%2C%22announcementPoint%22:%220%22%2C%22nicknameSup%22:%22%22%2C%22claimEditPoint%22:%220%22%2C%22state%22:%220%22%2C%22privateMessagePointWeb%22:%220%22%2C%22messageShowRedPoint%22:%220%22%2C%22riskManagement%22:{%22servicePhone%22:null%2C%22mobile%22:19927468536%2C%22title%22:null%2C%22currentStatus%22:null%2C%22lastStatus%22:null%2C%22quickReturn%22:false%2C%22oldVersionMessage%22:null%2C%22riskMessage%22:null}%2C%22realBossStatus%22:%222%22%2C%22vipManager%22:%220%22%2C%22originalScore%22:%220%22%2C%22redPoint%22:%220%22%2C%22privateMessagePoint%22:%220%22%2C%22vnum%22:%220%22%2C%22mobile%22:%2219927468536%22%2C%22myAnswerCount%22:%220%22%2C%22userId%22:%22298896701%22%2C%22token%22:%22eyJhbGciOiJIUzUxMiJ9.eyJzdWIiOiIxOTkyNzQ2ODUzNiIsImlhdCI6MTY2NjYwMDMzOSwiZXhwIjoxNjY5MTkyMzM5fQ.N4RcJ0rc5ECKYEzkbcC2JkA2pipxdPDe8V63E4-La6EDCrhG78ISvnscWLQqeKFL6QNkUJ4ITq349o5F73vfbQ%22%2C%22companyAuthStatus%22:%222%22%2C%22bossStatus%22:%222%22%2C%22showPost%22:%22%22%2C%22schoolAuthStatus%22:%222%22%2C%22showAnonymityName%22:%22%E5%8C%BF%E5%90%8D%E7%94%A8%E6%88%B711d0cd3d%22%2C%22isClaim%22:%220%22%2C%22companyGid%22:%22%22%2C%22discussCommendCount%22:%220%22%2C%22vipToMonth%22:%22false%22%2C%22claimCompanyStatus%22:%22%22%2C%22yellowDiamondStatus%22:%22-1%22%2C%22bizCardUnread%22:%220%22}; auth_token=eyJhbGciOiJIUzUxMiJ9.eyJzdWIiOiIxOTkyNzQ2ODUzNiIsImlhdCI6MTY2NjYwMDMzOSwiZXhwIjoxNjY5MTkyMzM5fQ.N4RcJ0rc5ECKYEzkbcC2JkA2pipxdPDe8V63E4-La6EDCrhG78ISvnscWLQqeKFL6QNkUJ4ITq349o5F73vfbQ; tyc-user-phone=%255B%252219927468536%2522%255D; Hm_lpvt_2acec3d3ec1827cad3f546d97f1050a5=1666600349'
}
session = rqs.Session()
print("爬取的网页为：", url)
# 该函数从指定的url中获得html代码，调用bs4库来解析
def getHtmlFromUrl(index_url):
    # 发送请求，并获得response
    response = session.get(index_url, headers=headers)

    time.sleep(random.randint(1, 5))
    # print(response.text)
    soup = bs4.BeautifulSoup(response.text, "lxml")
    results = soup.find_all("div", class_="result-item")
    for r in results:
    # result = soup.find_all("div", class_="detail")
        name = r.find("a", class_="name").text
        business_entity = r.find("span", class_="value").text
        card_nums = r.find_all("span",class_="value")
        card_num = card_nums[3].text
        age = '0'
        area = r.find("span",class_="site").text
        content = r.find("div",class_="results text-ellipsis").text
        publish_date = r.find("span",class_="result").text
        update_date = r.find("span",class_="result").text
        publish_units = r.find_all("span",class_="result")
        publish_unit  = publish_units[3].text

        curr_time = datetime.datetime.now();
        create_date = datetime.datetime.strftime(curr_time, '%Y-%m-%d %H:%M:%S')
        print(name,card_num,age,area,business_entity,content,publish_date,publish_unit,create_date,update_date)
    # result2 = soup.find_all("a", class_="site")
    print("url: "+index_url)
    if len(r) == 0:
        # 这里需要注意的是，如果在爬取的过程中发现返回的长度为0的话，说明网站在怀疑你是不是爬虫
        print("被识别为机器人")
        # 打开网页，输入验证码
        webbrowser.open(index_url)
        return None
    print(len(r))
    return r

save_file = "D:\pythonprojects\spiders\大作业\天眼查"+save_file_name
with open(save_file,'a',encoding="utf-8") as save_file:
    for i in range(start_pane,number_pane+1):
        result_list = getHtmlFromUrl(url.format(i))
        if result_list == None:
            # 输入验证码后，需要重新设置参数，继续爬取，参数在靠头
            raise Exception("请将start_pane参数修改为"+str(i))
        for k in result_list:
            # 写入文件
            save_file.write(k.text)
            save_file.write("\n")
    for i in range(start_pane, number_pane + 1):
        result_list = getHtmlFromUrl(url2.format(i))
        if result_list == None:
            # 输入验证码后，需要重新设置参数，继续爬取，参数在靠头
            raise Exception("请将start_pane参数修改为" + str(i))
        for k in result_list:
            # 写入文件
            save_file.write(k.text)
            save_file.write("\n")
    for i in range(start_pane, number_pane + 1):
        result_list = getHtmlFromUrl(url3.format(i))
        if result_list == None:
            # 输入验证码后，需要重新设置参数，继续爬取，参数在靠头
            raise Exception("请将start_pane参数修改为" + str(i))
        for k in result_list:
            # 写入文件
            save_file.write(k.text)
            save_file.write("\n")
    for i in range(start_pane, number_pane + 1):
        result_list = getHtmlFromUrl(url4.format(i))
        if result_list == None:
            # 输入验证码后，需要重新设置参数，继续爬取，参数在靠头
            raise Exception("请将start_pane参数修改为" + str(i))
        for k in result_list:
            # 写入文件
            save_file.write(k.text)
            save_file.write("\n")
    for i in range(start_pane, number_pane + 1):
        result_list = getHtmlFromUrl(url5.format(i))
        if result_list == None:
            # 输入验证码后，需要重新设置参数，继续爬取，参数在靠头
            raise Exception("请将start_pane参数修改为" + str(i))
        for k in result_list:
            # 写入文件
            save_file.write(k.text)
            save_file.write("\n")
    time.sleep(500)
print("爬取完成")
