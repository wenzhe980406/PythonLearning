# _*_ coding : UTF-8 _*_
# 开发人员 : ChangYw
# 开发时间 : 2019/8/12 15:51
# 文件名称 : tcpClient.PY
# 开发工具 : PyCharm


import socket

IP = "192.168.1.240"
PORT = 12345
ADDR = (IP,PORT)
BUFSIZE = 256


if __name__ == '__main__':
    # 1. 创建socket套接字
    tcpClient = socket.socket(socket.AF_INET,socket.SOCK_STREAM)

    # 2. 建立和服务器的连接
    tcpClient.connect(ADDR)

    while True:
        # 3. 发送消息
        msg = input(">>:").strip()

        tcpClient.send(msg.encode("utf-8"))
        if "Q" == msg.upper():
            break

        # 4. 接收消息
        received = tcpClient.recv(BUFSIZE)
        print("received response:",received.decode("utf-8"))

    # 5. 关闭套接字
    tcpClient.close()