# _*_ coding : UTF-8 _*_
# 开发人员 : ChangYw
# 开发时间 : 2019/7/19 10:40
# 文件名称 : Test.PY
# 开发工具 : PyCharm

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
}
}
print(list(city.get("北京"))[0])
print(city.keys())
print(list(city.values()))
print(type(city.values()))