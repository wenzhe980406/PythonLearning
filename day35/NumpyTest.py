# _*_ coding : UTF-8 _*_
# 开发人员 : ChangYw
# 开发时间 : 2019/8/30 10:36
# 文件名称 : NumpyTest.PY
# 开发工具 : PyCharm

import numpy as np

# 1)
arr1 = np.random.randint(1,10,size=(3,3))
print(arr1)

# 2)
print((arr1>6).sum(0))
print(arr1[arr1>6].sum())

# 3)
print((arr1>3).all(axis=1).sum())
