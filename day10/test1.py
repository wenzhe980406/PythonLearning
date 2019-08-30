# _*_ coding : UTF-8 _*_
# 开发人员 : ChangYw
# 开发时间 : 2019/7/26 15:17
# 文件名称 : test1.PY
# 开发工具 : PyCharm

# def city_country(city,country):
#     return "%s %s"%(city,country)
#
#
# def make_album(name,album,*songs_num):
#     music_album_dict = {}
#     music_album_dict.setdefault(name)
#     music_album_dict[name] = [album,*songs_num]
#     return music_album_dict
#
#
# def show_magicians(magic_list):
#     for x in magic_list :
#         print(x,end="\t")
#
# def make_great(aList):
#     bList = aList
#     for i in range(len(bList)) :
#         a = "the Great " + bList[i]
#         bList[i] = a
#     return bList
#
#
# if __name__ == '__main__':
#     city = "beijing"
#     country = "china"
#     print(city_country(city.capitalize(),country.capitalize()))
#
#     a = make_album("张杰","明天过后")
#     b = make_album("薛之谦","来日方长",10)
#     c = make_album("G.E.M.邓紫棋","毒苹果",3)
#     print(a,b,c)
#     while True:
#         name = input("请输入歌手的姓名：(q退出")
#
#         album = input("请输入歌手的专辑：(q退出")
#         if "Q" == name.upper() or "Q" == album.upper:
#             break
#         newLst = make_album(name,album)
#         print(newLst)
#     magic = ["LiuQian","Dynamo","Harary","Dean"]
#     show_magicians(magic)
#     make_great(magic)
#     show_magicians(magic)
#     new_list = make_great(magic)
#     show_magicians(magic)
#     show_magicians(new_list)
#
#     if "LiuQian" in magic :
#         print("包含1")
#     if "the Great" in magic:
#         print("包含2")

