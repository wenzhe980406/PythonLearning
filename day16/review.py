# _*_ coding : UTF-8 _*_
# 开发人员 : ChangYw
# 开发时间 : 2019/8/5 10:40
# 文件名称 : review.PY
# 开发工具 : PyCharm

# #何如判断是不是函数
# # from functools
# from inspect import isfunction
#
#
# # def addNum(f,a,b):
# #     print(isfunction(f))
# #     return f(a + b)
# f = ""
# print(isfunction(f))
#
# print(hasattr(f,'__call__'))
# print(callable(f))


# class A:
#     attr = 1
#     print(attr)
#
# a = A()
# a.attr = 5
# print(a.attr)
#
# b = A()
# print(b.attr)
a = 0
while True:
    a += 1
    print("a=",a)
    if a  == 100:
        break
else:
    print("111=",a)

print(a)
