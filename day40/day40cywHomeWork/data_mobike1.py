# _*_ coding : UTF-8 _*_
# 开发人员 : ChangYw
# 开发时间 : 2019/9/6 21:59
# 文件名称 : data_mobike1.PY
# 开发工具 : PyCharm

# 1\ 每个季度的平均骑行时间， 用柱状图表示


import os
import time
import pandas as pd
import matplotlib.pyplot as plt


FILE_DIR = '../bikeshare'
FILE_NAME = ['2017-q1_trip_history_data.csv',
             '2017-q2_trip_history_data.csv',
             '2017-q3_trip_history_data.csv',
             '2017-q4_trip_history_data.csv']

OUT_DIR = './out'

if not os.path.exists(OUT_DIR):
    os.makedirs(OUT_DIR)


def get_mobike_data(FILE_DIR,FILE_NAME):
    data = []
    for i in FILE_NAME:
        arr = pd.read_csv(os.path.join(FILE_DIR,i),low_memory=False,encoding='utf-8')
        data.append(arr.iloc[:,0].mean()/1000/60)
    # return pd.concat(data)
    return data


def show_and_sava_data(data):
    plt.figure(figsize=(6, 4),dpi=80)
    plt.subplot(1,1,1)
    plt.rcParams['font.sans-serif'] = ['SimHei']
    x = list(range(1,len(data)+1))
    width = 0.3
    plt.bar(x,data,width,label="骑行时间",color="#87CEFA")
    plt.title('每个季度的平均骑行时间')

    plt.xlabel('x轴')
    plt.ylabel('季度')

    plt.xticks(x,['第%d季度'%i for i in range(1,len(data)+1)])
    plt.yticks(list(range(0,31,10)))

    plt.legend()
    plt.savefig(os.path.join(OUT_DIR, 'avg_cyctime.png'))
    plt.show()


if __name__ == '__main__':
    start_time = time.time()
    # step 1 获得数据
    data_mobike_cyctime = get_mobike_data(FILE_DIR,FILE_NAME)

    # step 2 整理数据

    # step 3 分析数据

    # step 4 保存分析数据结果，分析结果的可视化
    show_and_sava_data(data_mobike_cyctime)

    print("程序所用时间：",time.time() - start_time)