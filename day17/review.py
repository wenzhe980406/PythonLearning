# _*_ coding : UTF-8 _*_
# 开发人员 : ChangYw
# 开发时间 : 2019/8/6 10:19
# 文件名称 : review.PY
# 开发工具 : PyCharm

import os
fdir = os.path.abspath(__file__)
print(os.path.basename(fdir))
print(os.path.dirname(fdir))
print(os.path.split(fdir))

import sys
print(sys.argv[0])
print(os.path.basename(sys.argv[0]))

print(sys.path)