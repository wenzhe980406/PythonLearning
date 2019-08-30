# _*_ coding : UTF-8 _*_
# 开发人员 : ChangYw
# 开发时间 : 2019/8/2 16:32
# 文件名称 : citys_info.PY
# 开发工具 : PyCharm


class Citys:
    def __init__(self, citys = {}):
        self.__citys = citys

    @property
    def citys(self):
        return self.__citys

    @citys.setter
    def citys(self, citys):
        self.__citys = citys

    def get_citys_list(self):
        return list(self.__citys.keys())

    def __getitem__(self, item):
        city = self.get_citys_list()[item]
        return self.__citys.get(city)

    def __setitem__(self, key, value):
        self.__citys.setdefault(key, value)

    def __contains__(self, item):
        return item in list(self.__citys)

    def __str__(self):
        rslt = ""
        for idx, city in enumerate(self.get_citys_list()):
            rslt += "%s -- %s\n" %(str(idx).ljust(3), city)
        rslt += "a   -- 增加城市\n"
        rslt += "d   -- 删除城市\n"
        rslt += "q   -- 退出\n"
        return rslt

    def __len__(self):
        return len(self.__citys)



cs = Citys()
cs.citys = {
    "beijing" : {

    },
    "shanghai" : {

    }
}

print(cs.citys)
for city in cs:
    print(city)

cs["wuhan"] = {

}
for city in cs:
    print(city)

print("lanzhou" in cs)
print(cs)
print(len(cs))

# cs.citys = "beijing"
# print(cs)