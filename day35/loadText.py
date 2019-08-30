# _*_ coding : UTF-8 _*_
# 开发人员 : ChangYw
# 开发时间 : 2019/8/30 16:12
# 文件名称 : loadText.PY
# 开发工具 : PyCharm

import numpy as np

# #loadtxt
# filename = 'presidential_polls.csv'
# data_array = np.loadtxt(filename,
#                         delimiter=',',
#                         dtype=str,
#                         usecols=(0,2,3))
# print(data_array.shape)

#loadtxt 明确指定每列数据的类型
filename = 'presidential_polls.csv'
data_array = np.loadtxt(filename,
                        delimiter=',',
                        skiprows=1,
                        dtype={'names': ('cycle', 'type', 'matchup'),
                               'formats': ('i4', 'S15', 'S50')},
                        usecols=(0,2,3))
print(data_array,data_array.shape)

#savetxt保存 np.savatxt('file',array,fmt='...',delimiter=None)
np.savetxt('demoSave.csv',data_array,fmt='%d %s %s',delimiter=',')

np.save('demoSave.npv',data_array)
data_arr = np.load('demoSave.npy')
print(data_arr,data_arr.shape)