# _*_ coding : UTF-8 _*_
# 开发人员 : ChangYw
# 开发时间 : 2019/9/9 1:42
# 文件名称 : data_mobike3.PY
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

# 3\ 全年会员和非会员的比例 用饼状图表示。
def get_mobike_data(FILE_DIR, FILE_NAME):
    data = []
    for i in FILE_NAME:
        arr = pd.read_csv(os.path.join(FILE_DIR, i), low_memory=False, encoding='utf-8')
        data.append(arr.iloc[:, -1])
    return pd.concat(data)


def clean_data(data):
    data_mem = data[data == 'Member']
    data_cas = data[data == 'Casual']
    return data_mem,data_cas


def analyze_data(mem,cas):
    return mem.count(),cas.count()


def show_and_sava_data(mem,cas):
    plt.figure(figsize=(6,4),dpi=80)
    plt.subplot(1,1,1)
    plt.rcParams['font.sans-serif'] = ['SimHei']
    plt.title('会员与非会员比例')
    labels = ['会员','非会员']
    sizes = [mem,cas]
    color = ['#4fc4aa','#dd5555']
    explode = [0.05,0]
    plt.pie(sizes,explode=explode,colors=color,labels=labels,autopct='%1.1f%%',shadow=False)
    plt.axis('equal')
    plt.legend()
    plt.savefig(os.path.join(OUT_DIR, 'mem_cas_ratio.png'))
    plt.show()


if __name__ == '__main__':
    start_time = time.time()
    # step 1 获得数据
    data_mobike_type = get_mobike_data(FILE_DIR, FILE_NAME)
    # print(data_mobike_type)

    # step 2 整理数据
    data_mem,data_cas = clean_data(data_mobike_type)
    # print(data_mem,data_cas)
    # print(data_mem.count(),data_cas.count())


    # step 3 分析数据
    mem_num,cas_num = analyze_data(data_mem,data_cas)

    # step 4 保存分析数据结果，分析结果的可视化
    show_and_sava_data(mem_num,cas_num)


    print('程序所用时间为：',time.time() - start_time)