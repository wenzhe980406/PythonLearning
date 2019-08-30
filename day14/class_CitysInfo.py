# _*_ coding : UTF-8 _*_
# 开发人员 : ChangYw
# 开发时间 : 2019/8/1 15:04
# 文件名称 : class_CitysInfo.PY
# 开发工具 : PyCharm


city_info = {}

class CitysInfo:
    def __init__(self,name):
        self.citys = dict()
        self.name = name

    def add_city(self,city):
        self.citys[self.name] = city

    def del_city(self,name):
        city_info.pop(name,None)

    @staticmethod
    def query_city():
        print("城市列表如下：")
        if city_info == {}:
            return "城市列表为空。"
        query_city_list = [i for i in city_info.keys()]
        for idx, city_name in enumerate(query_city_list):
            return "%d —— %s" % (idx + 1, city_name)

    def save(self):
        city_info.setdefault("%s"%self.name ,{})

class City:
    def __init__(self,name,area):
        self.name = name
        self.area = area
        self.areas = dict()

    def add_areas(self):
        self.areas.setdefault(self.area,[])


    def del_area(self,name,area):
        area_dict = city_info[name]
        area_dict.pop(area,None)

    @staticmethod
    def query_area(name):
        print("欢迎查询%s" % (name))
        if city_info[name] == {}:
            return "城市列表为空。"
        else:
            area_dict = dict(city_info[name])
            query_area_list = [i for i in area_dict.keys()]
            return [print("%d —— %s" % (idx + 1, area_name)) for idx, area_name in enumerate(query_area_list)]

    def save(self):
        city_info[self.name] = self.areas


class Area:
    def __init__(self,name,area,site):
        self.name = name
        self.area = area
        self.site = site
        self.sites = []

    def add_sites(self):
        self.sites.append(self.site)

    def del_sites(self,name,area,site):
        area_dict = city_info[name]
        site_list = area_dict[area]
        site_list.pop(site_list.index(site))

    @staticmethod
    def query_sites(name,area):
        area_dict = city_info[name]
        print("欢迎查询%s" % (area))
        if area_dict[area] == []:
            return "地点列表为空。"
        else:
            query_area_list = [i for i in area_dict[area]]
            return [print("%d —— %s" % (idx + 1, area_name)) for idx, area_name in enumerate(query_area_list)]

    def save(self):
        area_dict = city_info[self.name]
        area_dict[self.area] = self.sites


def main():
    print("*" * 60)
    print("{:^55}".format("欢迎使用城市之家："))
    print("*" * 60)

    while True:
        print(CitysInfo.query_city())
        city_name = input("请输入要添加的城市名称：").strip()
        if "Q" == city_name.upper():
            break
        city = CitysInfo(city_name)
        city.add_city(city_name)
        city.save()
        print(CitysInfo.query_city())

        print(City.query_area(city_name))
        area_name = input("请输入要添加的地区名称：").strip()
        if "Q" == area_name.upper():
            break
        area = City(city_name,area_name)
        area.add_areas()
        area.save()
        print(City.query_area(city_name))


        print(Area.query_sites(city_name,area_name))
        site_name = input("请输入要添加的地点名称：").strip()
        if "Q" == site_name.upper():
            break
        site = Area(city_name,area_name,site_name)
        site.add_sites()
        site.save()
        print(Area.query_sites(city_name, area_name))


if __name__ == '__main__':
    main()