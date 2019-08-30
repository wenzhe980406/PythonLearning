# _*_ coding : UTF-8 _*_
# 开发人员 : ChangYw
# 开发时间 : 2019/8/8 15:54
# 文件名称 : singleton.PY
# 开发工具 : PyCharm

# #单例模式1
def singleton(cls):
    instance = {}

    def getInstance(*args,**kwargs):
        if cls not in instance :
            instance[cls] = cls(*args,**kwargs)
        return instance[cls]
    return getInstance


#2
class Single():
    _instance = {}

    def __init__(self,_cls):
        self._cls = _cls

    def __call__(self, *args, **kwargs):
        if self not in self._instance:
            self._instance[self] = self(*args,**kwargs)
        return self._instance[self]


@Single   #Person = singleton(Person)
class Person:
    def __init__(self,name):
        self.name = name

if __name__ == '__main__':

    p1 = Person("chang")
    p2 = Person("zhang")
    print(p1,p2)



#3
class Single(object):
    _instance = None

    def __new__(cls, *args, **kwargs):
        if cls._instance == None:
            cls._instance = object.__new__(cls,*args,**kwargs)
        return cls._instance


def singleton(cls):
    instance = {}

    def getInstance(*args,**kwargs):
        if cls in instance:
            instance[cls] = cls(*args,**kwargs)
        return instance[cls]
    return getInstance()

