# _*_ coding : UTF-8 _*_
# 开发人员 : ChangYw
# 开发时间 : 2019/8/6 15:25
# 文件名称 : test1.PY
# 开发工具 : PyCharm
from collections import Counter
import re

with open("alice.txt",'r',encoding="utf-8") as f:
    english_word = f.read()


word_list = re.split("\W+",english_word,)
word_count = Counter(word_list)
print(word_count.most_common(10))