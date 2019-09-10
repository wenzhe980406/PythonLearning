# _*_ coding : UTF-8 _*_
# 开发人员 : ChangYw
# 开发时间 : 2019/9/10 16:09
# 文件名称 : sklearnDemo.PY
# 开发工具 : PyCharm

from sklearn.linear_model import LinearRegression
from sklearn import datasets
iris = datasets.load_iris()
digits = datasets.load_digits()

# 查看数据集
# iris
# print(iris.data[:10,:])
# print(iris.data.shape)
# print(iris.target_names)
# print(iris.target)

# digits
print(digits.data)
print(digits.data.shape)
print(digits.target_names)
print(digits.target)