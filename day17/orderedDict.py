# _*_ coding : UTF-8 _*_
# 开发人员 : ChangYw
# 开发时间 : 2019/8/6 14:46
# 文件名称 : orderedDict.PY
# 开发工具 : PyCharm
from collections import OrderedDict

items = [
    ("a",1),
    ("b",2),
    ("c",3),
    ("d",4),
    ("e",5)
]

regular_dict = dict(items)
ordered_dict = OrderedDict(items)

print(regular_dict)
print(ordered_dict)
