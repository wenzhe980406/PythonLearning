# _*_ coding : UTF-8 _*_
# 开发人员 : ChangYw
# 开发时间 : 2019/7/23 16:33
# 文件名称 : def_test2.PY
# 开发工具 : PyCharm

# def make_shirt(size,typeface_name) :
#     print("this T-shirt'size: {},T-shirt:{}".format(size,typeface_name))


def make_shirt(size = "大号",typeface_name = "I love python!") :
    print("this T-shirt'size: {},T-shirt:{}".format(size, typeface_name))


def describe_city(city_name,country) :
    print("{} in {}".format(city_name,country))


make_shirt(30,"i love python")
make_shirt()
make_shirt(size = "中号")
make_shirt("小号","I love java")

describe_city('beijing','china')