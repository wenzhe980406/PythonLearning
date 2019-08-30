# _*_ coding : UTF-8 _*_
# 开发人员 : ChangYw
# 开发时间 : 2019/7/19 10:42
# 文件名称 : high.PY
# 开发工具 : PyCharm

#高级特性
#1.enumerate
#吧一个序列的索引值和对应的数值，拼成一个元组

# aLst = list(range(10))[::-1]
# print(aLst)
#
# x = enumerate(aLst)
# print(type(x))
#
# for i in x :
#     print(i)

#####
# bLst = ["苹果",5000,"华为",5888,"戴尔",4888,"康师傅",5,"汤达人",9.8]
# proc_list = []
# price_list = []
# for x in bLst:
#     if (bLst.index(x) % 2) :
#         price_list.append(x)
#     else:
#         proc_list.append(x)
# print(proc_list)
# print(price_list)
#
# for idx,proc in enumerate(proc_list) :
#     # print("%d \t%6s \t%0.02f"%(idx + 1,proc,price_list[idx]))
#     print(" {:<2} {:<5} {:<9}".format(idx + 1,proc,float(price_list[idx])))

# #zip 把多个列表的列重新组织起来
# studen_list = ["Chang","Zhang","Jiang","Liu","Wu","Shao"]
# subject_list = ["C","Java","Python","c++","Oracle"]
# score_list = [70,75,80,65,90,86,73,58]
#
# mix_zip= zip(studen_list,subject_list,studen_list)
# print(type(mix_zip))
#
# #zip访问过之后就没有了
# # for x in mix_zip:
# #     print(type((x),x),sep="\n")
# #
# # for student,subject,score in mix_zip :
# #     print(student,subject,score)
#
# mix_list = list(mix_zip)
# print(mix_list)
# #还原，注意的是，zip的参数，一定要是一个列表，并且列表的每个元素都是同样长度的元组
# x,y,z = zip(*mix_list)
# print(x,y,z,sep="\n")
#
#
# import random
# aLst = list(range(1,10))
# random.shuffle(aLst)
# print(aLst)
# #如果是就地排序的话
# # aLst.sort()
# bLst = sorted(aLst) #反序 bLst = sorted(aLst,reverse = True)
# print(bLst)

# #推导式
# #列表推导式
# rslt = [i for i in range(101) if (i % 2)]
# print(rslt)
#
# #计算100以内所有整数的平方
# aLst =[i**2 for i in range(101)]
# print(aLst)

# #字典推导式
# aDict = {
#     "zhangsan" : 70 ,
#     "lisi" : 58,
#     "wangwu" : 91,
#     "zhengliu" : 55,
#     "zhuqi" : 81
# }
# cLst = [i for i in aDict.values() if (i < 60)]
# print(cLst)

# for i in aDict.values() :
#     print(i)

# faild_student = { }
# for i in aDict:
#     if (aDict[i] < 60) :
#         faild_student[i] =aDict[i]
# print(type(faild_student),faild_student)
#
##推导式
# faild_student = {name:aDict[name] for name in aDict if (aDict[i] < 60)}

#嵌套推导式
import random

# java_list = [random.randint(40,100) for _ in range(10)]
print([_>3  for _ in range(10) ])
# python_list = [random.randint(40,100) for x in range(10)]

# faild_list = [score for subject in[java_list,python_list] for score in subject if score < 60]