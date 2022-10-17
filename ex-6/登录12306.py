from time import sleep

from selenium.webdriver import Chrome
from selenium.webdriver.common.by import By
import random
web=Chrome()
web.get('https://kyfw.12306.cn/otn/resources/login.html')
sleep(random.randint(1,5))
web.find_element(By.XPATH,'//*[@id="J-userName"]').send_keys()
web.find_element(By.XPATH,'//*[@id="J-password"]').send_keys()
web.find_element(By.XPATH,'//*[@id="J-login"]').click()
