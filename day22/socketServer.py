# _*_ coding : UTF-8 _*_
# 开发人员 : ChangYw
# 开发时间 : 2019/8/13 13:37
# 文件名称 : socketServer.PY
# 开发工具 : PyCharm

import socketserver
import time

IP = "0,0,0,0"
PORT = 12345
ADRP = (IP,PORT)
BUFSIZE = 1024

class MyHandlerRequest(socketserver.BaseRequestHandler):
    def handle(self):
        while True:
            try:
                print("recevied from ",self.client_address)
                msg = self.request.recv(BUFSIZE)
                if not msg:
                    print("远端主机已经断开了连接。",self.client_address)
                print(msg)

                returned = "[%s]%s" % (time.ctime(),msg.decode("utf-8"))
                self.request.send(returned.encode("UTF-8"))
            except ConnectionResetError as e :
                print("远端客户已经断开了连接")
                break
            except Exception as e:
                print(e)
                break



if __name__ == '__main__':
    ss = socketserver.ThreadingTCPServer(ADRP,MyHandlerRequest)
    ss.server_forever()