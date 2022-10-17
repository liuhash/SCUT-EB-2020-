from time import sleep

from selenium.webdriver import Chrome
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select
from selenium.webdriver.chrome.webdriver import Options
opt=Options()
opt.add_argument('--headless')
web=Chrome(options=opt)
web.get("https://www.endata.com.cn/BoxOffice/BO/Year/index.html")
sleep(1)
year_item=web.find_element(By.XPATH,'//*[@id="OptionDate"]')
year_list=Select(year_item)
for i in range(len(year_list.options)):
    year=year_list.select_by_index(i)
    table = web.find_element(By.XPATH,'//*[@id="TableList"]/table')
    print(table.text)
    print('+++++++++++++++++++++++++++')
web.close()
