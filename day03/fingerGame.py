# _*_ coding : UTF-8 _*_
# 开发人员 : ChangYw
# 开发时间 : 2019/7/17 16:43
# 文件名称 : fingerGame.PY
# 开发工具 : PyCharm

#石头剪刀布finger
#stone石头：石头 剪刀 步
#scissors剪刀：石头 剪刀 步
#cloth布  ：石头 剪刀 步
import random

if __name__ == "__main__":
    print("欢迎来到猜拳环节:")
    print("请出拳！")
    print("1.石头")
    print("2.剪刀")
    print("3.布")
    finger_choice = input("请在以上三个选项中选择其中一个：（请不要选择其他选项，否则您就输了！）")

    if (not finger_choice.isdigit()):
        print("你输了！这么轻松的败给了电脑！请重新输入1-3中的任意数字！")
        exit(0)
    finger_choice = int(finger_choice)
    if(finger_choice >= 4):
        print("你输了！这么轻松的败给了电脑！请重新输入1-3中的任意数字！")
        exit(0)

    if finger_choice == 1 :
        finger = 'stone'
    elif finger_choice == 2 :
        finger = 'scissors'
    elif finger_choice == 3 :
        finger = 'cloth'
    else:
        print("你咋这么调皮呢，就是不好好出拳？！")

    fists = ["stone", "scissors", "cloth"]
    for _ in range(1):
        fist = random.choice(fists)
        # print(fist)

    if finger == 'stone' :
        if fist =='stone' :
            print("哇哦，平局！")
        elif fist =='scissors' :
            print("你赢了！真厉害")
        elif fist =='cloth' :
            print("你输了！垃圾")
        else:
            print("癞皮狗，不跟你玩了")
            exit(0)
    elif finger == 'scissors':
        if fist =='stone' :
            print("你输了！垃圾")
        elif fist =='scissors' :
            print("哇哦，平局！")
        elif fist =='cloth' :
            print("你赢了！真厉害")
        else:
            print("癞皮狗，不跟你玩了")
            exit(0)
    elif finger =='cloth':
        if fist =='stone' :
            print("你赢了！真厉害")
        elif fist =='scissors' :
            print("你输了！垃圾")
        elif fist =='cloth' :
            print("哇哦，平局！")
        else:
            print("癞皮狗，不跟你玩了")
            exit(0)
    else:
        print("癞皮狗，不跟你玩了")
        exit(0)

