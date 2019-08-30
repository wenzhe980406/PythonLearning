# _*_ coding : UTF-8 _*_
# 开发人员 : ChangYw
# 开发时间 : 2019/7/19 14:15
# 文件名称 : day04HomeWorkAgain.PY
# 开发工具 : PyCharm

#6
a = "aAsmr3idd4bgs7Dlsf9eAF"
# #1)
# print(a.swapcase())
# #2)
# aLst = [i for i in a if i.isdigit()]
# print(''.join(aLst))
#3)
# b = a
# b = b.lower()
# c = [i for i in b if (not i.isdigit())]
# aDict = dict.fromkeys(c)
# aDict = {name:c.count(name) for name in c}
# print(aDict)
#4)
# d = str(a)
# d = d.lower()
# d = [i for i in d if (not i.isdigit())]
# e = []
# for i in d :
#     if (i not in e ) :
#         e.append(i)
# print(e)

# #5)
# print(a[::-1])
#6)
# sorted_s = sorted(a)
# sorted_s = [i for i in sorted_s if (not i.isdigit())]
# print(sorted_s)
#
# lower_s = [i for i in sorted_s if i.islower()]
# lower_s = sorted(lower_s)
# upper_s = [i for i in sorted_s if i.isupper()]
# upper_s = sorted(upper_s)
# print(lower_s,upper_s)
# list_alpha = ''
# for i in sorted_s[:] :
#     if list_alpha == 1 :
#         continue
#     low_index = lower_s.index(i)
#

#7)