# _*_ coding : UTF-8 _*_
# 开发人员 : ChangYw
# 开发时间 : 2019/8/9 15:08
# 文件名称 : processingDemo05.PY
# 开发工具 : PyCharm

'''
进程间的通讯，使用进程Queue
'''


from multiprocessing import Process, Queue
import multiprocessing, os

def show(qq):
    print("in child:", qq.qsize())
    print("获得父进程的id: ", qq.get())
    qq.put(os.getpid())
    qq.put(os.getppid())


if __name__ == '__main__':
    # multiprocessing.freeze_support()
    q = Queue()
    q.put(os.getpid())

    p = Process(target=show, args=(q,))
    # p = Process(target=show(q))
    p.start()
    p.join()

    while (not q.empty()):
        print(q.get())