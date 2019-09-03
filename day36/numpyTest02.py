# _*_ coding : UTF-8 _*_
# 开发人员 : ChangYw
# 开发时间 : 2019/9/2 16:08
# 文件名称 : numpyTest02.PY
# 开发工具 : PyCharm
import os

import numpy as np
from datetime import datetime
import matplotlib.pyplot as plt

DATA_DIR = './'
DATA_FILE = 'presidential_polls.csv'
OUT_DIR = './output'
if (not os.path.exists(OUT_DIR)):
    os.makedirs(OUT_DIR)


def is_float(num):
    try:
        float(num)
        return True
    except Exception:
        return False


def get_year_month(date_obj):
    return '%4d-%02d' % (date_obj.year, date_obj.month)


def collection_data(file,cols):
    return np.loadtxt(file,delimiter=',',dtype=str,skiprows=1,usecols=cols)


def clean_data(arr):
    vptime = np.vectorize(datetime.strptime)
    vis_float = np.vectorize(is_float)
    vget_year_month = np.vectorize(get_year_month)

    for i in range(1,5):
        arr = arr[vis_float(arr[:,i])]

    dates_arr = vptime(arr[:, 0], "%m/%d/%Y")
    data_str = vget_year_month(dates_arr)
    arr[:,0] = data_str
    return arr


def analysis_data(arr):
    year_month_arr = np.unique(arr[:,0])
    for y_m in year_month_arr:
        col_y_m = arr[:,0]
        filter_arr = arr[col_y_m == y_m]
        col_2_sum = filter_arr[:,1].astype('float').sum()
        col_3_sum = filter_arr[:,2].astype('float').sum()
        col_4_sum = filter_arr[:,3].astype('float').sum()
        col_5_sum = filter_arr[:,4].astype('float').sum()
        yield (y_m,col_2_sum,col_3_sum,col_4_sum,col_5_sum)


def save_and_show_data(ym,rawc,rawt,adjc,adjt):
    #保存数据
    data_arr = np.array([ym,rawc,rawt,adjc,adjt])
    np.savetxt(os.path.join(OUT_DIR,'./2016presidential.csv'),data_arr.T,fmt='%s %s %s %s %s',delimiter=',')
    #显示数据
    fig,subplot_arr = plt.subplots(2,2,figsize=(15,10))

    #raw 的数据展示在0,0区域
    subplot_arr[0,0].plot(rawc,color='r')
    subplot_arr[0,0].plot(rawt,color='g')

    #raw数据的UI比用直方图在0,1区域
    width = 0.25
    x = np.arange(len(ym))
    subplot_arr[0,1].bar(x,rawc,width,color='r')
    subplot_arr[0,1].bar(x + width, rawt, width, color='g')
    subplot_arr[0,1].set_xticks(x+width)
    subplot_arr[0,1].set_xticklabels(ym,rotation='vertical')

    # 调整后的趋势图
    subplot_arr[1, 0].plot(adjc, color='r')
    subplot_arr[1, 0].plot(adjt, color='g')

    # raw数据的UI比用直方图在1,1区域
    width = 0.25
    x = np.arange(len(ym))
    subplot_arr[1, 1].bar(x, adjc, width, color='r')
    subplot_arr[1, 1].bar(x + width, adjt, width, color='g')
    subplot_arr[1, 1].set_xticks(x + width)
    subplot_arr[1, 1].set_xticklabels(ym, rotation='vertical')

    plt.subplots_adjust(wspace=0.2)

    plt.savefig(os.path.join(OUT_DIR,'2016presidential.png'))
    plt.show()

if __name__ == '__main__':
    # step 1 获得数据
    usecols = [7,13,14,17,18]
    arr = collection_data(os.path.join(DATA_DIR,DATA_FILE),usecols)

    # step 2 整理数据
    arr = clean_data(arr)

    # step 3 分析数据
    ym_list = []    #year_month  -- x轴
    rawc_list = []  #raw clinton 数据
    rawt_list = []  #raw trump 数据
    adjc_list = []  #adjust后cliton 数据
    adjt_list = []  #adjust后trump 数据
    for y_m,raw_c,raw_t,adj_c,adj_t in analysis_data(arr):
        ym_list.append(y_m)
        rawc_list.append(raw_c)
        rawt_list.append(raw_t)
        adjc_list.append(adj_c)
        adjt_list.append(adj_t)

    # step 4 保存分析数据结果，分析结果的可视化
    save_and_show_data(ym_list,rawc_list,rawt_list,adjc_list,adjt_list)