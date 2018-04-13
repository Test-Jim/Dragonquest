# coding: utf-8
from common.func import keyboard
from common.printColor import printColor
from random import choice
from valour.valour_attr import valourAttr
from valour.master_attr import masterAttr
from scenes import risk_scene as RS
class FightSystem(valourAttr):
    def __init__(self):
        #怪物列表
        # self.masterdict=['slime','Dark skeleton','Runny nose','Mutant wolves','robber','Dark magician']
        super(FightSystem,self).__init__()

    def fight(self):
        self.yuGuai()
        self.RiskS()


    def figureOut(self,master_attr):
        # self.attack,self.defense,self.hp,self.exp,self.lv
        # master_attr[0],master_attr[1],master_attr[2],master_attr[3]
        while master_attr[2]>0 and self.hp>0:
            if (self.attack-master_attr[1])>=0:
                master_attr[2]=master_attr[2]-(self.attack-master_attr[1])
            if master_attr[2]<0:
                printColor('CYAN', string='你对怪物造成%s点伤害，怪物剩余血量0' % self.attack)
            else:
                printColor('CYAN', string='你对怪物造成%s点伤害，怪物剩余血量%s' % (self.attack,master_attr[2]))
            if master_attr[2]<=0:
                printColor('BLACK', string='战斗胜利！')
                self.exp+=master_attr[3]
                #升级
                if self.exp/self.lv>100:
                    self.lv+=1
                    self.attack+=3
                    self.defense+=3
                    self.hp+=100
                printColor('CYAN', string='目前属性—等级:%s,攻击:%s,血量:%s,经验:%s' % (self.lv,self.attack, self.hp,self.exp))
                break
            if (master_attr[0]-self.defense)>=0:
                self.hp=self.hp-(master_attr[0]-self.defense)
            printColor('CYAN', string='你受到%s点伤害,你剩余血量%s' % (master_attr[0],self.hp))
            if self.hp<=0:
                printColor('RED',string='血量不足，你已死亡！')
                break

    def yuGuai(self):
        masterdict = masterAttr()
        if self.lv in xrange(1,5):
            master = choice(['史莱姆', '鼻涕怪'])
        elif self.lv in xrange(5,10):
            master = choice(['强盗', '黑暗骷髅'])
        else:
            master=choice(['变异野狼', '暗黑法师'])
        print '警告!你遇到了一只 %s,请选择逃跑还是战斗'%master
        end=keyboard.confirm()
        if end==True:
            master_attr=masterdict[master]
            self.figureOut(master_attr)
        else:
            print '逃跑成功，小心下次遇怪！'

    def RiskS(self):
        self.hp=RS.gas(self.hp)
        self.attack,self.hp=RS.maze(self.attack,self.hp)
        self.defense=RS.pick(self.defense)