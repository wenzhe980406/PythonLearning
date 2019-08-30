# _*_ coding : UTF-8 _*_
# 开发人员 : ChangYw
# 开发时间 : 2019/8/7 14:17
# 文件名称 : threadingDemo.PY
# 开发工具 : PyCharm

#创建线程
import threading
import time
import random

# def foo(info):
#     # 每个线程都会有个ID
#     print("线程ID:",threading.get_ident())
#     # 当前线程名字
#     print(threading.current_thread())
#     # 当前线程所在进程下，活的线程数目
#     print(threading.active_count())
#     print("%s : abcdef"%info)
#
# t = threading.Thread(target=foo,name="FirstThread",args=("first thread demo",))
# # t.start()
#
# def addnum():
#     m = 0
#     for i in range(1,101):
#         m += i
#     print("m: ",m)
#     # 每个线程都会有个ID
#     print("线程ID:", threading.get_ident())
#     # 当前线程名字
#     print(threading.current_thread())
#     # 当前线程所在进程下，活的线程数目
#     print(threading.active_count())
#
# t1 = threading.Thread(target=addnum,name="addNumThread" )
# t1.start()


#
# s_name = "常译文"
#
# def show(tname) :
#     print(tname,end=" : ")
#     while True:
#         for c in s_name:
#             print(c,end="")
#         print()
#
#
# #show("demo")
# threading.Thread(target=show,name = "C1",args=("thread-1",)).start()
# threading.Thread(target=show,name = "C2",args=("thread-2",)).start()


class MyThread(threading.Thread):
    def __init__(self,info):
        super().__init__()
        self.info = info


    def run(self):
        print(self.info)
        time.sleep(2)
        print("当前存活的线程数目：%d"%threading.active_count())
        print(threading.current_thread(),"  ending...")

if __name__ == '__main__':
    start_time = time.time()
    t1 = MyThread("Hello World!")
    t2 = MyThread("Heelo Python!")
    t1.start()
    t2.start()

    t1.join()
    t2.join()
    print("main : 当前存活的线程数目：%d !" % threading.active_count())

    print("main threading ...........")

    end_time = time.time()
    print("运行时间：",start_time-end_time)


