# _*_ coding : UTF-8 _*_
# 开发人员 : ChangYw
# 开发时间 : 2019/7/21 16:03
# 文件名称 : day05HomeWork#01.PY
# 开发工具 : PyCharm

#球星模拟比赛
# #1、产生一个球星列表，["梅西","C罗",""...]
# 模拟3轮比赛:
# 随机从著名球星的列表,找出3-8个球星,每个球星的进球数,随机从1到4个
# 计算:连续3轮都进球的球星列表
# import random
#
# if __name__ == "__main__" :
#     star_list = ["斯特林","阿扎尔","库蒂尼奥","德布劳内","格列兹曼","凯恩","萨拉赫","梅西","内马尔","姆巴佩"]
#     star_dict = dict.fromkeys(star_list)
#     #比赛场次
#     game_times = 3
#     #定义空列表random_list_all = [] 用来存储所有随机球星列表
#     random_list_all = []
#     #模拟三场比赛
#     for i in range(game_times) :
#         # 随机抽选3-8个球星
#         random_num = random.randint(3, 8)
#         # 随机球星列表
#         # random_list = [random.choice(star_list) for _ in range(random_num)]
#         random_list = random.sample(star_list, random_num)
#         random_list_all.append(random_list)
#
#         #累计成绩加入字典values
#
#         for i in random_list :
#             score = random.randint(1,4)
#             if None ==star_dict[i] :
#                 star_dict[i] = score
#             else:
#                 star_dict[i] += score
#     print(star_dict)
#     print(random_list_all)
#     #求交集
#     a = list(set(random_list_all[0]).intersection(set(random_list_all[1])))
#     print(a)
#     b = list(set(a).intersection(set(random_list_all[2])))
#     print(b)
#
#     #字典的遍历
#     star_list_new = [[key,values] for key,values in star_dict.items() if not values]
#     star_list_new.sort()
#     print(star_list_new)
#
#     for _ in range(star_list_new.__len__() - 1) :
#         for i in range(star_list_new.__len__() - 1) :
#             if star_list_new[i][1] < star_list_new[i+1][1] :
#                 star_list_new[i][1],star_list_new[i+1][1] = star_list_new[i+1][1],star_list_new[i][1]
#     print(star_list_new)

import random

list_name=['梅西','C罗','贝克汉姆','内马尔','努巴沛','杰克','贝尔','哈林','杰伦','哈瑞']
turns=[]
TOTAL_TURNS = 3
GOAL_MIN = 1
GOAL_MAX = 4
GOAL_PLAYER_MIN = 3
GOAL_PLAYER_MAX = 8

for turn in range(TOTAL_TURNS):
    goal_player = random.sample(list_name, random.randint(GOAL_PLAYER_MIN, GOAL_PLAYER_MAX))
    adict = {player: random.randint(GOAL_MIN,GOAL_MAX) for player in  goal_player}
    turns.append(adict)

rslt = set(list_name)

all_players = dict.fromkeys(list_name, 0)
for turn in turns :
    rslt &= set(turn.keys())
    for player in turn.keys() :
        all_players[player] = all_players.get(player) + turn.get(player)

stat_players = [(goal, player) for player, goal in all_players.items()]
stat_players.sort(reverse=True)
print(stat_players)

print(turns)
print(rslt)
print(all_players)