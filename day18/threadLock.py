# _*_ coding : UTF-8 _*_
# 开发人员 : ChangYw
# 开发时间 : 2019/8/7 16:52
# 文件名称 : threadLock.PY
# 开发工具 : PyCharm
import threading
#锁
# num = 0
# MAX_NUM = 1000000
#
# def foo():
#     global num
#     print(threading.current_thread().name, " beginning with num = ", num)
#     for _ in range(MAX_NUM):
#         lock.acquire()
#         num += 1
#         lock.release()
#     print(threading.current_thread().name," end with num = ",num)
#
#
# def goo():
#     global num
#     print(threading.current_thread().name, " beginning with num = ", num)
#     for _ in range(MAX_NUM):
#         lock.acquire()
#         num += 1
#         lock.release()
#     print(threading.current_thread().name, " end with num = ", num)
#
#
#
#
#
# lock = threading.Lock()
#
# t1 = threading.Thread(target=foo)
# t1.start()
# t2 = threading.Thread(target=goo)
# t2.start()
#
# t1.join()
# t2.join()
#
# print("main threading, sum = " ,num)






#死锁
import time


def foo():
    print(threading.current_thread().name, "ffff beginning")
    lock.acquire()
    time.sleep(1)
    lock.release()
    print(threading.current_thread().name,"ffff ending")
    return "foo"

def goo():
    print(threading.current_thread().name, "gggg beginning ")
    lock.acquire()
    time.sleep(1)
    lock.release()
    print(threading.current_thread().name, "gggg ending")
    return "goo"

def hoo():
    print(threading.current_thread().name, "hhhh beginning ")
    lock.acquire()
    ret1 = foo()
    print("between foo and goo")
    ret2 = goo()
    lock.release()
    print(threading.current_thread().name, "hhhh ending")
    print(ret1 , ret2)


if __name__ == '__main__':
    # lock = threading.Lock()     #死锁，会导致程序停顿，无法执行
    lock = threading.RLock()      #重入锁，决绝了死锁的问题

    start_time = time.time()
    t1 = threading.Thread(target=foo)
    t2 = threading.Thread(target=goo)
    t3 = threading.Thread(target=hoo)

    t1.start()
    t2.start()
    t3.start()

    t1.join()
    t2.join()
    t3.join()

    end_time = time.time()
    print("main thread end = ",end_time-start_time)