# _*_ coding : UTF-8 _*_
# 开发人员 : ChangYw
# 开发时间 : 2019/7/17 17:33
# 文件名称 : day03HomeWork.PY
# 开发工具 : PyCharm

#1
# #1)
# if __name__ == "__main__":
#     score = []
#
# #2)
# if __name__ == "__main__":
#     score.append(68)
#     score.append(87)
#     score.append(92)
#     score.append(100)
#     score.append(76)
#     score.append(88)
#     score.append(54)
#     score.append(89)
#     score.append(76)
#     score.append(61)
#
# #3)
# if __name__ == "__main__":
#     print(score[2])
#
# #4)
# if __name__ == "__main__":
#     print(score[:6])
#
# #5)
# if __name__ == "__main__":
#     score.insert(3,59)
#     print(score)
#
# #6)
# if __name__ == "__main__":
#     num = score.count(76)
#     print(num)
#
# #7)
# if __name__ == "__main__":
#     print(55 in score)
#
# #8)
# if __name__ == "__main__":
#     print(score.index(68)+19000100)
#     print(score.index(87)+19000100)
#     print(score.index(92)+19000100)
#     print(score.index(100)+19000100)
#
# #9)
# if __name__ == "__main__":
#     score[3] = score[3] + 1
#     print(score[3])
#
# #10)
# if __name__ == "__main__":
#     del score[0]
#     print(score)

#11)
# if __name__ == "__main__":
#     print(score.__len__())
#     print(len(score))

# #12)
# if __name__ == "__main__":
#     score.sort()
#     print(score)
#     print(min(score))
#     print(max(score))

#     #13)!!
# if __name__ == "__main__":
#     print(list(reversed(score)))

#14)
# if __name__ == "__main__":
#     del score[-1]
#     print(score)

# #15)???如何定位第一个值为88的字符？
# if __name__ == "__main__":
#     score.append(88)
#     del score[6]

# #16)
# if __name__ == "__main__":
#     score1 = [80,61]
#     score2 = [71,95,82]
#     score = score1.append(score2)
#     print(score)

#17)
# if __name__ == "__main__":
#     score1 = [80,61]
#     score2 = score1 *5
#     print(score2)

#2)
import random

# if __name__ == "__main__":
#     #1)入栈(先入后出，后入先出)
#     score1 = [70,45,15,48,25,70,75,35,76,88]
#     score2 = [22,84,63]
#     score = score1 + score2
#     # 2)出栈
#     del score[0:2]
#     print(score)
#     #3)查看栈顶的元素
#     print(score[-1])
#     print(score.pop())
#     #4)查看栈的长度
#     print(len(score))
#     #5)判断栈是否为空
#     if score is None :
#         print("score is null")
#     else:
#         print("score is not null")
#     #6)退出程序。
#     exit(0)


#3)
# if __name__ == "__main__":
#     comm_list = ["T恤", "长裤", "鞋子", "饮料", "餐巾纸", "手机", "电脑", "防晒霜", "疯狂Python书", "椅子"]
#     comm_price = ["88", "108", "168", "38", "18", "6288", "5288", "108", "68", "228"]
#
#     money = input("请输入你的余额：")
#     if (not money.isdigit()):
#         print("请输入一个正整数：")
#     print("输入成功，即将进入主界面")
#     # money = int(money)
#     while True :
#         print("--------------")
#         print("您的余额为：",money)
#         print("--------------")
#         print("1.显示余额")
#         print("2.充值")
#         print("3.显示商品")
#         print("4.显示商品价格")
#         print("5.购买商品")
#         print("6.退出程序")
#
#         choice = input("请输入你的选择：")
#         if (not choice.isdigit()):
#             print("请输入一个正整数：")
#         choice = int(choice)
#         if choice <0 and choice > 5 :
#             print("请正确输入界面选项！")
#
#         if choice == 1 :
#             continue
#         elif choice == 2 :
#             money_invest = input("请输入充值金额：(充值金额为正整数)")
#             if (not money_invest.isdigit()):
#                 print("请正确输入您的充值金额，金额为正整数：")
#             else:
#             # money_invest = int(money_invest)
#                 money = int(money)
#                 money_invest = int(money_invest)
#                 money = money + money_invest
#                 print("本次充值金额为：", money_invest, "元", "充值后的金额为：", money, "元")
#         elif choice == 3:
#             print("商品列表为：")
#             for i in comm_list :
#                 print(i,end=" ")
#             print()
#         elif choice == 4:
#             print("商品列表对应价格为：")
#             for i in comm_price :
#                 print(i,end=" ")
#             print()
#         elif choice == 5:
#             comm_choice = input("请输入要购买的商品：")
#             money = int(money)
#             if not comm_choice in comm_list:
#                 print("没有",comm_choice,"这款的商品，请按照列表重新输入")
#                 for i in comm_list:
#                     print(i, end=" ")
#                 print()
#             elif comm_choice in comm_list:
#                 print("您选中了", comm_choice)
#                 comm_buy_num = int(comm_list.index(comm_choice))
#                 comm_buy_money = int(comm_price[comm_buy_num])
#                 if int(money) < int(comm_buy_money) :
#                     print("您的余额不足，请及时充值！")
#                 else:
#                     print("您的余额为：", money, "购买", comm_choice, "即将扣除", comm_buy_money, "元，请稍后")
#                     money = int(money - comm_buy_money)
#                     print("购买成功，您的余额还剩余：",money,"元")
#             elif comm_choice is None :
#                 print("既然选择要买了，那可就要买一个哟！")
#             elif (comm_choice.isdigit()):
#                 print("请正确输入您想要购买的商品：")
#         elif choice == 6 :
#             print("谢谢光临，欢迎下次光临！")
#             exit(0)
#

#4
# if __name__ == "__main__":
# #7.3  True
#     print('abc' in ('abcdefg'))
# #7.4  True
#     print('abc' in ('abcdefg'))
# #7.5  True
#     print('\x41'=='A')
# #7.6  hello world!
#     print(''.join(list('hello world!')))
# #7.7  换行
#     # print('\n')
# #7.8  为啥是3
#     x = ['11','2','3']
#     print(max(x))
# #7.9  11
#     print(min(['11','2','3']))
#7.10   11
#     x = ['11', '2', '3']
#     print(max(x,key=len))
# #7.11   c:\test.htm
#     path = r'c:\test.html'
#     print(path[:-4]+'htm')
# #7.12   False
#     print(list(str([1,2,3])) == [1,2,3])
# #7.13   [1,2,3]
#     print(str([1,2,3]))
# #7.14   (1,2,3)
#     print(str((1,2,3)))
# #7.15   1+3+5+7+9=25
#     print(sum(range(1,10,2)))
# #7.16   1+2+3+4+5+6+7+8+9=45
#     print(sum(range(1,10)))
# #7.17   A
#     print('%c'%65)
# #7.18   65
#     print('%s'%65)
# #7.19   65,A
#     print('%d,%c'%(65,65))
# #7.20   The first:97,the second is 65
#     print('The first:{1},the second is {0}'.format(65,97))
# #7.21   65,0x41,0o101
#     print('{0:#d},{0:#x},{0:#o}'.format(65))
# #7.22   True
#     print(isinstance('abcdefg',str))
# #7.23   True
#     print(isinstance('abcdefg',object))
# #7.24   True
#     print(isinstance(3,object))
# #7.25   6
#     print('abcabcabc'.rindex('abc'))
# #7.26   ab:efg
#     print(':'.join('abcdefg'.split('cd')))
# #7.27   -1
#     print('Hello world.I like Python.'.rfind('python'))
# #7.28   3
#     print('abcabcabc'.count('abc'))
# #7.29   1
#     print('apple.peach,banana,pear'.find('p'))
# #7.30   -1
#     print('apple.peach,banana,pear'.find('ppp'))
# #7.31   ['abcdefg']
#     print('abcdefg'.split(','))
# #7.32   1:2:3:4:5
#     print(':'.join('1,2,3,4,5'.split(',')))
# #7.33   a,b,ccc,ddd
#     print(','.join('a   b   ccc\n\n\nddd    '.split()))
# #7.34 ???  345
#     x = {i:str(i+3) for i in range(3)}
#     print(''.join([item[1] for item in x.items()]))
# #7.35   HELLO WORLD
#     print('Hello world'.upper())
# #7.36   hello world
#     print('Hello world'.lower())
# #7.37   HELLO WORLD
#     print('Hello world'.lower().upper())
# #7.38   Hello world
#     print('Hello world'.swapcase().swapcase())
# #7.39   True
#     print(r'c:\windows\notepad.exe'.endswith('.exe'))
# #7.40
#     print(r'c:\windows\notepad.exe'.endswith('.jpg','.exe'))
# #7.41   True
#     print(r'C:\\Windows\\notepad.exe'.startswith('C:'))
# #7.42   20
#     print(len('Hello world!'.ljust(20)))