# _*_ coding : UTF-8 _*_
# 开发人员 : Administrator
# 开发时间 : 2019/8/7 22:51
# 文件名称 : singletonDemo002.PY
# 开发工具 : PyCharm

class Singleton(object):
    def __init__(self, cls):
        self._cls = cls
        self._instance = {}

    def __call__(self, *args, **kwargs):
        if self._cls not in self._instance:
            self._instance[self._cls] = self._cls(*args, **kwargs)
        return self._instance[self._cls]

@Singleton   # Person = Singleton(Person)
class Person(object):
    def __init__(self):
        pass


p1 = Person()
p2 = Person()
print(id(p1) == id(p2))
print(p1 is p2)
