# _*_ coding : UTF-8 _*_
# 开发人员 : ChangYw
# 开发时间 : 2019/7/19 15:58
# 文件名称 : day05fingerGame.PY
# 开发工具 : PyCharm
#终极猜拳游戏
#石头剪刀布finger
#stone      石头：石头 剪刀 步
#scissors   剪刀：石头 剪刀 步
#cloth      布  ：石头 剪刀 步
import random

if __name__ == "__main__" :
    win_list = []
    temp_list = []
    while True:

        print("欢迎来到终极猜拳游戏，您的每一步操作都有可能输到这次游戏，请慎重操作！程序过程中可按Q退出")
        print("接下来由您定义游戏规则")
        game_win = input("请输入这一局游戏中一共玩几把？")
        if ('Q' == game_win.upper()):
            if (win_list.__len__() == 0) :
                game_exit = input("您还没玩游戏哟，在来玩一次吧，所以没有成绩！继续退出请按1，否则游戏会继续进行！")
                if (not game_exit.isdigit()) :
                    print("输入错误，请正确输入！")
                    continue
                game_exit = int(game_exit)
                if (not game_exit == 1) :
                    print("输入错误，请正确输入！")
                    continue
                else:
                    exit(0)
            else:
                print("您的成绩为：")
                print(win_list,"\n")
            exit(0)
        if (not game_win.isdigit()):
            print("输入错误，请正确输入！")
            continue
        items_win = input("请输入这一局游戏中赢几把获胜？")
        if ('Q' == items_win.upper()):
            if (win_list.__len__() == 0) :
                game_exit = input("您还没玩游戏哟，在来玩一次吧，所以没有成绩！继续退出请按1，否则游戏会继续进行！")
                if (not game_exit.isdigit()):
                    print("输入错误，请正确输入！")
                    continue
                game_exit = int(game_exit)
                if (not game_exit == 1):
                    print("输入错误，请正确输入！")
                    continue
                else:
                    exit(0)
            else:
                print("您的成绩为：")
                print(win_list, "\n")
            exit(0)
        if (not items_win.isdigit()):
            print("输入错误，请正确输入！")
            continue

        game_win = int(game_win)
        items_win = int(items_win)
        if (game_win < items_win) :
            print("输入错误，您输入的赢的数量大于这局游戏的数量！")
            continue

        cpt_win_item = 0
        your_win_item = 0
        # cpt_win_list = []
        # your_win_list = []
        final_items = 0
        i = 0
        while True:
            fists = ["stone", "scissors", "cloth"]
            com_finger = random.choice(fists)
            print("1.石头")
            print("2.剪刀")
            print("3.布")
            your_finger = input("请出拳！请在1-3选项中任选一项，输入其他选项讲判定游戏失败！可按Q退出")
            if ('Q' == your_finger.upper()):
                exit(0)
            if (not your_finger.isdigit()) :
                print("请正确出拳，这把你输了")
                cpt_win_item +=1
                final_items += 1
                continue
            your_finger = int(your_finger)
            if your_finger < 0 or your_finger >3 :
                print("请正确出拳，这把你输了")
                cpt_win_item += 1
                final_items += 1
                continue
            finger = ''


            if   1 == your_finger :
                finger = 'stone'
            elif 2 == your_finger:
                finger = 'scissors'
            elif 3 == your_finger:
                finger = 'cloth'

            if finger == 'stone':
                final_items += 1
                if com_finger == 'stone':
                    print("哇哦，平局！")
                elif com_finger == 'scissors':
                    your_win_item += 1
                    print("你赢了！真厉害")
                elif com_finger == 'cloth':
                    cpt_win_item += 1
                    print("这把你输了！")


            elif finger == 'scissors':
                final_items += 1
                if com_finger == 'stone':
                    cpt_win_item += 1
                    print("这把你输了")
                elif com_finger == 'scissors':
                    print("哇哦，平局！")
                elif com_finger == 'cloth':
                    your_win_item += 1
                    print("你赢了！真厉害")


            elif finger == 'cloth':
                final_items += 1
                if com_finger == 'stone':
                    your_win_item += 1
                    print("你赢了！真厉害")
                elif com_finger == 'scissors':
                    cpt_win_item += 1
                    print("这把你输了")
                elif com_finger == 'cloth':
                    print("哇哦，平局！")

            i += 1
            temp_list = [i, finger, com_finger]
            win_list.append(temp_list)

            if items_win == cpt_win_item :
                print("这局游戏你输了！")
                break
            elif items_win == your_win_item :
                print("这局游戏你赢了")
                break

            if (game_win == final_items) :
                print("游戏结束：·············")
                if(your_win_item > cpt_win_item) :
                    print("这局游戏你赢了")
                    break
                elif(your_win_item <cpt_win_item) :
                    print("这局游戏你输了")
                    break
                else:
                    print("这局游戏平局！")
                    break
