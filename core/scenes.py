# coding: utf-8
from common.printColor import  printColor
from random import randint
from common.func import keyboard
class risk_scene(object):
    @staticmethod
    def gas(hp):
        if randint(1,15)==1:
            printColor(color='YELLOW',string='你为了穿越一片毒林，中毒了，减少了一定的生命值')
            hp-=5
        return hp

    @staticmethod
    def maze(attack,hp):
        if  randint(1,15)==2:
            printColor(color='YELLOW', string='你发现了一座迷宫，是否选择探索迷宫')
            end=keyboard.confirm()
            if end:
                if randint(1, 3) == 1:
                    printColor(color='YELLOW', string='探索迷宫，你发现了一件神秘的武器，攻击力+10')
                    attack+=10
                else:
                    printColor(color='YELLOW', string='探索迷宫，你不幸掉进陷阱，生命值-10')
                    hp-=10
        return attack,hp

    @staticmethod
    def pick(defense):
        if randint(1,15)==3:
            printColor(color='YELLOW', string='路过一个浪人营地，得到了吟游诗人的祝福，防御+5')
            defense+=5
        return defense




