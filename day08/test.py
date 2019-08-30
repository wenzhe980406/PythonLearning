# _*_ coding : UTF-8 _*_
# 开发人员 : ChangYw
# 开发时间 : 2019/7/24 10:30
# 文件名称 : test.PY
# 开发工具 : PyCharm
import json

student_score_dict ={
        "1000" : {
            "name" :'cyw',
            "English成绩" : 55,
            "Python成绩" : 65,
            "C语言成绩" : 85,
            "总成绩" : 205
         },
        "1001" :{
            "name" :'cyw',
            "English成绩" : 55,
            "Python成绩" : 65,
            "C语言成绩" : 85,
            "总成绩" : 205
        }
    }
a = {
    "name" :'cyw',
    "English成绩" : 55,
    "Python成绩" : 65,
    "C语言成绩" : 85,
    "总成绩" : 205
}

# id = '1001'
# student_score_dict[id] = {}
# student_score_dict_inner = student_score_dict[id]
# student_score_dict_inner['name'] = 'cyw'
#
# student_score_dict_inner['English成绩'] = 85
# student_score_dict_inner['English成绩'] = int(student_score_dict_inner['English成绩'])
#
# student_score_dict_inner['Python成绩'] = 65
# student_score_dict_inner['Python成绩'] = int(student_score_dict_inner['Python成绩'])
#
# student_score_dict_inner['C语言成绩'] = 85
# student_score_dict_inner['C语言成绩'] = int(student_score_dict_inner['C语言成绩'])
#
# sum_score = student_score_dict_inner['English成绩']+student_score_dict_inner['Python成绩']+student_score_dict_inner['C语言成绩']
# student_score_dict_inner['总成绩'] = sum_score
# print(student_score_dict_inner)
# print(student_score_dict)
#
#
#
# # while active :
# #     while active1:
# #         active1 = 1
# #     active = True


# for item in student_score_dict.keys():
#     for value in student_score_dict[item].values() :
#         if 'cyw' == value :
#             print("找到啦")

del student_score_dict['1000']
print(student_score_dict)