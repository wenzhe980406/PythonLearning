# _*_ coding : UTF-8 _*_
# 开发人员 : longyh
# 开发时间 : 2019/8/27 9:54
# 文件名称 : lagouDemo001.PY
# 开发工具 : PyCharm

import requests
import json

HOME_URL =  "https://www.lagou.com/jobs/list_python?labelWords=&fromSearch=true&suginput="

POSITION_URL = "https://www.lagou.com/jobs/positionAjax.json?city=%E4%B8%8A%E6%B5%B7&needAddtionalResult=false"

headers1 = {
    "User-Agent": "Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/76.0.3809.100 Safari/537.36",
}

headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/76.0.3809.100 Safari/537.36",
    "Referer": "https://www.lagou.com/jobs/list_python?labelWords=&fromSearch=true&suginput="
}

data = {
    "first": "true",
    "pn": 2,
    "kd": "java"
}

def get_cookies(session,url):
    print(url)
    response = session.get(url, headers=headers1)
    return response.cookies

def get_a_page(url, base_url):
    session = requests.Session()
    cookies = get_cookies(session,base_url)
    resp = session.post(url=url, data=data, headers=headers, cookies=cookies)
    return resp.text

def parse_a_page():
    info_json = get_a_page(POSITION_URL, HOME_URL)
    infos = json.loads(info_json)
    posts = infos.get('content').get('positionResult').get('result')

    for position in posts:
        print(position)

def main():
    parse_a_page()

if __name__ == '__main__':
    main()


