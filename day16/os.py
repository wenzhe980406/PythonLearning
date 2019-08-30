# _*_ coding : UTF-8 _*_
# 开发人员 : ChangYw
# 开发时间 : 2019/8/5 14:38
# 文件名称 : os.PY
# 开发工具 : PyCharm
import os
#
# print(os.sep)
# print(os.name)
print(os.getcwd())
print(os.getenv("PYTHONPATH"))
# # print(os.putenv())
# print(os.listdir("E:\\PythonFile\\day16"))
print(os.stat("os.py"))
# print(os.path.split("/x/y/z/wmn"))
# print(os.path.isfile("/x/y/z/wuminna"))
# print(os.path.isfile("E:\\PythonFile\\day16\\review.py"))
#
# print(os.path.isdir("E:\\PythonFile\\day16"))
# print(os.curdir)
#
# print(os.stat("E:\\PythonFile\\day16\\review.py"))
# print(os.path.getsize("E:\\PythonFile\\day16\\review.py"))
#
# print(os.path.abspath("E:\\PythonFile\\day16\\review.py"))
#
# print(os.path.isabs("/x/y/z/wmn"))
# print(os.path.isabs("E:\\PythonFile\\day16\\review.py"))
# print(os.path.split("E:\\PythonFile\\day16\\review.py"))

# import sys
# print(sys.getdefaultencoding())
# print(sys.path)
# print(sys.stdin)
# print(sys.stdout.write("hello10000"))
# print(sys.stderr)

# import hashlib
# # ## #########256############
# # ## 1、造出hash工厂
# hash = hashlib.sha256("898oaFs09f".encode('utf-8'))
# print(hash)
# ##2、运送原材料
# hash.update('alvin'.encode('utf-8'))
# ##3、产出hash值
# print(hash.hexdigest())

# hash = hashlib.sha256('898oaFs09falvin'.encode('utf-8'))
# print(hash.hexdigest())


# m = hashlib.md5()
# m.update("aa425443786".encode("utf-8"))
# print(m.hexdigest())


# m = hashlib.md5("aa".encode("utf-8"))
# m.update("425443786".encode("utf-8"))
# print(m.hexdigest())


# #“无限”迭代器
# import itertools
# # count()会创建一个无限的迭代器，所以上述代码会打印出自然数序列，根本停不下来，只能按Crtl+C结束
# # count(start[,step])
#
# natuals = itertools.count(1)
# print(type(natuals))
# for n in natuals:
#     if n > 100 :
#         break
#     print(n)
#
#
# #cycle()会把传入的一个序列无限重复下去：
# cs = itertools.cycle('ABC') #注意字符串也是序列的一种
# count = 0
# for c in cs:
#     count += 1
#     print(c)
#     if (count > 100):
#         break
#
#
#
# #repeat()负责把一个元素无限重复下去，不过如果提供第二个参数就可以限定重复次数：
# ns = itertools.repeat("A",10)
# for n in ns:
#     print(n)
#
#
#
# # 无限序列虽然可以无限迭代下去，但是通常我们会通过takewhile()等函数根据条件判断来截取一个有限的序列：
# natuals = itertools.count(1)
# ns = itertools.takewhile(lambda x:x <= 10,natuals)
# for n in ns :
#     print(n)
#
#
# #chain()可以把一组迭代对象串联起来，形成一个更大的迭代器：
# # for c in itertools.chain("ABC","XYZ") :
# #     print(c)
#
#
# #groupby()把迭代器中相邻的重复元素挑出来放在一起：
# for key,group in itertools.groupby("aaabbbcccaa"):
#     print(key,list(group))
#
#
# # 实际上挑选规则是通过函数完成的，只要作用于函数的两个元素返回的值相等，这两个元素就被认为是在一组的，
# # 而函数返回值作为组的key。如果我们要忽略大小写分组，就可以让元素‘A’和‘a’都返回相同的key：
#
# for key,group in itertools.groupby('AaaBBbcCAAa',lambda c:c.upper()):
#     print(key,list(group))







