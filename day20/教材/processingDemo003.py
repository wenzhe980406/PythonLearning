# _*_ coding : UTF-8 _*_
# 开发人员 : longyh
# 开发时间 : 2019/8/9 14:24
# 文件名称 : processingDemo003.py.PY
# 开发工具 : PyCharm

'''
进程间的通讯 IPC --- 通过pipe实现IPC
'''

from multiprocessing import Process, Pipe
import os

def show(conn):
    received = conn.recv()
    print("received from : ", received)
    conn.send("This is a chatroom, welcom Chang.")
    print(os.getpid())
    conn.close()


if __name__ == '__main__':
    aConn, bConn = Pipe()

    b = Process(target=show, args=(bConn,))
    b.start()
    aConn.send("Hello, I am Chang！ ... from %d" %os.getpid())
    received = aConn.recv()
    print("Chang received : ", received)

    b.join()
