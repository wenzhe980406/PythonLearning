# _*_ coding : UTF-8 _*_
# 开发人员 : ChangYw
# 开发时间 : 2019/8/5 21:52
# 文件名称 : WangShoot.PY
# 开发工具 : PyCharm

'''
	#1. 创建老王对象

	#2. 创建一个枪对象

	#3. 创建一个弹夹对象

	#4. 创建一些子弹

	#5. 创建一个敌人

	#6. 老王把子弹安装到弹夹中

	#7. 老王把弹夹安装到枪中

	#8. 老王拿枪

	#9. 老王开枪打敌人

	#10. 召唤电脑选手

'''
#玩家
import random

clip_num = 30
gun_list = ["M4A1", "AK47", "Kar-98K"]
clip_list = ["5.56mm", "7.62mm"]


class Player:
    def __init__(self,name):
        self.name = name
        self.HP = 100

    #拿枪
    def get_gun(self,Gun):
        print("玩家%s拿到了枪%s"%(self.name,Gun.name))

    #开枪
    def play_shoot(self,Gun,clip,bullet,enery_list):
        if len(enery_list) > 0:
            for i in enery_list:
                if i.HP <= 0:
                    print(i.name,"电脑已被击败一个。")
                    del enery_list[enery_list.index(i)]
        else:
            print("电脑已全部被击败，游戏结束")
            return False
        return Gun.shoot(clip,bullet,enery_list)

class Enery:
    def __init__(self):
        self.name = "电脑选手"
        self.HP = 100

    # 开枪
    def play_shoot(self,bullet,enery_list,player):
        if player.HP == 0:
            print("您已被击败，游戏结束。")
            return False
        return Gun.com_shoot(bullet,enery_list,player)




#枪
class Gun:
    def __init__(self,name):
        self.name = name

    #装上弹匣
    def gun_shot(self,clip):
        self.name = clip.shot()

    #老王开枪
    def shoot(self,clip,bullet,enery_list):
        clip.show_clip(bullet)
        bullet.num -= 1
        #随机概率命中
        hit_rate = random.random()
        if self.name == gun_list[0]:
            if hit_rate >= 0.3:
                clip.show_clip(bullet)
                enery_random = random.choice(enery_list)
                enery_random.HP -= 35
                print("已命中敌人，干的漂亮！")
                if len(enery_list) == 0:
                    return False
                return True
            else:
                if bullet.num  == 0 :
                    print("游戏结束,没能击中敌人！")
                    return False
                print("尚未命中，加油。")
                return True
        elif self.name == gun_list[1]:
            if hit_rate >= 0.5:
                clip.show_clip(bullet)
                enery_random = random.choice(enery_list)
                enery_random.HP -= 45
                print("已命中敌人，干的漂亮！")
                if len(enery_list) == 0:
                    return False
                return True
            else:
                if bullet.num  == 0 :
                    print("游戏结束,没能击中敌人！")
                    return True
                print("尚未命中，加油。")
                return True
        elif self.name == gun_list[2]:
            if hit_rate >= 0.5:
                clip.show_clip(bullet)
                enery_random = random.choice(enery_list)
                enery_random.HP -= 100

                print("已命中敌人，干的漂亮！")
                if len(enery_list) == 0:
                    return False
                return True
            else:
                if bullet.num  == 0 :
                    print("游戏结束,没能击中敌人！")
                    return False
                print("尚未命中，加油。")
                return True

    #电脑开枪
    def com_shoot(self,bullet,player):
        bullet.num -= 1
        #随机概率命中
        hit_rate = random.random()
        if hit_rate >= 0.8 :
            player.HP -= 20
            print("老王被击中，剩余HP：%s"%player.HP)
#弹匣:快速扩容弹匣
class Clip:
    def __init__(self,name):
        self.name = name
        self.num = clip_num

    #装弹
    def shot(self,bullet):
        print("已装备%s，正在装弹，子弹为%s，数量为：%d"%(self.name,bullet.name,bullet.num))

    #查看剩余子弹
    def show_clip(self,bullet):
        if bullet.num == 0 :
            print("子弹消耗完毕，没有完全消灭敌人。")
            return False
        print("子弹数量剩余：%d" % (bullet.num))

#子弹
class Bullet:
    def __init__(self,name,num = 30):
        self.name = name
        self.num = num

    #给弹
    def tobullet(self):
        if self.name == '7.62mm' :
            print("已检测到%s子弹，正在准备装弹%d颗"%(self.name,self.num))
            return [self.name * self.num]

#选装备
def equip(choice_list):
    for idx, choice in enumerate(choice_list):
        print("%s -- %s\n" % (str(idx + 1).ljust(3), choice), end="")
    choice_input = input("请选择一把你想要的装备:")
    return gun_list[int(choice_input) - 1]

def main():
    while True:
        wang = Player("老王")
        #选枪
        gun_choice = equip(gun_list)
        gun = Gun(gun_choice)
        wang.get_gun(gun)
        num = 5 if gun_choice == "Kar-98K" else 30
        #选子弹
        bullet_choice = equip(clip_list)
        bullet = Bullet(bullet_choice,num)
        print("已选择%s和子弹%s，自动配备快速扩容弹匣。"%(gun_choice,bullet_choice))
        clip = Clip("快速扩容弹匣")
        bullet.tobullet()
        clip.shot(bullet)

        enery1 = Enery()
        enery2 = Enery()
        enery3 = Enery()
        enery4 = Enery()
        enery5 = Enery()
        enery_list = [enery1 , enery2 , enery3 , enery4 , enery5]

        while True:
            a =  wang.play_shoot(gun, clip, bullet,enery_list)
            for i in enery_list:
                i.play_shoot(bullet,enery_list,wang)
            if not a:
                break




if __name__ == '__main__':
    main()