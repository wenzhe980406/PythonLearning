# _*_ coding : UTF-8 _*_
# 开发人员 : ChangYw
# 开发时间 : 2019/8/15 21:41
# 文件名称 : day24cywHomeWork.PY
# 开发工具 : PyCharm
import re
from collections import Counter


def fun26(n):
    print([i for i in range(2,n + 1) if str(i) == str(i**2)[(len(str(i)) * -1):]])


def fun27(a):
    aLst = []
    for i in a:
        if i.isdigit():
            aLst.append("*")
            aLst.append(i)
            aLst.append("*")
        else:
            aLst.append(i)
    print("".join(aLst))


def fun28():
    pass


def fun29(a):
    adict_l= {}
    [adict_l.setdefault(len(i),[]).append(i) for i in re.findall("(\d+)",a)]
    maxnum = (sorted(list(adict_l.keys()),reverse = True))[0]
    print(adict_l[maxnum],maxnum)


def fun30(a,b):
    aList = list(set(a))
    bList = list(set(b))
    count = 0
    if len(a) < len(b):
        for i in aList:
            if i in bList:
                count += 1
                if count == len(a):
                    print("yes")


if __name__ == '__main__':
    # fun26(10000)
    # fun27("15d6sa1d56a1sd56a1sd56asd")
    # fun29("12avc2345s1t2234")
    fun30('asg','aksgiwqm')