# _*_ coding : UTF-8 _*_
# 开发人员 : ChangYw
# 开发时间 : 2019/8/12 11:44
# 文件名称 : udpClientDemo.PY
# 开发工具 : PyCharm

import  socket

IP = "192.168.0.100"
PORT = 12345
ADDR = (IP,PORT)
BUFSIZE = 1024


if __name__ == '__main__':
    # 1. 创建套接字
    udpClient = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    # 2. 发送消息
    while True:
        msg = input(">>: ")
        if (not msg):
            break
        udpClient.sendto(msg.encode('utf-8'), ADDR)
        # 3. 接受消息
        received, conn = udpClient.recvfrom(BUFSIZE)
        # print('received response from ', conn)
        msg_len = int(received.decode())
        print("msg length = %d" %msg_len)
        received_msg_len = 0
        received_msg = ""
        udpClient.sendto("ACK".encode('utf-8'),conn)
        while received_msg_len < msg_len:
            received_msg_b, conn = udpClient.recvfrom(BUFSIZE)
            received_msg += received_msg_b.decode('utf-8')
            received_msg_len += len(received_msg_b)
        print("recieved ok!")
        print(received_msg)

    # 4. 关闭套接字
    udpClient.close()