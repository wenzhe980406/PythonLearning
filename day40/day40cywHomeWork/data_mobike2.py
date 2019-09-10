# _*_ coding : UTF-8 _*_
# 开发人员 : ChangYw
# 开发时间 : 2019/9/8 22:50
# 文件名称 : data_mobike2.PY
# 开发工具 : PyCharm

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


# 2\ 会员和非会员的每个季度平均时间
def get_mobike_data(FILE_DIR,FILE_NAME):
    for i in FILE_NAME:
        arr = pd.read_csv(os.path.join(FILE_DIR, i), low_memory=False, encoding='utf-8')
        yield arr.iloc[:, [0,-1]]


def clean_data(data):
    data_mem = []
    data_cas = []
    for i in data:
        data_mem.append(i[i['Member type'] == 'Member'])
        data_cas.append(i[i['Member type'] == 'Casual'])
    return data_mem,data_cas


def analyze_data(mem,cas):
    mem_list = [i.iloc[:,0].mean()/1000/60 for i in mem]
    cas_list = [i.iloc[:,0].mean()/1000/60 for i in cas]
    return mem_list,cas_list


# 用折线图在一个图中表示，会员和非会员的折线图颜色不同
def show_and_sava_data(mem,cas):
    plt.figure(figsize=(9, 6), dpi=80)
    plt.subplot(1, 1, 1)
    plt.rcParams['font.sans-serif'] = ['SimHei']
    x = list(range(1, len(mem) + 1))

    plt.plot(x, mem, label="会员", color="#9932CD")
    plt.plot(x, cas, label="非会员", color="#FF7F00")
    plt.title('每个季度的平均骑行时间')

    plt.xlabel('x轴')
    plt.ylabel('骑行时间')

    plt.xticks(x, ['第%d季度' % i for i in range(1, len(mem) + 1)])
    plt.yticks(list(range(0, 51, 10)))

    plt.legend()
    plt.savefig(os.path.join(OUT_DIR, 'avg_cyctime_type.png'))
    plt.show()


if __name__ == '__main__':
    start_time = time.time()
    # step 1 获得数据
    data_mobike_cyctime_type = get_mobike_data(FILE_DIR, FILE_NAME)

    # step 2 整理数据
    data_mem,data_cas = clean_data(data_mobike_cyctime_type)

    # step 3 分析数据
    mem_list,cas_list = analyze_data(data_mem,data_cas)

    # step 4 保存分析数据结果，分析结果的可视化
    show_and_sava_data(mem_list,cas_list)


    print('程序所用时间为：',time.time() - start_time)