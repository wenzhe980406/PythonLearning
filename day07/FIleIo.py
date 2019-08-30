# _*_ coding : UTF-8 _*_
# 开发人员 : ChangYw
# 开发时间 : 2019/7/23 11:32
# 文件名称 : FIleIo.PY
# 开发工具 : PyCharm

#openFIle

# f = open("text.txt","w")
# f.write("hello file\n")
# f.write("see u agein!")
# f.close()

# f = open("text.txt","r")
# for line in f:
#     print(line,end="")
# f.close()

#如何保存一个字典的数据
import json

data = {
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
#
# f = open("city_data.txt","w")
# f.write(str(data))
# f.close()
#
# f = open("city_data.txt","r")
# city_data = f.read()
# print(city_data)
# f.close()
# city_dict = eval(city_data)
# city_dict

#把字典存成json文件
#首先导入第三方的json模块
import  json
#
# f = open("city_json.json","w")
# f.write(json.dumps(data).encode("utf-8"))
# f.close()
#
# f = open("city_json.json","r")
# aDict = json.loads(f.read())
# f.close()
#
# print(aDict)

# #使用dump 和 load
#
# f = open("city_json2.json","w")
# json.dump(data,f)
# f.close()
#
# f = open("city_json2.json","r")
# aDict = json.load(f)
# f.close()
# print(aDict.get('北京'))


#pickle dump和load
import  pickle
# f = open("city_pickle1.pkl","wb")
# x = pickle.dumps(data)
# print(type(x))
# print(x)
# f.write(x)
# f.close()
#
# f = open("city_pickle1.pkl","rb")
# aDick = pickle.loads(f.read())
# f.close()
# print(aDick)

f = open("city_pickle2.pkl","wb")
pickle.dump(data,f)
f.close()

f = open("city_pickle2.pkl","rb")
aDict = pickle.load(f)
f.close()
print(aDict.get("北京"))