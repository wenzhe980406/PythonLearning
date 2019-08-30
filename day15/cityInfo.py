# _*_ coding : UTF-8 _*_
# 开发人员 : ChangYw
# 开发时间 : 2019/8/4 23:01
# 文件名称 : cityInfo.PY
# 开发工具 : PyCharm
# city = {
#     "北京" : {
#         "朝阳区" : ["朝阳公园","工体","朝阳大厦"],
#         "海淀区" : ["颐和园","香山公园","玉泉山"],
#         "丰台区" : ["园博园","卢沟桥文化旅游区","世界公园"]
# },
#     "上海" : {
#         "杨浦区": ["杨浦公园", "工体", "朝阳大厦"],
#         "虹口区": ["虹口足球场","鲁迅公园","上海大厦"],
#         "浦东新区": ["迪士尼","野生动物园","东方明珠"]
# },
#     "武汉" : {
#         "江汉区": ["武汉博物馆", "江汉关博物馆", "汉口江滩公园"],
#         "武昌区": ["黄鹤楼","东湖风景区","蛇山"],
#         "汉阳区": ["归元禅寺","古琴台","龟山"]
# },
#     "广州" : {
#         "天河区": ["广州世界大观", "华南植物园", "天河公园"],
#         "白云区": ["白云山","云台花园","帽峰山"],
#         "黄埔区": ["黄埔军校旧址纪念馆","南海神庙","辛亥革命纪念馆"]
#     }
# }
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
            rslt += "%s -- %s\n" %(str(idx + 1).ljust(3), city)
        rslt += "a   -- 增加城市\n"
        rslt += "d   -- 删除城市\n"
        rslt += "q   -- 退出\n"
        return rslt


    def __len__(self):
        return len(self.__citys)


class Areas:
    def __init__(self, Areas = {}):
        self.__Areas = Areas

    @property
    def Areas(self):
        return self.__Areas

    @Areas.setter
    def Areas(self, Areas):
        self.__Areas = Areas

    def get_Areas_list(self):
        return list(self.__Areas.keys())

    def __getitem__(self, item):
        Area = self.get_Areas_list()[item]
        return self.__Areas.get(Area)

    def __setitem__(self, key, value):
        self.__Areas.setdefault(key, value)

    def __contains__(self, item):
        return item in list(self.__Areas)

    def __str__(self):
        rslt = ""
        for idx, area in enumerate(self.get_Areas_list()):
            rslt += "%s -- %s\n" %(str(idx + 1).ljust(3), area)
        rslt += "a   -- 增加地区\n"
        rslt += "d   -- 删除地区\n"
        rslt += "q   -- 退出\n"
        return rslt

    def __len__(self):
        return len(self.__Areas)

class Sites:
    def __init__(self, Sites = []):
        self.__Sites = Sites

    @property
    def Sites(self):
        return self.__Sites

    @Sites.setter
    def Sites(self, Sites):
        self.__Sites = Sites

    def get_Sites_list(self):
        return self.__Sites

    def __getitem__(self, item):
        Site = self.get_Sites_list()[item]
        return self.__Sites[Site]

    def __setitem__(self, site):
        self.__Sites.append(site)

    def __contains__(self, item):
        return item in self.__Sites

    def __str__(self):
        rslt = ""
        for idx, site in enumerate(self.get_Sites_list()):
            rslt += "%s -- %s\n" %(str(idx + 1).ljust(3), site)
        rslt += "a   -- 增加地点\n"
        rslt += "d   -- 删除地点\n"
        rslt += "q   -- 退出\n"
        return rslt

    def __len__(self):
        return len(self.__Sites)

def func(city,choice_input):
    if "a" == choice_input.lower():
        city_set = input("请输入要添加的城市：").strip()
        city.setdefault(city_set, {})
    elif "d" == choice_input.lower():
        city_del_num = input("请输入要删除的城市：").strip()
        city_del = list(city)[int(city_del_num) - 1]
        city.pop(city_del)
    elif "q" == choice_input.lower():
        return None

def main():
    cs = Citys()
    if cs.citys == {}:
        print("暂未城市信息，请添加！")
    while True :
        city_choice_input = input(cs)
        func(cs.citys, city_choice_input)
        if city_choice_input.isdigit():
            if int(city_choice_input) > 0 or int(city_choice_input) < 10:
                area = list(cs.citys)[int(city_choice_input) - 1]
                break

    print("欢迎查询%s" % area)
    ar = Areas()
    if ar.Areas == {}:
        print("暂未地区信息，请添加！")
    while True:
        area_choice_input = input(ar)
        func(ar.Areas,area_choice_input)
        if area_choice_input.isdigit():
            if int(area_choice_input) > 0 or int(area_choice_input) < 10:
                site = list(ar.Areas)[int(area_choice_input) - 1]
                break

    print("欢迎查询%s" % site)
    st = Sites()
    if st.Sites == {}:
        print("暂未地区信息，请添加！")
    while True:
        site_choice_input = input(st)

        if "a" == site_choice_input.lower():
            site_set = input("请输入要添加的地点：").strip()
            st.Sites.append(site_set)
        elif "d" == site_choice_input.lower():
            city_del_num = input("请输入要删除的地点：").strip()
            city_del = list(st.Sites)[int(city_del_num) - 1]
            st.Sites.pop(city_del)
        elif "q" == site_choice_input.lower():
            return quit(0)


if __name__ == '__main__':
    main()