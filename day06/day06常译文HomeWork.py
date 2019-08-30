# _*_ coding : UTF-8 _*_
# 开发人员 : ChangYw
# 开发时间 : 2019/7/22 17:24
# 文件名称 : day06HomeWork.PY
# 开发工具 : PyCharm

# #1
# peach = 1
# for i in range(1,10)  :
#     peach = (peach + 1) * 2
# print(peach)
#
# 2
# jia =['a','b','c']
# yi = ['x','y','z']
# alist = []
# list_new = []
# for i in jia :
#     for j in yi :
#         if i == 'a' and j == 'x':
#             continue
#         elif i in list_new:
#             break
#         if i in list_new:
#             break
#         if i == 'c' and (j == 'x'or  j =='z') :
#             continue
#         # for x in range(len(jia) - 1) :
#         #     if i in alist[x] :
#         #         break
#         list_new = [i,j]
#         alist.append(list_new)
# print(alist)

#3 2/1，3/2，5/3，8/5，13/8，21/13
#分子：1    2      3    5    7
# #分母：1    1      2    3    5
# a = 2
# b = 1
# math_list = list()
# for i in range(20) :
#     math_list.append((a / b))
#     a , b= a + b , a
# print(sum(math_list))

# #4
# #阶乘的方法
# def jiecheng(n) :
#     if n == 1 :
#         return 1
#     else:
#         return n*jiecheng(n-1)
# sum_list = []
# for i in range(1,20) :
#     j = jiecheng(i)
#     print(type(j),j)
#     sum_list.append(j)
# print(sum(sum_list))


# #5
# num = input("给定一个不多于5位的正整数：")
# if num > '9999' or len(num) >= 5:
#     print("输入错误,请重新输入！")
#     exit(0)
# print("你输入的列表长度：",len(num))
# num = list(num)
# num.sort(reverse=True)
# print(num)

# #6
# # S = input("请输入你需要的移位值：")
# s = 25
# # decode_ago = ord('I')
# # if decode_ago < 114 :
# #     decode_ago = ord('I') + s - 1
# #     while decode_ago  >=  114
# decode_ago = ord('Z') + s - 1
# print(decode_ago)
# while decode_ago >= 122 :
#     if decode_ago >= 122 :
#         decode_ago -= 25
# print(chr(decode_ago))
# print(ord('a'),ord('z'),chr(114))

#7string.split(sep, maxsplit)

#8 Z:90 A:65   join的对象只能是列表
#  z:122 a:97
# #生成A-Z 字母表存在Alist
# import random
# #
# list_A = [chr(i) for i in range(ord('A'),ord('Z') + 1)]
# list_a = [chr(i) for i in range(ord('a'),ord('z') + 1)]
# list_num = [chr(i) for i in range(ord('1'),ord('9') + 1)]
# list_sum = list_A +list_a +list_num
#
# auth_code_list = list(random.sample(list_sum,4))
# print("生成的验证码为：",''.join(auth_code_list))
# auth_code_input = input("请输入验证码：")
# auth_code_input_list = list(auth_code_input)
# for i in range(len(auth_code_input_list) - 1):
#     print(i)
#     if auth_code_input_list[i].isdigit() :
#         continue
#     else:
#         auth_code_input_list[i].upper()
# x = 0
# for i in range(len(auth_code_list) - 1):
#     if auth_code_input_list[i] == auth_code_list[i] :
#         x += 1
# if 4 == x :
#     print("验证成功")
# else:
#     print("验证失败")

#9
list_sum = ['flower','flow','flight']
def longestCommonPrefix(strs):
    if len(strs) == 0 :
        return ''
    elif len(strs) == 1 :
        return strs[0]
    else:
        b = sorted(strs,key=lambda x:len(x))    #按字符串的长度进行排序
        s = ''
        s1 = b[0]
        for i,v in enumerate(s1):   #对第一个字符串进行枚举，遍历其每一个字符
            l =[]
            for j in b[1:]:     #从第二个字符串开始遍历之后的所有字符串
                l.append(v == j[i])     #将字符比较的bool值添加到列表l中
            if all(l):      #如果列表l中的所有值都为True
                s += v
            else:
                break
    return s

print(longestCommonPrefix(list_sum))
# #10
# num_list = []
# while True:
#     num = input("请输入随意个正整数，按Q结束。")
#     if ("Q" == num.upper()) :
#         print("即将退出输入。")
#         break
#     if (not num.isdigit()) :
#         print("输入错误，请重新输入")
#         continue
#     num = int(num)
#     if num < 0 :
#         print("输入错误，请重新输入")
#     num_list.append(num)
# print(num_list)
#
# for i in range(len(num_list)) :
#     for j in range(i) :
#         if num_list[i] < num_list[j] :
#             num_list[i],num_list[j] = num_list[j],num_list[i]
# print(num_list)

