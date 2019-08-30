# _*_ coding : UTF-8 _*_
# 开发人员 : ChangYw
# 开发时间 : 2019/8/12 15:34
# 文件名称 : tcpServer.PY
# 开发工具 : PyCharm


import socket
import time

IP = "0.0.0.0"
PORT = 33333
ADDR = (IP,PORT)
BUFSIZE = 256

if __name__ == '__main__':
    # 1. 创建socket套接字
    tcpServer = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
    # 2. 绑定ip和端口
    tcpServer.bind(ADDR)
    # 3. 监听端口
    tcpServer.listen(BUFSIZE)

    # 4. 做好准备  等待接收消息
    while True:
        print("准备接收消息。")
        conn,addr = tcpServer.accept()

        # 5. 接受消息
        while True:
            try:
                received = conn.recv(BUFSIZE)
                if not received:
                    print(addr, "hava lost connection...")
                    break
                print("received from",conn)
                received_msg = received.decode('utf-8')
                print("received msg:",received_msg)

                # 6. 发送消息
                returned = "[%s]%s" % (time.ctime(),received_msg)
                conn.send(returned.encode("utf-8"))
                print("send response!")
            except ConnectionResetError as e :
                print("连接已释放，准备建立新的连接")
                break
    # 7.关闭套接字
    tcpServer.close()