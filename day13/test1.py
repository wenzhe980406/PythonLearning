# _*_ coding : UTF-8 _*_
# 开发人员 : ChangYw
# 开发时间 : 2019/7/31 16:31
# 文件名称 : test1.PY
# 开发工具 : PyCharm
# from day12.class_test1 import Restaurant
#
#
# class IceCreamStand(Restaurant):
#     def __init__(self,restaurant_name,cuisine_type,number_served,flavors):
#         super().__init__(restaurant_name,cuisine_type,number_served)
#         self.flavors = flavors
#
#     def show_info(self):
#         print("%s现在正在售卖%s口味的冰淇淋"%(self.name,self.flavors))
#
#
# i = IceCreamStand("饮品店","甜品",50,"草莓")
# print(i.show_info())



#2)
# from day12.class_test import User
#
#
# class Admin(User):
#     def __init__(self,first_name,last_name,privileges):
#         super().__init__(first_name,last_name)
#         self.privileges = privileges
#
#     def show_privileges(self):
#         print(self.privileges)
#
#
# a = Admin("ad","min",["可以增加", "可以删除", "可以禁止用户"])
# a.show_privileges()


class Privileges:
    def __init__(self,privileges = ["可以增加", "可以删除", "可以禁止用户"]):
        self.privileges = privileges

    def show_privileges(self):
        print(self.privileges)