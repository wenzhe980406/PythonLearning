# _*_ coding : UTF-8 _*_
# 开发人员 : ChangYw
# 开发时间 : 2019/7/22 15:11
# 文件名称 : regularExpression01.PY
# 开发工具 : PyCharm

import re
# #语法 re.match(pattern,string,flag)
#                         # re.I表示忽略大小写
#                         # re.l表示
#                         # re.S表示换行符等同于空白符
#
# pattern = r"python_\w+" #r->row 原始字符串
#                         #u Unicode字符串
#                         #b bytes 表示字节流字符串
# string = "PYTHON_PROJECT python_project"
# match = re.match(pattern,string,re.I)
# print(match)

pattern = r"python_\w+"
string = "PYTHON_PROJECT python_project"
match = re.match(pattern,string,re.I)
print(match)
print("匹配值的起始位置：",match.start())
print("匹配值的结束位置：",match.end())
print("匹配位置的元组：",match.span())
print("要匹配的字符串：",match.string)
print("匹配数据：",match.group())