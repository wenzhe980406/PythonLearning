# _*_ coding : UTF-8 _*_
# 开发人员 : ChangYw
# 开发时间 : 2019/9/10 14:44
# 文件名称 : SeabornDemo.PY
# 开发工具 : PyCharm

import numpy as np
import pandas as pd
from scipy import stats
import scipy
import matplotlib.pyplot as plt
import seaborn as sns

# 单变量分布
x1 = np.random.normal(size=500)
print(x1.shape)
# sns.distplot(x1)
# plt.show()

x2 = np.random.randint(0,100,1000)
# sns.distplot(x2)
# plt.show()

# 直方图
# sns.distplot(x1,bins=20,kde=False,rug=True)
# plt.show()

# 核密度估计
# sns.distplot(x2,hist=False,rug=True)
# plt.show()

# sns.kdeplot(x2,shade=True)
# plt.show()

# 拟合参数分布
# sns.distplot(x1,kde=False,fit=stats.gamma)
# plt.show()

# 双变量分布
df_obj1 = pd.DataFrame({'x' : np.random.randn(500),
                        'y' : np.random.randn(500)})
df_obj2 = pd.DataFrame({'x' : np.random.randn(500),
                        'y' : np.random.randint(0,100,500)})

# 散布图
# sns.jointplot(x='x',y='y',data=df_obj1)
# plt.show()

# 二维直方图
# sns.jointplot(x='x',y='y',data=df_obj2,kind='hex')
# plt.show()

# 核密度分布
# sns.jointplot(x='x',y='y',data=df_obj1,kind='kde')
# plt.show()

# # 数据集中变量间关系可视化
# dataset = sns.load_dataset('tips')
# #daraset = sns.load_dataset('iris')
# sns.pairplot(dataset)
# plt.show()

# titanic = sns.load_dataset('titanic')
# planets = sns.load_dataset('planets')
# flights = sns.load_dataset('flights')
# iris = sns.load_dataset('iris')
exercise = sns.load_dataset('exercise')


sns.swarmplot(x='dict',y='pulse',data=exercise)