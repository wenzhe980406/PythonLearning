# _*_ coding : UTF-8 _*_
# 开发人员 : ChangYw
# 开发时间 : 2019/8/28 14:29
# 文件名称 : 随机漫步.PY
# 开发工具 : PyCharm

from matplotlib import pyplot as plt
import random

class RandomWalk:
    dire = [-1,1]

    def __init__(self,limit=10000,max_step = 3):
        self.limit = limit
        self.x = [0]
        self.y = [0]
        self.max_step = max_step

    def walk(self):
        for _ in range(self.limit):
            current_x = self.x[-1]
            current_y = self.y[-1]
            x = random.choice(RandomWalk.dire) * random.randint(0, self.max_step)
            y = random.choice(RandomWalk.dire) * random.randint(0, self.max_step)
            while x== 0 ==y :
                x = random.choice(RandomWalk.dire) * random.randint(0, self.max_step)
                y = random.choice(RandomWalk.dire) * random.randint(0, self.max_step)
            self.x.append(current_x + x)
            self.y.append(current_y + y)


    def draw(self):
        plt.scatter(self.x[0],self.y[0],s=300,c="green")
        plt.scatter(self.x[-1], self.y[-1], s=300, c="red")
        plt.scatter(self.x,self.y,s= 30,c=list(range(0,self.limit + 1)),cmap =plt.cm.Blues,edgecolors='none')
        plt.show()

def main():
    rm = RandomWalk(limit=50000)
    rm.walk()
    rm.draw()

if __name__ == '__main__':
    main()
