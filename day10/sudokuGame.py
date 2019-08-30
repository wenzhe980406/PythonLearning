# _*_ coding : UTF-8 _*_
# 开发人员 : ChangYw
# 开发时间 : 2019/7/26 11:56
# 文件名称 : sudokuGame.PY
# 开发工具 : PyCharm
import copy
import json
import random
import os
#数独游戏#全局变量✘
import re

sudoku_list = [
                [0, 0, 0, 0, 0, 0, 0, 0, 0],
                [0, 0, 0, 0, 0, 0, 0, 0, 0],
                [0, 0, 0, 0, 0, 0, 0, 0, 0],
                [0, 0, 0, 0, 0, 0, 0, 0, 0],
                [0, 0, 0, 0, 0, 0, 0, 0, 0],
                [0, 0, 0, 0, 0, 0, 0, 0, 0],
                [0, 0, 0, 0, 0, 0, 0, 0, 0],
                [0, 0, 0, 0, 0, 0, 0, 0, 0],
                [0, 0, 0, 0, 0, 0, 0, 0, 0]
]
sudoku_list_do= []


#主函数
def main():
    while True:
        i = main_show()
        if 1 == i:
            select_topic()
        elif 2 == i:
            add_topic()
        elif 3 == i:
            pass


#界面
def main_show() :
    while True:
        print("1.选择题目\n"
              "2.增加题目\n"
              "3.做题\n"
              "0.退出程序")
        i = input("请选择菜单：(请正确输入1-3中的菜单选项)")
        if not i.isdigit():
            print("输入错误，请重新输入！")
            continue
        i = int(i)
        if i < 0 or i > 3:
            print("数字超过范围，请确认后重新输入！")
            continue
        return i


#功能1：选择题目
def select_topic():
    # 先判断读取文件是否为空，如果是，当选择功能1时弹出暂无题目，写入空的数独列表，然后请输入者增加题目。
    #            如果不为空，则输出所有文件。
    while True :
        txtType = 'txt'
        list_topic = [i for i in os.listdir('E:\\PythonFile\\day10\\') if txtType in i]
        if list_topic == [] :
            print("暂时没有题目，请选择功能2增加题目。")
            break
        else :
            for i in list_topic:
                print("第%d题"%int(i[6]))
            choice_topic = input("请选择题目：")
            if_impr_comm(choice_topic)
            print("您选择了第%d题"%int(choice_topic))
            sudoku_list_do = read_file(int(choice_topic))
            sudoku_list_do = str_list(sudoku_list_do)
            print_sudoku(sudoku_list_do)
            q = input("按Q返回")
            if "Q" == q.upper():
                break
            else :
                continue


##功能2：增加题目

def add_topic():
    i = input("请输入题号：")
    if_impr_comm(i)
    write_file(sudoku_list,int(i))
    flags = False
    while True:
        line_input,list_input = fill_sudoku_num()
        num_input = add_num()
        line_norept(line_input, num_input, sudoku_list)
        list_norept(list_input,num_input,sudoku_list)
        th_th_norept(line_input, list_input, num_input, sudoku_list)
        update_sudoku(line_input,list_input,num_input,sudoku_list)
        write_file(sudoku_list,int(i))




#判断数独中是否已经含有数字
def fill_sudoku_num() :
    while True:
        line_input = input("请输入行数（注意慎重选择，以防输错！）")
        if if_impr_comm(line_input):
            continue
        list_input = input("请输入列数")
        if if_impr_comm(list_input):
            continue
        #判断所输入的行列中是否已经存在数字
        line_input = int(line_input)
        list_input = int(list_input)
        if sudoku_list[line_input - 1][list_input - 1] > 0 :
            print("第%d行第%d列中已经有数字了，请重新选择一个数进行填写"%(line_input,list_input))
            continue
        return line_input,list_input


#更新数独-添加数据
def update_sudoku(line,list,num_input,sudoku_list):
    line = int(line)
    list = int(list)
    num_input = int(num_input)
    sudoku_list[line - 1][list - 1] = num_input
    print("您在第%d行第%d列中添加了数字%d"%(line,list,num_input))
    #添加完后打印
    print_sudoku(sudoku_list)


#增加数字
def add_num():
    while True:
        num_input = input("请输入要添加的数字：")
        if if_impr_comm(num_input):
            continue
        return num_input


#判断行数字不重复 / 有数字覆盖报错
def line_norept(line,num_input,sudoku_list):
    for i in range(9) :
        if sudoku_list[line - 1][i] == 0 :
            if sudoku_list[line - 1][i] == num_input :
                print("line_norept第%d行第%d列已存在该数字，请重新输入"%(line,i))
                break
        else:
            print("line_norept第%d行第%d列已存在数字，请重新输入" % (line, i))
            break


#判断列数字不重复
def list_norept(list,num_input,sudoku_list):
    for i in range(9):
        if sudoku_list[i][list - 1] == 0:
            if sudoku_list[i][list - 1] == num_input:
                print("list_norept第%d行第%d列已存在该数字，请重新输入" % (list, i))
                return True
        else:
            print("list_norept第%d行第%d列已存在数字，请重新输入" % (list, i))
            return True
    return False

#判断9个3*3宫格内的数字不重复
def th_th_norept(line,list,num_input,sudoku_list):
    k,v = which_norept(line,list)
    for i in range(k,k+3):
        for j in range(v,v+3) :
            if int(num_input) == sudoku_list[i][j]:
                print("th_th_norept错误第%d行第%d列中的3*3宫格内已存在该数值"%(line,list))
                break


#判断在哪个3*3宫格内
def which_norept(line,list):
    if line >= 1 and line <= 3 :
        line = 0
    elif line >= 4 and line <= 6 :
        line = 3
    elif line >= 7 and line <= 9 :
        line = 6
    if list >= 1 and list <= 3 :
        list = 0
    if list >= 4 and list <= 6:
        list = 3
    if list >= 7 and list <= 9:
        list  = 6
    return line,list


#判断游戏是否胜利
def win_game(sudoku_list):
    for i in range(len(sudoku_list)):
        for j in range(len(sudoku_list)):
            if sudoku_list[i][j] == 0 :
                print("游戏尚未结束，继续加油！")
                return False
            else :
                return True


#将读出来的文件组成原列表格式
def str_list(sudoku_list):
    sudoku_list_new = []
    aLst = re.findall("\w+", sudoku_list)
    n = 0
    newLst = []
    for i in range(len(aLst)):
        newLst.append(int(aLst[i]))
        n += 1
        if n == 9:
            sudoku_list_new.append(newLst)
            newLst = []
            n = 0
            continue
    return sudoku_list_new


#打印数独
def print_sudoku(sudoku_list):
    for i in range(9):
        for j in range(9):
            print(" {:^1} ".format(sudoku_list[i][j]),end=" ")
        print()


#读文件
def read_file(qid):
    with open("sudoku%d.txt"%qid,"r",encoding="utf-8") as r:
        student_list = r.read()
    return student_list


#写文件
def write_file(sudoku_list,qid):
    with open("sudoku%d.txt"%qid,"w",encoding="utf-8") as w:
        w.write(str(sudoku_list))


#判断输入的数字是否为非法字符improper_command
def if_impr_comm(num) :
    if not num.isdigit() :
        print("您所输入的字符非法，请重新输入。")
        return True
    num = int(num)
    if num > 9 or num < 0 :
        print("请输入的字符超出数量，请重新输入")
        return True


if __name__ == '__main__':
    main()
