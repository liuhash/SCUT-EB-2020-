# 不要在开头引入乱七八糟的东西！
import time, csv
from lxml import etree
from selenium import webdriver
from selenium.webdriver.common.by import By
from pandas import DataFrame

res = []
# 创建文件并打开
# fp = open('拉勾网.csv', 'w', newline='', encoding='gbk')
# writer = csv.writer(fp)

lagou_url = "https://www.lagou.com/"

# 载入已下载好的驱动程序
# 实例化浏览器对象
driver = webdriver.Chrome()
driver.get(lagou_url)  # 打开网页
driver.find_element(By.XPATH, '/html/body/div[10]/div[1]/div[2]/div[2]/div[1]/div/p[1]/a').click()  # 点击全国站

# 通过ID定位搜索框标签
search_input = driver.find_element(By.ID, 'search_input')
# 标签交互-输入内容
search_input.send_keys('python')
time.sleep(2)
# 通过ID定位搜索标签并且点击"搜索"
driver.find_element(By.ID, 'search_button').click()
time.sleep(1)


# 提取信息
def spider_text():
    # 直接获取网页
    source = driver.page_source
    # 解析获取的网页内容
    html_page = etree.HTML(source)
    time.sleep(3)
    # 查找存放数据的位置，进行数据提取
    for item in html_page.xpath('//*[@class="item__10RTO"]'):
        # print(list(item))
        job_name = item.xpath('//div[starts-with(@class,"p-top")]/a/text()')
        company = item.xpath('//div[starts-with(@class,"company-name")]/a/text()')
        industry = item.xpath('//div[starts-with(@class,"industry")]/text()')
        job_price = item.xpath('//span[starts-with(@class,"money")]/text()')
        detail = item.xpath('//div[starts-with(@class,"il")]/text()')
        # 写入数据
        # writer.writerows((job_name,company,industry,job_price,detail))
        for i in range(len(job_name)):
            res.append([job_name[i], company[i], industry[i], job_price[i], detail[i]])
        break


def main():
    # 翻页爬取
    while True:
        spider_text()
        next_btn = driver.find_element(By.CLASS_NAME, 'lg-pagination-next')
        # next_link=driver.find_element(By.XPATH, '//*[@id="jobList"]/div[3]/ul/li[9]/a')
        end = next_btn.get_attribute("aria-disabled")
        # print(end)
        if end == "false":
            # print("click事件触发")
            next_btn.click()
        else:
            break
        time.sleep(2)


# 程序入口
if __name__ == '__main__':
    try:
        main()
    finally:
        df = DataFrame(res)
        # print(df)
        df.to_csv('拉勾网.csv')
        print('爬取完毕')

# fp.close()  # 关闭文件
