# _*_ coding : UTF-8 _*_
# 开发人员 : ChangYw
# 开发时间 : 2019/9/9 23:54
# 文件名称 : data_mobike5.PY
# 开发工具 : PyCharm

import os
import time

import numpy as np
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


# 5\ 不同用户类型季度平均骑行时间的分组柱状图
def get_mobike_data(FILE_DIR,FILE_NAME):
    data_mem = []
    data_cas = []
    for i in FILE_NAME:
        arr = pd.read_csv(os.path.join(FILE_DIR,i),low_memory=False,encoding='utf-8')
        data_mem.append(arr[arr['Member type'] == 'Member'].iloc[:,0].mean() / 1000 / 60)
        data_cas.append(arr[arr['Member type'] == 'Casual'].iloc[:,0].mean() / 1000 / 60)
    # return pd.concat(data)
    return data_mem,data_cas


def show_and_sava_data(mem,cas):
    plt.figure(figsize=(9,6),dpi=80)
    plt.subplot = [1,1,1]
    plt.rcParams['font.sans-serif'] = ['SimHei']

    index = np.arange(len(mem))
    width = 0.35
    plt.bar(index,mem,width,label='会员',color='#87CEFA')
    plt.bar(index + width,cas,width,label='非会员',color='red')

    plt.ylabel('平均骑行时间(单位：分钟)')
    plt.title("柱状图")
    plt.xticks(index,("第%d季度"%(i+1) for i in index),rotation=45)
    plt.gca()
    plt.yticks(np.arange(0,51,10))
    plt.legend()
    plt.savefig(os.path.join(OUT_DIR, 'type_qua_cyctime.png'))
    plt.show()


if __name__ == '__main__':
    start_time = time.time()
    # step 1 获得数据
    data_mem,data_cas = get_mobike_data(FILE_DIR,FILE_NAME)
    print(data_mem,data_cas)
    # step 2 整理数据

    # step 3 分析数据

    # step 4 保存分析数据结果，分析结果的可视化
    show_and_sava_data(data_mem,data_cas)

    print("程序所用时间：",time.time() - start_time)