# _*_ coding : UTF-8 _*_
# 开发人员 : ChangYw
# 开发时间 : 2019/8/29 14:34
# 文件名称 : numpayDemo04.PY
# 开发工具 : PyCharm

import numpy as np
import random

# # #矢量化
# arr1 = np.random.randint(20,size=(2,3))
# arr2 = np.random.randint(20,size=(2,3))
# print(arr1)
# print(arr2)
#
# print("-"*30)
# # print(arr1 * arr2)
# print(arr1 + arr2)
# # print(arr1 - arr2)

# arr2 = np.array(range(1,9)).reshape(4,2)
# print(arr2)
# print(1/arr2)
# #
# # #广播 -- 矩阵和场数的运算
# # arr = np.arange(1,13)
# # print(arr)
# # print(arr + 5)
# # print(1/arr)
#
# arr = np.arange(1,13).reshape(3,4)
# # arr2 = arr > 6
# # # print(arr2)
# # # print(arr[arr2])
# # print(arr[arr>6])
#
# print(arr)
# aLst = [True,False,True]
# print(arr[aLst])

# #条件索引和花式索引
# arr = np.arange(1,33).reshape(8,4)
# #花式索引 -- 获取不连续的行或列
# # -- 给定需要求的行号的列表
# idx_list = [0,4,7]
# idx2_list = [0,2,3]
# print(arr[idx_list,idx2_list])

# #转置transpose 特殊的转置T
# arr = np.random.rand(2,3)
# print(arr)
# print(arr.transpose())
#
#
# arr3d = np.random.rand(2,3,4)
# print(arr3d)
# print("````````````````````"*10)
# print(arr3d.transpose((2,0,1)))

# #矩阵的*乘和.乘
# arr1 = np.array([random.randint(0,2) for _ in range(4)]).reshape((2,2))
# arr2 = np.array([random.randint(0,2) for _ in range(4)]).reshape((2,2))
#
# print(arr1,arr2,sep='\n\n')
# print('````````````````````````````')
# print(arr1 * arr2)
# print()
# print(arr1.dot(arr2))
# print("``````````````````````````````````````````````")
# print(np.dot(arr1,arr2))

# # 把矩阵拉直ravel
# a = np.floor(10 * np.random.random((3,4)))
# print(a)
# print()
# print(a.ravel())
# print()
# a.shape = (6,2)
# print(a)
# print()
# print(a.T)

# a = np.arange(0,12)
# print(a)
# print(a.reshape(3,-1))
# print(a.reshape(-1,6))

# a = [1,2,3]
# b = [4,5,6]
# c = [7,8,9]
# print(np.stack((a,b,c)))
# print(np.stack((a,b,c),axis=1))

# a = [['a1','a2','a3'],
#      ['a4','a5','a6']]
# b = [['b1','b2','b3'],
#      ['b4','b5','b6']]
# c = [['c1','c2','c3'],
#      ['c4','c5','c6']]
# print('堆叠,axis=0')
# print(np.stack((a,b,c)))
# print()
# print('堆叠,axis=1')
# print(np.stack((a,b,c),axis=1))
# print()
# print('堆叠,axis= 2')
# print(np.stack((a,b,c),axis=2))


a = np.array((1,2,3))
b = np.array((2,3,4))
print(a,b,sep='\n')
print()
print(np.hstack((a,b)))
print(np.vstack((a,b)))
print()
print(np.stack((a,b),axis=0))
print(np.stack((a,b),axis=1))
#
# a = np.random.randint(1,10,(2,2))
# b = np.random.randint(1,10,(2,2))
# print('生成的两个矩阵：')
# print(a,b,sep='\n\n')
# print()
# print(np.hstack((a,b)))
# print("*"*30)
