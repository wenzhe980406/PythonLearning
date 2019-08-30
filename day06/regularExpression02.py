# _*_ coding : UTF-8 _*_
# 开发人员 : ChangYw
# 开发时间 : 2019/7/22 16:25
# 文件名称 : regularExpression02.PY
# 开发工具 : PyCharm

#search 和 match 的不同：
#match只能从头匹配，search在字符串中匹配，找到第一个就返回

#search方法
import re

pattern = r"python_\w+"
string = "PYTHON_PROJECT python_project"
match = re.search(pattern,string,re.I)
print(match)

#findall语法
import re

pattern = r"python_\w+"
string = "PYTHON_PROJECT python_project"
match = re.findall(pattern,string,re.I)
print(match)

string = "正则练习PYTHON_PROJECT python_project"
match = re.findall(pattern,string)
print(match)

# pattern = "\d{1,3}\.\d{1,3}\.\d{1,3}(\.\d{1,3})"
# strl = "127.0.0.1 192.168.1.66"
# match = re.findall(pattern,strl)
# print(match)
#
# pattern = "\d{1,3}(\.\d{1,3}){3}"
# strl = "127.0.0.1 192.168.1.66"
# match = re.findall(pattern,strl)
# print(match)

pattern = "\d{1,3}\.\d{1,3}(\.\d{1,3})\.\d{1,3}"
strl = "127.0.0.1 192.168.1.66"
match = re.findall(pattern,strl)
print(match)