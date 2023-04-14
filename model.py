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
#Class Item, contain all item data
class Item:
    # Code = {0:weapon, 1:equipment, 9:extra}
    #Constructor of Item class
    def __init__(self, name="", desc="", price=0, dur=1, atk=0, code=0,):
        self.code = code #item code
        self.name = name #item name
        self.desc = desc #item description
        self.price = price #item price
        self.dur = dur #item defence
        self.atk = atk #item attack damage
        self.isUse = False #check if item is use or not
    def __str__(self) -> str:#function to automatically return in a readable text
        return f"{self.name} {self.desc} {self.price} {self.dur} {self.atk} {self.code} "
