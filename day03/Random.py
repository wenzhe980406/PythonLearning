# _*_ coding : UTF-8 _*_
# 开发人员 : ChangYw
# 开发时间 : 2019/7/17 16:25
# 文件名称 : Random.PY
# 开发工具 : PyCharm

#要使用随机数，必须先导入随机数模块
#import random
import random

#1 产生一个[1,0)之间的随机数
# a = random.random()
# print(a)

#2 产生一个[a,b]范围内的随机整数（a，b为整数） dandint():
# for i in range(10) :
#     b = random.randint(1, 10)
#     print(b)

#3 产生一个[f1,f2)范围内的随机浮点数。(f1,f2浮点数) uniform()
# for i in range(10) :
#     b = random.randint(1.0, 2.0)
#     print(b)
#
#4 重新随机排列随机数据shuffle(list) ---乱序
# aLst = list(range(10))
# print(aLst)
# random.shuffle(aLst)
# print(aLst)

# 5 从序列中随机选择n个不重复选择的元素sample(seq,n):
aLst = list("ABCDEFGHIJKLMN")
for i in range(10):
    choice_list = random.sample(aLst,3)
    print(type(choice_list),choice_list)

# #6 从序列中随机选择一个 choice() 选择几个：choices()
# colors = ["red","yellow","bluee","orange"]
# for _ in range(10):
#     color = random.choice(colors)
#     print(color)


#7 扑克牌
# aLst = list("AAAA22223333444455556666777788889999++++JJJJQQQQKKKKwW")
# for i in range(3):
#     choice_list = random.sample(aLst,17)
#     print(choice_list.)