# _*_ coding : UTF-8 _*_
# 开发人员 : ChangYw
# 开发时间 : 2019/7/15 14:57
# 文件名称 : 算数运算符.PY
# 开发工具 : PyCharm


# a = 10 + 20
# b = 10 - 20
# c = 10 * 20
# d = 10 / 20
# e = 10 // 20
# f = 10 % 20
# g = 10 ** 2
#
# print(a,b,c,d,e,f,g)
#
#
# print(8**7)
# print(7**8)
#
# a = 10
# b = 29
#
# print(a and b)
# print(a or b)
# print(not a)
# print(not b)
# print('a & b',a & b)
# print('a | b',a | b)
# print('a ^ b',a ^ b)
# print('~ a',~ a)
# print('~ b',~ b)
#
# print(8>>2)
#
# print(type(5))
# print(type(5.5))
# print(type(true))
# print(type(True))
# print(type(4+3j))

a = '10101011'
b = int(a)
print(b)
c = int(a,base=2)   #2就是让a当做二进制
print(c)
#
# print('this is a string.')
# print('this is a string')
# print('I told my friend,"Python is my favorite language!"')
# print('The language "Python" is named after Monty python,not the snake.')

print('\ti test tab')
print('今天\n不高兴。')
print('今天要讲\"的作用')
print('如果要用到\\，那么需要两个。')

a = 100
b = 'Python'
c = 'good good study,day day up!'
# # print(a,'\n',b,'\n',c)
# #
print(a,end=" ")
print(b,end=" ")
print(c,end=" ")
#
print(a,b,c,sep="|")
print(a,b,c,sep="\n")


bytes
cStr = '天安门'
cBytes = bytes(cStr,encoding="UTF8")
print(cBytes)

cStr = '天安门'
cBytes = bytes(cStr,encoding="gbk")
print(cBytes)

cStr = '天安门'
cBytes = bytes(cStr,encoding="unicode_escape")
print(cBytes)

cBytes = cStr.encode("gbk")
print(cBytes)
#
# cStr = cBytes.decode("utf-8")
# print(cStr)

money = input('请输入金额：')
#
# print(ord('@'))

# a = '\u9AD8\u5C71\u6D41\u6C34\u9047\u77E5\u97F3'
#
# print(a.encode("utf-8").decode('unicode_escape'))