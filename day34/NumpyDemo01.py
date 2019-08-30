# _*_ coding : UTF-8 _*_
# 开发人员 : ChangYw
# 开发时间 : 2019/8/29 9:55
# 文件名称 : NumpyDemo01.PY
# 开发工具 : PyCharm

import numpy as np

if __name__ == '__main__':
    # #<class 'numpy.ndarray'>  nd多维的意思
    # arr = np.array([1,2,3,4])
    # print(arr)
    # print(type(arr))
    # print(arr.shape)
    # print(arr.ndim)
    # print(arr.dtype)

    # a = [0.1,0.2,0.3,0.4,0.5,0.6]
    # print(a)
    # arr = np.array(a)
    # print(arr.ndim)
    # print(arr.shape)
    # print(arr.dtype)
    # print(arr)
    #
    # arr1 = np.asarray(a)
    # print(arr1.ndim)
    # print(arr1.shape)
    # print(arr1.dtype)
    # print(arr1)
    #
    # #np.array 和 np.asarray 的区别，在于参数是ndarray时，np.arrat会产生新的复制数据，erasarray不会
    #
    # arr2 = np.array(arr)
    # arr3 = np.asarray(arr)
    # print(arr2)
    # print(arr3)
    # print(arr2 is arr3)
    # print(arr3 is arr)
    # print(arr2 is arr)



    aLst = [[1.0,2.0,3.0,4.0],[5.0,6.0,7.0,8.0]]
    arr = np.array(aLst)
    print(arr.ndim)
    print(arr.shape)
    print(arr.dtype)
    print(arr)


