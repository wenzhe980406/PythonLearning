# _*_ coding : UTF-8 _*_
# 开发人员 : ChangYw
# 开发时间 : 2019/9/5 14:55
# 文件名称 : day39HomeWork.PY
# 开发工具 : PyCharm
import matplotlib
import time
import pandas as pd
import matplotlib.pyplot as plt
import os

# 1\ 每个季度的平均骑行时间， 用柱状图表示
# 2\ 会员和非会员的每个季度平均时间，用折线图在一个图中表示，会员和非会员的折线图颜色不同
# 3\ 全年会员和非会员的比例 用饼状图表示。
# 4\ 统计不同用户骑行时间的直方图
# 5\ 不同用户类型季度平均骑行时间的分组柱状图

FILE_DIR = './bikeshare'
FILE_NAME_1 = '2017-q1_trip_history_data.csv'
FILE_NAME_2 = '2017-q2_trip_history_data.csv'
FILE_NAME_3 = '2017-q3_trip_history_data.csv'
FILE_NAME_4 = '2017-q4_trip_history_data.csv'

OUT_DIR = './out'

if not os.path.exists(OUT_DIR):
    os.makedirs(OUT_DIR)

start_time = time.time()

def get_file():
    mb_quarter_1 = pd.read_csv(os.path.join(FILE_DIR, FILE_NAME_1), usecols=[0, 1, 2, 8],header=0,names=['cyctime','star_time','end_time',"is_mem"])
    mb_quarter_2 = pd.read_csv(os.path.join(FILE_DIR, FILE_NAME_2), usecols=[0, 1, 2, 8],header=0,names=['cyctime','star_time','end_time',"is_mem"])
    mb_quarter_3 = pd.read_csv(os.path.join(FILE_DIR, FILE_NAME_3), usecols=[0, 1, 2, 8],header=0,names=['cyctime','star_time','end_time',"is_mem"])
    mb_quarter_4 = pd.read_csv(os.path.join(FILE_DIR, FILE_NAME_4), usecols=[0, 1, 2, 8],header=0,names=['cyctime','star_time','end_time',"is_mem"])
    return mb_quarter_1,mb_quarter_2,mb_quarter_3,mb_quarter_4


def get_avg_cyc(qua):
    return qua.cyctime.mean()/1000/60

def get_cyctime_and_show(mb_quarter_1,mb_quarter_2,mb_quarter_3,mb_quarter_4):
    avg_cyc = pd.DataFrame(
        [get_avg_cyc(mb_quarter_1), get_avg_cyc(mb_quarter_2), get_avg_cyc(mb_quarter_3), get_avg_cyc(mb_quarter_4)])
    avg_cyc.index = [1, 2, 3, 4]
    avg_cyc.plot(kind='bar')
    plt.xlabel("季度", fontproperties='SimSun')
    plt.ylabel("平均骑行时间", fontproperties='SimSun')
    plt.savefig(os.path.join(OUT_DIR, 'avg_cyctime.png'))
    plt.show()

def get_ismem_cyctime_and_show(mb_quarter_1,mb_quarter_2,mb_quarter_3,mb_quarter_4):
    mb_ismem_1 = mb_quarter_1.loc[:, ['cyctime', 'is_mem']]
    mb_ismem_2 = mb_quarter_2.loc[:, ['cyctime', 'is_mem']]
    mb_ismem_3 = mb_quarter_3.loc[:, ['cyctime', 'is_mem']]
    mb_ismem_4 = mb_quarter_4.loc[:, ['cyctime', 'is_mem']]

    mb_mem_1 = mb_ismem_1[mb_ismem_1.is_mem == 'Member']
    mb_cas_1 = mb_ismem_1[mb_ismem_1.is_mem == 'Casual']
    mb_mem_2 = mb_ismem_2[mb_ismem_2.is_mem == 'Member']
    mb_cas_2 = mb_ismem_2[mb_ismem_2.is_mem == 'Casual']
    mb_mem_3 = mb_ismem_3[mb_ismem_3.is_mem == 'Member']
    mb_cas_3 = mb_ismem_3[mb_ismem_3.is_mem == 'Casual']
    mb_mem_4 = mb_ismem_4[mb_ismem_4.is_mem == 'Member']
    mb_cas_4 = mb_ismem_4[mb_ismem_4.is_mem == 'Casual']

    avg_mem_cyctime = pd.DataFrame(
        [get_avg_cyc(mb_mem_1), get_avg_cyc(mb_mem_2), get_avg_cyc(mb_mem_3), get_avg_cyc(mb_mem_4)])

    avg_cas_cyctime = pd.DataFrame(
        [get_avg_cyc(mb_cas_1), get_avg_cyc(mb_cas_2), get_avg_cyc(mb_cas_3), get_avg_cyc(mb_cas_4)])

    avg_mem_cyctime.index = [1, 2, 3, 4]
    avg_cas_cyctime.index = [1, 2, 3, 4]
    # avg_mem_cyctime.plot(color='r')
    # avg_cas_cyctime.plot(color='g')
    plt.plot(avg_mem_cyctime, linewidth=2.5, linestyle='-', color='r')
    plt.plot(avg_cas_cyctime, linewidth=2.5, linestyle='-', color='g')
    plt.xlabel("季度", fontproperties='SimSun')
    plt.ylabel("平均骑行时间", fontproperties='SimSun')

    plt.savefig(os.path.join(OUT_DIR, 'avg_cyctime.png'))
    plt.show()

def get_ismem_ratio(mb_quarter_1,mb_quarter_2,mb_quarter_3,mb_quarter_4):
    # 3\ 全年会员和非会员的比例 用饼状图表示。
    # print(mb_quarter_1.count())
    mem_num = mb_quarter_1[mb_quarter_1.is_mem == 'Member'].count() + \
              mb_quarter_2[mb_quarter_2.is_mem == 'Member'].count() + \
              mb_quarter_3[mb_quarter_3.is_mem == 'Member'].count() + \
              mb_quarter_4[mb_quarter_4.is_mem == 'Member'].count()
    mem_num = mem_num['is_mem']

    cas_num = mb_quarter_1[mb_quarter_1.is_mem == 'Casual'].count() + \
              mb_quarter_2[mb_quarter_2.is_mem == 'Casual'].count() + \
              mb_quarter_3[mb_quarter_3.is_mem == 'Casual'].count() + \
              mb_quarter_4[mb_quarter_4.is_mem == 'Casual'].count()
    cas_num = cas_num['is_mem']

    print(mem_num, cas_num)
    ismem_ratio = pd.Series([mem_num / (mem_num + cas_num), cas_num / (mem_num + cas_num)], index=['会员', '非会员'],
                            name='series')
    # 解决汉字乱码问题
    matplotlib.rcParams['font.sans-serif'] = ['SimHei']
    ismem_ratio.plot.pie(figsize=(6, 6))
    plt.savefig(os.path.join(OUT_DIR, 'ismem_ratio.png'))
    plt.show()

def get_ismem_cyctime(mb_quarter_1,mb_quarter_2,mb_quarter_3,mb_quarter_4):
    # 4\ 统计不同用户骑行时间的直方图
    mem_sum = mb_quarter_1[mb_quarter_1.is_mem == 'Member'].cyctime.sum() + \
              mb_quarter_2[mb_quarter_2.is_mem == 'Member'].cyctime.sum() + \
              mb_quarter_3[mb_quarter_3.is_mem == 'Member'].cyctime.sum() + \
              mb_quarter_4[mb_quarter_4.is_mem == 'Member'].cyctime.sum()

    # mem_num = mem_num['is_mem']

    cas_sum = mb_quarter_1[mb_quarter_1.is_mem == 'Casual'].cyctime.sum() + \
              mb_quarter_2[mb_quarter_2.is_mem == 'Casual'].cyctime.sum() + \
              mb_quarter_3[mb_quarter_3.is_mem == 'Casual'].cyctime.sum() + \
              mb_quarter_4[mb_quarter_4.is_mem == 'Casual'].cyctime.sum()

    # cas_num = cas_num['is_mem']

    sum_is_mem_cyctime = pd.Series([mem_sum, cas_sum, cas_sum - mem_sum, cas_sum + mem_sum],
                                   index=['非会员骑行时间', '会员骑行时间', '相差时间', '总时间'],
                                   name='aaaa')
    # 解决汉字乱码问题
    matplotlib.rcParams['font.sans-serif'] = ['SimHei']
    sum_is_mem_cyctime.plot(kind='bar')
    plt.show()
    plt.savefig(os.path.join(OUT_DIR, 'sum_is_mem_cyctime.png'))

def get_mem_or_cas_avg_cyctime(mb_quarter_1,mb_quarter_2,mb_quarter_3,mb_quarter_4):
    # 5\ 不同用户类型季度平均骑行时间的分组柱状图
    mem_sum_1 = mb_quarter_1[mb_quarter_1.is_mem == 'Member']
    mem_sum_2 = mb_quarter_2[mb_quarter_2.is_mem == 'Member']
    mem_sum_3 = mb_quarter_3[mb_quarter_3.is_mem == 'Member']
    mem_sum_4 = mb_quarter_4[mb_quarter_4.is_mem == 'Member']

    cas_sum_1 = mb_quarter_1[mb_quarter_1.is_mem == 'Casual']
    cas_sum_2 = mb_quarter_2[mb_quarter_2.is_mem == 'Casual']
    cas_sum_3 = mb_quarter_3[mb_quarter_3.is_mem == 'Casual']
    cas_sum_4 = mb_quarter_4[mb_quarter_4.is_mem == 'Casual']

    sum_is_mem_cyctime = pd.Series(
        [get_avg_cyc(mem_sum_1), get_avg_cyc(cas_sum_1), get_avg_cyc(mem_sum_2), get_avg_cyc(cas_sum_2),
         get_avg_cyc(mem_sum_3), get_avg_cyc(cas_sum_3), get_avg_cyc(mem_sum_4), get_avg_cyc(cas_sum_4)],
        index=[1, 1, 2, 2, 3, 3, 4, 4], name='aaaa')
    # 解决汉字乱码问题
    matplotlib.rcParams['font.sans-serif'] = ['SimHei']
    sum_is_mem_cyctime.plot(kind='bar')
    plt.show()
    plt.savefig(os.path.join(OUT_DIR, 'sum_is_mem_cyctime.png'))

if __name__ == '__main__':
    start_time = time.time()
    mb_quarter_1,mb_quarter_2,mb_quarter_3,mb_quarter_4 = get_file()
    # get_cyctime_and_show(mb_quarter_1,mb_quarter_2,mb_quarter_3,mb_quarter_4)
    # get_ismem_cyctime_and_show(mb_quarter_1,mb_quarter_2,mb_quarter_3,mb_quarter_4)
    # get_ismem_ratio(mb_quarter_1,mb_quarter_2,mb_quarter_3,mb_quarter_4)
    # get_ismem_cyctime(mb_quarter_1, mb_quarter_2, mb_quarter_3, mb_quarter_4)
    # get_mem_or_cas_avg_cyctime(mb_quarter_1,mb_quarter_2,mb_quarter_3,mb_quarter_4)



    print('程序所用时间为：',time.time() - start_time)
