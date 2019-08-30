# _*_ coding : UTF-8 _*_
# 开发人员 : ChangYw
# 开发时间 : 2019/7/31 11:20
# 文件名称 : class_.PY
# 开发工具 : PyCharm


# class Person():
#     def __init__(self,name,age):
#         self.__name = name
#         self.__age = age
#
#
#     #使用装饰器，访问属性更加简单
#     @property
#     def name(self):
#         return self.__age
#
#     @name.setter
#     def name(self,name):
#         if (isinstance(name, str)):
#             self.__name = name.title()
#
#
#     @property
#     def age(self):
#         return self.__age
#
#
#     @age.setter
#     def age(self,age):
#         if (isinstance(age,int)):
#             if (age < 150 and age > 0) :
#                 self.__age = age
#
#
#     def show_info(self):
#         print("my name is %s,and i am %d old"%(self.__name,self.__age))
#
# p = Person("wu minna", 22)
# p.name = "liu zhendong"
# print(p.name,p.age)
# p.age = 29
# p.show_info()


#python 类中的类方法和静态方法
class Animal():
    def __init__(self,category):
        self.__category = category


    @property
    def category(self):
        return self.__category


    @category.setter
    def category(self,category):
        self.__category = category


    def info(self):
        print("Category : " , self.category)


    @classmethod#类方法
    def show_myinfo(cls):
        print(type(cls),cls.__name__)
        print("I am an animal!")


    @staticmethod#静态方法
    def show():
        print("世界有多种动物，我要好好保护他们。")


pet = Animal("cat")

print(pet.category)
pet.category = "dog"

pet.info()

Animal.show_myinfo()
Animal.show()