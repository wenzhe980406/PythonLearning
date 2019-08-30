# _*_ coding : UTF-8 _*_
# 开发人员 : ChangYw
# 开发时间 : 2019/8/6 15:59
# 文件名称 : shelveDemo1.PY
# 开发工具 : PyCharm

import shelve

s = shelve.open("shelveTest.db")
try:
    s['kk'] = {'int': 10, 'float': 9.5, 'String': 'Sample date'}
    s['MM'] = [1,2,3]
finally:
    s.close()

try:
    s = shelve.open("shelveTest.db")
    value = s['kk']
    print(value)
    print(value.get('float'))
finally:
    s.close()

#writeback:默认为False，当设置为True以后，shelf将会从DB中读取的对象存放到一个内存缓存。
#当我们close()打开的shelf的时候，缓存中所有的对象会被重新写入DB

s = shelve.open('shelveTest.db',flag="w",writeback=True)
try:
    #增加
    s['QQQ'] = 2333
    #删除
    s['kk'] = {}
finally:
    s.close()


class Person:
    def __init__(self,name,age):
        self.__name = name
        self.__age = age

    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self,name):
        self.__name = name

    @property
    def age(self):
        return self.__age

    @age.setter
    def age(self,age):
        self.__age = age

try:
    s = shelve.open('shelveTest.db')
    chang = s['chang']
    zhang = s['zhang']
    print(chang.name,chang.age)
    print(zhang.name,chang.age)
finally:
    s.close()