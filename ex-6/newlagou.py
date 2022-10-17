import time, csv
from lxml import etree
from selenium import webdriver
from selenium.webdriver.common.by import By

# 创建文件并打开
# fp = open('拉勾网.csv', 'a', newline='', encoding='utf-8')
# writer = csv.writer(fp)
# writer.writerow(('职位名称', '公司名称','工资及地区','相关信息','详情','工作特点'))

lagou_url = "https://www.lagou.com/"

#载入已下载好的驱动程序
# 实例化浏览器对象
driver = webdriver.Chrome()
driver.get(lagou_url) #打开网页
driver.find_element(By.XPATH,'/html/body/div[10]/div[1]/div[2]/div[2]/div[1]/div/p[1]/a').click() #点击全国站

#通过ID定位搜索框标签
search_input = driver.find_element(By.ID,'search_input')
#标签交互-输入内容
search_input.send_keys('python')
time.sleep(2)
#通过ID定位搜索标签并且点击"搜索"
driver.find_element(By.ID,'search_button').click()
time.sleep(1)

# 提取信息
def spider_text():
    #直接获取网页
    source = driver.page_source
    # print (source)
    #解析获取的网页内容
    html_page = etree.HTML(source)
    #查找存放数据的位置，进行数据提取
    # 提取信息
    for item in html_page.xpath('//*[@class="item__10RTO"]'):
        job = item.xpath('//div[starts-with(@class,"p-top")]/a/text()')
        salary = item.xpath('//span[starts-with(@class,"money")]/text()')
        print(job, salary)
        # print("没找到！")

        # job_name = item.xpath('./div[1]/div[1]/div[1]/div[1]/div[1]/a/text')
        # company = item.xpath('./div[1]/div[1]/div[1]/div[2]/div[1]/a/text')
        # job_price = item.xpath('./div[1]/div[1]/div[1]/div[1]/div[2]/span/text')
        # detail = item.xpath('./div[1]/div[1]/div[2]/div[1]/span/text')
        # features = item.xpath('./div[1]/div[1]/div[2]/div[2]/text')
        # 写入数据
        # print(job_name,company,job_price,detail,features)
        # writer.writerow((job_name,company,job_price,detail,features))

def main():
    while True:
        spider_text()
        next_btn = driver.find_element(By.CLASS_NAME, 'lg-pagination-next')
        # next_link=driver.find_element(By.XPATH, '//*[@id="jobList"]/div[3]/ul/li[9]/a')
        end = next_btn.get_attribute("aria-disabled")
        # end是str类型，需转换,把我麻烦的批爆。false文字转是True类型。试了1h。气死我了。
        # print(end)
        if end == "false":
            # print("click事件触发")
            next_btn.click()
        else:
            break
        time.sleep(2)
    
#程序入口
if __name__ =='__main__':
    main()
    print('爬取完毕')
# fp.close()  # 关闭文件