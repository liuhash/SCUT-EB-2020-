import time, csv
from lxml import etree
from selenium import webdriver
from selenium.webdriver.common.by import By

# 创建文件并打开
fp = open('拉勾网.csv', 'a', newline='', encoding='utf-8')
writer = csv.writer(fp)
writer.writerow(('职位名称', '薪资'))

lagou_url = "https://www.lagou.com/"

# 创建一个浏览器
driver = webdriver.Chrome()
driver.get(lagou_url)  # 打开网页
driver.find_element(By.XPATH,'//*[@id="changeCityBox"]/p[1]/a').click()  # 点击全国站

search = driver.find_element(By.ID,'search_input')  # 搜索框
search.send_keys('python 爬虫')  # 发送内容
time.sleep(2)
driver.find_element(By.ID,'search_button').click()
time.sleep(1)
# driver.find_element(By.XPATH,'/html/body/div[8]/div/div[2]').click()  # 点击关闭红包


# 提取信息
def spider_text():
    source = driver.page_source  # 获取该网页源码
    html_page = etree.HTML(source)
    # 数组元素这块就麻烦你了，自己寻找xpath。也可以多写几个属性。因为页面在变化。xpath也在变化。
    #以及，驱动使用chrome的可能会比较好一些。我本机chrome调试可以进行正常的页面跳转。
    for item in html_page.xpath('//*[@id="s_position_list"]/ul/li'):
        job = item.xpath('./div[1]/div[1]/div[1]/a/h3/text()')
        salary = item.xpath('./div[1]/div[1]/div[2]/div/span/text()')
        print(job, salary)
        # 写入数据
        writer.writerow((job, salary))


# 翻页爬取
def main():
    while True:
        spider_text()
        next_btn = driver.find_element(By.CLASS_NAME, 'lg-pagination-next')
        # next_link=driver.find_element(By.XPATH, '//*[@id="jobList"]/div[3]/ul/li[9]/a')
        end=next_btn.get_attribute("aria-disabled")
        # end是str类型，需转换,把我麻烦的批爆。false文字转是True类型。试了1h。气死我了。
        # print(end)
        if end=="false":
            # print("click事件触发")
            next_btn.click()
        else:
            break
        time.sleep(2)
# 程序入口
if __name__ == '__main__':
    main()
fp.close()  # 关闭文件
