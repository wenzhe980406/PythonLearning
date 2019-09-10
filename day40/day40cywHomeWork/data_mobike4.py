# _*_ coding : UTF-8 _*_
# 开发人员 : ChangYw
# 开发时间 : 2019/9/9 1:42
# 文件名称 : data_mobike4.PY
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


# 4\ 统计不同用户骑行时间的直方图
def get_mobike_data(FILE_DIR,FILE_NAME):
    data = []
    for i in FILE_NAME:
        arr = pd.read_csv(os.path.join(FILE_DIR, i), low_memory=False, encoding='utf-8')
        data.append(arr.iloc[:,[0,-1]])
        return pd.concat(data)


def clean_data(data):
    return data.groupby('Member type')


def analyze_data(data):
    mem_list = []
    # for i in mem:
    for i in data:
        print(i)
        mem_list.append(i[1].iloc[:,0]/1000/60)
    for i in mem_list:
        print(i)


def show_and_sava_data():
    pass


if __name__ == '__main__':
    start_time = time.time()
    # step 1 获得数据
    data_mobike_cyctime_type = get_mobike_data(FILE_DIR, FILE_NAME)

    # step 2 整理数据
    data_mobike_type_group = clean_data(data_mobike_cyctime_type)
    # for i in data_mobike_type_group:
    #     print(i)
    #     print('1111111111',type(i))

    # step 3 分析数据
    analyze_data(data_mobike_type_group)

    # step 4 保存分析数据结果，分析结果的可视化
    # show_and_sava_data(data_mobike_cyctime)

    print("程序所用时间：", time.time() - start_time)