# _*_ coding : UTF-8 _*_
# 开发人员 : ChangYw
# 开发时间 : 2019/8/2 13:49
# 文件名称 : exception.PY
# 开发工具 : PyCharm

#
# aLst = [1,2,3]
# aDict = dict(namee = "zhangsan",age = 33)
# try:
#     # print(aLst[3])
#     # print(4/0)
#     # print(aDict["lisi"])
#     # print('i' + 1)
#     # print(i)
#     # with open("zw.txt") as f:
#     #     f.read()
#     # import cyw
#     pass
# except IndexError as I:
#     print(I)
# except ZeroDivisionError as Z:
#     print(Z)
# except KeyError as K:
#     print(K)
# except TypeError as T:
#     print(T)
# except NameError as N:
#     print(N)
# except IOError as I:
#     print(I)
# except FileNotFoundError as F:
#     print(F)
# except ImportError  as Im:
#     print(Im)
# else:
#     print("hhh")
# finally:
#     print("aaa")
# # aLst.append(4)
# # print(aLst[3])
#

# #else 的作用
# #finally一般处理资源的关闭。
# aLst = [1,2,3]
# try:
#     print(aLst[3])
#     a = 4 / 2
# except IndexError as e :
#     print(e)
#     print("处理列表的异常错误。")
# except Val

#
# class MyException(Exception):
#     def __init__(self,code,msg):
#         self.code = code
#         self.msg = msg
#         super().__init__(msg)
#
#     def __str__(self):
#         return "%d %s"%(self.code,self.msg)
#
#
#
# a = 12
# try:
#     if (a < 18) :
#         raise MyException("你好啊！")
# except KeyError as K:
#     print(K)
# except Exception as E:
#     print(E)



# import enum
#
# Season = enum.Enum('Season',("春","夏","秋","冬"))
#
# print(Season.冬.name)
# import enum
#
#
#
#
# class MyErrCode(enum.Enum):
#     TooYoung = 555
#     TooOld = 556
#     ExceedTime = 557
#
# print(MyErrCode.TooYoung.value)

from random import randint
print(randint(1,3))