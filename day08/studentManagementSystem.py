# _*_ coding : UTF-8 _*_
# 开发人员 : ChangYw
# 开发时间 : 2019/7/24 8:57
# 文件名称 : studentManagementSystem.PY
# 开发工具 : PyCharm
#学生信息管理系统
import json

student_score_dict = dict()
student_score_dict_found = dict()

def student_main():
    # 主菜单
    while True :
        menu_main()
        choice_input = input("请选择：")
        if not choice_input.isdigit():
            print("输入错误，请重新输入！（输入的为非正整数！）")
            continue
        choice_input = int(choice_input)
        # 判断数字是否超范围：
        if choice_input < 0 or choice_input > 7:
            print("输入的数超过了选择范围，请重新输入！")
            continue
        elif 1 == choice_input:
            try:
                ipt_infmtion()
            except KeyError as e:
                print("程序出错！请重试")
            except NameError as e :
                print("输入错误！请重试")
            except TypeError as e :
                print("类型错误！请重试")
            except Exception as e :
                print("无效错误！请重试")
        elif 2 == choice_input:
            try:
                fnd_infmtion()
            except KeyError as e:
                print("程序出错！请重试")
            except NameError as e :
                print("输入错误！请重试")
            except TypeError as e :
                print("类型错误！请重试")
            except Exception as e :
                print("无效错误！请重试")
        elif 3 == choice_input:
            try:
                del_infmtion()
            except KeyError as e:
                print("程序出错！请重试")
            except NameError as e :
                print("输入错误！请重试")
            except TypeError as e :
                print("类型错误！请重试")
            except Exception as e :
                print("无效错误！请重试")
        elif 4 == choice_input:
            try:
                upt_infmtion()
            except KeyError as e:
                print("程序出错！请重试")
            except NameError as e :
                print("输入错误！请重试")
            except TypeError as e :
                print("类型错误！请重试")
            except Exception as e :
                print("无效错误！请重试")
        elif 5 == choice_input:
            try:
                sort_infmtion()
            except KeyError as e:
                print("程序出错！请重试")
            except NameError as e :
                print("输入错误！请重试")
            except TypeError as e :
                print("类型错误！请重试")
            except Exception as e :
                print("无效错误！请重试")
        elif 6 == choice_input:
            try:
                cut_stu()
            except KeyError as e:
                print("程序出错！请重试")
            except NameError as e :
                print("输入错误！请重试")
            except TypeError as e :
                print("类型错误！请重试")
            except Exception as e :
                print("无效错误！请重试")
        elif 7 == choice_input:
            try:
                show_stu()
            except KeyError as e:
                print("程序出错！请重试")
            except NameError as e :
                print("输入错误！请重试")
            except TypeError as e :
                print("类型错误！请重试")
            except Exception as e :
                print("无效错误！请重试")
        elif 0 == choice_input:
            exit_program()

#主菜单
def menu_main():
    print('''\033[0;34m
            ╔———————————————学生信息管理系统————————————————
            │                                              
            │   =============== 功能菜单 ===============    
            │                                              
            │   1 录入学生信息                              
            │   2 查找学生信息                              
            │   3 删除学生信息                              
            │   4 修改学生信息                              
            │   5 排序                                     
            │   6 统计学生总人数                            
            │   7 显示所有学生信息                          
            │   0 退出系统                                  
            │  ==========================================  
            │  说明：通过数字选择菜单              
            ╚——————————————————————————————————————————————
            \033[0;34m''')

#功能1的实现：录入学生信息
def ipt_infmtion():
    flags = False
    while not flags:
        #id,name,English,Python,C语言
        ipt_id_ifmt = id_input()
        name_id_ifmt = name_input()
        English_score = int(project_input('English成绩'))
        python_score = int(project_input('Python成绩'))
        c_score= int(project_input('C语言成绩'))

        student_score_dict[ipt_id_ifmt] = {
                "name" : name_id_ifmt,
                "English成绩" : English_score,
                "Python成绩" : python_score,
                "C语言成绩" : c_score,
                "总成绩" : English_score + python_score + c_score
            }
        dump_file(student_score_dict)
        flags = exit_back()


#功能2的实现：查找学生信息
def fnd_infmtion():
    flags = False
    while not flags:
        id_choice = input("按ID查输入1；按姓名查输入2：")
        if not id_choice.isdigit():
            print("输入错误，请重新输入！（输入的为非正整数！）")
            continue
        id_choice = int(id_choice)
        if id_choice < 0 or id_choice > 2:
            print("数字输入超出范围，请重新输入。")
            continue
        if 1 == id_choice:
            id_found()
            flags = exit_back()
        elif 2 == id_choice:
            name_found()
            flags = exit_back()


#功能3的实现：删除学生信息
def del_infmtion():
    flags = False
    while not flags:
        student_score_dict = load_file()
        while True:
            del_id_input = input("请输入要删除的学生ID：")
            if not del_id_input in student_score_dict.keys():
                print("ID为%s的学生不存在...." % del_id_input)
                continue
            if not del_id_input.isdigit():
                print("输入错误，请重新输入！（输入的为非正整数！）")
                continue
            if len(del_id_input) > 4:
                print("请正确输入ID(如 1001)：")
                continue
            break
        a = student_score_dict[del_id_input]
        print_title()
        print_score(del_id_input,a)
        flags = exit_back()
        if flags == True:
            break
        del_id_input_again = input("请输入要删除的学生ID：")
        if del_id_input_again == del_id_input:
            del student_score_dict[del_id_input]
            dump_file(student_score_dict)
            print("ID为%s的学生已经被删除...." %del_id_input)
            flags = True
        else:
            break

#功能4的实现：修改学生信息
def upt_infmtion():
    student_score_dict = load_file()
    print_title()
    for i in student_score_dict.keys():
        a = student_score_dict[i]
        print_score(i,a)
    update_id = input("请输入要改的学生ID：")
    if update_id in student_score_dict.keys():
        print("找到了这名学生,可以修改他的信息！")
        update_name = input("请输入姓名：")
        update_Englsh_score = input("请输入英语成绩：")
        update_Englsh_score = int(update_Englsh_score)
        update_python_score = input("请输入Python成绩：")
        update_python_score = int(update_python_score)
        update_c_score = input("请输入C语言成绩：")
        update_c_score = int(update_c_score)
        a = student_score_dict[update_id]
        a["name"] = update_name
        a["English成绩"] = update_Englsh_score
        a["Python成绩"] = update_python_score
        a["C语言成绩"] = update_c_score
        a["总成绩"] = update_Englsh_score + update_python_score + update_c_score
        dump_file(student_score_dict)
        print("该学生的信息已经修改!")
        come_bake()

#功能5的实现：排序
def sort_infmtion():
    aList = []
    student_score_dict = load_file()
    print_title()
    for i in student_score_dict.keys():
        a = student_score_dict[i]
        bList = [i for i in a.values()]
        bList.insert(0, i)
        aList.append(bList)

    k = input("请选择排序方式(1按英语排序，2按Python成绩排序，3按C语言成绩排序；0按总成绩排序)")
    k = int(k)
    if 0 == k:
        k = 5
    elif k >= 1 and k <= 3:
        k += 1
    reverse_input = input("请选择(0升序；1降序)：")
    reverse_input = int(reverse_input)
    if 0 == reverse_input:
        reverse_input = False
    elif 1 == reverse_input:
        reverse_input = True
    sorted_lambda(aList, k, reverse_input)
    come_bake()


#功能6的实现：统计学生总人数
def cut_stu():
    student_score_dict_found = load_file()
    student_num = len(student_score_dict_found.keys())
    print("一共有%d学生!" % student_num)
    come_bake()


#功能7的实现：显示所有学生信息
def show_stu():
    student_score_dict = load_file()
    print_title()
    for i in student_score_dict.keys():
        a = student_score_dict[i]
        print_score(i,a)
    come_bake()


####定义一个lambda函数与sorted使用
def sorted_lambda(aList,i,truefalse):
    aList = sorted(aList,key=lambda k:k[i],reverse=truefalse)
    print_title()
    for i in range(len(aList)):
        print("{:^8} {:^8} {:^9} {:^12} {:^9} {:^11}".format
              (aList[i][0], aList[i][1], aList[i][2], aList[i][3], aList[i][4], aList[i][5]))


# 定义ID
def id_input():
    file_dict = load_file()
    while True:
        id = input("请输入ID(如 1001)：")
        if id in file_dict.keys():
            print("ID已存在，请重新输入")
            continue
        if not id.isdigit():
            print("输入错误，请重新输入！（输入的为非正整数！）")
            continue
        if len(id) > 4:
            print("请正确输入ID(如 1001)：")
            continue
        return id

# 定义name
def name_input():
    while True:
        name = input("请输入名字：")
        if name.isalpha():
            return name
        else:
            print("请正确输入你的姓名！")
            continue

#学科成绩输入函数
def project_input(project):
    while True:
        #定义学科成绩
        score = input("请输入%s：" %project)
        if not score.isdigit():
            print("输入错误，请重新输入")
            continue
        score = int(score)
        if score < 0 or score > 100:
            print("输入的成绩超出范围，请输入1-100之间的数字。")
            continue
        return score


#通过id查询
def id_found():
    file_dict = load_file()
    while True:
        id_found_input = input("请输入学生ID：")
        if not id_found_input.isdigit():
            print("输入错误，请重新输入！（输入的为非正整数！）")
            continue
        if len(id_found_input) > 4:
            print("ID输入超出范围，请重新输入。")
            continue
        break
    a = file_dict[id_found_input]
    print_title()
    print_score(id_found_input,a)


#通过name查询
def name_found():
    file_dict = load_file()
    while True:
        name_found_input = input("请输入学生姓名：")
        if name_found_input.isalpha():
            break
        else:
            continue
    b = 0
    for i in file_dict.keys():
        for value in file_dict[i].values():
            if name_found_input == value:
                b = i
    if 0 == b:
        print("没找到这个学生请重试")
        return False
    a = file_dict[b]
    print_title()
    print_score(b,a)


#是否继续操作函数
def exit_back() :
    while True:
        choice_input = input("是否继续操作？(y/n)：")
        if not choice_input.isalpha():
            print("输入的字符非字母，请输入y/n来继续您的操作(不区分大小写)")
            continue
        if len(choice_input) > 1:
            print("输入的字符为多个请重新输入")
            continue
        if "N" == choice_input :
            flages = True
        return "N" == choice_input.upper()
        # if "Y" == choice_input_add.upper():
        #     return False
        # elif "N" == choice_input_add.upper():
        #     return True

#是否继续操作，防止567功能自动返回
def come_bake() :
    while True:
        if_comebake_input = input("是否要回主菜单？输入任意字符回退")
        if if_comebake_input.isalpha() :
            return
        else:
            print("输入错误，请重新输入")
            continue
#读文件
def load_file():
    f = open("studentManagementSystem.json","r",encoding='UTF-8')
    student_dict = json.load(f)
    f.close()
    return student_dict


#print标题
def print_title():
    print("{:^8} {:^8} {:^8} {:^8} {:^8} {:^8}".format
          ("ID", "name", "English成绩", "Python成绩", "C语言成绩", "总成绩"))


#format格式化打印成绩
def print_score(i,aList):
    print("{:^8} {:^8} {:^9} {:^12} {:^9} {:^11}".format
          (i, aList["name"], aList["English成绩"], aList["Python成绩"], aList["C语言成绩"], aList["总成绩"]))


#写文件
def dump_file(student_score_dict):
    f = open("studentManagementSystem.json", "w")
    json.dump(student_score_dict, f)
    f.close()


#退出系统功能
def exit_program():
    print("您已退出学生成绩管理系统")
    exit(0)


if __name__ == '__main__':
    student_main()