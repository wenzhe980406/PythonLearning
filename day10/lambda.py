# _*_ coding : UTF-8 _*_
# 开发人员 : ChangYw
# 开发时间 : 2019/7/26 16:25
# 文件名称 : lambda.PY
# 开发工具 : PyCharm

#匿名函数
#因为函数最好是功能单一，所以有很多函数其实非常简单，采用匿名函数非常适合
#因为匿名函数没有名字，所以不能重复利用。

# def max(a,b) :
#     return a if a >= b else b
#
# max(5,6)
#
# max(-5,9)
#
# m = lambda a,b :a if a >=b else b
#
# n = lambda a,b :(a+b)/2
#
# print(n(2,5))
#
# #高阶函数  函数作为另外我一个函数的参数，或者函数作为另外一个函数的返回值
# #函数作为另外一个函数的参数
#
# def oper_math(f,a,b) :
#     return f(a,b)
#
# def add_f(a,b) :
#     return a + b
#
# def sub_f(a,b) :
#     return a - b
#
# def mul_f(a,b) :
#     return a * b
#
# def div_f(a,b) :
#     return a / b
#
# fun_list = [add_f,sub_f,mul_f,div_f]
#
# a = int(input("请输入一个数："))
# b = int(input("请输入另外一个数："))
# for f in fun_list:
#     print(type(f))
#     print(f)
#     print(oper_math(f,a,b))
#
#
# #查看函数的本质
# def foo():
#     print("IN FOO")
#
# print(foo)
# g = foo
# print(g)
# g()

#test
# a = "$98 7.123"
# def fun(f,a):
#     return f(a)
#
# def del_symbol(a):
#     return a.replace("$","")
#
# def del_space(a):
#     return a.replace(" ","")
#
# func = [del_symbol,del_space]
#
# for i in func:
#     a = fun(i,a)
# print(a)

# #函数还可以作为返回值
# def foo():
#     print("in foo")
# def goo():
#     print("in goo")
#     return foo
#
# # print(goo())
# goo()()

#lambda 在排序中的使用
lst = ["C","C++","C#","Pascal","Vb","Java","Python","R"]
# def sort_by_length(item) :
#     return len(item)
# sorted(lst,key= sort_by_length)

lst1 = sorted(lst,key=lambda x:x[-1])
print(lst1)