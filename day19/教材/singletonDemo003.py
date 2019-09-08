# _*_ coding : UTF-8 _*_
# 开发人员 : Administrator
# 开发时间 : 2019/8/7 22:56
# 文件名称 : singletonDemo003.PY
# 开发工具 : PyCharm

class Single(object):
    _instance = None

    def __new__(cls, *args, **kw):
        if cls._instance is None:
            cls._instance = object.__new__(cls, *args, **kw)
        return cls._instance

    def __init__(self):
        pass

single1 = Single()
single2 = Single()
print(id(single1) == id(single2))