# _*_ coding : UTF-8 _*_
# 开发人员 : ChangYw
# 开发时间 : 2019/8/29 10:34
# 文件名称 : numpyDemo02.PY
# 开发工具 : PyCharm
import numpy as np

#产生新的数组的方法

# 学习使用np.random产生多维数据
#1 np.random.rand  -- 生成[0,1)之间的随机数
# x = np.random.rand()
# print(x)
#
# data = np.random.rand(2, 3, 3)
# print(data)
# print(type(data))

# #2 np.random.randn --标准的正态分布的随机样本
# x = np.random.randn()
# print(x)
# data = np.random.randn(2,3,3)
# print(data)

# #3 随机整数 np.random.randint 注意，是一个半闭区间，前闭后开[a,b)
# x = np.random.randint(1,9)
# print(x)
# data = np.random.randint(5,size=10)
# print(type(data))
# print(data.ndim)
# print(data.shape)
# print(data)


# data = np.random.randint(1,9,size=(4,5))
# print(data)
# print(data.ndim)


#4 浮点型的随机数 np.random.rand np.random.ranf np.random.sample np.ranom.random_sample  一样
# print(np.random.ranf())
# arr1 = np.random.ranf(5)
# arr2 = np.random.ranf((5,))
# print(arr1)
# print(arr2)


# #5 np.arange() -- 生成连续的,指定范围的数值组成一维的ndarray
# arr1 = np.arange(1,9)
# arr2 = np.arange(9)
# arr3 = np.arange(0,9,2)
# print(arr1)
# print(arr2)
# print(arr3)


# #生成随机样本
# arr1 = np.random.choice(5,7)
# print(arr1.shape)
# print(arr1)
#
# arr2 = np.random.choice(10,5,replace=False)
# print(arr2)

# aList = ["梅西","C罗","内马尔","阿扎尔","苏亚雷斯"]
# players = np.random.choice(aList,3,p=[0.3,0.25,0.2,0.15,0.1],replace=False)
# print(players)

# # 数组打乱，类似洗牌 shuffle
# data = np.arange(1,10)
# print(data)
# np.random.shuffle(data)
# print(data)

# data = np.random.permutation(10)
# print(data)
# data = np.random.permutation(range(1,10))
# print(data)

# # 等差数列
# print(np.linspace(0,100,21,dtype = int))
#
# print(np.linspace(0,1,1001))


# #np.zeros  np.ones  np.empty
# arr1 = np.zeros((2,3),dtype=int)
# print(arr1)
#
# arr2 = np.ones((3,4),dtype=int)
# print(arr2)
#
# arr3 = np.empty((4,5))
# print(arr3)

# arr4 = np.eye(4,3,-1)
# print(arr4)
#
# arr5 = np.identity(4)
# print(arr5)

arr = np.random.randn(3,4)
arr_zero = np.zeros_like(arr)
zrr_one = np.ones_like(arr)
print(arr)
print('*'*30)
data = np.zeros_like(arr)

