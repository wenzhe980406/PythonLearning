# _*_ coding : UTF-8 _*_
# 开发人员 : ChangYw
# 开发时间 : 2019/8/9 11:40
# 文件名称 : processingDemo01.PY
# 开发工具 : PyCharm


'''
创建进程，
'''
import  multiprocessing
import  os
import time

sum = 0

def foo(num):
    print("in foo -->",os.getpid(),"-->>",os.getppid())
    global sum
    for i in range(num) :
        sum += i
    print(sum)
    time.sleep(1)

def goo(num):
    print("in foo -->",os.getpid(),"-->>",os.getppid())
    global sum
    for i in range(num):
        sum += i
    print(sum)
    time.sleep(1)

if __name__ == '__main__':
    print("pid -- :",os.getpid())
    p1 = multiprocessing.Process(target=foo,args=(100000,),name="jiang yizhong")
    p2 = multiprocessing.Process(target=foo,args=(100000,),name="liu jingdong")

    p1.start()
    p2.start()
    p1.join()
    p2.join()

    print(p1.pid,p1.name,p1.ident)
    print(p2.pid,p2.name,p2.ident)