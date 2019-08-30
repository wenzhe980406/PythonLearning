# _*_ coding : UTF-8 _*_
# 开发人员 : ChangYw
# 开发时间 : 2019/7/30 11:36
# 文件名称 : def_demo.PY
# 开发工具 : PyCharm

#生成器 -- 就是根据需要生成数据，而不是一股脑的把数据给你。

# aLst = [x for x in range(10)]
#
# if __name__ == '__main__':
#     g = (x for x in range(10))
#
#     while True :
#         print(g.__next__())


#斐波拉契数列 --- 兔子数列
#r1r2r3
# 0 1 1 2 3 5 8 13 21 34 55


# #生成器
# def rabbit(n):
#     r1,r2 = 0 ,1
#     for i in range(int(n)):
#         r1,r2 = r2,r1 + r2
#         yield r2
#
# g = rabbit(10)
# print(g)
#
# for i in range(10):
#     fabo_num = next(g)
#     print(fabo_num)

# #协程
import random
import time
#

def customer(name):
    print(name + "等着吃包子！")
    while True:
        bun = yield
        print(name + "吃了一个" + bun)

def bun_shop(name):
    chang = customer("cyw")
    zhang = customer("zw")
    jiang = customer("jzy")
    customer_list = [chang,zhang,jiang]
    for i in customer_list:
        next(i)

    while True:
        print(name + "开始坐包子咯！")
        time.sleep(random.randint(1,3))
        bun_list = ["豆沙包","鲜肉包","奶黄包","小笼包","灌汤包"]
        bun = random.choice(bun_list)
        print("一个%s出笼了。"%bun)
        cust = random.choice(customer_list)
        cust.send(bun)

bun_shop("龙老师")
