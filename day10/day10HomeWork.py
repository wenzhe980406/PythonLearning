# _*_ coding : UTF-8 _*_
# 开发人员 : ChangYw
# 开发时间 : 2019/7/27 16:07
# 文件名称 : day10HomeWork.PY
# 开发工具 : PyCharm

#31)
# a = input("请输入一个字符串")
# b = input("请输入另外一个字符串")
# aSet = set(a)
# bSet = set(b)
# print(len(aSet.intersection(bSet)))

# #32)
# a = 'fahdjkhfdjakblvafds23643'
# bSet = set(a)
# aDict={}
# aLst = []
# aDict = aDict.fromkeys(a,0)
# for i in range(len(a)) :
#     aDict[a[i]] += 1
# aDict1 = aDict.copy()
# b = min(aDict.values())
# for k,v in aDict1.items():
#     if v == b :
#         aDict.pop(k)
# print(aDict)

# 33)
# a = "word!in@!#$your heart!hjs@ai&&&dsa!"
# m = 0
# n = 0
# aLst = []
# a += '!'
# for i in a :
#     n+=1
#     if not i.isalpha():
#         aLst.append(a[m:n-1])
#         m = n
# space = aLst.count("")
# for _ in range(space) :
#     aLst.remove('')
# bLst = [i[::-1] for i in aLst]
# b = ' '.join(bLst)
# print(b)
#34)
# nLst = []
# while True:
#     a  = input("请输入整数：按Q退出")
#     if "Q" == a.upper() :
#         break
#     a = int(a)
#     nLst.append(a)
# k = input("请输入你想得到多少个最小的数：")
# nLst = sorted(nLst)
# for i in range(k):
#     print(nLst[i])

#35)
# a = input("请输入字符串")
# for i in range(len(a)) :
#     if a.count(a[i]) == 1 :
#         print("第一个在字符串中只出现一次的字符为：",a[i])
#         break

# #36)
# #素数
# a = input("请输入一个偶数")
# num=[]
# prime_num = []
# for i in range(3,a):
#    for j in range(2,i):
#       if(i%j==0):
#          break
#    else:
#       num.append(i)
# print(num)
# for i in range(len(num)) :
#     for j in range(len(num)) :
#         if num[i] + num[j] == a and num[i] - num[j] > 0:
#             prime_num.append([num[i],num[j]])
#
# prime_sub = [i[0]-i[1] for i in prime_num]
# print("差值最小的素数对为：",prime_num[prime_sub.index(min(prime_sub))])

#37)
# a ="GCATTAGACGT"
# DNA = ['A','C','G','T']
# c_num = 0
# g_num = 0
# for i in a :
#     if i == "c" :
#         c_num += 1
#     elif i == "G" :
#         g_num += 1
# GC_Ratio = (c_num + g_num) / len(a)
# 38)
n = int(input("请输入您所拥有的空瓶子数量"))
d = 0
while True :
    n -= 3
    d += 1
    n += 1
    if n == 2:
        d += 1
        break
    elif n == 1 or n == 0:
        break
print(d)

#39)
# astr = 0
# num = 0
# Astr = 0
# symbol = 0
# while True:
#     pswd = input("请输入你的密码")#Asndwjunj123!~
#     if len(pswd) < 8 :
#         print("输入的密码少于8位，请重新输入")
#         continue
#     pswd_list = [i for i in pswd]
#     for i in pswd_list :
#         if ord(i) >= 97 and ord(i) <= 122:#小写字母
#             astr += 1
#             continue
#         elif ord(i) >= 65 and ord(i) <= 90:#大写字母
#             Astr += 1
#             continue
#         elif ord(i) >= 48 and ord(i) <= 57:#数字
#             num += 1
#             continue
#         elif (ord(i) >= 32 and ord(i) <= 47) or (ord(i) >= 58 and ord(i) <= 64) :#大写字母
#             symbol += 1
#             continue
#     if astr >= 1 :
#         astr = 1
#     if Astr >= 1:
#         Astr = 1
#     if num >= 1:
#         num = 1
#     if symbol >= 1:
#         symbol = 1
#     if (astr + Astr + num + symbol) <= 3:
#         print("密码复杂度不高，请重新输入")
#         break
#     bLst = [pswd[i:i+2] for i in range(len(pswd))]
#     for i in range(len(bLst)):
#         for j in range(i):
#             if bLst[i] == bLst[j]:
#                 print("您输入的字符串中含有重复的，请重新输入")
#     print("密码验证成功！")
#     break


#40)
# answer = {
#     2 : [97,98,99],
#     3 : [100,101,102],
#     4 : [103,104,105],
#     5 : [106,107,108],
#     6 : [109,110,111],
#     7 : [112,113,114,115],
#     8 : [116,117,118],
#     9 : [119,120,121,122]
# }
# a = input("请输入一串字符：")
# aLst = list(a)
# for i in range(len(aLst)) :
#     if aLst[i].isalpha():
#         for k, v in answer.items():
#             b = ord(str(aLst[i]))
#             if b in v:
#                 aLst[i] = str(k)
# for i in range(len(aLst)) :
#     if ord(aLst[i]) >= 65 and ord(aLst[i]) <90 :
#         aLst[i] = str(chr(ord(aLst[i]) + 33))
#     elif ord(aLst[i]) == 90 :
#         aLst[i] = str(chr(97))
# print(aLst)

# #41)
# import random
# def sum_name(name) :
#     sum = 0
#     for i in range(len(name)):
#         sum += aDict[name[i]]
#     return sum
# a = [chr(97+i) for i in range(26)]
# aDict = {}
# random_num = [i for i in range(1,27)]
# random.shuffle(random_num)
# aDict = aDict.fromkeys(a,0)
# for i in range(len(aDict)):
#     aDict[chr(97 + i)] = random_num[i]
# print(aDict)
#
# name1 = "nike"
# name2 = "Weston"
# print(sum_name(name1))
# print(sum_name(name2))
