from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options

if __name__ == '__main__':
    # 加载谷歌浏览器驱动
    chrome_options = Options()

    # linux下运行记得加上这些参数 ----------------------------
    # chrome_options.add_argument('--headless')
    # chrome_options.add_argument('--no-sandbox')
    # chrome_options.add_argument('--disable-gpu')
    # chrome_options.add_argument('--disable-dev-shm-usage')
    # -----------------------------------------------------

    # 加载chromedriver -------------------------------------------------
    # windows 下的 chromedriver 默认加载路径是当前路径下的 chromedriver.exe
    # linux 下的 chromedriver 默认加载路径是 /usr/bin/chromedriver
    # 当然也可以通过 executable_path 自定义
    driver = webdriver.Chrome(options=chrome_options)
    # -----------------------------------------------------------------

    # 打开百度首页
    driver.get('https://www.baidu.com/')

    # 获取百度导航栏中的文本
    xp = '//*[@id="s-top-left"]/a'
    nav_list = [elm.get_attribute('text') for elm in driver.find_elements(by=By.XPATH, value=xp)]
    print(nav_list)
    # ['新闻', 'hao123', '地图', '贴吧', '视频', '图片', '网盘']
