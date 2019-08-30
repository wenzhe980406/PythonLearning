# _*_ coding : UTF-8 _*_
# 开发人员 : ChangYw
# 开发时间 : 2019/7/21 23:16
# 文件名称 : 14HomeWork.PY
# 开发工具 : PyCharm


if __name__ == "__main__" :
    height = 100
    height_down = 0
    height_rebound = 0
    count = 0

    while height > 0 :
        print("回调！",height / 2)
        height_down += height / 2
        count += 1
        height =int (height / 2)
        print(height)

    print("1",count)
    print("2",height_down)