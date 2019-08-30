# _*_ coding : UTF-8 _*_
# 开发人员 : ChangYw
# 开发时间 : 2019/8/6 10:57
# 文件名称 : collectionDemo2.PY
# 开发工具 : PyCharm

#返回一个新的命名元组实例，并将指定域替换为新的值 somenamedtuple._replace(**kwatgs)
from collections import namedtuple

from day16.collectionDemo1 import p, Point

p3 = p._replace(x = 33)
print(p,p3,sep = "\n -----------\n")

#列出命名元组的域名  somenamedtuple._fields
print(p._fields)

Color = namedtuple('Color','red green blue')
Pixel = namedtuple('Pixel',Point._fields + Color._fields)
print(Pixel(11, 22, 128, 255, 0))

print('------------')
#默认值的字典。 _fields_defaults
Account = namedtuple('Account',['type','balance'],defaults=[0])
print(Account._fields_defaults)
print(Account('premium'))
print(getattr(p,'x'))


# #一个命名元组是一个正常的Python类，它可以很容易的通过子类更改功能。
# class Point(namedtuple('Point',['x','y'])):
#     __slot___ = () #__slots__为一个空元组。通过阻止创建实例字典保持了较低的内存开销
#
#     @property
#     def hypot(self):
#         return (self.x ** 2 + self.y ** 2) ** 0.5
#
#     def __str__(self):
#         return 'Point: x =%6.3f y=%6.3f  hypot=%6.3f' % (self.x,self.y,self.hypot)
#
#
# for p in Point(3,4),Point(14,5/7):
#     print(p)


#默认值可以用 _replace()来实现，通过自定义一个原型实例：
Account = namedtuple('Account','owner balance transaction_count')
default_account = Account('<owner name>', 0.0,0)
johns_account = default_account._replace(owner='John')
janes_account = default_account._replace(owner='Jane')
print(johns_account,janes_account,sep='\n------------\n')


