# _*_ coding : UTF-8 _*_
# 开发人员 : longyh
# 开发时间 : 2019/8/9 13:54
# 文件名称 : processingDemo002.PY
# 开发工具 : PyCharm

'''
进程之间的数据共享
用Manager传递数据，在进程间
'''

from multiprocessing import Process, Manager
import os

def show(aDict, aLst) :
    aDict['%s' %os.getpid()] = os.getpid()
    aLst.append(os.getpid())
    print(aDict, aLst, sep="\n **************************** \n")

if __name__ == '__main__' :

    with Manager() as manager:
         aDct = manager.dict(name='cyw', age=21)
         aLst = manager.list(range(1,5))

         p_list = []
         for i in range(1,10):
             p_list.append(Process(target=show, args=(aDct, aLst)))

         for p in p_list:
             print(p)
             p.start()

         for p in p_list:
             p.join()

         print('Main Process: ',aDct, aLst,sep='\n ================================ \n')

