# _*_ coding : UTF-8 _*_
# 开发人员 : ChangYw
# 开发时间 : 2019/8/30 16:46
# 文件名称 : vectoryDemo01.PY
# 开发工具 : PyCharm

import numpy as np

arr = np.array([['a bc','de f','g hi'],
                ['xy z','u vw','rs t']])
print(arr)

aStr = 'ab c'
aStr = aStr.replace(' ','')
print(aStr)

vreplace = np.vectorize(str.replace)
print(vreplace(arr,' ',''))
vlen = np.vectorize(str.__len__)
print(vlen(arr))

print(np.core.defchararray.replace(arr," ",""))