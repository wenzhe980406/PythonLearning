# # _*_ coding : UTF-8 _*_
# # 开发人员 : ChangYw
# # 开发时间 : 2019/7/21 12:54
# # 文件名称 : day05HomeWork#02.PY
# # 开发工具 : PyCharm
#
# #2 三级菜单的综合练习系统
# if __name__ == "__main__" :
#     while True :
#         print("请选择城市编码:")
#         print("0 -- 北京")
#         print("1 -- 上海")
#         print("2 -- 武汉")
#         print("3 -- 广州")
#         print("q -- 退出")
#         city_choice = input("请输入您的选择: ")
#         if ("Q" == city_choice.upper()) :
#             print("您尚未操作，即将退出")
#             exit(0)
#         if (not city_choice.isdigit()) :
#             print("输入错误，请重新输入！")
#
#         city_choice = int(city_choice)
#         if (city_choice < 0 or city_choice > 3):
#             print("输入错误，请重新输入！")
#             break
#         if (0 == city_choice) :
#             while True:
#                 print("\t请选择北京的区：")
#                 print("\t0 -- 朝阳区")
#                 print("\t1 -- 海淀区")
#                 print("\t2 -- 丰台区")
#                 print("\tb -- 回退")
#                 print("\tq -- 退出")
#                 area_choice = input("请输入您的选择: ")
#                 if ("Q" == area_choice.upper()):
#                     print("您选择了退出，即将退出")
#                     exit(0)
#                 elif("B" == area_choice.upper()):
#                     print("您选择了返回上一级菜单，即将返回")
#                     break
#                 if (not area_choice.isdigit()):
#                     print("输入错误，请重新输入！")
#
#                 area_choice = int(area_choice)
#                 if (area_choice < 0 or area_choice > 3):
#                     print("输入错误，请重新输入！")
#                 elif(area_choice == 0) :
#                     while True :
#                         print("\t\t\t请选择北京朝阳区的地点：：")
#                         print("\t\t\t0 -- 朝阳公园")
#                         print("\t\t\t1 -- 工体")
#                         print("\t\t\t2 -- 人大")
#                         print("\t\t\tb -- 回退")
#                         print("\t\t\tq -- 退出")
#                         site_choice = input("请输入您的选择: ")
#                         if ("Q" == site_choice.upper()):
#                             print("您选择了退出，即将退出")
#                             exit(0)
#                         elif ("B" == site_choice.upper()):
#                             print("您选择了返回上一级菜单，即将返回")
#                             break
#                         if (not site_choice.isdigit()):
#                             print("输入错误，请重新输入！")
#                         site_choice = int(site_choice)
#                         if (site_choice < 0 or site_choice > 3):
#                             print("输入错误，请重新输入！")
#                         elif(site_choice == 0) :
#                             print("***********************************")
#                             print("   欢迎来到北京市朝阳区朝阳公园      ")
#                             print("          好山好水好妹子            ")
#                             print("***********************************")

city = dict()
city = {
    "北京" : {
        "朝阳区" : ["朝阳公园","工体","朝阳大厦"],
        "海淀区" : ["颐和园","香山公园","玉泉山"],
        "丰台区" : ["园博园","卢沟桥文化旅游区","世界公园"]
},
    "上海" : {
        "杨浦区": ["杨浦公园", "工体", "朝阳大厦"],
        "虹口区": ["虹口足球场","鲁迅公园","上海大厦"],
        "浦东新区": ["迪士尼","野生动物园","东方明珠"]
},
    "武汉" : {
        "江汉区": ["武汉博物馆", "江汉关博物馆", "汉口江滩公园"],
        "武昌区": ["黄鹤楼","东湖风景区","蛇山"],
        "汉阳区": ["归元禅寺","古琴台","龟山"]
},
    "广州" : {
        "天河区": ["广州世界大观", "华南植物园", "天河公园"],
        "白云区": ["白云山","云台花园","帽峰山"],
        "黄埔区": ["黄埔军校旧址纪念馆","南海神庙","辛亥革命纪念馆"]
    }
}
if __name__ == "__main__" :
    print("*" * 60)
    print("{:^60}".format("欢迎使用城市之家："))
    print("*" * 60)
    while True :
        print("城市列表如下：")
        citys = list(city.keys())
        for idx,city_name in enumerate(citys) :
            print("%d —— %s" %(idx + 1, city_name))
        print("q —— 退出")
        city_choice = input("请选择城市编码： ").strip()
        if("q" == city_choice.lower()) :
            print("感谢使用城市之家，欢迎下次再来")
            exit(0)
        if(not city_choice.isdigit()) :
            print("输入错误，请重新输入")
            continue
        city_choice = int (city_choice)
        if (city_choice < 1 or city_choice > len(citys)):
            print("您选择的城市编码不存在")
            continue
        city_name = citys[city_choice - 1]
        areas = city.get(city_name)
        while True :
            print("欢迎查询%s"%(city_name))
            for idx, area_name in enumerate(areas):
                print("%d —— %s" % (idx + 1, area_name))
            print("b —— 回退")
            print("q —— 退出")
            area_choice = input("请选择地区编码： ").strip()
            if ("q" == area_choice.lower()):
                print("感谢使用城市之家，欢迎下次再来")
                exit(0)
            if (not area_choice.isdigit()):
                print("输入错误，请重新输入")
                continue
            area_choice = int(area_choice)
            if (area_choice < 1 or area_choice > len(citys)):
                print("您选择的城市编码不存在")
                continue
            areasList = list(areas.keys())
            area_name = areasList[area_choice - 1]
            places = areas.get(area_name)
            while True :
                print("欢迎查询%s" % (area_name))
                for idx, place_name in enumerate(places):
                    print("%d —— %s" % (idx + 1, place_name))
                place_choice = input("请选择景点编码：")
                place_choice = int(place_choice)
                place_name = places[place_choice - 1]
                print("欢迎来到%s"%place_name)
                if 1 == city_choice :
                    if 1 == area_choice :
                        if 1 == place_choice :
                            print("***********************************")
                            print("   欢迎来到北京市朝阳区朝阳公园      ")
                            print("          好山好水好妹子            ")
                            print("***********************************")
                break
            break
        break

