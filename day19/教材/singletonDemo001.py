# _*_ coding : UTF-8 _*_
# 开发人员 : Administrator
# 开发时间 : 2019/8/7 22:38
# 文件名称 : singletonDemo001.PY
# 开发工具 : PyCharm

def singleton(cls):
    instances = {}

    def getinstance(*args, **kw):
        if cls not in instances:
            # instances[cls] = cls(*args, **kw)
            instances.setdefault(cls, cls(*args, **kw))
        return instances.get(cls)

    return getinstance

@singleton
class Person(object):
    def __init__(self):
        pass

p1 = Person()
p2 = Person()

print(id(p1))
print(id(p2))
