# _*_ coding : UTF-8 _*_
# 开发人员 : ChangYw
# 开发时间 : 2019/9/2 15:34
# 文件名称 : NumpyReview02.PY
# 开发工具 : PyCharm
import numpy as np

def thanAvg(score,avg_score):
    return score if score>avg_score else 0

if __name__ == '__main__':
    '''
    正态分布 np.random.normal(loc = 0.0,scale = 1.0,size = None)
    .loc 浮点数，分布的平均值
    .scale 浮点数，分布的标准差
    .size 整数或整数元素的元组，输出的数据个数
    '''
    g = np.random.normal(loc=0.0,scale=1.0,size=1000)
    g1 = np.random.randn(1000)

    #模拟得到物理成绩
    g = 20 + (100.1 - 20) * (g - g.min()) / 10
    phy = np.round(g,1)

    g1 = 20 + (100.1 -20) * (g1 - g1.min()) / 10
    mat = np.round(g1,1)

    phy_avg = np.mean(phy)
    mat_avg = np.mean(mat)

    thanAvg_ = np.frompyfunc(thanAvg,2,1)
    phy_arr1 = thanAvg_(phy,phy_avg)
    # print(phy_arr1)
    a_arr1 = thanAvg_(phy,mat_avg)
    print(a_arr1)


    marks = np.vstack((phy,mat))
    print(np.mean(marks,axis=1))
    print(np.mean(marks,axis=0))

    print((phy>60).sum())

    # print(marks)
    print(marks[:,marks[0]>marks[1]])
    print(marks[0]>marks[1])