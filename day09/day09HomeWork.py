# _*_ coding : UTF-8 _*_
# 开发人员 : ChangYw
# 开发时间 : 2019/7/25 23:39
# 文件名称 : day09HomeWork.PY
# 开发工具 : PyCharm

#21)
# aStr = "I am a boy 1 2 ."
# aList = aStr.split()
# bList = [i for i in aList if i.isalpha()]
# bStr = ' '.join(bList[::-1])
# print(bStr)

#22)
# a = int(input("请输入一个正整数"))
# print(bin(a),bin(a).count("1"))

# #23)
# a = int(input("请输入a的值"))
# b = int(input("请输入b的值"))
# x , y = a , b
# while True :
#     c = a % b
#     if c == 0 :
#         c = b
#         break
#     else :
#         a ,b = b , c
# if c == 1:
#     print("最大公倍数为：",x * y)
# else:
#     print("最大公倍数为：",x if x > y else y)

# #24)
# numList = []
# while True :
#     i = input("请输入任意个整型数，按Q退出")
#     if "Q" == i.upper():
#         break
#     numList.append(int(i))
# a = 0
# avglen = 0
# avg = 0
# for i in range(len(numList)) :
#     if numList[i] < 0 :
#         a += 1
#     else:
#         avg += numList[i]
#         avglen += 1
# print("负数有%d个"%a)
# print("平均值为：",avg/avglen)

#25)
# aDict = {}
# a = input("请输入想要输入的字符串")
# aList = list(a)
# aSet = set(aList)
# bList = list(aSet)
# aDict = aDict.fromkeys(bList,0)
# for i in bList :
#     aDict[i] = aList.count(i)
# cTup = ((k,v) for k,v in aDict.items())
# b = sorted(cTup,key=lambda k:k[1],reverse=True)
# d = ''.join([i[0] for i in b])
# print(d)

# #26)
# a = 0
# n = 10000
# count = 0
# for i in range(1,n+1):
#     if str(i) == str(i**2)[(len(str(i)) * -1):] :
#         count += 1
#         print(i,i**2,end="\t\n")
# print()
# print("count:",count)

# #27)
# a = "sasd51dsaf15a"
# aLst = []
# for i in a :
#     "*" + i + "*" if i.isdigit() else aLst.append(i)
# print(''.join(aLst))
#
# #28)
# num = input("请输入候选人的人数： ")
# name = input("请输入候选人的姓名： ")
# voteNum = input("请输入投票人的人数： ")
# vote = input("请输入投票：")

#29)
a = '123456asd1234aasd654987'
aLst = list(a)
bLst = []
x = 0
for i in range(len(aLst)):
    if aLst[i].isalpha() :
        bLst.append(aLst[x:i-1])
        x = i
    if aLst[i].isdigit():
        bLst.append(aLst[x:i])
        x = i
print(bLst)

# #30)
a = input("输入一个长的字符串")
b = input("输入一个短的字符串")
a = set(a)
b = set(b)
c = a .intersection(b)
if len(c) == len(b) :
    print("短字符串全在长字符串中。")