# _*_ coding : UTF-8 _*_
# 开发人员 : ChangYw
# 开发时间 : 2019/8/5 16:34
# 文件名称 : collectionDemo1.PY
# 开发工具 : PyCharm
from collections import namedtuple
'''
collections是Python内建的一个集合模块，提供了许多有用的集合类
'''

'''
#namedtuple -- 我们用namedtuple可以很方便的定义一种数据类型，它具备tuplee的不变性，又可以根据属性来引用，使用十分方便
collections
'''


# Student = namedtuple("Student",["name","age","gender","email"])
# zhangsan = Student("zhangsan",21,"male","zs@163.com")
# print(zhangsan)
# print(zhangsan.name,zhangsan.age,zhangsan.gender)
# print(type(zhangsan))
#
# for x in zhangsan:
#     print(x)
#

Point = namedtuple('Point',['x','y'])
# p1 = Point(1,2)
# p2 = Point(2,3)
# print(p1.x,p1.y,p2.x,p2.y)

#
p = Point(11,y = 22)  #instantiate with positional or keyword arguments
# print(p[0] + p[1])    #indexblee like the plain tuple(11,22)
# x,y =p                #unpack like a regular tuple
# print(x,y)
# print(p.x,p.y)        #fields also accessible by name
# print(p)              #readable __repr__ with a name = value style

#classmethod somenamedtuple._make(iterable)
t = [11,22]
print(Point._make(t))

#和字典的转换 somenamedtuple._asdict()
aDict = p._asdict()
print(type(aDict))
print(aDict)

#字典转换成命名元组  要将字典转换为命名元组，请使用**运算符
d = {"x":11 ,"y":22}
print(Point(**d))