# _*_ coding : UTF-8 _*_
# 开发人员 : longyh
# 开发时间 : 2019/8/8 14:01
# 文件名称 : eventDemo001.PY
# 开发工具 : PyCharm

import threading
import enum
import time

event = threading.Event()

class TrafficColor(enum.Enum):
    GREEN = '绿灯'
    YELLOW = '黄灯'
    RED = '红灯'

class TrafficLight(threading.Thread):
    def __init__(self, tcolor, switchset):
        super().__init__()
        self.__traffic = tcolor
        self.green, self.yellow, self.red = switchset

    @property
    def traffic(self):
        return self.__traffic

    @traffic.setter
    def traffic(self, tc):
        self.__traffic = tc

    def run(self):
        count = 0
        while True:
            time.sleep(1)
            count += 1
            print("%s计数：%d" % (self.traffic.value, count))
            if (self.traffic == TrafficColor.GREEN) :
                if (count == self.green) :
                    print("信号灯要从%s变成%s了！" %(self.traffic.value, TrafficColor.YELLOW.value))
                    self.traffic = TrafficColor.YELLOW
                    count = 0
            elif (self.traffic == TrafficColor.YELLOW):
                if (count == self.yellow) :
                    print("注意：信号灯要从%s变成%s了！" %(self.traffic.value, TrafficColor.RED.value))
                    self.traffic = TrafficColor.RED
                    count = 0
            else :
                if (count == self.red) :
                    print("信号灯要从%s变成%s了！" %(self.traffic.value, TrafficColor.GREEN.value))
                    self.traffic = TrafficColor.GREEN
                    event.set()
                    event.clear()
                    count = 0

class Car(threading.Thread):
    def __init__(self, name, traffic_light):
        super().__init__()
        self.name = name
        self.traffic_light = traffic_light

    def run(self):
        while True :
            time.sleep(1)
            if (self.traffic_light.traffic == TrafficColor.GREEN):
                print(self.name, "心情好，跑得快，现在是绿灯。。。")
            elif (self.traffic_light.traffic == TrafficColor.YELLOW):
                print(self.name, "得赶紧的了，现在是黄灯。。。")
            else:
                print(self.name, "要停下来，现在是红灯。")
                event.wait()

if __name__ == "__main__":
    traffic_light = TrafficLight(TrafficColor.GREEN, (15, 10, 15))
    car = Car("特斯拉", traffic_light)
    traffic_light.start()
    car.start()









