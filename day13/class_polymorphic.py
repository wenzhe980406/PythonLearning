# _*_ coding : UTF-8 _*_
# 开发人员 : ChangYw
# 开发时间 : 2019/7/31 15:38
# 文件名称 : class_polymorphic.PY
# 开发工具 : PyCharm


#3鸭子类型 --python中的多态


 #有一只鸟，他走路像鸭子，有用像鸭子，它叫起来也像鸭子，它就是鸭子


#python中的魔术方法 / 魔法函数


class Classmate():
    def __init__(self,mates):
        self.mates = mates

    __slots__ = ["show","place","mates"]
    #实现了这个魔法函数，就可以把这个对象当做bool值
    def __bool__(self):
        return len(self.mates) != 0


    def __cmp__(self, other):
        if len(self.mates) > len(other.mates) :
            return 1
        elif len(self.mates) < len(other.mates) :
            return -1
        else:

            return 0


    # 实现了这个魔法函数，就可以对这个类产生的对象，使用len函数
    def __len__(self):
        return len(self.mates)


    #实现了这个魔法函数，就可以对这个类产生的UI想，使用str函数
    def __str__(self):
        print("".join(self.mates))
        return " ".join((self.mates))

    #实现了这个魔法函数，就可以对这个类产生的对象，使用repr函数
    def __repr__(self):
        return " / ".join(self.mates)


    #实现了这个魔法函数，就可以把这个类产生的对象，当做是可迭代对象
    def __getitem__(self, item):
        return self.mates[item]


    #
    def __del__(self):
        print("Bye Bye!")

python_class = Classmate(["liu qiangdong","shao zhikun","wu minna","zhang wei","chang yiwen","jiang yizhong"])
java_class = Classmate(["jia","yi","bing"])

print(len(python_class))
print(str(python_class))
print(repr(python_class))

for x in python_class:
    print(x)

print(python_class[::-1])

python_class.place = "杨浦区"
print(python_class.place)

python_class.show = lambda x:print(x)

python_class.show("刘京东")

print(Classmate.__dict__)