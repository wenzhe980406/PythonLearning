# _*_ coding : UTF-8 _*_
# 开发人员 : ChangYw
# 开发时间 : 2019/8/9 16:03
# 文件名称 : processingDemo06.PY
# 开发工具 : PyCharm


from  multiprocessing import Process, Pool,freeze_support
import time
import os

def Foo(i):
    time.sleep(2)
    print("in process",os.getpid())
    return i + 100

def Bar(arg):
    print('-->exec done:', arg,os.getpid())

if __name__ == '__main__':
    # freeze_support()
    pool = Pool(processes=3) #允许进程池同时放入5个进程
    print("主进程",os.getpid())
    for i in range(10):
        # pool.apply_async(func=Foo, args=(i,), callback=Bar) #callback=回调
        # pool.apply(func=Foo, args=(i,)) #串行
        pool.apply_async(func=Foo, args=(i,)) #串行
    print('end')
    pool.close()
    pool.join() #进程池中进程执行完毕后再关闭，如果注释，那么程序直接关闭。.join()