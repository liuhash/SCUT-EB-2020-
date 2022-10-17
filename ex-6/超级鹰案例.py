from selenium.webdriver import Chrome
from selenium.webdriver.common.by import By
web =Chrome()
web.get('http://www.chaojiying.com/user/login')
img1=web.find_element(By.XPATH,'')