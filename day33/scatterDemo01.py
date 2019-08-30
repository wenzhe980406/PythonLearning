# _*_ coding : UTF-8 _*_
# 开发人员 : ChangYw
# 开发时间 : 2019/8/28 13:50
# 文件名称 : scatterDemo01.PY
# 开发工具 : PyCharm

from matplotlib import pyplot as plt

if __name__ == '__main__':
    x = [i for i in  range(1,1001)]
    y = [i**2 for i in x]
    # 散点图    通过edgecolor空值点的边缘颜色
    plt.scatter(x,y,s=30,edgecolors='none',c=y)
    plt.xlabel("X轴",fontproperties = 'SimSun',fontsize = 18)
    plt.ylabel("Y轴",fontproperties = 'SimSun',fontsize = 18)
    plt.title("y = x^2",fontproperties = 'SimSun',fontsize = 24)
    # 指定坐标轴刻度标记的大小
    plt.tick_params(axis='both',which='major',labelsize=14)
    # 指定x轴和y轴的范围
    plt.axis([0,1100,0,110000])
    plt.show()

