# _*_ coding : UTF-8 _*_
# 开发人员 : ChangYw
# 开发时间 : 2019/7/29 22:46
# 文件名称 : test.PY
# 开发工具 : PyCharm
# import json
import time
#
#
# def dump_file(sudoku_list):
#     with open("sudoku.json","w",encoding="utf-8") as w:
#         json.dump(sudoku_list,w)
#
#
# #读文件
# def load_file():
#     with open("sudoku.json","r",encoding="utf-8") as r:
#         student_dict = json.load(r)
#     return student_dict
#
# dump_file(sudoku_list = [
#                 [0, 0, 0, 0, 0, 0, 0, 0, 0],
#                 [0, 0, 0, 0, 0, 0, 0, 0, 0],
#                 [0, 0, 0, 0, 0, 0, 0, 0, 0],
#                 [0, 0, 0, 0, 0, 0, 0, 0, 0],
#                 [0, 0, 0, 0, 0, 0, 0, 0, 0],
#                 [0, 0, 0, 0, 0, 0, 0, 0, 0],
#                 [0, 0, 0, 0, 0, 0, 0, 0, 0],
#                 [0, 0, 0, 0, 0, 0, 0, 0, 0],
#                 [0, 0, 0, 0, 0, 0, 0, 0, 0]
# ])


def count_time(f):
    def inner():
        start_time = time.time()
        f()
        end_time = time.time()
        print("%s所用时间为：  --  %s"%(f.__name__,end_time - start_time))
    return inner

@count_time
def run():
    relst = []
    for i in range(10000):
        if not i % 2:
            relst.append(i)
    print(len(relst), relst[0], relst[-1])
    return relst