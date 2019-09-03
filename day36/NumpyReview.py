# _*_ coding : UTF-8 _*_
# 开发人员 : ChangYw
# 开发时间 : 2019/9/2 11:08
# 文件名称 : NumpyReview.PY
# 开发工具 : PyCharm


import numpy as np

# da = np.arange(1,13).reshape((3,4))
#
# #生成全部是6.5的数组
# nums_arr = 6.5 * np.ones(da.shape)
# print(nums_arr)
# nums_arr = np.full(da.shape,6.5)
# print(nums_arr)
#
# # 指定对角线的值，其他值都是0
# # np.diag
# arr = np.diag([1,2,3,4])
# print(arr)
#
# arr = np.diag([1,2,3,4],k=-1)
# print(arr)

# arr = np.arange(1,17).reshape(4,4)
# arr1 = np.diag(arr)
# print(arr,arr1,sep='\n\n')
# print(np.diag(np.diag(arr)))
#
# darr1 = np.arange(1,100,3)
# print(darr1)
#
# # np.linspace(start=,stop=,num=,endpoint=True,retstep=False,dtype=None)
# darr2 = np.linspace(1,10,4,)
# print(darr2)
#
# #logspace(start, stop, num=50, endpoint=True, base=10.0, dtype=None,
#              # axis=0)
# sarr1 = np.logspace(2,3,num=4)
# print(sarr1)


# # np中，自定义数据类型
# # 参数是一个字典，name，这个字典的keys就必须是names和formats
# my_typel = np.dtype({
#     'names' :['book','version'],
#     'formats' :['S40' , np.int]
# })
#
# mybooks = np.array([('HeadFirst Python',4),('Python CookBook',3)],dtype=my_typel)
# print(mybooks)
# print(mybooks['book'])
# # print(mybooks[:2,1])
# mybooks[0]['book'] = 'yachengdabaisha'
# print(mybooks)

# #另外一种方式
# my_type2 = np.dtype(
#     [('book','S40'),('version',np.int)]
# )
#
# mybooks = np.array([('HeadFirst Python',4),('Python CookBook',3)],dtype=my_type2)
# print(mybooks)

# # from 系列创建数组
# s = 'Hello world'
# #offset偏移量
# print(np.frombuffer(s.encode('utf-8'),dtype='S1',count=5,offset=6))
#
# # fromfunction(function, shape, **kwargs)
# print(np.fromfunction(lambda x:x+1,(9,),dtype=np.int))
# print(np.fromfunction(lambda x,y:(x+1)*(y+1),(9,9),dtype=np.int))

#数组的变形
# arr = np.arange(10)
# print(arr)
# arr1 = arr.reshape((-1,1))
# arr2 = arr.reshape((1,-1))
# print(arr1)
# print(arr2)
#
# # np.newaxis 就是 None，切片的时候可以把某个轴设置为None
# data1 = arr[:,np.newaxis] # arr[:,None]
# print(data1)
# data2 = arr[np.newaxis,:] # arr[None,:]
# print(data2)
#
# arr[3] = 300
# print(arr)
# print(arr1)
# print(arr2)
# print(data1)
# print(data2)

# # 可以使用方法expand_dims 替代前面的操作
# data3 = np.expand_dims(arr,axis=0)
# print(data3)
# data4 = np.expand_dims(arr,axis=1)
# print(data4)

# # 数组的组合
# a = np.arange(9).reshape(3,3)
# b = np.arange(12).reshape(3,4)

# # a b 的shape不同，是不能使用stack的
# stack_arr = np.hstack((a,b))
# concatenate_arr = np.concatenate((a,b),axis=1)
# print(stack_arr)
# print(concatenate_arr)

# # 如果要把a和b进行垂直堆叠，怎么办？
# # a,b的列不同，不能直接垂直堆叠
# v_arr1 = np.vstack((a,b.T))
# v_arr2 = np.concatenate((a,b.T),axis=0)
# print(v_arr1)
# print(v_arr2)

# # np.dstack -- 深度组合
# a = np.arange(9).reshape(3,3)
# b = 3 * a
# print(a,b,sep='\n\n')
#
# #可以把a,b分别想象为两个平面，一上一下，然后沿着竖直方向组合上下对应的元素，形成三个垂直的面。
# # 这新的三个面就是新的数组
# dstack_arr = np.dstack((a,b))
# print(dstack_arr)

