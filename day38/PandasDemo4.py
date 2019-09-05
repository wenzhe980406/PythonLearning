# _*_ coding : UTF-8 _*_
# 开发人员 : ChangYw
# 开发时间 : 2019/9/4 16:57
# 文件名称 : PandasDemo4.PY
# 开发工具 : PyCharm
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt


# df_obj = pd.DataFrame(np.random.randn(5,4),columns=list('abcd'))
# print(df_obj)
#
# print(df_obj.sum())
# print(df_obj.max())
# print(df_obj.min(axis=1))
# print(df_obj.describe())

ser_obj = pd.Series(np.random.randn(10).cumsum())
# print(ser_obj.head())
#
# ser_obj.plot()
# plt.show()

df_obj = pd.DataFrame(np.random.randn(10,5),columns=list('abcde'))
print(df_obj.head())
# df_obj.plot()
# plt.show()

# 柱状图
# ser_obj.plot(kind='bar')
# plt.show()

# df_obj.plot(kind='bar')
# plt.show()

# 散点图
df = pd.DataFrame(np.random.randint(1,11,size=(5,4)),index=list('abcde'),columns=list('ABCD'))
print(df)

pd.plotting.scatter_matrix(df)
plt.show()