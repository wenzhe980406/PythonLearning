# _*_ coding : UTF-8 _*_
# 开发人员 : ChangYw
# 开发时间 : 2019/7/23 11:16
# 文件名称 : regularExpression.PY
# 开发工具 : PyCharm
import re

pattern = r"[?|&]"
url = 'http://www.python.com/login.jsp?username="python"&pwd="newbie"'
result = re.split(pattern,url)
print(result)
