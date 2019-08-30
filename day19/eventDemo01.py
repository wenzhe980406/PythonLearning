# _*_ coding : UTF-8 _*_
# 开发人员 : ChangYw
# 开发时间 : 2019/8/8 13:54
# 文件名称 : 线程之间的通讯.PY
# 开发工具 : PyCharm

'''
#线程之间的通讯：
#1、 event
#    一个线程运行的时候，可以通过event.wait()等待。等到event被其他线程set了位置
    event.set()     -- 默认是False，set就改变了
    event.is_set()  -- 判断这个event是不是set状态
    event.wait()    --等待event的状态是True
    event.clear()   -- 清除event的状态
'''
import threading
import enum
import time


event = threading.Event()

class TrafficColor(enum.Enum):
    GREEN = "绿灯"
    YELLOW = "黄灯"
    RED = "红灯"

class TrafficLight(threading.Thread):
    def __init__(self,traffic,switchset):
        super().__init__()
        self.__traffic = traffic
        self.green,self.yellow,self.red = switchset

    @property
    def traffic(self):
        return self.__traffic

    @traffic.setter
    def traffic(self,traffic):
        self.__traffic = traffic

    def run(self):
        time.sleep(1)
        count = 0
        while True:
            count += 1

            print("%s计数：%d"%(self.traffic.value,count))
            if self.traffic == TrafficColor.GREEN :
                if count == self.green :
                    print("信号灯要从%s变成%s了"%(self.traffic.value,TrafficColor.YELLOW))
                    self.traffic = TrafficColor.YELLOW
                    count = 0

            elif(self.traffic == TrafficColor.YELLOW):
                if count == self.yellow:
                    print("信号灯要从%s变成%s了" % (self.traffic.value, TrafficColor.YELLOW))
                    self.traffic = TrafficColor.RED
                    count = 0
            else:
                if count == self.red:
                    print("信号灯要从%s变成%s了" % (self.traffic.value, TrafficColor.GREEN))
                    self.traffic = TrafficColor.GREEN
                    event.set()
                    event.clear()
                    count = 0


class Car(threading.Thread):
    def __init__(self,name,traffice_light):
        super().__init__()
        self.name = name
        self.traffice_light = traffice_light

    def run(self):
        while True:
            time.sleep(1)
            if self.traffice_light.traffic == TrafficColor.GREEN :
                print("心情好跑得快，现在是绿灯")
            elif self.traffice_light.traffic == TrafficColor.YELLOW :
                print("得抓紧了，现在是黄灯")
            else:
                print("要停下来，现在是红灯")
                event.wait()



if __name__ == '__main__':
    traffic_light = TrafficLight(TrafficColor.GREEN,(15,10,15))
    car = Car("特斯拉",traffic_light)
    traffic_light.start()
    car.start()