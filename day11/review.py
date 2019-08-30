# _*_ coding : UTF-8 _*_
# 开发人员 : ChangYw
# 开发时间 : 2019/7/29 11:27
# 文件名称 : review.PY
# 开发工具 : PyCharm
import datetime
import time


# #时间time,datetime
# #三种方式表示时间
# t = time.localtime() #结构化时间 是个元组 有九个元素
# print(t)
# print(t.tm_year,t.tm_yday)
#
# #第二种方式表示时间 --时间戳
# print(time.time(1347892345))
# print(time.localtime(1347892345))
#
# #字符串表示时间
# print(time.mktime())
# print(time.localtime(1561371117))
#
# t2012 = time.localtime(1347892345)
# print(t2012)
# print(time.strftime("%Y:%m:%d %H:%M:%S"),t2012)
#
time_str = "2017:07:21 14:14:14"
print(time.strptime(time_str,"%Y:%m:%d %H:%M:%S"))
print(time.mktime(time.strptime(time_str,"%Y:%m:%d %H:%M:%S")))
#
# before3day = datetime.datetime.today() + datetime.timedelta(-3)
# print(before3day)


#
# import re
#
# pattern = r"\((?P<areaName>\d{3,4})\) (?P<tel>\d{7,8})"
# aStr = """
#     (010) 45362767
#     (021) 89723098
#     (027) 98634213
#     (0515) 85055736
#     (0372) 6734098
# """
# # match = re.search(pattern,aStr)
# # print(match)
# # findall = re.findall(pattern,aStr)
# # print(findall)
#
# groupdict = re.search(pattern,aStr)
# print(groupdict.groupdict())
#
# sub = re.sub(pattern,"\g<areaName>-\g<tel>",aStr)
# print(sub)


#json,pickle
#把对象序列化成字符串 --dumps
# import json
# import pickle
# import random
#
# data = {
#     "name":"cyw",
#     "age" :21
# }
# #
# #把字典转成字符串 用dumps
# with open("demo1.json","w",encoding="utf-8") as w :
#     aStr = json.dumps(data)
#     print(aStr,type(aStr))
#     w.write(aStr)
#
# with open("demo1.json","r",encoding="utf-8") as r :
#     cyw = json.loads(r.read())
#     print(cyw)
#
# #dump和load
# with open("demo2.json","w",encoding="utf-8") as w :
#     json.dump(data,w)
#
# with open("demo2.json","r",encoding="utf-8") as r :
#     cyw = json.load(r)
#     print(cyw)
#
# with open("demo3.pkl","wb")as w :
#     pickle.dump(data,w)
#
# with open("demo3.pkl","rb")as r :
#     cyw = pickle.load(r)
#     print(cyw)

# #函数
# def total_score(*scores) :
#     sum = 0
#     for i in scores:
#         sum += i
#     return sum
#
# tup = (random.randint(40,100) for _ in range(20))
# total = total_score(*tup)
# print(total)
#
# def show_info(name,**kwargs) :
#     print("%4s的信息显示如下："%name)
#     for k,v in kwargs.items() :
#         print("%10s --> %20s"%(k,v))
# cyw_info = {
#     "height" : 175 ,
#     "weight" : 105 ,
#     "glasses" : "baodao"
# }
# show_info("常译文",height = 175,weight = 105,glasses = "baodao")
# show_info("常译文",**cyw_info)


# sum = [lambda x:x**2 for i in range(100)]
# print(sum)

# num = 20
# def grandpa():
#     num = 15
#     def father():
#         num = 10
#         def son() :
#             num = 5
#             print("num = ",num)
#         son()
#     father()
#
#
# print(grandpa())

# scores = {
#     "c" :{#期中30%，期末50%，平时20%
#         "cyw" : [65,75,50],
#         "zw" :  [68,78,62],
#         "jyz" : [61,89,30],
#         "wmn" : [63,70,90],
#         "ljd" : [85,88,93],
#         "szk" : [79,82,80]
#      },
#     "java" : {
#         "cyw" : [75,85,80],
#         "zw" :  [78,78,70],
#         "jyz" : [71,96,70],
#         "wmn" : [73,80,65],
#         "ljd" : [75,78,63],
#         "szk" : [74,88,70]
#     },
#     "python" :{
#         "cyw" : [85,95,85],
#         "zw" :  [82,79,92],
#         "jyz" : [91,73,84],
#         "wmn" : [93,92,98],
#         "ljd" : [75,98,93],
#         "szk" : [69,87,70]
#     }
# }
# #3门功课的总成绩排行，从高到低
# def rank(project):
#     rank_list = []
#     for i in scores[project] :
#         scores[project][i].append(int(scores[project][i][0]*0.3+scores[project][i][1]*0.5+scores[project][i][2]*0.2))
#         rank_list += [scores[project][i]]
#     print("{:^8} {:^8} {:^8} {:^8}".format
#           ( "期中成绩", "期末成绩", "平时分","总成绩",))
#
#     rank_list = sorted(rank_list,key=lambda x:x[3])
#
#     for i in range(len(rank_list)):
#         print("{:^10} {:^10} {:^12} {:^12}".format
#               (rank_list[i][0], rank_list[i][1], rank_list[i][2], rank_list[i][3]))
#     return rank_list
# c_rank = rank("c")
# java_rank = rank("java")
# python_rank = rank("python")
# #3门功课的平时，期中，期末平均分
# def rank_avg():
#     adict = {}
#     rank_list = []
#     for i in scores :
#         pass
#



#3门功课的期中，期末，平时的排名






