# _*_ coding : UTF-8 _*_
# 开发人员 : ChangYw
# 开发时间 : 2019/7/30 17:04
# 文件名称 : class_test1.PY
# 开发工具 : PyCharm

#1)
class Restaurant():

    def __init__(self,restaurant_name,cuisine_type,number_served):
        self.name = restaurant_name
        self.type = cuisine_type
        self.served = number_served
        self.number_served = 0

    def describe_restaurant(self):
        msg = self.name + "提供美味的" + self.type
        print(msg)

    def open_restaurant(self):
        open_res = self.name + "正在营业"
        print(open_res)

    def set_num_served(self,eat_num):
        self.number_served = eat_num
        print(self.number_served)

    def increment_num_served(self,num):
        pass

lamian_restaurant = Restaurant("小小拉面馆","拉面",0)
print("餐馆中有%d个人来用餐过。"%lamian_restaurant.number_served)
lamian_restaurant.open_restaurant()
lamian_restaurant.describe_restaurant()
lamian_restaurant.set_num_served(10)