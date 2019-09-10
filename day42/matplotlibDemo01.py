# _*_ coding : UTF-8 _*_
# 开发人员 : ChangYw
# 开发时间 : 2019/9/10 14:03
# 文件名称 : matplotlibDemo01.PY
# 开发工具 : PyCharm

import matplotlib.pyplot as plt
import numpy as np

fig , ax = plt.subplots(1)
ax.set_xlim([0,800])
ax.set_xticks(range(0,501,100))
ax.set_yticklabels(['Jan','Feb','Mar'])
ax.set_xlabel('Number')
ax.set_ylabel('Month')
ax.set_title('Example')
ax.plot(np.random.randn(1000).cumsum(),label='line1')
ax.plot(np.random.randn(1000).cumsum(),label='line2')
ax.legend(loc='best')
plt.show()