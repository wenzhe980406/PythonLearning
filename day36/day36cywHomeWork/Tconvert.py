# _*_ coding : UTF-8 _*_
# 开发人员 : ChangYw
# 开发时间 : 2019/9/2 22:46
# 文件名称 : Tconvert.PY
# 开发工具 : PyCharm
#Temperature converter
import os
import matplotlib.pyplot as plt
import numpy as np

CONV_DIR = './'
CONV_FILE = 'temp.csv'
OUT_DIR = './output'

if not os.path.exists(OUT_DIR):
    os.makedirs(OUT_DIR)

def t_conv(c):
    return 1.8 * float(c) + 32


def collection_conv(file):
    return np.loadtxt(file,delimiter=',',dtype=str,skiprows=1)


def clean_conv(arr):
    vt_re = np.vectorize(str.replace)
    vt_conv = np.vectorize(t_conv)
    arr[:,1] = vt_conv(vt_re(arr[:,1]," C",""))
    return arr


def analysis_conv(arr):
    vt_conv = np.vectorize(t_conv)
    arr[:,1] = vt_conv(arr[:,1])
    return arr


def save_show_conv(arr):
    m_list = arr[:,0].tolist()
    conv_list = arr[:,1].tolist()
    np.savetxt(os.path.join(OUT_DIR,'./Tconv.csv'),arr,fmt='%s %s',delimiter=',')

    fig, subplot_arr = plt.subplots(2, figsize=(15, 10))

    subplot_arr[0].plot(conv_list,color='r')

    width = 0.25
    x = np.arange(len(m_list))
    subplot_arr[1].bar(x,conv_list,width,color='r')
    subplot_arr[1].set_xticks(x+width)
    subplot_arr[1].set_xticklabels(m_list)

    plt.subplots_adjust(wspace=0.2)

    plt.savefig(os.path.join(OUT_DIR, 'Tconv.png'))
    plt.show()

if __name__ == '__main__':
    # 1 获取数据
    conv_arr = collection_conv(os.path.join(CONV_DIR,CONV_FILE))

    # 2 整理数据
    conv_arr = clean_conv(conv_arr)
    print(conv_arr)

    # 3 分析数据
    # conv_arr = analysis_conv(conv_arr)

    # 4 保存分析数据结果，分析结果的可视化
    save_show_conv(conv_arr)