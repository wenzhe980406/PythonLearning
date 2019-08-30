# _*_ coding : UTF-8 _*_
# 开发人员 : ChangYw
# 开发时间 : 2019/7/18 15:47
# 文件名称 : dict.PY
# 开发工具 : PyCharm

#字典     key -- value --键值对
#json 很类似 {key:value}
#字典的创建
# aDict = {
#     "name":"changyiwen",
#     "gender":"male",
#     "height": 185
# }
#
# print(type(aDict))
# print(aDict)

# bDict = dict()
# print(type(bDict))
#
# #增加key-value
# bDict["name"] = "changyiwen"
# bDict["gender"] = "male"
# bDict["age"] = 21
# bDict["height"] = 185
# # print(bDict)
#
# age = bDict.pop('age')
# print(age)
# # print(bDict)
# age = bDict.pop('age',100)
# print(age)
#
# #字典的key --不能重复，后面的会把前面的覆盖
# bDict["name"] = "zhangwei"
# print(bDict)

# 哪些数据类型可以作为字典的key
#不能修改的数据，可以作为字典的key，能修改的数据类型，不可以作为字典的key
#数值类型，字符串，元组是不可以修改的数据类型，可以作为字典的key
#列表，set是可以修改的数据类型，不能作为字典的key
# aDict = {
#     1:"编号",
#     "name":"tom",
#     ('a','b'):['a','b'],
#     'ef':('e','f')
# }
# print(aDict)
#
# #字典是可迭代的对象，迭代如下，打印的是字典的key
# for x in aDict:
#     print(x)
#
# #用len()来计算字典的长度，就是有多少个key
# print(len(aDict))
#
# print(str(aDict))

#字典的拷贝
#浅拷贝(copy)(deepcopy)

#fromkeys 用已经存在的可迭代对象，作为新的字典的key
# aLst = list("ABCDEF")
# aDict = dict.fromkeys(aLst)
# print(aDict)
#
# bDict = dict.fromkeys(aDict)
# print(bDict)
#
# cDict = dict.fromkeys("ABCDEF")
# print(cDict)

##最重要的几个字典的方法: keys(),values(),items()
aDict = {
    "name":"changyiwen",
    "gender":"male",
    "height": 185
}
print(type(aDict))
print(aDict)

print("keys = ",end=' ')
print(aDict.keys())
print("values = ",end=' ')
print(aDict.values())
print("items = ",end=' ')
print(aDict.items())

# #循环遍历
# for x in aDict:
#     print(x,end=" ")
#     print(aDict.get(x))     #aDict[x] = aDict.get(x)

#字典的get，setdefault
#如果key不存在，aDict['key']会报错
print(aDict.get("sex",'dont knew'))
#当我们给字典增加新的key和value时，如果直接用dict['key'] = value的方式，那么如果原来的字典中已经存在，就会覆盖。
#有时候我们不想覆盖，就用setdefault
aDict.setdefault("sex","male")
print(aDict)
aDict.setdefault("name","zhangwei")
print(aDict)
y=dict()
y.setdefault('a',1)
print("fdfdsfs",type(y.get('a')))
z="12ddfdsfs"
print(z[1],type(z[1]),int(z[1]),type(int(z[1])))
z.replace('2','123')
print(z,z[2]>z[3])

# d4 = {'Year': 2018, 'Month': 3, 'Day': 18}
# # 循环所有的key (或这么写：for item in d4.keys():)
# for item in d4:
#     print(item)
# 打印结果：
# Year
# Month
# Day
#
# # 循环所有的value
# for item in d4.values():
#     print(item)
# 打印结果：
# 2018
# 3
# 18
#
# # 循环所有的key：value
# for item in d4.keys():
#     print(item, ':', d4[item])
#
# for k, v in d4.items():  # 用items方法 k接收key ,v接收value
#     　　print(k, v)