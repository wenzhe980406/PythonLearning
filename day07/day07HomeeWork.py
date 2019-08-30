# _*_ coding : UTF-8 _*_
# 开发人员 : ChangYw
# 开发时间 : 2019/7/23 17:20
# 文件名称 : day07HomeeWork.PY
# 开发工具 : PyCharm

# 11)
# aStr = "k:1|k1:2|k2:3|k3:4"
# aStr = aStr.replace(':',',')
# aStr = aStr.replace('|',',')
# bList = ''.join(aStr)
# for i in range(0,len(bList),3) :
#     aList = bList[i]
#     print(aList)
# print("1",aList)

#12)
# def ex_num(mylist) :
#     return [i for i in mylist if i in [1,2,3,4,5,6,7,8,9]]
# my_list = ["a","a","a",1,2,3,4,5,"A","B","C"]
#
# ex = ex_num(my_list)
# print(ex)

#13)
def numIndex(target,list) :
    return [i for i in range(len(list)) if target == list[i]]
#
a = [3,4,5,6,6,5,4,3,2,1,7,8,8,3]
target_list = numIndex(3,a)
print(target_list)

#14)
# import random
#
# num_list =[random.randint(20,100) for _ in range(0,1000)]
# num_list.sort()
# for i in range(20,81) :
#     print(["%d："%i,num_list.count(i)])

#15)
# import random
#
# n = input("请输入一个随机整数")
# if not n.isdigit():
#     print("输入错误请重新输入正整数")
# n = int(n)
# if n < 0 or n >1000:
#     print("输入错误请重新输入")
#
# aList = []
# # aList = [random.randint(1,1000) for i in range(n) if i not in aList]
# for i in range(n) :
#     x = random.randint(1,1000)
#     if x not in aList:
#         aList.append(x)
# aList.sort()
# print(aList)

# #16)
# word_input = input("请输入一个句子： ")
# word_input = word_input.split()
# word_input = list(word_input)
# print(len(word_input[-1]))

# #17)
# word_input = input("请输入一个句子： ").strip()
# word_input = list(word_input)
# chr_input = input("请输入一个字符： ").strip()
# print("您输入的字符在句子中有%d个"%word_input.count(chr_input))

# #18)
#
# if __name__ == "__main__" :
#     def list_sum(alist):
#         num_group = int(len(alist) / 8)
#         for i in range(num_group):
#             blist = "".join(list(alist[i: i + 8]))
#             aList.append(blist)
#             i = i + 8
#     word_input = input("请输入一段字符串： ").strip()
#     word_input = list(word_input)
#     for i in range(word_input.count(' ')) :
#         word_input.remove(' ')
#     aList = []
#     if len(word_input) % 8 == 0 :
#         list_sum(word_input)
#         print(aList)
#     else:#sadfsasda  ???????????????
#         print(word_input)
#         x = 8 - len(word_input) % 8
#         for _ in range(x) :
#             word_input.append('0')
#         print(len(word_input))
#         list_sum(word_input)
#         print(aList)
#19)
# hexadecimal = input("请输入一位或多位的十六进制数： ").strip()
# hexadecimal = hexadecimal.split(' ')
# hexadecimal = list(hexadecimal)
# for i in hexadecimal :
#     print(i,"的十六进制为:",int(i,16))

# #20)
# aStr = 'abcda'
# repeat  = 0
# noRepeat = 0
# aList = list(aStr)
# for i in aList :
#     if aList.count(i) >= 2:
#         repeat +=1
#     elif 1 == aList.count(i) :
#         noRepeat += 1
# print("不重复字符串的个数为：%d"%noRepeat)