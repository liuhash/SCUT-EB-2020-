from selenium import webdriver

options = webdriver.FirefoxOptions()
options.add_argument('--headless')
driver = webdriver.Firefox(firefox_options=options)
driver.get('https://blog.csdn.net/u014595589/')
print(driver.title)
driver.close()