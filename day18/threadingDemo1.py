# _*_ coding : UTF-8 _*_
# 开发人员 : ChangYw
# 开发时间 : 2019/8/7 15:51
# 文件名称 : threadingDemo1.PY
# 开发工具 : PyCharm
import random
import threading
import time

# SUM = 0
# MAX_TIME = 100000000
#
# class MyThread(threading.Thread):
#     def __init__(self, info):
#         super().__init__()
#         self.info = info
#
#     def run(self):
#         global SUM
#         for _ in range(MAX_TIME):
#             SUM += 1
#         print(threading.current_thread()," :Sum = ",SUM)
#
#
# if __name__ == '__main__':
#     start_time = time.time()
#     t1 = MyThread("Hello World!")
#     t2 = MyThread("Heelo Python!")
#     t1.start()
#     t2.start()
#     t1.join()
#     t2.join()
#
#     print("sum = ",SUM)
#     print("main : 当前存活的线程数目：%d !" % threading.active_count())
#     print("main threading ...........")
#     end_time = time.time()
#     print("运行时间：", start_time - end_time)


class MyThread(threading.Thread):
    def run(self):
        print("%d %s beginning!"%(threading.get_ident(),threading.current_thread().name))
        time.sleep(random.randint(1,3))
        print("main : 当前存活的线程数目：%d !" % threading.active_count())
        print(threading.current_thread()," ending.....")

if __name__ == '__main__':
    t_list = []
    start_time = time.time()
    for i in range(1,51):
        t = MyThread()
        t.setDaemon(True)#子线程跟随主线程
        t.start()

        t_list.append(t)

    for t in t_list:
        t.join()

    print("main : 当前存活的线程数目：%d !" % threading.active_count())
    print("main threading ...........")
    end_time = time.time()
    print("运行时间：",end_time - start_time)
