# _*_ coding : UTF-8 _*_
# 开发人员 : ChangYw
# 开发时间 : 2019/7/20 0:00
# 文件名称 : day04HomeWorkAnswer.PY
# 开发工具 : PyCharm


# 已知字符串 a = "aAsmr3idd4bgs7Dlsf9eAF",要求如下：
# 　　1） 请将a字符串的大写改为小写，小写改为大写
# 　　2）  请将a字符串的数字取出，并输出成一个新的字符串
# 　　3） 请统计a字符串出现的每个字母的出现次数（忽略大小写，a与A是同一个字母），并输出成一个字典。 例 {'a':4,'b':2}　
# 　　4） 去除a字符串多次出现的字母，仅留最先出现的一个。例 'abcabb'，经过去除后，输出 'abc'
# 　　5) 请将a字符串反转并输出。例：'abc'的反转是'cba'
#    6) 去除a字符串内的数字后，请将该字符串里的单词重新排序（a-z），并且重新输出一个排序后的字符 串。（保留大小写,a与A的顺序关系为：A在a前面。例：AaBb）
# 　　7) 请判断 'boy'里出现的每一个字母，是否都出现在a字符串里。如果出现，则输出True，否则，则输 出False.
# 　　8) 要求如1.7，此时的单词判断，由'boy'改为四个，分别是 'boy','girl','bird','dirty'，请判断如上这4个字符串里的每个字母，是否都出现在a字符串里。
# 　　9) 输出a字符串出现频率最高的字母

a = "aAsmr3idd4bgs7Dlsf9eAF"
# 1） 请将a字符串的大写改为小写，小写改为大写
print("1):")
print(a.swapcase())  # upper变大写，lower变小写，title首字母大写，swapcase是大小写交换
print()
# 2）  请将a字符串的数字取出，并输出成一个新的字符串
print("2):")
aStr_digit = ''.join([i for i in a if i.isdigit()])
print(aStr_digit)
print()
# 3） 请统计a字符串出现的每个字母的出现次数（忽略大小写，a与A是同一个字母），并输出成一个字典。 例 {'a':4,'b':2}　
print("3):")
aStr_alpha = ''.join([i for i in a if i.isalpha()]) # isalpha是否是字母， isdigit是否是数字
aLower = aStr_alpha.lower()
aDict = {x: aLower.count(x) for x in set(aLower)}
print(aDict)
print()
# 4） 去除a字符串多次出现的字母，仅留最先出现的一个。例 'abcabb'，经过去除后，输出 'abc'
print("4):")
aList = list(a)
aList_set = list(set(aList))
# 利用原来字符串a中的字符排序
aList_set.sort(key=aList.index)
print(aList_set)
print()
print()
# 5) 请将a字符串反转并输出。例：'abc'的反转是'cba'
print("5):")
print(a[::-1])  # 利用切片也是可以的，使用reversed函数也可以，但作为要输出结果反而麻烦，因为要转列表，再合并成字符串
print()
# 6) 去除a字符串内的数字后，请将该字符串里的单词重新排序（a-z），并且重新输出一个排序后的字符 串。（保留大小写,a与A的顺序关系为：A在a前面。例：AaBb）
print("6):")
sorted_s = sorted(a)
lower_s = [i for i in sorted_s if i.islower()]
upper_s = [i for i in sorted_s if i.isupper()]
last_alpha = ""
for i in lower_s[:]:
    if (last_alpha == i):
        continue
    last_alpha = i
    idx = lower_s.index(i)
    upper_i = i.upper()
    count_i = upper_s.count(upper_i)
    for _ in range(count_i):
        lower_s.insert(idx, upper_i)

print(lower_s)
print()
# 7) 请判断 'boy'里出现的每一个字母，是否都出现在a字符串里。如果出现，则输出True，否则，则输 出False.
print("7):")
search1 = 'boy'
aSet1 = set(a)
aSet1.update(list(search1))
print(len(set(a)) == len(aSet1)) # 长度相等说明没有boy中没有字母丢失，也就是说没有字母在aSet中
print()
# 8) 要求如1.7，此时的单词判断，由'boy'改为四个，分别是 'boy','girl','bird','dirty'，请判断如上这4个字符串里的每个字母，是否都出现在a字符串里。
print("8):")
search = ['boy', 'girl', 'bird', 'dirty']
aSet2 = set(a)
for i in search:
    print("check ",i)
    aSet2.update(list(i))
    print(len(set(a)) == len(aSet2))
print()
# 9) 输出a字符串出现频率最高的字母
print("9):")
aCountList = [(x, a.count(x)) for x in set(a)]
aCountList.sort(key=lambda x:x[1], reverse=True) # 排序，利用出现的次数，从高到低排序
# print(aCountList)
print("频率最高的字母是：%s, 出现的次数是：%d" %(aCountList[0][0],aCountList[0][1]))




