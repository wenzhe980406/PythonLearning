# _*_ coding : UTF-8 _*_
# 开发人员 : longyh
# 开发时间 : 2019/8/9 11:36
# 文件名称 : processingDemo.PY
# 开发工具 : PyCharm

'''
创建进程，进程的数据是彼此独立的。
'''
import multiprocessing
import os, time

sum = 0
def foo(num):
    global sum
    print("in foo -->", os.getpid(), " --->", os.getppid())
    print('num = ', num)
    for i in range(num):
        sum += 1
    print(sum)


def goo(num):
    global sum
    print("in goo -->", os.getpid(), " --->", os.getppid())
    print('num = ', num)
    for i in range(num):
        sum += 1
    print(sum)


if __name__ == "__main__":
    print('pid = ', os.getpid())
    p1 = multiprocessing.Process(target=foo,args=(1000000,), name='jiang yizhong')
    p2 = multiprocessing.Process(target=goo,args=(1000000,), name='liu jingdong')

    p1.start()
    p2.start()
    p1.join()
    p2.join()

    print(sum)

    print(p1.pid, p1.name, p1.ident)
    print(p2.pid, p2.name, p2.ident)

