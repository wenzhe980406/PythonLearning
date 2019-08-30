# _*_ coding : UTF-8 _*_
# 开发人员 : ChangYw
# 开发时间 : 2019/7/19 13:48
# 文件名称 : guessNumber.PY
# 开发工具 : PyCharm
#猜数字

import random

if __name__ == "__main__" :
    total = []
    print("开始游戏，按Q退出")

    while True :
        if(total) :
            print("开始第%d局游戏。"%(len(total) + 1))
        else:
            print("开始您的游戏，祝你好运!")
        guess_number = random.randint(0,100)
        guess_path = []
        while True:
            if (guess_path) :
                print("这是您地%d次猜解本数字。"%len(guess_path))
            your_number_str = input("请输入0-100的数字：")

            if ("Q" == your_number_str.upper()):
                print("您总共进行了%d局的猜解。详情如下"%(len(total)))
                for guess in total :
                    print(guess)
                exit(0)
            if (not your_number_str.isdigit()):
                print("输入错误，请重新输入")
                continue
            your_number = int(your_number_str)
            if (your_number < 0 or your_number > 100):
                print("您的数字不在0-100之间，请重新输入。")
                continue
            guess_path.append(your_number)
            if(your_number == guess_number) :
                print("您经过%d次猜解，终于猜对了"%len(guess_path))
                total.append(guess_path)
                break
            elif((your_number > guess_number)) :
                print("您猜的数字大了。")
            else:
                print("您猜的数字小了")