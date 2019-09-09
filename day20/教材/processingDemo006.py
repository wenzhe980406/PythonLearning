# _*_ coding : UTF-8 _*_
# 开发人员 : longyh
# 开发时间 : 2019/8/9 15:27
# 文件名称 : processingDemo006.PY
# 开发工具 : PyCharm

import time
import multiprocessing

def f(q):
    q.put([time.asctime(), 'from Eva', 'hello'])  #调用主函数中p进程传递过来的进程参数 put函数为向队列中添加一条数据。

if __name__ == '__main__':
    # multiprocessing.freeze_support()
    q = multiprocessing.Queue() #创建一个Queue对象
    p = multiprocessing.Process(target=f(q)) #创建一个进程
    p.start()
    print(q.get())
    p.join()
