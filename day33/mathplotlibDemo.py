# _*_ coding : UTF-8 _*_
# 开发人员 : ChangYw
# 开发时间 : 2019/8/28 11:35
# 文件名称 : mathplotlibDemo.PY
# 开发工具 : PyCharm

from matplotlib import pyplot as plt


if __name__ == '__main__':
    # x = [1,2,3,4,5,6]
    # y = [i**2 for i in x]
    # #plot 折线图
    # #如果plot中只有一个参数，这个参数代表了Y轴的值
    # # plt.plot(y)
    # # 修改线条的粗细 -- 参数 linewidth
    # plt.plot(x,y,linewidth=5)
    # # 给图配置一个标题,并且可以指定标题的字体大小
    # plt.title('Square of Integer',fontsize = 24)
    # # 给x轴 y轴指定名字，也可以指定名字的字体大小
    # plt.xlabel('Numbers',fontsize = 20)
    # plt.ylabel('Squares',fontsize = 20)
    # plt.show()

    #y = x^2 + x + 1

    x = [i for i in range(100)]
    y = [i*i+i+1 for i in x]

    plt.plot(x,y,linewidth = 3)
    plt.title('计算y = x^2 + x + 1',fontsize = 12,fontproperties='SimSun')

    plt.xlabel('x轴',fontsize=15,fontproperties='SimSun')
    plt.ylabel('y轴',fontsize=15,)
    plt.show()