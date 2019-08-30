# _*_ coding : UTF-8 _*_
# 开发人员 : ChangYw
# 开发时间 : 2019/8/27 11:03
# 文件名称 : taobaoDemo.PY
# 开发工具 : PyCharm

import re
import pymongo
from selenium import  webdriver
from selenium.webdriver.common.by import By

from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException

from bs4 import BeautifulSoup

URL = "https://www.taobao.com"
SUBJ = '美食'

MONGO_URL = 'localhost'
MONGO_DB = 'taobao'
MONGO_TABLE = 'meishi'

brower = webdriver.Chrome()
wait = WebDriverWait(brower,10)

def search():
    try:
        brower.get(URL)
        input = wait.until(EC.presence_of_element_located(
            (By.CSS_SELECTOR,"#q")
        ))
        submit = wait.until(EC.element_to_be_clickable(
            (By.CSS_SELECTOR, "#J_TSearchForm > div.search-button > button")
        ))
        input.send_keys(SUBJ)
        submit.click()

        total = wait.until(EC.presence_of_element_located(
            (By.CSS_SELECTOR, "mainsrp-pager > div > div > div > div.total")
        ))
        get_product()
        return total.text
    except TimeoutException:
        search()

def next_page(num):
    try:
        input = wait.until(EC.presence_of_element_located(
            (By.CSS_SELECTOR, "mainsrp-pager > div > div > div > div.form > input")
        ))
        submit = wait.until(EC.element_to_be_clickable(
            (By.CSS_SELECTOR, "mainsrp-pager > div > div > div > div.form > span.btn.J_Submit")
        ))
        input.clear()
        input.send_keys(num)
        submit.click()

        wait.until(EC.text_to_be_present_in_element(
            (By.CSS_SELECTOR, "mainsrp-pager > div > div > div > ul > li.item.active > span"),
            str(num)
        ))
    except TimeoutException:
        next_page(num)

def get_product():
    input = wait.until(EC.presence_of_element_located(
        (By.CSS_SELECTOR, "mainsrp-itemlist .items .item")
    ))
    html = brower.page_source
    soup = BeautifulSoup(html,'lxml')
    items = soup.select("mainsrp-itemlist .items .item")
    for item in items:
        imgurl = item.select(".pic .img").attr['href']
        print(imgurl)
        break



def main():
    totalStr = search()
    total = int(re.search('(\d+)',totalStr).group(1))
    for i in range(2,total + 1):
        next_page(i)


if __name__ == '__main__':
    main()