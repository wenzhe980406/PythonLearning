# _*_ coding : UTF-8 _*_
# 开发人员 : ChangYw
# 开发时间 : 2019/8/29 13:50
# 文件名称 : numpaydemo03.PY
# 开发工具 : PyCharm

import numpy as np

# # 多维数组的属性dtype
#
# zeros_arr_float = np.zeros((3,4),dtype=np.float64)
# print(zeros_arr_float)
# print(zeros_arr_float.dtype)
#
# # 转换ndarray的数据类型 --astype  生成一个新的数据类型
# zeros_arr_int = zeros_arr_float.astype(np.int32)
# print(zeros_arr_int)
#
# # ndim 和 shape
# arr1 = np.arange(12)
# print(arr1)
# #arr.shape  (12,)
# arr1.shape = (3,4)
# print(arr1)
# arr1.shape = (2,3,2)
# print(arr1)
# #提供了一个方法  reshape -- 改变数组的维度数目
# arr = np.arange(1,13).reshape(3,4)
# print(arr)

# # 多维数组数据的操作
# arr1 = np.arange(12)
# for i in arr1:
#     print(i)
# print(len(arr1))
# arr2 = np.arange(12).reshape(2,6)
# for i in arr2:
#     for j in i:
#         print(j)
# print(len(arr2))

# # 对多维数组数据的访问
# arr1 = np.arange(12)
# print(arr1[6])
# print(arr1[:2])
# print(arr1[-2:])

# arr2 = np.arange(12).reshape(3,4)
# # # 取单个
# print(arr2)
# # print(arr2[1,2])
# #
# # #取一行
# # print(arr2[1])
# # print(arr2[:2,:2])
# #
# # #取一列 #取一列得到的是一维数组
# # print(arr2[:,3])
# # #取一列，得到的是二维数组
# # print(arr2[:,-1:])
# #取一部分  行列都进行切片
# print(arr2[-2:,-2:])


