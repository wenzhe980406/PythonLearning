# _*_ coding : UTF-8 _*_
# 开发人员 : ChangYw
# 开发时间 : 2019/8/23 16:25
# 文件名称 : xpathDemo01.PY
# 开发工具 : PyCharm
from lxml import etree


parse = etree.HTMLParser(encoding = 'utf-8')
html = etree.parse("tencent.html",parser=parse)

# print(type(html))
# print(html)
# print(etree.tostring(html,encoding = 'utf-8').decode('utf-8'))


#1 获取所有的tr标签
#xpath命令 //tr
# trs = html.xpath("//tr")
# for i in trs:
#     print(etree.tostring(i,encoding = 'utf-8').decode('utf-8'))

#2 获取第2个tr标签
# tr = html.xpath("//tr[2]")[0]
# print(etree.tostring(tr,encoding = 'utf-8').decode('utf-8'))

#3 获取第3个class等于even的标签
# tr = html.xpath('//tr[@class="even"][3]')[0]
# print(etree.tostring(tr,encoding = 'utf-8').decode('utf-8'))

#4 获取所有a标签的href属性
# tr = html.xpath('//a/@href')
# for i in tr :
#     print(i)
#     break
#5 获取所有的职位信息（纯文本）
# trs = html.xpath('//tr/td/a/text()')
# print(type(trs))
# print(trs)
# # for tr in trs:
# #     print(etree.tostring(tr,encoding = 'utf-8').decode('utf-8'))

trs = html.xpath('//tr[position()>1 and @class!="f"]')

for tr in trs:
    plink = tr.xpath('.//a/@href')[0]
    pname = tr.xpath('.//a/@href')[0]
    pcate = tr.xpath('.//a/@href')[0]
    pnum = tr.xpath('.//a/@href')[0]
    plocation = tr.xpath('.//a/@href')[0]
    pdate = tr.xpath('.//a/@href')[0]

    positon = {
        'link' : plink,
        'title' : pname,
        'category' : pcate,
        'number' :pnum,
        'location' : plocation,
        'pub date' : pdate
    }