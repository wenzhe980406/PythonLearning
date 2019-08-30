# _*_ coding : UTF-8 _*_
# 开发人员 : ChangYw
# 开发时间 : 2019/8/12 15:51
# 文件名称 : tcpClient.PY
# 开发工具 : PyCharm


import socket
import hashlib

IP = "192.168.1.240"
PORT = 12345
ADDR = (IP,PORT)
BUFSIZE = 1024

ERRORMSG = "命令无法执行"

if __name__ == '__main__':
    # 1. 创建socket套接字
    tcpClient = socket.socket(socket.AF_INET,socket.SOCK_STREAM)

    # 2. 建立和服务器的连接
    tcpClient.connect(ADDR)

    while True:
        # 3. 发送消息
        msg = input(">>:").strip()
        if not msg:
            break

        tcpClient.send(msg.encode("utf-8"))

        # 4. 接收消息
        msg_info_str = tcpClient.recv(BUFSIZE).decode("utf-8")
        print("received response:",msg_info_str)
        if ERRORMSG == msg_info_str :
            print(ERRORMSG)
            continue


        md5, msg_len_str = msg_info_str.split()
        msg_len = int(msg_len_str)

        # 会送一个确认消息
        tcpClient.send("ACK".encode("UTF-8"))
        received = ''
        received_len = 0
        md5_received = hashlib.md5()
        while received_len < msg_len:
            received_msg = tcpClient.recv(BUFSIZE)
            md5_received.update(received_msg)
            received_len += len(received_msg)
            received += received_msg.decode('utf-8', errors='ignore')
        if md5_received.hexdigest() == md5 :
            print(received)
        else:
            print("not ok",md5,md5_received)

    # 5. 关闭套接字
    tcpClient.close()