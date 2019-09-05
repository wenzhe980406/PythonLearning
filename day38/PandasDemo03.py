# _*_ coding : UTF-8 _*_
# 开发人员 : ChangYw
# 开发时间 : 2019/9/4 14:01
# 文件名称 : PandasDemo03.PY
# 开发工具 : PyCharm

import numpy as np
import pandas as pd

# df = pd.DataFrame(np.random.randn(5,4) - 1)
# print(df)
#
# print(np.abs(df))
# print(np.fabs(df))

# # 使用apply 应用行或者列数据，把每行或者每列的数据传给f
# f = lambda x : x.max()
# print(df.apply(f)) # 默认是每列，即axis=0
# print(df.apply(f,axis=1))
# # 可以简化为 -- 仍然可以指定轴
# print(df.apply(np.max))
# # 计算累计 -- 仍然可以指定轴
# print(df.apply(np.cumsum))
# # 计算最大值和最小值的差
# print(df.apply(lambda x:x.max()- x.min()))

# # 使用applemap应用到每个数据 -- 元素级的函数应用
# f2 = lambda x:'%.2f' % x
# print(df.applymap(f2))

# # value_counts 和 mode
# s = pd.Series(np.random.randint(10,20,20))
# print(s)
# print('value_counts方法，统计每个成员出现的次数：')
# print(s.value_counts())
# print('mode方法，找出出现次数最多的成员：')
# print(s.mode())

#concat(objs,axis=0,join="outer",join_axes=None,ignore_index=False,
# keys=None,levels=None,names=None,verify_integrity=False,sort=None,
# copy=True,)

df = pd.DataFrame(np.random.randn(10,4),columns=list('ABCD'))

# df1 = pd.concat([df.iloc[0:3],df.iloc[7:]])
# print(df1)

# df1 = pd.concat([df.iloc[0:3],df.iloc[3:7],df.iloc[7: ]])
# print((df1 == df).all().all())
# print(df1)

# ## 多个df的联合操作 -- merge
# left = pd.DataFrame({'key':['foo','foo'],'lval':[1,2]})
# right = pd.DataFrame({'key':['foo','foo'],'ravel':[4,5]})
# print(left,right,sep='\n\n')
#
# print('\nmerged')
# merged = pd.merge(left,right,on='key')
# print(merged)

# df1 = pd.DataFrame({'A':['A0','A1','A2','A3'],
#                     'B':['B0','B1','B2','B3'],
#                     'C':['C0','C1','C2','C3'],
#                     'D':['D0','D1','D2','D3']},index=[0,1,2,3])
#
# df2 = pd.DataFrame({'A':['A4','A5','A6','A7'],
#                     'B':['B4','B5','B6','B7'],
#                     'C':['C4','C5','C6','C7'],
#                     'D':['D4','D5','D6','D7']},index=[4,5,6,7])
#
# df3 = pd.DataFrame({'A':['A8','A9','A10','A11'],
#                     'B':['B8','B9','B10','B11'],
#                     'C':['C8','C9','C10','C11'],
#                     'D':['D8','D9','D10','D11']},index=[8,9,10,11])
#
# frames = [df1,df2,df3]
# result = pd.concat(frames)
# print(result)

# # concat 中的keys参数 -- 分组的概念
# result = pd.concat(frames,keys=['x','y','z'])
# print(result)

# # JOIN参数 默认join = 'outer',为取并集的关系
# df4 = pd.DataFrame({'B': ['B2','B3','B6','B7'],
#                     'D': ['D2','D3','D6','D7'],
#                     'F': ['F2','F3','F6','F7']},index=[2,3,6,7])

# result = pd.concat([df1,df4],axis=1)
# print(result)

# result = pd.concat([df1,df4],axis=1,join='inner')   #inner交集
# print(result)

# 设置索引为df1的索引
# result = pd.concat([df1,df4],axis=1,join_axes=[df1.index])
# print(result)

# # 1 添加字典
# print("添加字典")
# data = pd.DataFrame()
# a = {"x" : 1,'y' : 2}
# data = data.append(a,ignore_index=True)
# print(data)

# # 添加Series
# print('\n添加Series')
# data = pd.DataFrame()
# s = {"x" : 1,'y' : 2}
# # 如果不带ignore_index = Trrue 会报错
# data = data.append(s,ignore_index=True)
# print(data)
# #或者改成如下
# print('另外一种方式，通过制定Series的名字')
# series = pd.Series({'x':1,'y':2},name = 'a')
# data = data.append(series)
# print(data)

# #3 append添加list
# print('\n添加list')
# data = pd.DataFrame()
# a = [1,2,3]
# data = data.append(a)
# print(data)

# # 如果是二维列表，增加的是行数据
# print('\n添加二维list')
# data = pd.DataFrame()
# a = [[1,2,3]]
# data = data.append(a)
# print(data)

# # 如果是三维列表，增加的是：一个行数据
# # 如果是二维列表，增加的是行数据
# print('\n添加三维list')
# data = pd.DataFrame()
# a = [[[1,2,3]]]
# data = data.append(a)
# print(data)

# # 多次添加的index
# print('多次添加数据')
# data = pd.DataFrame()
# a = [[1,2,3],[4,5,6]]
# data = data.append(a)
# print(data)
# print('\n')
# a = [[7,8,9],[10,11,12]]
# data = data.append(a)
# print(data)
# # 使用ignore_index = True
# print('\n')
# a = [[13,14,15],[16,17,18]]
# data = data.append(a,ignore_index=True)
# print(data)

# print(df)
# s = pd.Series(np.random.randint(1,5,size=4),index=list('ABCD'))
# print(s)
# print('\n\n')
# print(df.append(s,ignore_index=True),sep='\n')

# 如果Series的数据比df的列数多，结果会多出一列数据，其他行这列的数据为NaN
# s1 = pd.Series(np.random.randint(1,5,size=5),index=list("ABCDE"))
# print(df.append(s1,ignore_index=True).applymap(lambda x:'%.2f'%x))


# s4 = pd.Series(range(10,15),index=np.random.randint(5,size=5))
# print(s4)

# 索引排序
# print(s4.sort_index())

# df4 = pd.DataFrame(np.random.randn(3,4),
#                    index=np.random.randint(3,size=3),
#                    columns=np.random.randint(4,size=4))
# print(df4)

# print(df4.sort_index(axis=1))

### 按值排序
# print(df4.sort_values(by=2,axis=1))

# df_data = pd.DataFrame([np.random.randn(3),[1.,np.nan,np.nan],
#                         [4.,np.nan,np.nan],[1.,np.nan,2.]])
# print(df_data.head())
# print(df_data.info())

# is null
# print(df_data.isnull())
# print(df_data.isnull().sum())

# dropna
# df_data.dropna()
# df_data.dropna(axis=1)
# print(df_data.dropna(axis=1))

# fillna
# df_data.fillna(-100.)


data = {
    'name':['tom','bob','dog'],
    'phone':[123,444,789]
}
df_data =pd.DataFrame(data)
# print(df_data)

data = {
    'name':['tom','bob','dog'],
    'phone':[123,444,789],
    'year':2017,
    'xuehao':pd.Series([2,3,4])
}
df_data =pd.DataFrame(data)
# print(df_data)

# print(df_data.name)
# print(df_data['name'])
#
# # print(df_data.ix[1])
# print(df_data.loc[1])
# print(df_data.iloc[1])

# #给列赋值
df_data.xuehao = np.arange(1,4)
# print(df_data)

# # 给行赋值
df_data.loc[0] = ['cat',456,2017,5]
# print(df_data)
#
# #新加一列
df_data['class'] = 'class1'
# print(df_data)

#新加一行
df_data.loc[3] = ['tom','123',2018,1,'class2']
# print(df_data)

# 删除一行
# 下列的结果删除了列，但df_data并没有
# 只删除一列，可以不采用列表，而是字符串
# df_data.drop('year',axis=1)
# df_data2 = df_data.drop(['year'],axis=1)
# print(df_data2)

#要直接删除的话，需要增加参数 inplace= True
# df_data.drop('year',inplace=True)
print(df_data)
df_data.drop(['year','class'],axis=1,inplace=True)
print(df_data)

# index
# values
# shape
# describe()
# .T

print(df_data.describe())