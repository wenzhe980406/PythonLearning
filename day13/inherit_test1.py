# _*_ coding : UTF-8 _*_
# 开发人员 : ChangYw
# 开发时间 : 2019/7/31 11:46
# 文件名称 : inherit_test1.PY
# 开发工具 : PyCharm

#1
#封装就是把相关的数据和操作这些数据的方法，把他们包装在一起
#2）  对于一个类而已，把数据隐藏，提供一个数据接口，

#2
#继承：继承可以最大实现代码的复用，父类提供了很多的属性和方法，子类可以更好的继承父类的属性和方法
#继承的弊端在于其间耦合性太强，它属于硬耦合,不要滥用。
#在python中也可以实现多继承，

#3 python 中的多态 class_polymorphic.PY


#test
class Person():

    def __init__(self,name,age,id,project):
        self.__name = name
        self.__age = age


    @property
    def name(self):
        return self.__name


    @name.setter
    def name(self,name):
        if (isinstance(name, str)):
            self.__name = name.title()


    @property
    def age(self):
        return self.__age


    @age.setter
    def age(self,age):
        if isinstance(age,int):
            if age < 150 and age > 0 :
                self.__age = age


    def show_info(self):
        print("my name is %s,and i am %d old"%(self.__name,self.__age))



class Student(Person):
    def __init__(self,name,age,id,project):
        super().__init__(self,name,age)
        self.__id = id
        self.__project = project


    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, name):
        if (isinstance(name, str)):
            self.__name = name.title()

    @property
    def age(self):
        return self.__age

    @age.setter
    def age(self, age):
        if isinstance(age, int):
            if age < 150 and age > 0:
                self.__age = age


    @property
    def id(self):
        return self.__id

    @id.setter
    def id(self, id):
        if isinstance(id, int):
            self.__id = id

    @property
    def project(self):
        return self.__project

    @project.setter
    def project(self, project):
        if isinstance(project, str):
            self.__name = project.title()

    def show_info(self):
        print("my name is %s,and i am %d old" % (self.__name, self.__age))
        print("my id is %d,and my project is %s"%(self.__id,self.__project))


s = Student("cyw",21,10004,"math")

s.show_info()