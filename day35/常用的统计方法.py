# _*_ coding : UTF-8 _*_
# 开发人员 : ChangYw
# 开发时间 : 2019/8/30 14:14
# 文件名称 : 常用的统计方法.PY
# 开发工具 : PyCharm

import numpy as np

# # sum 对数组总全部或某轴向的元素求和，零长度的数组sum为0
# arr = np.arange(10).reshape(5,2)
# print(arr)
#
# print(np.sum(arr))
# print(np.sum(arr,axis=0))
# print(np.sum(arr,axis=1))

# # mean 算数平均值， std， var 分别是标准差， 方差， 自由度可调（默认n）
# # max min 最大值，最小值， argmax, argmin 最大值，最小值得索引
# # cumsum 所有元素累计求和  cumprod 所有元素累计求积

# arr = np.random.randn(4,3)
# print(arr)
# print(arr.mean())
# print(np.mean(arr))
# print(arr.mean(axis=1))
# print(arr.sum(0))

# # 布尔值在统计方法中 会被强制转换为1或0
# # 正太分布的10*10矩阵中，统计大于0的数的个数
# arr = np.random.randn(10,10)
# print((arr>0).sum())


# np.all np.any

# arr = np.random.randn(2,3)
# print(arr)
#
# print(np.any(arr > 0))
# print(np.all(arr > 0))

# # 排序 sort
# arr = np.random.randn(10)
# print(arr)
# arr.sort()
# print(arr)
# print("*"*50)
#
# arr = np.random.randn(4,3)
# print(arr)
# print("`````````````np.sort 生成排序的副本：")
# brr = np.sort(arr,axis=1)
# print(brr)
# print(arr)
#
# print("`````````````数组的sort方法就地排序：")
# arr.sort(axis=1)
# print(arr)

#返回排序后的索引
# x = np.array([3,1,2])
# print(np.argsort(x)) #按升序排序，返回后的是对应的索引。
# print(np.argsort(-x))#按降序排序
# print()
# print(x[np.argsort(x)]) #通过索引值排序后的数组
# print(x[np.argsort(-x)])

# # np.unique
# arr = np.random.randint(5,size=10)
# print(arr)
# print(np.unique(arr))
# print(sorted(set(arr)))

# arr = np.array([[1,2,1],[2,3,4]])
# print(arr)
# print(arr.tolist())
#
# print(set(arr))
# print(np.unique(arr))
# print()

# arr = np.random.randint(5,size=10)
# arr1 = np.random.randint(5,size=10)
# print(arr)
# print(arr1)
#
# print("----------交集----------------")
# arr2 = np.intersect1d(arr,arr1)
# print(arr2)
# print("----------并集----------------")
# arr2 = np.union1d(arr,arr1)
# print(arr2)
# print("----------in----------------")
# arr2 = np.in1d(arr,arr1)
# print(arr2)
# print("----------差集x-y----------------")
# arr2 = np.setdiff1d(arr,arr1)
# print(arr2)


# # 数组文件的输入输出
# # np.save 和np.load ---保存的扩展名为.npy(默认，未压缩的原始二进制格式保存)
# arr = np.array(10)
# np.save("some_array",arr)
#
# arr1 = np.load("some_array.npy")
# print(arr1)