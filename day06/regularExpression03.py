# _*_ coding : UTF-8 _*_
# 开发人员 : ChangYw
# 开发时间 : 2019/7/22 16:33
# 文件名称 : regularExpression.PY
# 开发工具 : PyCharm
import re

#替换字符串
pattern = r"1[34578]\d{9}"
string = "中奖号码为：86538712  联系电话为：13699973788"
result = re.sub(pattern,"13833331111",string)
print(result)

string = "life is shrot,i need python"
pattern = r"need"
result = re.sub(pattern,"love",string)
print(result)