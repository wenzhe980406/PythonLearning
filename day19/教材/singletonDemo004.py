# _*_ coding : UTF-8 _*_
# 开发人员 : Administrator
# 开发时间 : 2019/8/7 22:59
# 文件名称 : singletonDemo004.PY
# 开发工具 : PyCharm

class Singleton(type):
    _instances = {}

    def __call__(cls, *args, **kwargs):
        if cls not in cls._instances:
            cls._instances[cls] = super(Singleton, cls).__call__(*args, **kwargs)
        return cls._instances[cls]

class Person(metaclass=Singleton):
    pass


p1 = Person()
p2 = Person()
print(id(p1) == id(p2))