# _*_ coding : UTF-8 _*_
# 开发人员 : ChangYw
# 开发时间 : 2019/8/8 14:43
# 文件名称 : semaphoraDemo.PY
# 开发工具 : PyCharm

'''
2.  queue --队列
    Queue -- FIFO
    LIFOQueue -- LIFO
    PRIORITYQueue -- 有优先级的队列

    put() --往队列中装值。当队列满的时候，就等着，直到队列中被取走了一个
    get() --往队列中取值。当队列空的时候，就等着，直到队列中被放入了一个

    from queue import Queue #LILO队列
    q = Queue() #创建队列对象
    q.put(0)    #在队列尾部插入元素
    q.put(1)
    q.put(2)
    print('LILO队列',q.queue)  #查看队列中的所有元素
    print(q.get())  #返回并删除队列头部元素
    print(q.queue)

    from queue import LifoQueue #LIFO队列
    lifoQueue = LifoQueue()
    lifoQueue.put(1)
    lifoQueue.put(2)
    lifoQueue.put(3)
    print('LIFO队列',lifoQueue.queue)
    lifoQueue.get() #返回并删除队列尾部元素
    lifoQueue.get()
    print(lifoQueue.queue)

    from queue import PriorityQueue #优先队列
    priorityQueue = PriorityQueue() #创建优先队列对象
    priorityQueue.put(3)    #插入元素
    priorityQueue.put(78)   #插入元素
    priorityQueue.put(100)  #插入元素
    print(priorityQueue.queue)  #查看优先级队列中的所有元素
    priorityQueue.put(1)    #插入元素
    priorityQueue.put(2)    #插入元素
    print('优先级队列:',priorityQueue.queue)  #查看优先级队列中的所有元素
    priorityQueue.get() #返回并删除优先级最低的元素
    print('删除后剩余元素',priorityQueue.queue)
    priorityQueue.get() #返回并删除优先级最低的元素
    print('删除后剩余元素',priorityQueue.queue)  #删除后剩余元素
    priorityQueue.get() #返回并删除优先级最低的元素
    print('删除后剩余元素',priorityQueue.queue)  #删除后剩余元素
    priorityQueue.get() #返回并删除优先级最低的元素
    print('删除后剩余元素',priorityQueue.queue)  #删除后剩余元素
    priorityQueue.get() #返回并删除优先级最低的元素
    print('全部被删除后:',priorityQueue.queue)  #查看优先级队列中的所有元素

    from collections import deque   #双端队列
    dequeQueue = deque(['Eric','John','Smith'])
    print(dequeQueue)
    dequeQueue.append('Tom')    #在右侧插入新元素
    dequeQueue.appendleft('Terry')  #在左侧插入新元素
    print(dequeQueue)
    dequeQueue.rotate(2)    #循环右移2次
    print('循环右移2次后的队列',dequeQueue)
    dequeQueue.popleft()    #返回并删除队列最左端元素
    print('删除最左端元素后的队列：',dequeQueue)
    dequeQueue.pop()    #返回并删除队列最右端元素
    print('删除最右端元素后的队列：',dequeQueue)
'''
import random
import threading
import enum
import time
from queue import Queue

event = threading.Event()
bun_list = ["豆沙包","鲜肉包","奶黄包","小笼包","灌汤包"]
customer_list = []
q = Queue()

class Customer(threading.Thread):
    def __init__(self,name):
        super().__init__()
        self.__name = name
        self.num = 0
        customer_list.append(self.__name)

    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self,name):
        self.__name = name

    def run(self):
        while True:
            customer = random.choice(customer_list)
            event.wait()
            eat_bun = q.get()
            print("%s吃了一个%s。"%(customer,eat_bun))


class Bun(threading.Thread):
    def __init__(self):
        super().__init__()
        self.__name = "龙老湿"
        self.__time = 2

    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, name):
        self.__name = name

    def run(self):
        print(self.__name + "开始做包子咯！")
        while True:
            bun = random.choice(bun_list)
            event.set()
            print("一个%s出笼了。"%bun)
            q.put(bun)
            time.sleep(random.randint(0,1))
            print("现在能吃的包子：",q.qsize())


if __name__ == '__main__':
    zhang = Customer("zhang")
    jiang = Customer("jiang")
    chang = Customer("chang")

    bun = Bun()
    bun.start()
    zhang.start()