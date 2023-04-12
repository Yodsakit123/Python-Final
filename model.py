import random

class GameData:
    def __init__(self):
        self.name = "Jane"
        self.money = random.randint(150, 310) + 0
        self.health = 100
        self.point = 0
        self.atk = 0
        self.dur = 1
        self.isUseWeapon = False
        self.isUseDef = False
