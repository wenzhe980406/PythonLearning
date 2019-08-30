# _*_ coding : UTF-8 _*_
# 开发人员 : ChangYw
# 开发时间 : 2019/8/28 16:05
# 文件名称 : die_visual.PY
# 开发工具 : PyCharm
import pygal
from day33.die import Die

# die = Die()
#
# rslts = list()
# for roll_num in range(100):
#     rslt = die.roll()
#     rslts.append(rslt)
#
# frequences = list()
#
# for value in range(1,die.num_sides + 1):
#     frequency = rslts.count(value)
#     frequences.append(frequency)
#
# print(frequences)
#
#
# hist = pygal.Bar()
# hist.title = "Results of rolling one D6 1000 times"
# hist.x_labels = ["1","2","3","4","5","6"]
# hist.x_title = "Result"
# hist.y_title = "Frequency of Result"
#
# hist.add('D6',frequences)
# hist.render_to_file('die_visual.svg')


die_1 = Die()
die_2 = Die()

results = list()
for roll_num in range(1000):
    results.append(die_1.roll() + die_2.roll())

# 分析结果，把每个数字出现的频率统计出来，保存在一个列表中
frequences = list()

for value in range(2,die_1.num_sides + die_2.num_sides + 1):
    frequency = results.count(value)
    frequences.append(frequency)

# 对结果进行可视化
hist = pygal.Bar()
hist.title = "Results of rolling two D6 1000 times"
hist.x_labels = ["2", "3", "4", "5", "6", "7", "8", "9", "10", "11", "12"]
hist.x_title = "Result"
hist.y_title = "Frequency of Result"

hist.add('D6 + D6', frequences)
hist.render_to_file('dice_visual1.svg')