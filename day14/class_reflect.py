# _*_ coding : UTF-8 _*_
# 开发人员 : ChangYw
# 开发时间 : 2019/8/1 10:51
# 文件名称 : class_reflect.PY
# 开发工具 : PyCharm

# #反射 hasattr  getattr
#
# def not_define(self):
#     print("我也很迷茫啊。。。")
#
# class Person():
#     def __init__(self,name):
#         self.name = name
#
#     def walk(self):
#         print("%s走在乡间的小路上。"%(self.name))
#
#     def eat(self,food = "面包"):
#         print("%s正在吃%s"%(self.name,food))
#
#
#
#
# jiang = Person("jiang yizhong")
# cmd = input(">>:").strip()
#
# # if "walk" == cmd :
# #     jiang.walk()
#
# #hasattr(obj,字符串'method_str') -- 判断obj中是否定义了method_str这个字符串代表的方法
# if hasattr(jiang,cmd):
#     method = getattr(jiang,cmd)
#     print(type(method),method)
#     method()
# else:
#     setattr(jiang,"i dont know","cyw")
#     method = getattr(jiang,"i dont know")
#     method(jiang)


a = "abc"
print(type(str))

def walk(self):
    print("%s走在乡间的小路上"%self.name)
Foo = type("Foo",(object,),{"name":"chang yw","walk":walk})

print(type(Foo),Foo.__name__)
f = Foo()
print(f.walk())