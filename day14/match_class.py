# _*_ coding : UTF-8 _*_
# 开发人员 : ChangYw
# 开发时间 : 2019/8/1 13:35
# 文件名称 : match_class.PY
# 开发工具 : PyCharm

# import random
#
# list_name=['梅西','C罗','贝克汉姆','内马尔','努巴沛','大卫','安东尼',
#            '杰克','贝尔','哈林','杰伦','哈瑞','埃尔克森','加雷斯','保罗']
#
# TOTAL_TURNS = 20
# GOAL_MIN = 1
# GOAL_MAX = 4
# GOAL_PLAYER_MIN = 5
# GOAL_PLAYER_MAX = 12
# turns = []
#
# for turn in range(TOTAL_TURNS):
#     goal_player = random.sample(list_name, random.randint(GOAL_PLAYER_MIN, GOAL_PLAYER_MAX))
#     adict = {player: random.randint(GOAL_MIN,GOAL_MAX) for player in  goal_player}
#     turns.append(adict)
#
# print(turns)
#
# turns=[]
# class Match:
#     def __init__(self,name,score):
#         self.name = name
#         self.score = score
#
#     def goal_player(self):
#         return  random.sample(list_name, random.randint(GOAL_PLAYER_MIN, GOAL_PLAYER_MAX))