# _*_ coding : UTF-8 _*_
# 开发人员 : ChangYw
# 开发时间 : 2019/8/12 11:28
# 文件名称 : udpServerDemo.PY
# 开发工具 : PyCharm
import os
import socket
import time
#电脑上的mac地址和IP地址是通过ARP实现的

IP = "0.0.0.0"
PORT = 12345
ADDR = (IP,PORT)
BUFSIZE = 1024


if __name__ == '__main__':
    # 1. 创建一个socket套接字
    udpServer = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    # 2. 给创建的socket bind一个地址
    udpServer.bind(ADDR)

    while True:
        print('waiting for receiving msg ...')
        # 3. 接受客户端送来的消息
        received, conn = udpServer.recvfrom(BUFSIZE)
        if not received:
            print(conn, ' have lost connection....')
            break
        print('received from ', conn)
        received_msg = received.decode()
        print(received_msg)

        # 4. 向客户端发送消息
        result = os.popen(received_msg)
        res = result.read()
        res_b = res.encode('utf-8')
        msg_len = len(res_b)
        udpServer.sendto(str(msg_len).encode('utf-8'),conn)
        i = 0
        ack_msg, conn = udpServer.recvfrom(BUFSIZE)
        if ('ACK' != ack_msg.decode()):
            print('确认消息不正确。', ack_msg.decode())
            break
        for _ in range(msg_len//BUFSIZE):
            udpServer.sendto(res_b[i*BUFSIZE:(i+1)*BUFSIZE], conn)
            i += 1
        udpServer.sendto(res_b[i*BUFSIZE:], conn)

        # udpServer.sendto(res.encode('utf-8'), conn)

    # 5. 关闭socket套接字
    udpServer.close()
