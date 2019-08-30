# _*_ coding : UTF-8 _*_
# 开发人员 : ChangYw
# 开发时间 : 2019/7/26 23:44
# 文件名称 : test.PY
# 开发工具 : PyCharm
# import random
#
# aList = [1,2,3,4,5,6,7,8,9]
# slice = str(random.sample(aList,1))
# a = ' '.join(slice)
# print(a)
import os

# sudoku_list = [
#                 [0, 0, 0, 0, 0, 0, 0, 0, 0],
#                 [0, 1, 0, 0, 0, 0, 0, 0, 0],
#                 [0, 0, 2, 0, 0, 0, 0, 0, 0],
#                 [0, 0, 0, 3, 0, 0, 0, 0, 0],
#                 [0, 0, 0, 0, 4, 0, 0, 0, 0],
#                 [0, 0, 0, 0, 0, 5, 0, 0, 0],
#                 [0, 0, 0, 0, 0, 0, 6, 0, 0],
#                 [0, 0, 0, 0, 0, 0, 0, 7, 0],
#                 [0, 0, 0, 0, 0, 0, 0, 0, 8]
# ]

# import os
# def file_name(file_dir):
#     for root, dirs, files in os.walk(file_dir):
#         print('root_dir:', root)  # 当前目录路径
#         print('sub_dirs:', dirs)  # 当前路径下所有子目录
#         print('files:', files)  # 当前路径下所有非目录子文件
#
#
# file_name('D:\stock_data')

# allpath=[]
# allname=[]
#
# def getallfile(path):
#     allfilelist=os.listdir(path)
#     # 遍历该文件夹下的所有目录或者文件
#     for file in allfilelist:
#         filepath=os.path.join(path,file)
#         # 如果是文件夹，递归调用函数
#         if os.path.isdir(filepath):
#             getallfile(filepath)
#         # 如果不是文件夹，保存文件路径及文件名
#         elif os.path.isfile(filepath):
#             allpath.append(filepath)
#             allname.append(file)
#     return allpath, allname
#
#
# if __name__ == "__main__":
#     rootdir = "."
#     files, names = getallfile(rootdir)
#     for file in files:
#         print(file)
#     print("-------------------------")
#     for name in names:
#         print(name)



import os

# txtPath = 'E:\\PythonFile\\day10\\'
txtType = 'txt'
txtLists = [i for i in os.listdir('E:\\PythonFile\\day10\\') if txtType in i]
print(txtLists[1][6])

