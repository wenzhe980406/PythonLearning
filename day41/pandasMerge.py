# _*_ coding : UTF-8 _*_
# 开发人员 : ChangYw
# 开发时间 : 2019/9/10 10:49
# 文件名称 : pandasMerge.PY
# 开发工具 : PyCharm
import numpy as np
import pandas as pd

# df_obj1 = pd.DataFrame({'key' : ['b','b','a','c','a','a','b'],
#                         'data1' : np.random.randint(0,10,7)})
# df_obj2 = pd.DataFrame({'key' : ['a','b','d'],
#                         'data2' : np.random.randint(0,10,3)})
#
# # print(df_obj1)
# # print(df_obj2)
#
# # left_on ,right_on分别制定左侧数据和右侧数据的‘外键’
# #更改列名
# df_obj1 = df_obj1.rename(columns={'key':'key1'})
# df_obj2 = df_obj2.rename(columns={'key':'key2'})
# print(df_obj1)
# print(df_obj2)
#
# print(pd.merge(df_obj1,df_obj2,left_on='key1',right_on='key2'))
#
# # '外连接'
# pd.merge(df_obj1,df_obj2,left_on='key1',right_on='key2',how='outer')
#
# #左连接 -- 左为主的外链接
# pd.merge(df_obj1,df_obj2,left_on='key1',right_on='key2',how='left')
#
# #右连接 -- 右为主的外链接
# pd.merge(df_obj1,df_obj2,left_on='key1',right_on='key2',how='right')

# #处理重复列名
# df_obj1 = pd.DataFrame({'key' : ['b','b','a','c','a','a','b'],
#                         'data' : np.random.randint(0,10,7),
#                         'data1' : np.random.randint(0,10,7)})
# df_obj2 = pd.DataFrame({'key' : ['a','b','d'],
#                         'data' : np.random.randint(0,10,3)})
#
# # 默认为内连接，只有suffixes，没有prefixs suffixes默认为_x,_y
# pd.merge(df_obj1,df_obj2,on='key',suffixes=('_left','_right'))
# print(pd.merge(df_obj1,df_obj2,on='key'))

# 按索引连接
df_obj1 = pd.DataFrame({'key' : ['b','b','a','c','a','a','b'],
                        'data1' : np.random.randint(0,10,7)})
df_obj2 = pd.DataFrame({'data2' : [np.random.randint(0,10,3)]},index=['a','b','d'])