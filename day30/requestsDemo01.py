# _*_ coding : UTF-8 _*_
# 开发人员 : ChangYw
# 开发时间 : 2019/8/23 10:57
# 文件名称 : requests.PY
# 开发工具 : PyCharm
import re

import requests
import json

# response = requests.get('https://www.baidu.com/')
# print(type(response))
# print(response.status_code)
# print(type(response.text))
# print(response.text)
# print(response.cookies)
# for cookie in response.cookies:
#     print(cookie)

# requests.post('http://httpbin.org/post')
# requests.put('http://httpbin.org/put')
# requests.delete('http://httpbin.org/delete')
# requests.head('http://httpbin.org/get')
# requests.options('http://httpbin.org/get')

# response = requests.get('http://httpbin.org/get')
# print(response.text)
#
# response = requests.get('http://httpbin.org/get?name=germey&age=22')
# print(response.text)

data = {
    "age": "22",
    "name": "germey"
  }
#
# response = requests.get('http://httpbin.org/get',params=data)
# print(response.text)


#解析json
# response = requests.get('http://httpbin.org/get')
# print(type(response.text))
# print(response.json())
# print(json.loads(response.text))
# print(type(response.json()))


#获取二进制数据
# response = requests.get('https://github.com/favicon.ico')
# # print(type(response.text),type(response.content))
# # print(response.text)
# # print(response.content)

# response = requests.get('https://github.com/favicon.ico')
# with open('favicon.ico','wb') as f:
#     f.write(response.content)
#
#
# response = requests.get('https://www.baidu.com/img/bd_logo1.png')
# with open('baidu1.png','wb') as f:
#     f.write(response.content)

# response = requests.get('https://www.zhihu.com/explore')
# print(response.text)


# Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/70.0.3538.25 Safari/537.36 Core/1.70.3722.400 QQBrowser/10.5.3776.400
headers = {
    'User-Agent':'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/70.0.3538.25 Safari/537.36 Core/1.70.3722.400 QQBrowser/10.5.3776.400'
}
# response = requests.get('https://www.zhihu.com/explore',headers=headers)
# print(response.text)

# response = requests.post('http://httpbin.org/post',data=data,headers=headers)
# print(response.text)
# print(response.json())
#
# response = requests.get('http://www.jianshu.com',headers=headers)
# print(type(response.status_code),response.status_code)
# print(type(response.headers),response.headers)
# print(type(response.cookies),response.cookies)
# print(type(response.url),response.url)
# print(type(response.history),response.history)

# response = requests.get('http://www.jianshu.com/hello.html',headers = headers)
# exit() if not response.status_code == requests.codes.not_found else print("404 not found")

# response = requests.get('http://www.jianshu.com/',headers = headers)
# exit() if not response.status_code == 200 else print("Request Successfully")

#会话维持 模拟登陆
# requests.get('http://httpbin.org/cookies/set/number/123456789')
# response = requests.get('http://httpbin.org/cookies')
# print(response.text)

# s = requests.Session()
# s.get('http://httpbin.org/cookies/set/password/123456789')
# response = s.get('http://httpbin.org/cookies')
# print(response.text)


# response = requests.get('https://www.13206.cn',headers=headers,data=data)
# print(response.status_code)
#
#
#
# proxies = {
#     "HTTP":"115.42.34.4:8088"
# }
#
# response = requests.get("https://wwww.taobao.com",proxies=proxies)
# print(response.status_code)



# #贪婪模式
# content = 'Hello 1234567 World_This is a Regex Demo'
# result = re.match('^He.*(\d+).*Demo$',content)
# print(result)
# print(result.group(1))
#
# #非贪婪模式
# content = 'Hello 1234567 World_This is a Regex Demo'
# result = re.match('^He.*?(\d+).*Demo$',content)
# print(result)
# print(result.group(1))
#
# content = '''Hello 1234567 World_This
# is a Regex Demo
# '''
# result = re.match('^He.*?(\d+).*?Demo$',content,re.S)
# print(result.group(1))

html = '''<div id="songs-list">
    <h2 class="title">经典老歌</h2>
    <p class="introduction">
        经典老歌列表
    </p>
    <ul id="list" class="list-group">
        <li data-view="2">一路上有你<>
        <li data-view="7">
            <a href="/2.mp3" singer="任贤齐">沧海一声笑</a>
        <>
        <li data-view="4" class="active">
            <a href="/3.mp3" singer="齐秦">往事随风</a>
        <>
        <li data-view="6"><a href="/4.mp3" singer="beyond">光辉岁月</a><>
        <li data-view="5"><a href="/5.mp3" singer="陈慧琳">记事本</a><>
        <li data-view="5">
            <a href="/6.mp3" singer="邓丽君"><i class="fa fa-user"></i>但愿人长久</a>
        </li>
    </ul>
</div>'''

# '<li.*?>\s*?(<a.*?>)?'

# result = re.search('<li.*?active.*?singer="(.*?)">(.*?)</a>',html,re.S)
# if result:
#     print(result.group(1),result.group(2))

# result = re.findall('<li.*?href="(.*?)".*?singer="(.*?)">(.*?)</a>',html,re.S)
# print(result)
# print(result[0],result[1],result[2])
#
# result = re.search('<li.*?singer="(.*?)">(.*?)</a>',html)
# print(result.group(1),result.group(2))


# results = re.findall('<li.*?>\s*?(<a.*?>)?(\w+)(</a>)?\s*?</li>',html,re.S)
# print(results)
# for result in results:
#     print(result[1])
#
# content = 'Extra stings Hello 1234567 World_This is a Regex Demo Extra stings'
# content = re.sub('\d+\s','',content)
# print(content)

# content = 'Extra stings Hello 1234567 World_This is a Regex Demo Extra stings'
# content = re.sub('(\d+)',r'\1 8910',content)
# print(content)
#
# html = re.sub('<a.*?>|</a>','',html)
# print(html)
# results = re.findall('<li.*?>(.*?)</li>',html,re.S)
# print(results)
# for result in results:
#     print(result.strip())


content = requests.get('https://book.douban.com/').text
# print(content)
# pattern = re.compile('<li.*?href="(.*?)">.*?alt="(.*?)".*?作者：(.*?).*?class="year">(.*?)</span></li>')
results = re.findall('<li.*?href="(.*?)">.*?alt="(.*?)".*?作者：(.*?).*?class="year">(.*?)</span></li>',html,re.S)
print(results)
for result in results:
    print(result.strip())
