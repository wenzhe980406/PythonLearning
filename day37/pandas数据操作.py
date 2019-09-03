# _*_ coding : UTF-8 _*_
# 开发人员 : ChangYw
# 开发时间 : 2019/9/3 16:21
# 文件名称 : pandas数据操作.PY
# 开发工具 : PyCharm
import numpy as np
import pandas as pd

# ser_obj = pd.Series(range(5),index=list('abcde'))
# print(ser_obj.head())
#
# #行索引
# print(ser_obj['a'])
# print(ser_obj[0])
#
# #切片索引
# print(ser_obj[1:3])
# print(ser_obj['b':'d'])
#
# #不连续索引
# print(ser_obj[[0,2,4]])
# print(ser_obj[['a','e']])
#
# #布尔索引




# #DateFrame索引
# df_obj = pd.DataFrame(np.random.randn(5,4),columns=list('abcd'))
# print(df_obj.head())
#
# # 列索引
# print('列索引')
# print(df_obj['a']) # 返回Series类型
# print(df_obj.index)
# print(df_obj[['a']]) # 返回DataFrame类型，因为用的是多列模式
# print(type(df_obj[['a']]))
#
# #不连续索引
# print('不连续索引')
# print(df_obj[['a','c']])
# print(df_obj.loc[[1,3]])

#三种索引方式
# 标签索引 loc -- 如果是切片的话，头和尾都包括
#Series
# print(df_obj)
# print(df_obj['b':'d']) #一维才可以用
# print(df_obj.loc['b':'d'])#一维才可以用

# #DateFrame
# print(df_obj)
# df_obj.index = list('abcde')
# df_obj.columns = list('ABCD')
# print(df_obj)
# print(df_obj['A'])
# print(df_obj.loc['a':'c',['A','C']])
#
# # 位置索引 iloc -- 必须用位置索引值，0,1,2,3......切片的话 和list,tuple一样，顾头不顾尾
# # print(ser_obj[1:3])
# # print(ser_ovj.iloc[1:3])
#
# #DataFrame
# print(df_obj.iloc[0:2,0])# 注意两者区别
# print(df_obj.loc['a':'c','A'])


#运算与对齐
# # s1 = pd.Series(range(10,20),index=range(10))
# # s2 = pd.Series(range(20,25),index=range(5))
# # print(s1)
# # print(s2)
# # #Series 对齐运算
# # print(s1 + s2)
#
# df1 = pd.DataFrame(np.ones((2,2)),columns=['a','b'])
# df2 = pd.DataFrame(np.ones((3,3)),columns=['a','b','c'])
# # DateFrame对齐操作
# print(df1 + df2)
#
# #填充未对齐的数据进行运算
# # print(s1.add(s2,fill_value = -1))
# # # 减
# # print(df1.sub(df2,fill_value = 2.))
#
# # # 对NaN的处理，可以fillna,把NaN转换成自己想要的值
# # # 也可以使用dropna，直接把NaN的行数据丢弃
# # s3_filled = s3.fillna(-1)
# # print(s3_filled)
# # print(s3.dropna())

# df3 = df1 + df2
# print(df3)
# print(df3.dropna()) # df3.dropna(axis=1)可以指定轴

# # 参数inplace=True， 表示就地替换，dataFrame本身就改变了
# # 否则，本身是不变的，返回一个改变了的dataFrame副本
# df3.fillna(100,inplace=True)
# print(df3)

# # pd的shift是把dataFrame平移，根据指定的方向和大小 默认是axis=0的方向平移，即 行整体移动
s = pd.Series([1,3,5,np.nan,6,8],index=list('abcdef')).shift(2)
# print(s)
df = pd.DataFrame(np.random.randn(6,4),index=list('abcdef'),columns=list('ABCD'))
print(df)

# s也必须要由和df一样的index，否则不能加减乘除
# s会横向扩展广播，然后进行加减，期中的axis不能省略
print(df.sub(s,axis=0))