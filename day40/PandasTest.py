# _*_ coding : UTF-8 _*_
# 开发人员 : ChangYw
# 开发时间 : 2019/9/6 16:26
# 文件名称 : PandasTest.PY
# 开发工具 : PyCharm

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

FILE_NAME = 'users.csv'

# 1.使用pandas.read_csv()可以直接将csv导入到DataFrame中
users = pd.read_csv(FILE_NAME,encoding='utf-8')
# print(users.info())
# print(users.describe())

# 2.获取前20条记录
# users_20 = users.head(20)
# users_20_

# 3.共有多少条数据（共有多少行）
# users_count = users.count()[0]
print(users.shape[0])

# 4.打印出所有的列名和索引名
# print(users.columns)
# print(users.index)

# 5.打印出occupation这一列的内容
# print(users.occupation)

# 6.一共有多少个不同的职位
# a= []
# [a.append(i) for i in users.occupation if not i in a]
# print(a)
# print('一共有%d个不同的职位'%a.__len__())

ocu = users.occupation.unique()  # 对职位列去重返回数组
print(ocu.size,len(ocu))

# 7.最多出现的职位是哪些(value_counts()分类统计)  重点
# print(users.occupation.value_counts())

# 8.所用user的平均年龄
# print('user中的平均年龄%d岁'%users.age.mean())

# 9.所用男性 user的平均年龄
# print('user中男性的平均年龄%d岁'%users[users.gender == 'M'].age.mean())