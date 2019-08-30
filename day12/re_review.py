# _*_ coding : UTF-8 _*_
# 开发人员 : ChangYw
# 开发时间 : 2019/7/30 9:53
# 文件名称 : re_review.PY
# 开发工具 : PyCharm

#正则表达式
#密码校验
import re
#
# #首字符必须是数字或字母，必须有@符号，@符号后还必须有字母，数字，可能会出现小数点，在@后的字符串中间
# pattern1 = r"^\w+([.][\w]+)*@\w+[.][\w]+)*$"
#
# #用户名首字符必须是字母，名字中间不能有空格，只能由字母和数字组成，长度必须在6-16之间
# username = r"(?!.*\s)(?=^[a-z])^[\w]{6,16}$"
#
# #密码是由16个字符组成，不能全数字，也不能包含空格
# pattern = r"(?!.*\s)(?![0-9]{8,16}$)^.{8,16}$"
# string = input("请输入密码")
# re = re.findall(pattern,string)
# print(re)

pattern1 = r"(\w+)@\w+\.(com|cn|org)"
string ="cyw980406@icloud.com"
findall = re.search(pattern1,string)
print(findall)

