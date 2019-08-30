# _*_ coding : UTF-8 _*_
# 开发人员 : ChangYw
# 开发时间 : 2019/8/6 11:42
# 文件名称 : deque.PY
# 开发工具 : PyCharm
from collections import deque

dq = deque(['a','b','c'])
dq.append('x')
dq.appendleft('y')
print(dq)

d = deque('ghi')
for elem in d :
    print(elem.upper())
print("*" * 20)

d.append('j')
d.appendleft('f')
print(d)
print('*' * 20)

poped = d.pop()
print(poped)
list(d)
print(d[0],d[-1])
print("*" * 20)

print(list(reversed(d)))
print('h' in d)
d.extend('jkl')
print(d)
print('*' * 20)

d.rotate(1)
print(d)
d.rotate(-1)
print(d)
print(deque(reversed(d)))
print("*"*20)

d.clear()
#d.pop()
d.extendleft('abc')
print(d)