# _*_ coding : UTF-8 _*_
# 开发人员 : ChangYw
# 开发时间 : 2019/8/12 15:34
# 文件名称 : tcpServer.PY
# 开发工具 : PyCharm
import hashlib
import os
import socket
import time

IP = "0.0.0.0"
PORT = 33333
ADDR = (IP,PORT)
BUFSIZE = 256

ERRORMSG = "命令无法执行"

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
                rlst = os.popen(received_msg)
                rlst_msg = rlst.read()
                if not rlst_msg:
                    print("收到了无法执行的命令！")
                    conn.send(ERRORMSG.encode("utf-8"))
                    continue

                rlst_msg_b = rlst_msg.encode("utf-8")
                rlst_md5 = hashlib.md5(rlst_msg_b).hexdigest()
                msg_info = "%s %d"%(rlst_md5,len(rlst_msg_b))

                # 6.1 发送消息大小给对方
                conn.send(msg_info.encode("utf-8"))
                ack = conn.recv(BUFSIZE)
                if "ACK" != ack.upper().decode("utf-8"):
                    print('暗号不对！')
                    break
                returned = "[%s]%s" % (time.ctime(),received_msg)
                conn.send(rlst_msg.encode("utf-8"))

                print("The execute over!")
            except ConnectionResetError as e :
                print("连接已释放，准备建立新的连接")
                break
    # 7.关闭套接字
    tcpServer.close()