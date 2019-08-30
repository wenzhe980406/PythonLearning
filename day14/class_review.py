# _*_ coding : UTF-8 _*_
# 开发人员 : ChangYw
# 开发时间 : 2019/8/1 9:42
# 文件名称 : class_review.PY
# 开发工具 : PyCharm

class Person:

    def __init__(self,name):
        print("Person set")
        self.name = name


p = Person("zhang")
print(p.name)


class Classmate():
    def __init__(self,mates):
        self.mates = mates


    def __getitem__(self, item):
        return self.mates[item]


    def __len__(self):
        return len(self.mates)


    def __str__(self):
        return "/".join(self.mates)


    # def __setitem__(self, key, value):
    #     self.mates.insert(key,value)



py_class = Classmate(["liu","shao","wu","zhang","jiang","chang"])
for i in py_class:
    print(i)

    print(py_class[4:])

print(len(py_class))
print(py_class)
print()