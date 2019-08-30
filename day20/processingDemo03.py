# _*_ coding : UTF-8 _*_
# 开发人员 : ChangYw
# 开发时间 : 2019/8/9 14:25
# 文件名称 : processingDemo03.PY
# 开发工具 : PyCharm


"""
进程间的通讯 IPC ----通过pipe实现IPC
"""
import os
from multiprocessing import Process,Pipe

def show(conn):
    received = conn.recv()
    print("received from:",received)
    conn.send("this is a prison,Welcom Chang")
    print(os.getpid())
    conn.close()


if __name__ == '__main__':
    aConn , bConn = Pipe()
    b = Process(target=show,args=(bConn,))
    b.start()
    aConn.send("hello , im chang!")

    received = aConn.recv()
    print("chang recevied",received)

    b.join()