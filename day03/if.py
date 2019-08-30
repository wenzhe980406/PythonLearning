# _*_ coding : UTF-8 _*_
# 开发人员 : ChangYw
# 开发时间 : 2019/7/17 15:12
# 文件名称 : if.PY
# 开发工具 : PyCharm

#1 1)
# age = int(input("请输入您的年龄："))
# if age >= 18 :
#     print("可以进去嗨皮了!")
# else:
#     print("滚回家去！")

#2 2)
# python_score = int(input("请输入您的python成绩"))
# c_score = int(input("请输入您的c语言成绩"))
#
# if python_score > 60 or c_score > 60 :
#     print("你合格了！")
# else :
#     print("抱歉，你不及格！")

# a = -1000
# b = -1000
# print(a == b)
# print(a is b)

# height = float(input("请输入身高：（单位：米）"))
# weight = float(input("请输入体重：（单位：公斤）"))
# print("您的身高为：",height,"您的体重为：",weight)
#
# BMI =weight / (height * height)
# print("您的BMI指数为：",BMI)
# if BMI < 18.5 :
#     print("太瘦了！")
# elif BMI >= 18.5 and BMI < 25:
#     print("正常！")
# elif BMI >=25 and BMI < 28:
#     print("有点重哦朋友")
# elif BMI>= 28 and BMI <= 32:
#     print("你有点胖了朋友")
# else :
#     print("你太胖了朋友，都成猪了！")


if __name__ == "__main__":
    print("1.情人节")
    print("2.平安夜")
    print("3.生日")
    print("4.其他的日子")
    day = input("今天是什么日子请选择：")
    if (not day.isdigit()):
        print("你输入的不正确，请输入1-4之间的正整数！")
        exit(0)
    x = [1,2,3,4]
    if day in x :
        if day == 1:
            print("买玫瑰，看电影")
        if day == 2:
            print("买苹果，吃大餐")
        if day == 3:
            print("买蛋糕HappyBirthday")
        if day == 4:
            print("每天都是节日呀！")
    else :
        print("警告！输入错误，请重新输入！")
