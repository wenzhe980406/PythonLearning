# _*_ coding : UTF-8 _*_
# 开发人员 : ChangYw
# 开发时间 : 2019/9/10 11:08
# 文件名称 : pandasConcat.PY
# 开发工具 : PyCharm

import numpy as np
import pandas as pd
# pd.concat
# 沿轴方向将多个对象合并到一起
# NUmpy的concat      np.concatenate

#pd.concat
    # 注意指定轴方向, 默认axis=0
    # join指定合并方式，默认为outer
    # Seres合并时查看行索引
    # DataFrame合并时同时查看行索引和列索引


arr1 = np.random.randint(0,10,(3,4))
arr2 = np.random.randint(0,10,(3,4))

# 默认轴axis = 0
print(np.concatenate([arr1,arr2],axis = 0))

# Serise上的concat
ser_obj1 = pd.Series(np.random.randint(1,))
ser_obj2 = pd.Series(np.random.randint())
ser_obj3 = pd.Series(np.random.randint())