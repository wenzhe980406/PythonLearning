# _*_ coding : UTF-8 _*_
# 开发人员 : ChangYw
# 开发时间 : 2019/8/5 21:13
# 文件名称 : day16HomeWork.PY
# 开发工具 : PyCharm

#已知某门功课的学生成绩，要求对这些成绩分类，统计优\良\中\及格和不及格的人数。
import itertools
from random import randint

score_list = sorted([randint(40,100) for _ in range(20)])

aLst = ["不及格","及格","中","良","优"]

for key,group in itertools.groupby(score_list,lambda c:c//10 if c != 100 else c//11) :
    print("{:<10}".format(aLst[key - 5]),"\t",list(group))