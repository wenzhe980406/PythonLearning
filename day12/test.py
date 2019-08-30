# _*_ coding : UTF-8 _*_
# 开发人员 : ChangYw
# 开发时间 : 2019/7/30 11:18
# 文件名称 : test.PY
# 开发工具 : PyCharm
import time


# def time_sub(f) :
#     def inner() :
#         start_time = time.time()
#         f()
#         end_time = time.time()
#         print("%s 所用的时间为： %s"%(f.__name__,(end_time - start_time)))
#     return inner
#
#
# @time_sub
# def list_drive():
#     aLst = [i for i in range(10000000) if i % 2]
#     return aLst
#
#
# @time_sub
# def list_getNumber() :
#     aList  = []
#     for i in range(10000000) :
#         if i%2 == 0 :
#             aList.append(i)
#
#
# list_drive()
# list_getNumber()
#



alist = ['1','2','3','4','5','6','6','7','8','9']

next(alist)