# _*_ coding : UTF-8 _*_
# 开发人员 : ChangYw
# 开发时间 : 2019/7/18 16:51
# 文件名称 : day04HomeWork.PY
# 开发工具 : PyCharm
#1
# if __name__ == "__main__":
#     list1 = ['life','is','short']
#     list2 = ['you','need','python']
#     print(list2.index('python'))
#     list2.append('!')
#     list1.append(',')
#     list1.append(list2)
#     print(len(list1))
#     list2[2] = 'python3'
#     print(list2)
#     del list1[3]#pop remove
#     del list2[3]
#     print(list1,list2)

#2
# if __name__ == "__main__":
#     list1 = [1,2,3,16,17,23,29,40,41]
#     list2 = []
#     for i in list1 :
#         list2.append(str(i))
#     print(list2)
#     for n in list2:
#         print(n,end='')

# #3
# if __name__ == "__main__":
#     score = (68,87,92,100,76,88,54,89,76,61)
#     print(score[2])
#     print(score[1:7])
#     print(score.count(76))
#     print(score.index(100))
#     print(len(score))
#     lstScore = list(score)
#     tpScore = tuple(lstScore)
#     score1 = (80,61)
#     score2 = (71,95,82)
#     score3 = score1 + score2
#     print(score3)

# #4
# import random
#
# if __name__ == "__main__":
#     aLst = []
#     bLst = []
#     #A组数据
#     for i in range(10) :
#         b = random.randint(10,20)
#         aLst.append(b)
#     #B组数据
#     for i in range(10) :
#         b = random.randint(10,20)
#         bLst.append(b)
#     sumLst = aLst + bLst
#     # print(sumLst)
#     # print(aLst)
#     # print(bLst)
#
#     set_sumlist=set()
#     d=set()
#     for item in sumLst:
#         if( item in set_sumlist):
#             d.add(item)
#         else:
#             set_sumlist.add(item)
#
#     print("原来的数组:",sumLst)
#     print("去重:",set_sumlist)
#     print("重复的元素:",d)
#     print("重复的个数：",d.__len__())
#     print("不重复的元素:",set_sumlist-d)
#     print("不重复的个数:",(set_sumlist-d).__len__())
# #5
# if __name__ == "__main__" :
#     adict = {
#         "k1" : "v1",
#         "k2" : "v2",
#         "k3" : "v3",
#         "k4" : "v4",
#         "k5" : "v5",
#         "k6" : "v6"
#     }
#     #1)
#     for x in adict :
#         print(x,end=" ")
#     print()
#     #2)
#     for x in adict :
#         print(adict[x],end=" ")
#     print()
#     #3)
#     print("---------------------")
#     for x in adict :
#         print(x,end=" ")
#         print(adict[x])
#     #4)
#     adict["k7"] = "v7"
#     print(adict)
#     #5)
#     del adict["k1"]
#     print(adict)
#     #6)
#     del adict["k5"]
#     print(adict)
#     del adict["k5",None]
#     #7)
#     print(dict.get("k2"))
#6
# if __name__ == "__main__" :
#     a = "aAsmr3idd4bgs7Dlsf9eAF"
#     #1)
#     print(a.swapcase())
#     #2)
#     b = []
#     for i in a :
#         if(i.isdigit() == True) :
#             b.append(i)
#     c = ''.join(b)
#     print(c)
#     #3)
#     aDict = dict()
#     a=a.lower()
#     for s in range(0,len(a)):
#         if (None == aDict.get(a[s])) :
#             aDict.setdefault(a[s],1)
#         else:
#             y = aDict.get(a[s]) + 1
#             aDict[a[s]] = y
#     print(aDict)
#
#     #4)
#
#
#
#     l = set()
#     m =" "
#     for s in a :
#         if (s in l ) or s.isdigit():
#             continue
#         else:
#             l.add(s)
#             m += s
#     print("m..",m)
#
#     #5)
#     print(a[::-1])
    #6)
# from functools import cmp_to_key
# def mycmp(x, y):
#     if x == y:
#         return y > x
#     x = x.lower()
#     y = y.lower()
#     if x > y:
#         return 1
#     else:
#         return -1
#
#
# a = "aAsmr3idd4bgs7Dlsf9eAF"
# b = ""
# for i in a:
#     if not i.isdigit():
#         b += i
# a = list(b)
# print(a)
# a = sorted(a, key=cmp_to_key(mycmp))
# print(a)
# c = ''.join(a)
# print(c)

#     #7)
#
# #7
# if __name__ == "__main__" :
#     pswd = str(123456)
#     item = 0
#     while True:
#         pswd_input = input("请输入密码: ")
#         if ((not pswd_input.isdigit()) or (not len(pswd_input) == 6)) :
#             print("密码输入不正确，请输入6位数字密码！")
#             continue
#         else:
#             if (item == 2):
#                 print("您的卡将被锁死，请和发卡行联系。")
#                 break
#             if (not pswd_input == pswd) :
#                 print("密码输入错误，您已经输入了%d次"%(item+1))
#                 item += 1
#             elif(pswd_input == pswd):
#                 print("密码输入正确，正进入系统！")
#                 break
#7)
# a = "aAsmr3idd4bgs7Dlsf9eAF"
# b = 'boy'
#
# item = 0
# for i in b :
#     if (i in a) :
#         if i == b[b.__len__()-1] :
#             print("True")
#         continue
#     else:
#         print("Fasle")
#         break

#8)
# a = "aAsmr3idd4bgs7Dlsf9eAF"
# b = ['boy','girl','bird','dirty']
#
# item = 0
#
# for i in b :
#     for j in i :
#         if j in a :
#             if j == i[i.__len__()-1] :
#                 print("True")
#             continue
#         else:
#             print("Fasle")
#             break
#9)

#         if (None == aDict.get(a[s])) :
#             aDict.setdefault(a[s],1)
#         else:
#             y = aDict.get(a[s]) + 1
#             aDict[a[s]] = y
#     print(aDict)
a = "aAsmr3idd4bgs7Dlsf9eAF"
b = dict()
for i in a :
    if (None == b.get(i)) :
        b.setdefault(i,1)
    else:
        y = int(b.get(i))+ 1
        b[i] = y
print(b)
M = max(b.values())
print(M)
# print(list(b.keys())[list(b.values()).index(M)])
y = list(b.keys())
z =list(b.values())
print(y[z.index(M)])

#8
# if __name__ == "__main__" :
#     num = None
#     if num * 3

# #9) ???答案
# if __name__ == "__main__" :
#     finnal = 99
#     item = 0
#     i = 1
#     for i in range(1,99):
#         if (i % 7 == 0) :
#
#             item += 1
#         elif(i % 10 == 7) :
#
#             item += 1
#     print("拍腿%d次"%item)
