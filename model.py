#Model file, use to save all the data in the game
import random
#Class GameData, contain all the player data
class GameData:
    #Constructor of GameData class
    def __init__(self):
        self.name = "Jane" #player name
        self.money = random.randint(150, 310) + 0 #player money, random between 150 - 310 following the rule
        self.health = 100 #player health
        self.point = 0 #player point
        self.atk = 0 #player attack damage
        self.dur = 1 #player defence
        self.isUseWeapon = False #check if the weapon is use or not
        self.isUseDef = False #check if the armour is use or not
