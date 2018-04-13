# coding: utf-8
from random import  randint
def masterAttr():
    masterdict =  {'史莱姆': [randint(11, 12), randint(4, 7), randint(8, 11), randint(10, 16)],
                   '鼻涕怪': [randint(11, 13), randint(4, 8), randint(8, 11), randint(10, 20)],
                   '强盗': [randint(30, 35), randint(20,25), randint(15, 30), randint(16, 22)],
                   '黑暗骷髅': [randint(33, 40), randint(20, 28), randint(15, 35), randint(16, 24)],
                   '变异野狼': [randint(40, 50), randint(30, 35), randint(20, 25), randint(25, 33)],
                   '暗黑法师': [randint(45, 55), randint(30, 38), randint(25, 35), randint(45, 50)],
                    }
    return masterdict