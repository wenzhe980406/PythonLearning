# _*_ coding : UTF-8 _*_
# 开发人员 : ChangYw
# 开发时间 : 2019/7/23 15:35
# 文件名称 : def_test.PY
# 开发工具 : PyCharm

def display_message() :
    msg = "i'm learning python"
    print(msg)


def favorite_book(title) :
    print(title + " is one of my favorite books is Alice in Wonderland")


def addNum(num) :
    print("in addNum,num =", num)
    num += 1
    print("in addNum,num changed to : ", num)

# 必须参数
# 关键字传参
# def show_info(name,age) :
#     print("my name is {},and my age is {} old.".format(name,age))

# 默认值参数
# def show_info(name,age,national = "China") :
#     print("my name is {},and my age {} old,i came from {}.".format(name,age,national))

# 不定长参数
def sum(*args) :
    s = 0
    for i in args :
        s += i
    return s


def show_info(name,age,**kwargs) :
    print("name = ",name)
    print("age = ",age)
    for k,w in kwargs.items():
        print("{} = {}".format(k,w))


display_message()
favorite_book('huluwa')

a = 50
addNum(a)
print("Now a = ", a)

# show_info(age = "sunwokong",name = 500)
show_info(age = "sunwokong",name = 500)
show_info(age = "sunwokong",name = 500,national = "US")

s = sum(12,76,5,41,68,112,68,451,83,56,1588,158,55)
print(s)

show_info(name = "xunwukong",age = 800,kill = "jindouyun",weight = 80)

#python作用域
chang = "male"
if ("male" == chang) :
    a = 10

print(a)


#L E G B
chang = "male"

a = 10
def assignVAlue(chang):
    global  a
    if  "male" == chang :
        a = 20
    print("a = ",a)

assignVAlue(chang)
print(a)


a = 5
def outer():
    a = 10
    def inner():
        a = 20
        print("inner a = ", a)
    inner()

outer()
print('global a =',a )