# _*_ coding : UTF-8 _*_
# 开发人员 : ChangYw
# 开发时间 : 2019/8/6 13:44
# 文件名称 : defaultdict.PY
# 开发工具 : PyCharm
from collections import defaultdict
#使用list作为default_factory,很容易将序列作为键值对加入字典
s = [('yellow',1),('blue',2),('yellow',3),('blue',4),('red',1)]
#当每个键第一次遇见时，它还没有在字典里面：所以条目自动创建，通过default_factory 方法，并返回一个空的list。
#list.append()操作添加值到这个新的列表里，当键再次被存取时，就正常操作，list.append()添加另一个值到列表中。

dfd = defaultdict(list)
for k,v in s :
    dfd[k].append(v)
print(dfd)

#↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑用dict的setdefault方法
d = {}
for k,v in s:
    d.setdefault(k,[]).append(v)

print(d.items())

s = 'mississippi'
#当一个字母首次遇到时，它就查询失败，所以default_factory调用int()来提供一个整数作为默认值
d = defaultdict(int)
for k in s :
    d[k] += 1
print(d)

#一个更快和灵活的方法是使用lambda函数，可以提供任何常量值
def constant_factory(value):
    return lambda :value

d = defaultdict(constant_factory('<missing>'))
d.update(name = "John",action = 'ran')
print(d)
print('%(name)s %(action)s to %(object)s' % d)

#设置default_factory 为set使defaultdict用于构建字典集合:
s = [('red',1),('blue',2),('red',3),('blue',4),('red',1),('blue',4)]
d = defaultdict(set)
for k,v in s:
    d[k].add(v)

print(d)