# _*_ coding : UTF-8 _*_
# 开发人员 : ChangYw
# 开发时间 : 2019/7/18 10:17
# 文件名称 : if-while.PY
# 开发工具 : PyCharm


#写if需要注意的地方
# a = 100
# b = 50
# condtion = a == 100
# # if(True == condtion) :
# #     print("True")
# # elif(False == condtion):
# #     print("Fasle")
#
# print("True") if condtion else print("False")
#
#
# print(a if a < b else b)

#循环 -- 循环条件，循环体，玄幻的退出机制
# #计算1-100奇数和
# count = 1
# num_num = 1
# while count < 99 :
#     count += 2
#     num_num += count
#     print(num_num)

# #break -- 把当前的循环结束掉
# while True :
#     get_string  = input("请请输入信息，Q退出").strip()
#     if('Q' == get_string.upper()):
#         break
#     print(get_string)
# print("All done")

# #continue --本次循环结束，直接进行下一次循环判断和循环运行
# while True:
#     get_string = input("请输入信息，Q退出").strip()
#     if("Q" == get_string.upper()):
#         break
#     if("C" == get_string.upper()):
#         print("你的输入被忽略了。")
#         continue
#     print(get_string)
# print("All done")

# num = input("请输入你想求和的数：(本次求和不含7的倍数)")
# if (not num.isdigit()):
#     print("输入错误！")
# num = int(num)
# count = 1
# num_sum = 0
# while count <= num :
#     if count % 7 == 0 :
#         count += 1
#         continue
#     else:
#         num_sum = num_sum +count
#         count +=1
#         print(num_sum)
# print("最终结果为：",num_sum)
#
# num = input("请输入你想求和的数：(本次求和不含7以及7的倍数)")
# if (not num.isdigit()):
#     print("输入错误！")
# num = int(num)
# count = 1
# num_sum = 0
# while count <= num :
#     if count % 7 == 0 :
#         count += 1
#         continue
#     if count % 10 == 7 :
#         count +=1
#         continue
#     else:
#         num_sum = num_sum +count
#         count +=1
#         print(num_sum)
#     print("count",count)
# print("最终结果为：",num_sum)
#

# #打印*号
# hangshu = int(input("请输入行数"))
# count = 1
# while count < hangshu:
#     print('*' * count)
#     count+=1

# #九九乘法表 1
# line =1
# while line <= 9 :
#     column = 1
#     while column <= line :
#         # print(line,"*",column,"=",line * column,end=" ")
#         print("%d * %d = %-2d"%(line,column,line*column),end=' ')
#         column +=1
#     print()
#     line +=1

# #九九乘法表 2
# line =1
# while line <= 9 :
#     column = 1
#     blank = 1
#     while blank <= 9-line :
#         print("           ",end='')
#         blank += 1
#     while column <= line :
#         print("%d * %d = %-2d"%(line,column,line*column),end=' ')
#         column +=1
#     print()
#     line +=1

# #九九乘法表 3
# line =9
# while line >= 1 :
#     column = 1
#     while column <= line :
#         print("%d * %d = %-2d"%(column,line,line*column),end=' ')
#         column +=1
#     print()
#     line -=1

#九九乘法表 4
line =9
while line >= 1 :
    column = 1
    blank = 1
    while blank <= 9-line :
        print("           ",end='')
        blank += 1
    while column <= line :
        # print("%d * %d = %-2d"%(column,line,line*column),end=' ')
        print("{0} * {1} = {2:0>2}".format(line,column,line*column),end=" ")
        column +=1
    print()
    line -=1