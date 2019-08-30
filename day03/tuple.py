# _*_ coding : UTF-8 _*_
# 开发人员 : ChangYw
# 开发时间 : 2019/7/17 13:48
# 文件名称 : tuple.PY
# 开发工具 : PyCharm

#元组
#创建元组
# aTup = ()
# print(type(aTup))   #<class 'tuple'>
# aTup = (1,)
# print(type(aTup))
#
# #创建元组的第二种方式tuple()
# aTup = tuple()
# print(type(aTup))
#
#元组中的数据不能修改，但是变量是可以修改的
# aTup = tuple("ABCDEFGDR")
# print('s' in aTup)
# print(aTup)
# aTup = tuple("xxxxxxxxx")
# for i in aTup:
#     print(i)

#range
#range([start,]end[,step]) start    --默认值0  step    --默认值为0
#range也是一个可迭代的对象
# x = range(100)#左闭右开，顾头不顾尾
# print(x)
# print(type(x))
# aLst = list(x)
# aTup = tuple(x)
# print(aTup)

#元组中的内置元素
# tup1 = tuple(range(1,9))
# tup1 += tuple(range(23,78))
# print(tup1)
# print(len(tup1))
# print(max(tup1))
# print(min(tup1[ :30]))
#
# aLst = ['a','b','c','d']
# print(type(aLst))
#
# tup1 = tuple(aLst)
# print(type(tup1))

#
# aTup  = 1,2,3
# print(type(aTup))
# print(aTup)
#
# x, _ ,y = aTup
# print(x,y)
# print(aTup[0],aTup[2])


#ab相互赋值简单的算法
# a = 3
# b = 2
#
# # a = a + b
# # b = a - b
# # a = a - b
# # print(a,b)
#
# a , b = b , a
# print(a,b)

#count方法
# tup1 = tuple("AAAbbbbxxxxx")
# print(tup1.count("x"))

#内置函数#计算序列的长度、最大值和最小值
# num = [7,15,21,37,29,5,42,9,13]
# # print(len(num),max(num),min(num))
# print(sum(num))
# #sort sorted
# #list.sort() --就地排序
# #sorted(list) --生成排序列表
# print(sorted(num))
# aLst = list("TOM Jerry")
# bLst = sorted(aLst)
# print(aLst)
# print(bLst)
# #print(aLst.sort()) #结果：None
# aLst.sort()
# print(aLst)

