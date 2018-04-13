# coding: utf-8
from colorama import Fore

def printColor(color,string):
    colorlist=["BLACK",
                "RED",
                "GREEN",
                "YELLOW",
                "BLUE",
                "MAGENTA",
                "CYAN",
                "WHITE"]
    if color in colorlist:
        if color=="RED":
            print Fore.RED + string
        if color=="GREEN":
            print Fore.GREEN + string
        if color == "YELLOW":
            print Fore.YELLOW + string
        if color == "BLUE":
            print Fore.BLUE + string
        if color == "MAGENTA":
            print Fore.MAGENTA + string
        if color == "WHITE":
            print Fore.WHITE + string
        if color == "CYAN":
            print Fore.CYAN + string
        if color == "BLACK":
            print Fore.BLACK + string
    else:
        print u"传入颜色异常"