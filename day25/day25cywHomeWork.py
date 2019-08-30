# _*_ coding : UTF-8 _*_
# 开发人员 : ChangYw
# 开发时间 : 2019/8/16 23:11
# 文件名称 : day25cywHomeWork.PY
# 开发工具 : PyCharm
import random

def fun40(a):
    answer = {
        2 : [97,98,99],
        3 : [100,101,102],
        4 : [103,104,105],
        5 : [106,107,108],
        6 : [109,110,111],
        7 : [112,113,114,115],
        8 : [116,117,118],
        9 : [119,120,121,122]
    }
    for i in a :
        print(ord(i))
        if ord(i) in [str(i) for i in range(97,123)]:
            for k,v in answer.items():
                if i in v:
                    print(k)
        elif ord(i) in [str(i) for i in range(65,90)]:
            print(chr(int(ord(i)) + 1))
        elif ord(i) == 90 :
            print("a")
        else:
            print(i)




def fun41():
    str_list = [i for i in range(1,27)]
    print(str_list)

if __name__ == '__main__':
    # fun41()
    fun40("NAsalnjASDB")
