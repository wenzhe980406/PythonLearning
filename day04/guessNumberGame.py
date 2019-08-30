# _*_ coding : UTF-8 _*_
# 开发人员 : ChangYw
# 开发时间 : 2019/7/18 10:00
# 文件名称 : guessNumberGame.PY
# 开发工具 : PyCharm
import random

# if __name__ == "__main__":
#     print("游戏开始！（1-100）")
#     num = random.randint(1, 100)
#     count = 1
#
#     while True :
#         guess_num = input("请输入您猜的数字：")
#         if (not guess_num.isdigit()) :
#             print("请正确输入一个正整数！")
#         guess_num = int(guess_num)
#         if guess_num > num :
#             print("大了")
#         elif guess_num < num :
#             print("小了")
#         elif guess_num == num :
#             print("猜对啦！")
#             print("您猜的次数为：",count)
#
#         else:
#             break
#         count += 1
#

# if __name__ == "__main__":
#     print("游戏开始！（1-100）")
#     num = random.randint(1, 100)
#     count = 1
#     score = []
#
#     while True:
#         get_string = input("请输入您猜的数字：(按Q退出)").strip()
#         if ('Q' == get_string.upper()):
#             print("游戏结束，即将打印成绩单")
#             break
#         else:
#             guess_num = int(get_string)
#             count += 1
#             if guess_num > num:
#                 print("大了")
#             elif guess_num < num:
#                 print("小了")
#             elif guess_num == num:
#                 print("猜对啦！")
#
#                 print("您猜的次数为：", count)
#         score.append(count)
#
#     print("您的成绩为：",score)
#

