# _*_ coding : UTF-8 _*_
# 开发人员 : ChangYw
# 开发时间 : 2019/7/18 14:43
# 文件名称 : aggregate.PY
# 开发工具 : PyCharm

#choices补充
# import random
#
# aLst = list("ABCDEF")
# choiced = random.choices(aLst,weights=[0.05,0.2,0.2,0.3,0.1,0.15],k=3,)
# print(choiced)

#集合set --无序 不能重复
#创建set

# aSet = {1,}
# print(type(aSet))
#
# aSet = {1,5,3,7,2,5,1,7,6,3,2}
# print(aSet)
aSet = set("life is short,i need python")
# print(aSet)

#删除操作 remove discard pop
# x = aSet.pop()
# print(aSet,x)

# print('l' in aSet)
# aSet.remove('l')
# print('l' in aSet)
# aSet.remove('l')#删除不存在对象会报错
# print(aSet)

# aSet.discard('e')
# print(aSet)
# print('e' in aSet)

#set增加操作 add update
#add是把参数作为一个元素，增加到set中
#update 是把参数转换成了一个set，然后在和这个set合并
# aSet = set("python")
# aSet.add("hello")
# print(aSet)
# aSet.update("hello")
# print(aSet)

#集合的运算
#集合的交、并、差、对称差
s = set("Hello World")
t = set("youneedPython")

# print(s.intersection(t))
# #
# print(s.intersection(t),s&t)
#
print(s.union(t))

print(s.union(t),s|t)
#
# print(s.difference(t))
#
# print(s.difference(t),s-t)
#
# print(s.symmetric_difference(t),s^t)
