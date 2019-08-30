# _*_ coding : UTF-8 _*_
# 开发人员 : ChangYw
# 开发时间 : 2019/7/31 14:14
# 文件名称 : inherit_test3.PY
# 开发工具 : PyCharm


class Animal():
    def __init__(self,category):
        self.category = category


    def show_info(self):
        print("Im a annimal")


class Fish(Animal):
    def __init__(self,category,name):
        super().__init__(category)
        self.name = name

    def show_info(self):
        print("Im a fish,i have name :%s"%self.name)

class Food():
    def __init__(self,frag):
        self.frag = frag

    def show_info(self):
        print("Im having %s's smell")


class Shark(Food,Fish):
    def __init__(self,name,age):
        super().__init__(name)
        self.age = age


    def show_info(self):
        print("Im a %d'%s,and i'm having %s's smell,"%(self.age,self.name,self.farg))


s = Shark("nike","area",10)
s.show_info()


