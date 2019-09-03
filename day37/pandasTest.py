# _*_ coding : UTF-8 _*_
# 开发人员 : ChangYw
# 开发时间 : 2019/9/3 15:39
# 文件名称 : pandasTest.PY
# 开发工具 : PyCharm
import numpy as np
import pandas as pd

# dic = {
#     'name':['tome','bob','dog'],
#     'phone':[123,444,789],
#     'year':2019,
#     'xuehao':pd.Series([2,3,4])
# }
# df_ob3 = pd.DataFrame(dic)
# print(df_ob3)
# # 获取一行 name列
# print(df_ob3.name)
# print(df_ob3['name'])
# print(df_ob3.loc[:,'name'])
#
# # 获取一行  第二行或者第一行
# print(df_ob3.loc[0])
# print(df_ob3.iloc[1])
# print(df_ob3[0:1])
#
# # 给列赋值 给xuehao这列赋值
# df_ob3.xuehao = [10,11,12]
# df_ob3.xuehao = pd.Series([10,11,12])
# print(df_ob3)
#
# # 给行赋值 给第三行赋值
# df_ob3.loc[2] = ['jzy',523,2019,22]
# print(df_ob3)
#
# # 新加一列
# df_ob3.loc[3] = ['wmn',368,2019,20]
# print(df_ob3)

# # 新加一列 score，都给60分
# df_ob3['score'] = 60
# print(df_ob3)
#
# # 删除一列 score
# del df_ob3['score']
# print(df_ob3)

# arr = np.random.randint(1,10,(6,4))
# df_ob4 = pd.DataFrame(arr,index=list("dbcfea"),columns=list("BDAC"))
# print(df_ob4)

# # 查看前几行数据
# print(df_ob4.head(3))
# print(df_ob4.tail(4))

# # 获取行名、列名
# print(df_ob4.index)
# print(df_ob4.columns)

# #获取数据
# print(df_ob4.values)
#
# #获取dataframe维度
# print(df_ob4.shape)
#
# #显示一些汇总统计信息
# print(df_ob4.describe())
#
# #查看dataframe的数据特性，info
# print(df_ob4.info())
#
# #索引排序
# df_ob4.sort_index()
# df_ob4.sort_index(axis=0)
# df_ob4.sort_index(axis=1)
# df_ob4.sort_index(axis=1,ascending=False)
#
# # # 数据排序
# df_ob4.sort_values(by='B')
# df_ob4.sort_values(by=['A','B'])
# #一行上的数据类型可能不同，不提供排序
#
# #矩阵转置，行变列，列边行
# print(df_ob4.T)
#
# #获取多列数据
# print(df_ob4[['A','B']])
#
