# _*_ coding : UTF-8 _*_
# 开发人员 : ChangYw
# 开发时间 : 2019/8/22 15:40
# 文件名称 : urlibDemo01.PY
# 开发工具 : PyCharm
# Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/70.0.3538.25 Safari/537.36 Core/1.70.3722.400 QQBrowser/10.5.3776.400
import random
from urllib import request,parse,error
import urllib.request

proxy_list = [
        {"http": "114.88.53.19:53281"},
        {"http": "61.184.109.33:61320"},
        {"http": "121.69.37.6:9797"},
    ]

# resp = request.urlopen('http://www.jd.com')
#
# print(type(resp))
#
# print(dir(resp))
# # print(resp.text)
#
# print(resp.status,resp.url,resp.headers)
#
# text = resp.read()
# print(type(text))
# print(text.decode('utf-8'))

data = {
    "name" : "cyw",
    "age" : 21
}
#
# data = parse.urlencode(data)
# print(type(data))
# print(data)
#
# data1 = parse.parse_qs(data)
# print(data1)

# resp = request.urlopen('https://httpbin.org',data = data)
# print(resp.read().decode('utf-8'))

headers = {
    'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/76.0.3809.100 Safari/537.36',
    'Referer' :'https://www.baidu.com'
}

data = parse.urlencode(data).encode(encoding='utf-8')
try:
    req = request.Request('http://httpbin.org/post',headers=headers,data=data)
    resp = request.urlopen(req)
    print(resp.read().decode())
except error.HTTPError as e:
    print(e.code)
    print(e.name)
    print(e.msg)
except error.URLError as u:
    print(u.reason)
except Exception as e:
    print(e)
else:
    print("成功！")
