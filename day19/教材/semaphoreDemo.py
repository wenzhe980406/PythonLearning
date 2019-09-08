# _*_ coding : UTF-8 _*_
# 开发人员 : longyh
# 开发时间 : 2019/8/8 14:46
# 文件名称 : semaphoreDemo.PY
# 开发工具 : PyCharm

import threading
import time


class MyThread(threading.Thread):
    def run(self):
        if semaphore.acquire():
            print(self.name)
            time.sleep(2)
            semaphore.release()


if __name__ == '__main__':
    semaphore = threading.BoundedSemaphore(5)
    thrs = []
    for i in range(100):
        thrs.append(MyThread())
    for i in thrs:
        i.start()

