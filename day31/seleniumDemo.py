# _*_ coding : UTF-8 _*_
# 开发人员 : ChangYw
# 开发时间 : 2019/8/26 17:11
# 文件名称 : seleniumDemo.PY
# 开发工具 : PyCharm

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait

browser = webdriver.Chrome()

#kw
try:
    browser.get("https://www.baidu.com")
    input = browser.find_element_by_id('kw')
    input.send_keys('Python')
    input.send_keys(Keys.ENTER)
    wait = WebDriverWait(browser,10)
    wait.until(EC.presence_of_element_loacted(By.ID,"content_left"))
    print(browser.current_url)
    print(browser.get_cookie())
    print(browser.page_source)
finally:
    browser.close()