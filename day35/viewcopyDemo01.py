# _*_ coding : UTF-8 _*_
# 开发人员 : ChangYw
# 开发时间 : 2019/8/30 10:45
# 文件名称 : viewcopyDemo01.PY
# 开发工具 : PyCharm

import numpy as np




if __name__ == '__main__':
    # # 给变量另外一个别名
    # a = np.arange(12)
    # b = a
    # b.shape = 3, 4
    # print(a.shape)
    # print(id(a), id(b))
    # print(a is b)
    # print(a)
    #

    # #浅拷贝
    # a_arr = np.arange(1,10).reshape(3,3)
    # b_arr = a_arr.view()
    #
    # print(a_arr)
    # print(b_arr)
    # print(a_arr is b_arr)
    #
    # a_arr[1,0] = 400
    # print(a_arr)
    # print(b_arr)
    # print(id(a_arr),id(b_arr))

    # #深拷贝
    # a_arr = np.arange(1, 10).reshape(3, 3)
    # b_arr = a_arr.copy()
    # print(a_arr is b_arr)
    # a_arr[1,0] = 400
    # print(b_arr)
    # print(a_arr)

    # #元素级数组函数
    # #一元
    # #abs fabs -- fabs不处理复数（a+ib）
    # data = np.random.randn(4,3)
    # print(data)
    # #sign计算各元素的正负号 1正 0零 -1负
    # print(np.sign(data))
    # # print(np.abs(data))
    # print(np.fabs(data))

    # data = np.random.randn(2,3)
    # print(data)
    # print(np.ceil(data))#天花板值取整
    # print(np.floor(data))#地板值取整
    # print(np.rint(data))#四舍五入取整
    # print(np.isnan(data))#if isnum  :False

    # arr = np.random.randn(3,2)
    # print(arr)
    # print("max:",np.max(arr),sep="\n")
    # print("min:",np.min(arr),sep="\n")
    # print("*"*50)
    # print("np.maximum:", np.maximum(arr,0),sep="\n")
    # print("np.minimum:", np.minimum(arr, 0),sep="\n")
    # print("np.fmax:", np.fmax(arr, 0),sep="\n")
    # print("np.fmin:", np.fmin(arr, 0),sep="\n")

    # print('************************')
    # print("--------np.argmax 0轴----------------")
    # print(np.argmax(arr,0))
    # print(np.argmin(arr,0))
    # print("--------np.argmax 1轴----------------")
    # print(np.argmax(arr, 1))
    # print(np.argmin(arr,1))


    # #布尔索引和花式索引
    # arr = np.arange(28).reshape((7,4))
    # print(arr)
    # print()
    # names = np.array(['Ben','Tom','Ben','Jeremy','Jason','Michael','Ben'])
    # print(arr[names == 'Ben'])
    # print()
    # print(arr[names == 'Ben',3])
    # print()
    # print(arr[names == 'Ben',1:4])
    #
    #
    # print(arr[names != 'Ben'])
    #
    # print(arr[~(names == 'Jason')])
    #
    # print(arr[(names == 'Jason') | (names == "Tom")])
    # print(arr)
    #

    #花式索引
    # arr = np.array(['zero','one','two','three','four'])
    # print(arr[1:4])
    # print(arr[[1,4]])
    pass