# _*_ coding : UTF-8 _*_
# 开发人员 : ChangYw
# 开发时间 : 2019/7/29 16:18
# 文件名称 : def_high.PY
# 开发工具 : PyCharm

#
# #高阶函数filter
import random
#
# aLst = [random.randint(-10,10) for _ in range(20)]
#
# # def isPositive(num):
# #     return True if num > 0 else False
#
# aLst = list(filter(lambda x : x > 0,aLst))
# print(aLst)

# #高阶函数map
# #f(x) = 2x + 5
#
# def foo(x):
#     return 2 * x + 5
#
# x = [random.randint(-10,10) for _ in range(20)]
# print(x)
# y = list(map(lambda x : 2 * x + 5 , x ))
# print(y)

# #reduce
import time
# from functools import reduce
#
# # def addNum(a,b) :
# #     return a + b
# #
# # aTup = (12,56,-16,-10,78,27,32,56)
# # totla = reduce(lambda a , b : a + b , aTup)
# # print(totla)
#
#
# alst = [i for i in range(1,9)]
# totla = reduce(lambda a,b : (a * 10 + b),alst)
# print(totla)

#装饰器 ：让函数具有更多的功能
#1 不能修改函数
#2 不能改变函数的调用方法
#3
# def generateList():
#     rslt = []
#     for i in range(10000):
#         if (not i % 2):
#             rslt.append(i)
#     print(len(rslt),rslt[0],rslt[-1])
#     return rslt
#
# def deriveList():
#     rslt = [x for x in range(10000) if (not x % 2)]
#     print(len(rslt), rslt[0], rslt[-1])
#     return rslt

# generateList()
# deriveList()


# def count_time(f):
#     start_time = time.time()
#     f()
#     end_time = time.time()
#     print("count time : %s"%(end_time - start_time))
#
#
# count_time(generateList)
# count_time(deriveList)

# def log_func(f):
#     print("准备运行%s"%(f.__name__))
#     return f

# generateList = log_func(generateList)
# generateList()


def count_time(f):
    def deco():
        start_time = time.time()
        f()
        end_time = time.time()
        print("count time : %s" % (end_time - start_time))

    return deco
#
#
# @count_time   #generateList = count_time(generateList)
# def generateList():
#     rslt = []
#     for i in range(10000):
#         if (not i % 2):
#             rslt.append(i)
#     print(len(rslt),rslt[0],rslt[-1])
#     return rslt
#
# @count_time   #deriveList = count_time(deriveList)
# def deriveList():
#     rslt = [x for x in range(10000) if (not x % 2)]
#     print(len(rslt), rslt[0], rslt[-1])
#     return rslt
#
#
# generateList()

@count_time
def aaaa():
    relst = []
    for i in range(10000):
        if not i % 2:
            relst.append(i)
    print(len(relst),relst[0],relst[-1])
    return relst

aaaa()