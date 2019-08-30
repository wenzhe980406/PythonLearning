# _*_ coding : UTF-8 _*_
# 开发人员 : ChangYw
# 开发时间 : 2019/8/6 0:55
# 文件名称 : test.PY
# 开发工具 : PyCharm
import random

#
# print([random.random() for _ in range(20)])


# import PIL
# from PIL import Image
#
# im = Image.open('枪战.jpg')
# im.show()

# class father:
#     x =1
#
# class child1():
#     pass
#
# class child2(father):
#     pass
#
# print(child1.x)#AttributeError

#
# l = []
# a = {'num' : 0}
# for i in range(10):
#     a['num'] = i
#     l.append(a)
# print(l)
#


class father:
    def __init__(self):
        pass


    def __new__(cls, *args, **kwargs):
        pass