# _*_ coding : UTF-8 _*_
# 开发人员 : ChangYw
# 开发时间 : 2019/8/9 15:02
# 文件名称 : processingDemo04.PY
# 开发工具 : PyCharm

#Lock 多进程的互斥锁
from multiprocessing import  Process,Lock


def f(lock,i):
    # lock.acquire() #win 下有权限问题。。。

    print("hello world",i)
    # lock.release()


if __name__ == '__main__':
    lock = Lock()

    for num in range(100):
        Process(target=f,args=(lock,num)).start()