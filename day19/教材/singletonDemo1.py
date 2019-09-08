# _*_ coding : UTF-8 _*_
# 开发人员 : longyh
# 开发时间 : 2019/8/8 15:54
# 文件名称 : singletonDemo1.PY
# 开发工具 : PyCharm

def singleton(cls):
    instance = {}

    def getInstance(*args, **kwargs):
        if (cls not in instance) :
            instance[cls] = cls(*args, **kwargs)
        return instance[cls]
    return getInstance


@singleton  # Person = singleton(Person)
class Person(object):
    def __init__(self, name):
        self.name = name

if __name__ == "__main__":
    p1 = Person('chang yiwen')
    p2 = Person('zhang wei')
    print(id(p1), id(p2))
    print(p1 is p2)
    print(p2.name)

