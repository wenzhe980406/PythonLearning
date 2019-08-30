# _*_ coding : UTF-8 _*_
# 开发人员 : ChangYw
# 开发时间 : 2019/8/6 15:04
# 文件名称 : Counter.PY
# 开发工具 : PyCharm
from collections import Counter

c = Counter()
print(c)
c = Counter('gallahad')
print(c)
c = Counter({'red' : 4,'blue' : 2})
print(c)
c = Counter(cats = 4,dogs = 8)
print(c)


#Counter对象有一个字典接口，如果引用的键没有任何记录，就返回一个0，而不是弹出一个KeyError：
c = Counter(['eggs','ham'])
print(c)
print(c['bacon'])

c['sausage'] = 0
print(c)
del c['sausage']
print(c)

#elements()返回一个迭代器，每个元素重复计数的个数。元素顺序是任意的。如果一个元素的计数小于1，elements()就会忽略它。

c = Counter(a = 4,b = 2,c = 0,d = -2)
print(sorted(c.elements()))


#most_common([n])返回一个列表，提供n个频率最高的元素和计数
#如果没提供n，或者是None，most_common()返回计数器中的所有元素。相等个数的元素顺序随机：
Counter('abracadabra').most_common(3)

#subtract([iterable-or-mapping]) 从迭代对象或映射对象减去元素。像dict.update()但是减去，而不是替换。
c = Counter(a = 4,b = 2,c = 0, d = -2)
d = Counter(a = 1,b = 2,c = -3, d = 4)
c.subtract(d)
print(c)

#Counter 对象的常用案例
print(c.values())
#total of all counts
print(sum(c.values()))

#reset all counts
d.clear()
print(c)

#list unique lements
print(list(c))
