# _*_ coding : UTF-8 _*_
# 开发人员 : ChangYw
# 开发时间 : 2019/7/16 22:10
# 文件名称 : day02HomeWork.PY
# 开发工具 : PyCharm

#*7
# #1)
# print(ord('@'),ord('%'),ord('&'),ord('*'),ord('?'),ord(']'))
# #2)
# pythonWord = 'i love python'
# print(pythonWord.upper())
# print(pythonWord.capitalize())
# print(pythonWord.title())
# print(pythonWord.lower())
# #3)
# inputnumber = int(input("请输入数字"))
# if inputnumber > 33 and inputnumber < 125 :
#     print(inputnumber,'对应的字符为：',chr(inputnumber))
# else:
#     print("输入错误请重新输入")
#4)
# inputAmount = int(input('请输入要输出#的数量：'))
# print("{:*>30}".format('#' * inputAmount))

# #5)
# inputWord = input("请输入要转换的字符：")
# print(inputWord.upper())

#b = int(input("请输入要转换的字符"))
#if b >= 97 and b <= 122:
#   print(chr(b-32))

# #6)
# inputMovie = input("请输入电影名称：")
# print('您输入的电影名称为：',inputMovie)
# # inputScore = int(input("请输入您对",inputMovie,"这部电影的分数："))
# inputScore = int(input("请输入您对这部电影的分数："))
# print('您为《',inputMovie,"》电影的评价为：",inputScore,'分')

#7)

# #8)
# print("请您填写如下的验证码：")
# print("abcd")
# verificationCode = input("请您输入验证码")
#
# if verificationCode == 'abcd' :
#     print("验证码输入正确，您的验证码为：",verificationCode.upper())

#1
# a = '00010  00000 00010 00000 00001 01010'
# print("报道日期",a)
# list = a.split()
# print(list)
# print(int('00010',base=2))
# print(int('00000',base=2))
# print(int('00010',base=2))
# print(int('00000',base=2))
# print(int('00001',base=2))
# print(int('01010',base=2))


#2
# height = float(input("请输入身高：（单位：米）"))
# weight = float(input("请输入体重：（单位：公斤）"))
# print("您的身高为：",height,"您的体重为：",weight)
#
# BMI =weight / (height * height)
# print("您的BMI指数为：",BMI)

#3输入两个正整数a,b，分别计算这两个数的加减乘除，
# 以及整除数，余数，两个数的平方，立方，开方，开三次方。

# a = int(input('a:'))
# b = int(input('b:'))
# print('a+b=',a+b)
# print('a-b=',a-b)
# print('a*b=',a*b)
# print('（整除数）a/b',a/b)
# print('（余数）a%b',a%b)
# print('a^2',a*a,'b^2',b*b)
# print('a的开方：',a**(1/2),'b的开方：',b**(1/2))
# print('a的开三次方：',a**(1/3),'b的开三次方：',b**(1/3))

# #4
# PythonGrades = int(input('请输入Python成绩：'))
# EnglishGrades = int(input('请输入英语成绩：'))
# ClanguageGrades = int(input('请输入C语言成绩：'))
# avg = (PythonGrades + EnglishGrades + ClanguageGrades) / 3
# print("您的平均成绩为：",avg)

# #5 输入两个100内的整数，分别计算它们的“位与”，“位或”，“位亦或”，以及各自的“位取反”，并且输出。
# x = int(input("x："))
# y = int(input("y："))
# if x > 0 and x < 100 :
#     if y > 0 and y < 100 :
#         print("x & y",x & y)
#         print("x | y",x | y)
#         print("x ^ y",x ^ y)
#         print("~x",~x)
#         print("~y",~y)
#         print("x>>y",x>>y)
#         print("x<<y",x<<y)
#     else :
#         print("您输入的Y值不正确请重新输入")
# else :
#     print("您输入的Y值不正确请重新输入")

#6
# base_number =float(input("请输入一个底数："))
# index_number =float(input("请输入一个指数："))
# print("这个数的幂为：",base_number**index_number)

# #7
# petrol_money = int(input("请输入加油的钱数："))
# petrol_mileage = int(input("请输入运行的公里数："))
# petrol_avg_money = petrol_money / petrol_mileage
# print("您车辆油耗每公里花费为：",petrol_avg_money,"元")
# petrol_total_mileage = int(input("请输入车辆1年运行的公里数："))
# print("您的车辆一年的油费为：%d"%(petrol_avg_money * petrol_total_mileage),"元")

#8
# c = int(input("请输入C："))
# f = int(input("请输入F："))
# c = (f - 32) * 5 / 9
# f = (c * 9 / 5) + 32
# print("C转换为F：%d" %f)
# print("F转换为C：%d" %c)

# #9 格式string[start : end : step]
# str1 = input("请输入字符：")
# aLst = list(str1)
# new_str = int(input("请输入要替换的位置："))
# new_repalce = input("请输入要替换的字符：")
# aLst[new_str] = new_repalce
# str = "".join(aLst)
# print(str)
#

#10
# inputWord = input("请输入要判断的字符")
# print(inputWord.islower())