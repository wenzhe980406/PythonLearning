# _*_ coding : UTF-8 _*_
# 开发人员 : ChangYw
# 开发时间 : 2019/7/31 13:50
# 文件名称 : inherit_test2.PY
# 开发工具 : PyCharm

class Person():

    def __init__(self,name,age):
        self.name = name
        self.age = age

    def look(self):
        print("%s正在专注的看Python"%self.name)

    def walk(self):
        print("%s正在散步")


    @classmethod
    def info(cls):
        print("这是一个人")


    @staticmethod
    def show():
        print("龙老师讲python")

class Student(Person):
    def __init__(self,name,age,sno,subj):
        super.__init__(name,age)
        self.sno = sno
        self.subj = subj

    def look(self):
        print("%s注意力不集中了"%self.name)

    def study(self):
        print("%d岁的%s正在教室学习%s，面容专注。"%(self.age,self.name,self.subj))


chang = Student("cyw",21,16011407,"Python")

print(chang.study())