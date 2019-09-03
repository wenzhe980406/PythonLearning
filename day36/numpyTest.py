# _*_ coding : UTF-8 _*_
# 开发人员 : ChangYw
# 开发时间 : 2019/9/2 14:31
# 文件名称 : numpyTest.PY
# 开发工具 : PyCharm

#height：1.40 --2.20   1.40+(2.20-1.40)*random.randf()
#weight: 30.0 -- 120.0
import numpy as np

#np.round(f,1)


def bmi(weight,height):
    bmi = weight / height ** 2
    return -1 if bmi <= 18 else 0 if bmi <=25 else 1


if __name__ == '__main__':
    # height_arr = np.round(1.40 + (2.20 - 1.40) * np.random.ranf(size=(100,)),1)
    # # print(height_arr)
    # weight_arr = np.round(30.0 + (120.0 - 30.0) * np.random.ranf(size=(100,)), 1)
    # # print(weight_arr)
    #
    # print(np.round(weight_arr / height_arr ** 2),1)
    #
    # vbmi = np.vectorize(bmi,otypes=[np.float])
    # b_arr = vbmi(weight_arr,height_arr)
    # print(b_arr)
    #
    # bim_f = np.frompyfunc(bmi,2,1)
    # b_arr1 = bim_f(weight_arr,height_arr)
    # print(b_arr1)

    print(bmi(55,1.75))