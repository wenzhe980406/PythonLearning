# _*_ coding : UTF-8 _*_
# 开发人员 : ChangYw
# 开发时间 : 2019/8/26 14:06
# 文件名称 : 51job爬.PY
# 开发工具 : PyCharm
import csv

import requests
from lxml import etree
from bs4 import BeautifulSoup

baseUrl = "https://search.51job.com/list/020000,000000,0000,00,9,99,python,2,"
endUrl = ".html"


# def get_doubanNowPLaying(url):
#     ua_list = [
#         'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/76.0.3809.100 Safari/537.36'
#     ]
#     user_agent = ua_list
#     headers = {
#         "User-Agent": user_agent
#     }
#
#     r = requests.get(url)
#     print(r.encoding)
#     etree.HTML(r.content.decode(r.encoding))

def get_a_page(url,encoding = 'utf-8'):
    r = requests.get(url,encoding)
    return etree.HTML(r.content.decode(encoding=encoding))

def parse_a_page_bs(html):
    soup = BeautifulSoup(html,'lxml')
    etList = soup.select("div.el")[16:]
    for et in etList:
        detail = et.select('p.t1 a')[0]['href']
        company_url = et.select("span.t2 a")[0]['href']
        info_list = list(et.stripped_strings)
        if (len(info_list) < 5):
            info_list[3] == None

def parse_a_page(htmlStr):
    html = etree.HTML(htmlStr)
    etList = (etree.ElementTree(x) for x in html.xpath('//div[@id="resultList"]/div[@class="el"]'))
    for et in etList:
        detail = et.xpath('/div/p[@class="t1"]/span/a/@href')
        title = et.xpath('/div/p[@class="t1"]/span/a/@title')
        company = et.xpath('/div/span[@class="t2"]/a/text()')
        company_url = et.xpath('/div/span[@class="t2"]/span/a/@href')
        place = et.xpath('/div/span[@class="t3"]/text()')
        salary = et.xpath('/div/span[@class="t4"]/text()')
        pubtime = et.xpath('/div/span[@class="t5"]/text()')
        etree.tostring(et,encoding='utf-8').decode('utf-8')
        yield map(lambda x:x[0] if x else None,(detail,title,company_url,company,place,salary,pubtime))


def writeCsv(file,data,mode='a',encoding='utf-8'):
    with open(file,mode=mode,encoding=encoding,newline="") as f:
        writer = csv.writer(f)
        writer.writerow(data) if "w" == mode else writer.writerow(data)
        f.close()


def writeCsvHeader(file):
    data = ("职位详情","职位","公司网站","公司","工作地方","薪资","发布时间")
    writeCsv(file,data=data,mode="w",encoding = "gbk")


def get_page_url(page):
    return baseUrl+ str(page) + endUrl

def main():
    html = get_a_page(get_page_url(1),encoding='gbk')
    for position in parse_a_page(html):
        print(tuple(position))

if __name__ == '__main__':
    main()