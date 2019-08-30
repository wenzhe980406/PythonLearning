# _*_ coding : UTF-8 _*_
# 开发人员 : ChangYw
# 开发时间 : 2019/7/23 15:09
# 文件名称 : def_demo1.PY
# 开发工具 : PyCharm

#python函数的五大要素
#def -- 定义一个函数所用到的关键字
#函数名 -- 给函数取一个标志符
#函数的参数  --实参，形参
#函数体 -- 函数要做的事，要执行的任务
#返回值 -- 函数执行完任务后的返回值

def my_func(a,b) :
    sum = a + b
    return sum


def print_func(s) :
    print(s)

def changyiwen() :
    pass

def my_abs(input_val):
    # if (input_val >= 0) :
    #     return input_val
    # else:
    #     return -input_val
    return input_val if input_val >= 0 else -input_val

sum_relt = my_func(1,2)
print(sum_relt)

val1 = my_abs(-5)
val2 = my_abs(3)
print(val1,val2)