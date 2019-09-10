# _*_ coding : UTF-8 _*_
# 开发人员 : ChangYw
# 开发时间 : 2019/9/9 13:42
# 文件名称 : Pandas层级索引.PY
# 开发工具 : PyCharm

import pandas as pd
import numpy as np

# ser_obj = pd.Series(np.random.randn(12),
#                     index=[list('aaabbbcccddd'),[0,1,2,0,1,2,0,1,2,0,1,2]])
# print(ser_obj)
# # print(type(ser_obj.index))
# # print(ser_obj.index)
# print('`````````````````````````')
# print(ser_obj.c)
# print(ser_obj[: , 1])
#
# #交换分层
# print(ser_obj.swaplevel())
# #交换分层并排序
# print(ser_obj.swaplevel().sort_index())

dict_obj = {'key1' : ['a','b','a','b',
                      'a','b','a','a'],
            'key2' : ['one','one','two','three',
                      'two','two','one','three'],
            'data1' : np.random.randn(8),
            'data2' : np.random.randn(8)}
df_obj = pd.DataFrame(dict_obj)
# print(df_obj)

# # # dataframe 根据key1进行分组
# print(type(df_obj.groupby('key1')))
# print(df_obj.groupby('key1'))

# #data1列根据key1进行分组
# print(df_obj['data1'].groupby(df_obj['key1']))

# #分组运算
# grouped1 = df_obj.groupby('key1')
# print(grouped1.mean())
#
# grouped2 = df_obj['data1'].groupby(df_obj['key1'])
# print(grouped2.mean())

# #Size
# print(grouped1.size())
# print(grouped2.size())
# print('❤'*100)
# print(grouped1.count())
# print(grouped2.count())

# df_obj.loc[0,'data1'] = np.NaN
# grouped1 = df_obj.groupby('key1')
# grouped2 = df_obj['data1'].groupby(df_obj['key1'])
# print(grouped1.count())
# print(grouped2.count())

# # 按自定义key分组，列表
# self_def_key = [1,1,2,2,2,1,1,1]
# df_obj.groupby(self_def_key).size()

# # 按自定义key分组，多层列表
# df_sz = df_obj.groupby([df_obj['key1'],df_obj['key2']]).count()
#
# print(df_sz)
# print(type(df_sz))
# print(df_sz['data1']['a','one'])


# #按多个列多层分组
# grouped2 = df_obj.groupby(['key1','key2'])
# print(grouped2.size())

# # 多层分组按key的顺序进行
# grouped3 = df_obj.groupby(['key2','key1'])
# print(grouped3.mean())
#
# grouped4 = grouped3.mean().unstack()
# print(grouped4)
# print(type(grouped4))
# print(grouped4.shape)
# print(grouped4.index)
# print(grouped4.values)


# GroupBy 对象的分组迭代
# for group_name ,group_data in grouped1:
#     print(group_name)
#     print(group_data)

# # 多层分组
# for group_name ,group_data in grouped2:
#     print(group_name)
#     print(group_data)

# #按列分组
# print(df_obj)
# print(df_obj.dtypes)
# print(df_obj.dtypes.index)

# # 按数据类型分组
# grouped5 = df_obj.groupby(df_obj.dtypes,axis=1)
# print(grouped5.size())

# # 其他分组方法
# df_obj2 = pd.DataFrame(np.random.randint(1,10,(5,5)),columns=['a','b','c','d','e'],index=['A','B','C','D','E'])
#
# df_obj2.iloc[1,1:4] = np.NaN
# print(df_obj2)
#
# # 通过字典分组
# mapping_dict = {'a':'python','b':'python','c':'java','d':'C','e':'java'}
# print(df_obj2.groupby(mapping_dict,axis=1).size())
# print(df_obj2.groupby(mapping_dict,axis=1).count())
# print(df_obj2.groupby(mapping_dict,axis=1).sum())  # 忽略NaN

# # 通过函数分组
# df_obj3 = pd.DataFrame(np.random.randint(1,10,(5,5)),
#                        columns=['a','b','c','d','e'],
#                        index=['AA','BBB','CC','D','EE'])
# print(df_obj3)

# def group_key(idx):
#     '''
#
#     :param idx: idx为索引或行索引
#     :return: idx
#     '''
#     return len(idx)
# #  把df的行索引传递给groupby指定的函数，这个函数的返回值如果一样，就是一组的。
# df_obj3.groupby(group_key).size()
# df_obj3.groupby(len).size()

# # 通过索引级别分组
# columns = pd.MultiIndex.from_arrays([['Python','Java','Python','Java','Python'],['A','A','B','C','B']],
#                                     names=['language','index'])
# df_obj4 = pd.DataFrame(np.random.randint(1,10,(5,5)),columns=columns)
# print(df_obj4)
#
# #根据language进行分组
# print(df_obj4.groupby(level='language',axis=1).sum())
# print(df_obj4.groupby(level='index',axis=1).sum())

indexs = pd.MultiIndex.from_arrays([['Python','Java','Python','Java','Python'],['A','A','B','C','B']],
                                    names=['language','index'])
df_obj5 = pd.DataFrame(np.random.randint(1,10,(5,5)),index=indexs)
print(df_obj5)

# 根据language进行分组
print(df_obj5.groupby(level='language',axis=0).sum())
print(df_obj5.groupby(level='index',axis=0).sum())


#内置的聚合函数
'''
sum()
max()
min()
mean()
size()
count()
describe()
'''

#自定义的聚合函数
def peak_range(df):
    return df.max() - df.min()
print(df_obj5.groupby('key1').agg(peak_range))
print(df_obj5.groupby('key1').agg(lambda x:x.max() - x.min()))

# 应用多个聚合函数

# 同事应用多个聚合函数
print(df_obj.groupby('key1').agg(['mean','std','count',peak_range])) #默认列名为函数名

print(df_obj.groupby('key1').agg(['mean','std','count',('range',peak_range)])) # 通过元组修改列名

#每列作用不同的聚合函数
dict_mapping = {'data1':'mean',
                'data2':'sum'}
print(df_obj.groupby('key1').agg(dict_mapping))

dict_mapping = {'data1':['mean','max'],
                'data2':'sum'}
print(df_obj.groupby('key1').agg(dict_mapping))

'''
函数名      说明
count       分组中非NaN值的数量
sum         非NaN值的和
mean        非NaN值的平均值
median      非NaN值的算术中位数
std、var    无偏(分母为n-1)标准差和方差
min、max    非NaN值的最小值和最大值
prod        非NaN值的积
first、last 第一个和最后一个非NaN值
'''