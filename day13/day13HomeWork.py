# _*_ coding : UTF-8 _*_
# 开发人员 : ChangYw
# 开发时间 : 2019/7/31 21:32
# 文件名称 : day13HomeWork.PY
# 开发工具 : PyCharm

# 1)1)
aList = [['A','1'],['B','2'],['C','3'],['A','4'],['B','5'],['C','6'],['A','1'],['B','1'],['C','1']]
aDict = dict.fromkeys([i[0] for i in aList],0)
for i in range(len(aList)):
    aDict[aList[i][0]] += int(aList[i][1])
print(aDict)
# 2)
aDict = {}
for i in aList:
    if i[0] not in aDict.keys():
        aDict.setdefault(i[0],0)
    else:
        aDict[i[0]] += int(i[1])

#2)激活码生成器
import random
aList = [chr(i) for i in range(97,123)]
Alist = [chr(i) for i in range(65,91)]
numList = [i for i in range(10)]

def Captcha_generator():
    str, n = '', 0
    code = []
    for i in range(16):
        str_choice = random.choices([aList, Alist, numList], weights=[0.4, 0.4, 0.2])
        str = random.choice(str_choice[0])
        code.append(str)
        n += 1
        if n == 4:
            code.append("-")
            n = 0
            continue
    code.pop()

code_list = [Captcha_generator() for _ in range(200)]
