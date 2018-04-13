# coding: utf-8
'''
    Time: 2015.10.02
    Author: Lionel
    Cotent: start up Game Class.
            I am coding in a coffer bar with a girl.
            I love this kind of feel
'''
from common.func import keyboard
from common.printColor import printColor
from valour.valour_attr import valourAttr


class StartUpGame(object):
    def __init__(self):
        self.__User = valourAttr()

    def opening(self):
        print u'勇者城镇附近的火焰山，最近发生了一些稀奇古怪的事情，出现很多之前未曾出现的怪物，影响了勇者城镇和其他城市之间的贸易往来。'
        print u'于是商盟会决定出资一部分佣金，雇佣一个位强大的勇者，去探清事情的来龙去脉。'
        keyboard.next()
        printColor('RED',string='现在你就是这位勇者，请给角色起名：')
        self.__User.name = keyboard.input()
        printColor('RED', string='%s勇者诞生，初始化属性：攻击10，防御10，血量120,经验值0'%self.__User.name)
        keyboard.next()





