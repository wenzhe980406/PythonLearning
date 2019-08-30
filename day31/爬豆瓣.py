# _*_ coding : UTF-8 _*_
# 开发人员 : ChangYw
# 开发时间 : 2019/8/26 10:30
# 文件名称 : 爬豆瓣.PY
# 开发工具 : PyCharm
import requests
from lxml import etree


def get_doubanNowPLaying(url):
    ua_list = [
        'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/76.0.3809.100 Safari/537.36'
    ]
    user_agent = ua_list
    headers = {
        "User-Agent": user_agent
    }

    r = requests.get(url)
    print(r.encoding)
    etree.HTML(r.content.decode(r.encoding))










    tr_list = html.xpath('//ul[@class="lists"]')
    list_data = []
    for tr in tr_list:
        name = tr.xpath('./li[@data-title]')
        score = tr.xpath('./li[@data-score]')
        region = tr.xpath('/li[@data-region]')
        actors = tr.xpath('/li[@data-actors]')
        img_src = tr.xpath('/li//a[@img]')
        dict_data = {
            "name" : name,
            "score" : score,
            "region" : region,
            "actors" : actors,
            "img_scr" : img_src
        }
        list_data.append(dict_data)
    json_data = json.dumps(list_data)

    with open('douban.json',"w",encoding="utf-8") as o:
        o.write(json_data)


def main():
    url =  "https://movie.douban.com/cinema/nowplaying/shanghai/"
    get_doubanNowPLaying(url)


if __name__ == '__main__':
    main()