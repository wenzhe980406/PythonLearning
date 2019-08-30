# _*_ coding : UTF-8 _*_
# 开发人员 : ChangYw
# 开发时间 : 2019/7/30 15:08
# 文件名称 : class_demo1.PY
# 开发工具 : PyCharm

#万物皆对象，对象都有类
#从程序员的角度，类就是数据和方法的封装
#所有的对象都是通过类产生的
class Person():
    #类具有的属性和方法
    #__init__() 可以暂时称为构造方法，用来初始化对象的属性

    #类属性的定义
    legs = 2


    def __init__(self,name,age,gender):
        # 对象已经创建之后，然后再把对象的属性初始化
        self.name = name
        self.age = age
        self.gender = gender
        self._height = 180
        self.__weight = 65  # 私有的属性，实际是python把私有属性换了个名字而已。 _类名__weight


    def show_info(self):
        print("信息    姓名：%s，年龄：%d，性别：%s"%(self.name,self.age,self.gender))
#使用定义好的类，创建对象
#因为要调用Person的__init__初始化对象的属性，所以，这里需要使用__init__的参数


#类的继承 -- 为了更好的复用某些功能
#面向对象的三大特性：

#继承
class Student(Person) :

    def __init__(self,name,age,gender):
        self.name = name
        self.age = age
        self.gender = gender


stu1 = Student("chang",21,"male")
stu1.show_info()




#
# chang = Person("cyw",21,"male")
# wu = Person("wmn",20,"female")
# print(chang.legs)
# print(chang._height)
# print(chang._Person__weight)
#
# Person.legs = 4
# print(Person.legs)
# print(chang.legs)
# print(wu.legs)
#
# wu.legs = 2
# print(Person.legs)
# print(wu.legs)
# print(chang.legs)



