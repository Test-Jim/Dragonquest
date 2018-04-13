# coding: utf-8
from printColor import *
from common.printColor import  printColor

class keyboard:
    @staticmethod
    def next():
        printColor(color='GREEN',string='---敲击任意键继续---')
        raw_input()

    @staticmethod
    def confirm():
        printColor(color='GREEN', string='---按Y确认, 按其他键跳过---')
        user_input = raw_input().strip()
        if str(user_input).lower() == 'y':
            return True
        else:
            return False

    @staticmethod
    def input():
        printColor(color='RED', string='---请输入---')
        user_input = raw_input().strip()

        while 1:
            if not user_input:
                printColor(color='RED', string='---输入内容为空，请重新输入---')
                user_input = raw_input().strip()
            else:
                break
        return user_input