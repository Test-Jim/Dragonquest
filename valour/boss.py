# coding: utf-8
from common.printColor import  printColor
class boss(object):
    def __init__(self):
        self.attack=100
        self.defense=100
        self.hp=1200
    def boss_(self):
        printColor(color='RED',string='警告警告！最终boss，暗黑王出现！！！')

