
from core.startUp import StartUpGame
from core.fightsys import FightSystem

# class startHere(object):
#     def __init__(self):
#         _instance_valour = StartUpGame()
#         _instance_fight = FightSystem()

if __name__=='__main__':
    _instance_valour = StartUpGame()
    _instance_fight = FightSystem()
    _instance_valour.opening()
    while True:
        _instance_fight.fight()

