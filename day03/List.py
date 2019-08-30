# _*_ coding : UTF-8 _*_
# 开发人员 : ChangYw
# 开发时间 : 2019/7/17 10:04
# 文件名称 : List.PY
# 开发工具 : PyCharm

#split()
# aStr = "life is short , i need Python"
#                   #切割内容，几刀
# aList = aStr.split(None,3)
#
# print(aList)
#
# aList =aStr.split('is')
# print(aList)

#list操作
# aList1 = list("ABCDEFGH")
# print(aList1.count('X'))
# #//print(aList1.index('X'))
# print('H' in aList1)


# print(aList1)
# print(aList1[0:4])
# print(aList1[2:6])
# print(aList1[5:])
# print(aList1[-3:])
# print(aList1[::2])
# bLst = aList1[:]
# print(bLst)
#
# print(aList1[::-3])

#列表的删、改
# aLst = list("ABCDEFGH")
# bLst = [1,2,3,4,5]
# cLst = ['beijing','shanghai','guangzhou','shenzhen']
# aLst.append(bLst)
# aLst.append(cLst)
# # print(aLst)
#
# aLst[8].remove(3)
# aLst[9][2] = 'wuhan'
# print(aLst)

#列表的排序和反转
# aLst = [65,87,67,98,71,79,65,90]
# #排序有两种方式，一种就是就地排序，用的是列表方法，
# aLst.sort(reverse=True) #如果不用reverse，默认排序从低往高。有了reverse，就是反过来排序，从高往地排序
# print(aLst)
#
# #不希望就地排序，只是希望产生一个排序的列表副本
# bLst = sorted(aLst,reverse=True) #reverse如果没有就是默认排序，从低到高
# print(bLst)
# print(aLst)
#
# #反转列表的方法
# #通过切片的方式，产生一个反转的列表副本[::-1]
# #通过reverse方法反转
# aLst.reverse()
# print(aLst)

#列表的加、乘
# aLst = [1,2,3]
# print(aLst * 3)
# print(aLst + [2,3,5])
# print(1 in [1,2,3])

#for 循环     遍历     迭代       只要能在for循环中可以用的 都是可迭代对象
                                    #字符串，列表都是可迭代对象
# aLst = [65,87,67,98,71,79,65,90]
# for i in aLst : #i代表列表中的每一项内容都存放在i中
#     print(i,end=' ')

#字符串的拆分和拼接 join:把列表拼接乘字符串，可以指定拼接的连接符号
                #split:把字符串分割成列表，可以指定分割符号
import copy

aStr = "life is short,i need python"
# aLst = list(aStr)
# print(aLst)
# bStr = "".join(aLst)
# print(bStr)


# bLst = []
# for x in aStr :
#     if x.isalpha():
#         y = ord(x) + 3
#         bLst.append(chr(y))
#     else:
#         bLst.append(x)
# print("".join(bLst))

#列表的拷贝 --浅拷贝
aLst = [1.1,1.2,1.3]
bLst = [2.1,2.2,2.3]
bLst.append(aLst)
print(bLst)

#浅拷贝（常见
aLst_cpy = aLst[:] #aLst_cpy = aLst.copy()
bLst_cpy = bLst[:] #bLst_cpy = bLst.copy()
# bLst_cpy = copy.copy(bLst) #深拷贝

bLst_cpy = copy.deepcopy(bLst)

print(aLst_cpy)
print(bLst_cpy)
aLst[2] = 100.3
bLst[2] = 200.3

print(aLst)
print(aLst_cpy)
print(bLst)
print(bLst_cpy)