# _*_ coding : UTF-8 _*_
# 开发人员 : ChangYw
# 开发时间 : 2019/9/4 17:20
# 文件名称 : matplotlib_codes.PY
# 开发工具 : PyCharm

import numpy as np
import pandas as pd
import scipy as sp
from scipy import stats
import matplotlib.pyplot as plt

#创建figure
fig = plt.figure()

#fig.add_subplot(a,b,c) --> a x b的区域，当前是c区域，从1开始编号
ax1 = fig.add_subplot(2,2,1)
ax2 = fig.add_subplot(2,2,2)
ax3 = fig.add_subplot(2,2,3)
ax4 = fig.add_subplot(2,2,4)

# # 在subplot上作图
# random_arr = np.random.randn(100)
# # print(random_arr)
#
# #默认是在最后一次使用subplot的位置上作图，但是在jupyter里面无效
# plt.plot(random_arr)
# plt.show()

# 返回指定范围内，均匀分布的指定数量的数，
x = np.linspace(-5,15,50)
# print(x.shape)
#绘制高斯分布
#norm正太分布，pdf概率密度函数：x指定的范围，loc堆成轴，scale大小
# plt.plot(x,sp.stats.norm.rvs(loc=5,scale=2,size=200),bins=50,normed=True,color='red',)


#柱状图
x = np.arange(5)
y1,y2 = np.random.randint(1,25,)
width = 0.25
ax = plt.subplot(1,1,1)
ax.bar(x,y1,width,color='r')
ax.bar(x+width,y1,width,color='r')