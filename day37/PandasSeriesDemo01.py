# _*_ coding : UTF-8 _*_
# 开发人员 : ChangYw
# 开发时间 : 2019/9/3 10:11
# 文件名称 : PandasSeriesDemo01.PY
# 开发工具 : PyCharm

import pandas as pd
import numpy as np

# ## Series
# # 通过list构建Series
# ser_obj = pd.Series([1,2,3,4])
# print(ser_obj)
# print(ser_obj.shape)
# ser_obj = pd.Series(range(10,20))
# print(type(ser_obj))
#
# for x in ser_obj:
#     print(x)
# aList = ser_obj.tolist()
# print(aList)
# bList = list(ser_obj)
# print(bList)
#
# # 可以在构建Series时指定索引，注意：index
# ## 位置索引（用数字表示）
# ser_obj = pd.Series(range(10,20),index=range(1,11))
# print(type(ser_obj.index))
# # ser_obj.index = range(10,20)
# print(ser_obj)
# ## 用字符串和其他索引是标签索引
# ser_obj2 = pd.Series(range(21,31),index=list('abcdefghij'))
# print(ser_obj2)
# print(ser_obj.values)
# print(ser_obj2.index)
#
# print(ser_obj.head(3))
# print(ser_obj.tail(3))
#
# print(ser_obj[1])
# print(ser_obj[8])
#
# print()
# print(ser_obj2[5])

# ser_obj = pd.Series()

# # 通过dict构建Series，字典的key就是Series的索引
# # Series的数据可以不同类型，Series有索引列，可以给数据列取名字，ndarray必须同一种类型，ndarray只能有默认索引
# year_data = {2001:'abc',2002:20.1,2003:16.5}
year_data = {2001:17.1,2002:20.1,2003:16.5}
ser_obj2 = pd.Series(year_data)
# print(ser_obj2.head())
# print(ser_obj2.index)
# print(ser_obj2.dtype)
# print(ser_obj2.ndim)
# print(ser_obj2.shape)
#
# # name 属性
ser_obj2.name = 'temp'
print('Series values的类型：',type(ser_obj2.values))
print('Series index的类型：',type(ser_obj2.index))
#
ser_obj2.index.name = 'year'
print(ser_obj2.head())
print(ser_obj2[2001])

# dict3 = {'y01' : 17.7,'y02' : 20.1 ,'y 03' : 16.5}
# ser_obj3 = pd.Series(dict3)
# print(ser_obj3)
# print(ser_obj3['y02'])
# print(ser_obj3.y01)
# print(ser_obj3['y 03'])

# # DataFrame
# ## 通过ndarray构建DataFrame
# arr = np.random.rand(5,4)
# df_obj = pd.DataFrame(arr)
# print('df_obj.info()')
# print(df_obj.info())
# print('df_obj.head()')
# print(df_obj.head())

# print(list(df_obj))  # -- 返回的是列索引值的列表
# print(df_obj.values.tolist())  # --得到一个嵌套的列表
# print(list(np.array(df_obj)))  #-- 得到一个列表，每个元素是一个数组

# df = pd.DataFrame([['A','B',"C"],["D","E","F"],["H","i","j"]])
# print(df)

# df2 = pd.DataFrame(arr,index=range(1,6),columns=list("ABCD"))
# print(df2)

# df3 = pd.DataFrame([1,2,3],[4,5,6])
# print(df3)

# s= pd.Series(np.random.randn(5),name='temp',index=list("ABCDE"))
# print('序列为：',s,sep='\n')
# df4 = pd.DataFrame(s)
# print("用序列生成的DataFrame：",df4,sep='\n')
#
# # 用concat在生成的列表中添加数据
# print("\nconcat一个序列成df")
# df5 = pd.DataFrame()
# print(pd.concat([df5,s],axis=0,sort=False))
#
# print('\n两个序列拼成')
# s2 = pd.Series(np.random.randn(5),name='xxx',index= list("ABCDE"))
# df6 = pd.concat([s,s2],axis=1)
# print(df6,df6[0])###???

datas = pd.date_range('20190711',periods=6)
# print(datas)
#
df = pd.DataFrame(np.random.randn(6,4),index=datas,columns=list("ABCD"))
# print(df)
# print(df.index,df.columns,df.values,sep='\n')
# print(df.shape,df.ndim)


# dict_data = {'A':1.,
#              'B':pd.Timestamp("20161217"),
#              'C':pd.Series(1,index=list(range(1,5)),dtype='float32'),
#              'D':np.array([3]*4,dtype='int32'),
#              'E':pd.Categorical(['Python','Java','C++','C#']),
#              'F':'ChinaHadoop'}
#
# #print dict_data
# df_obj2 = pd.DataFrame(dict_data)
# print(df_obj2)
#
# # 访问列，可以直接饮用列标签
# print(df_obj2['A'])
# print(df_obj2.E)
# print()
# print(type(df_obj2.F))
#
# # 增加列
# df_obj2['G'] = df_obj2.D + 4
# print(df_obj2)
#
# # 删除列
# del df_obj2['G']
# print(df_obj2)

# # 标签（索引）排序
# print(df)
# # 默认是升序，可以用ascending = False改成降序，轴0 表示行标签 ，轴1表示列标签
# print(df.sort_index(axis=1,ascending=False))
# #数据的排序
# print(df.sort_values(by='A'),)


ser = pd.Series(np.random.randint(1,10,10))
# print(ser)
# print(ser.sort_index(ascending=False))
# print(ser.sort_values())


# 索引对象Index
# print(type(ser.index))
# print(type(df.index))
# print(df.index)
# print(type(df_obj2.index))
# print(df_obj2.index)

# 索引对象不可变
# df_obj2.index[0] = 20
# 获取一行 loc 或者 iloc，loc用的是标签索引，包含了头，也包含了尾
# iloc用的是位置索引，符合索引的顾头不顾尾的原则

# print(df.loc['2019-07-12'])
# print(df.loc['2019-07-12':'2019-07-15'])
#
# print(df.iloc[0])
# print(df.iloc[1:4])

# 关于标签索引loc的切片
# print(df.loc[:,['B','C']])
# print(df[['B','D']])
# print(df.loc[:,'A':'C'])

# print(df.loc['2019-07-12':,['B','C']])
# # 关于iloc的切片
# print(df.iloc[:3,1:3])

# print(df[:-2]['A']) #直接在这里使用切片，取的是行

# #可以访问具体DaraFrame中的具体某个值
# print(df.loc['2019-07-12','C'])
# # 还有更简单的方式：但必须用原生的数据结构，不能用字符串
# print(df.at[pd.Timestamp('2019-07-13'),'D'])
#
# print(df.iloc[1,2])
# print(df.iat[1,2])

# # DataFarme的布尔应用
# # print(df.A>0)
# # 对行进行筛选，不符合的行就不要了
# # print(df[df.A > 0])
# # 对整个dataFrame进行筛选，符合的留下，不符合的，写作NaN
# print(df[df>0])
#
# # 符合条件的，True的值保留，不符合False位置的值，写作NaN
# # 按条件索引的方式操作，True的位置的数据保留，False的位置的数据写作NaN
# print(df[df.iloc[0:3] > 0])

# # isin
# df2 = df.copy()
# df2['TAG'] = list('aabbcc')
# print(df2)
# # isin只保留了所在的行，不符合的行去掉了
# # 筛选条件是一个Series ，不符合isin条件的行删除，而不是写作NaN
# print(df2[df2.TAG.isin(['a','c'])])

# #修改元素
# df.iat[0,1] = 100
# print(df)
# # 修改一列
# df.B = 100
# print(df)
# df.A = range(1,7)
# print(df)

