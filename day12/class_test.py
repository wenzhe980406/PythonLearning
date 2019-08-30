# _*_ coding : UTF-8 _*_
# 开发人员 : ChangYw
# 开发时间 : 2019/7/30 16:10
# 文件名称 : class_test.PY
# 开发工具 : PyCharm

# #1)
# class Restaurant():
#
#     def __init__(self,restaurant_name,cuisine_type):
#         self.name = restaurant_name
#         self.type = cuisine_type
#
#     def describe_restaurant(self):
#         msg = self.name + "提供美味的" + self.type
#         print(msg)
#
#     def open_restaurant(self):
#         open_res = self.name + "正在营业"
#         print(open_res)
#
#
# lamian_restaurant = Restaurant("小小拉面馆","拉面")
#
# lamian_restaurant.open_restaurant()
# lamian_restaurant.describe_restaurant()
#
# sichuan_restaurant = Restaurant("川菜馆","川菜")
# sichuan_restaurant.open_restaurant()
# sichuan_restaurant.describe_restaurant()
#
# steweb_restaurant = Restaurant("河南烩面馆","烩面")
# steweb_restaurant.open_restaurant()
# steweb_restaurant.describe_restaurant()

#2)
class User():
    def __init__(self,first_name,last_name):
        self.first_name = first_name
        self.last_name = last_name

    def describe_user(self):
        info = "用户的性别为：" + self.first_name + "\n用户的名字为：" + self.last_name
        print(info)


    def greet_user(self):
        hello = "hello " + self.first_name + self.last_name
        print(hello)

chang = User("Chang","Yiwen")
chang.greet_user()
chang.describe_user()

zhang = User("Zhang","Wei")
zhang.greet_user()
zhang.describe_user()
