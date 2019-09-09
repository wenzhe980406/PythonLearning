# _*_ coding : UTF-8 _*_
# 开发人员 : longyh
# 开发时间 : 2019/8/9 15:00
# 文件名称 : processingDemo004.PY
# 开发工具 : PyCharm

'''
进程锁

'''

from multiprocessing import Process, Lock


def f(lock, i):
    lock.acquire()   # win下有权限问题。。。
    print('hello world', i)
    lock.release()


if __name__ == '__main__':
    lock = Lock()

    for num in range(100):
        Process(target=f, args=(lock, num)).start()
