# _*_ coding : UTF-8 _*_
# 开发人员 : ChangYw
# 开发时间 : 2019/9/10 20:16
# 文件名称 : getPM2.5.PY
# 开发工具 : PyCharm

import requests
import lxml
from lxml import etree

BASE_URL = 'https://www.aqistudy.cn/historydata/monthdata.php?city=%E5%8C%97%E4%BA%AC&month='
HEADERS = {
    'User-Agent' : 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:69.0) Gecko/20100101 Firefox/69.0'
}

#//tbody

def get_a_page(url,header,encoding):
    response = requests.get(url,headers=header)
    return response.content.decode(encoding=encoding)
    # html = etree.HTML(response.content.decode('UTF-8'))
    # uls = html.xpath("//table/tbody/tr")
    # # trs = uls.xpath("/tr")
    # for tr in uls :
    #     print(etree.tostring(tr,encoding='UTF-8').decode('UTF-8'))



def main():
    get_a_page(BASE_URL,header=HEADERS,encoding='utf-8')

if __name__ == '__main__':
    main()
