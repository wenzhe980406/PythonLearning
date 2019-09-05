# _*_ coding : UTF-8 _*_
# 开发人员 : ChangYw
# 开发时间 : 2019/9/4 13:47
# 文件名称 : pandasTest.PY
# 开发工具 : PyCharm

import pandas as pd

df = pd.Series([1,2,3,4])
print(df)
print(df[3])
df[4] = 5
df[5] = 10,11
print(df)