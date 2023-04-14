#controller file, the user controller(input) are in this file
from model import  GameData, Item, Room 
from view import WelcomeView, MenuView, InventoryView, ShopView, RoomView
import threading
import time
import tkinter.messagebox as messagebox
import random
#UserController class, all the user control function 
class UserController:
    #constructor
    def __init__(self, master):
        self.master = master
        self.gamedata = GameData()#delegation from class GameData to be able to save the game data
        self.inventory = []
        self.state = 0#state 0 = game not end, state 1 = game finish
  
        #Initialise all rooms
        room1 = Room("Welcome to Dubrovnik", ["You wanna fight?\n"], 5, 100,2, 50)
        room1.drops = [Item("Shovel", "weapon", 15, 0, 80), Item("Treasure", "Extra", 10, 0, 3, 10)]

        room2 = Room("Welcome to Seville", ["the most dangerous land in the game\nHave big skeleton\nYou wanna fight?\n"], 70, 150, 7, 250)
        room2.drops = [Item("Shotgun", "weapon", 35, 0, 200 ), Item("Treasure", "It have somthing?", 10, 0, 4, 10)]

        room3 = Room("Welcome to Sibenik", [ "You wanna fight?\n"], 30, 100,3, 100)
        room3.drops = [Item("PistolExtra", "weapon", 100, 0, 50), Item("Healing Pad", "health +50", 20, 5, 50, 8)]

        room4 = Room("Welcome to Girona", [ "You wanna fight?\n"], 40, 200,4, 100)
        room4.drops = [Item("Healing Pad", "health +50", 20, 5, 50, 8), Item("Key", "for open treasure", 0, 0, 0, 9)]
        
        self.roomrun = Room("You running" , ["You run you lost 1 point.\n", f"you lose money\n"])
        self.roomWin = Room("You Win" , ["You can defeat monster.\n"])
        self.roomLose = Room("You loose" , ["You lost 3 point.\nYou got some money\n"])
        self.win = Room("You Win The Game Congratulation!" , ["Thank you for play this Game!\n"])
        self.gameover = Room("Game over!" , ["You do best, You can try again any time.\n"])

        self.rooms = [
            room1, room2, room3, room4
        ]
        self.currentRoom = self.rooms[random.randint(0, len(self.rooms)-1)]#random room
        #delegation all GUI class
        self.welcome_view = WelcomeView(self.master, self)
        self.menu_view = MenuView(self.master, self)
        self.inventory_view = InventoryView(self.master, self)
        self.shop_view = ShopView(self.master, self)

        self.room_view = RoomView(self.master, self)

        
        #Threading to loop program and keep update player info
        self.update_thread = threading.Thread(target=self.update_player_info, daemon=True)
        self.update_thread.start()
    def end(self):
        self.setBtn("disabled")
        self.room_view.run_btn.config(state="disabled")
        self.room_view.fight_btn.config(state="disabled")
    def update_player_info(self):#function to update player info
        while True:
            chwin = self.checkWin()#check if game is finish or not
            if chwin == 0 and self.state ==0:
                self.popup("Success", "You win the Game! Thank for playing!")
                self.room_view.refresh_view(self.win)
                self.state = 1
                self.end()
            elif chwin ==1 and self.state ==0:
                self.popup("Failed", "Game Over! Try again!")
                self.room_view.refresh_view(self.gameover)
                self.state = 1
                self.end()
            #setter, set all the label in menu with gamedata
            self.menu_view.name_label.config(text=f"Player: {self.gamedata.name}")
            self.menu_view.health_label.config(text=f"Health: {self.gamedata.health}")
            self.menu_view.money_label.config(text=f"Money: {self.gamedata.money}")
            self.menu_view.point_label.config(text=f"Point: {self.gamedata.point}")
            self.menu_view.damage_label.config(text=f"Damage: {self.gamedata.atk} Defense: {self.gamedata.dur}")
            if len(self.inventory) == 0:#if inventory is empty, disable use and sell btn
                self.inventory_view.drop_button.config(state="disabled")
                self.inventory_view.use_button.config(state="disabled")
            else:
                self.inventory_view.drop_button.config(state="normal")
                self.inventory_view.use_button.config(state="normal")

            time.sleep(1)#set delay to 1 second, to prevent from runtime error because of threading 
    #function to add item to inventory        
    def addItem(self, item):
        item.price = int(item.price*0.6)
        self.inventory.append(item)
    #function to sell item
    def dropItem(self, index):
        del self.inventory[index]
        self.inventory_view.selected_item_name.set('')
        self.inventory_view.selected_item_desc.set('')
        self.inventory_view.selected_item_price.set('')
        self.updateInv()
    #function to buy item
    def buyItem(self, item):
        if self.getItem(item.name) != None:#check item
            self.popup("Caution" , f"You cannot buy a {item.name}! You already have it.")
            return
        if(self.gamedata.money >= item.price):#
            if self.decidePopup("Confirm Action", "Are you sure?") :
                self.gamedata.money -= item.price
                self.addItem(item)
                self.popup("Complete" , f"You got a {item.name}!")
            else:
                pass
        else:
            self.popup("Caution" , "No enought money!")
    def updateInv(self):#function update inventory
        self.inventory_view.update(self.inventory)
    def popup(self, title, message):#function to show messagebox
        messagebox.showinfo(title, message)
    def decidePopup(self, title, message):#function to show messagebox with option
        confirmed = messagebox.askokcancel(title, message)
        return confirmed
    #Function to use item
    def useItem(self, name):
        item = self.getItem(name)
        if item.code == 8:#health pad
            self.dropItem(self.getItemIndex(name))
            self.gamedata.health += item.atk
            self.popup("Complete" , f"You Use a {item.name}!, Heal {item.atk} Health")
            return
        if item.code == 10:#tresure
            self.popup("Caution" , "You need key!")
            return
        if item.code == 9:#key
            for i in self.inventory:
                if i.code == 10:#check if inventory have tresure
                    self.popup("Complete" , f"You Use a {item.name}!, open {i.name} Health. Got {i.atk} point")  
                    self.dropItem(self.getItemIndex(name))
                    self.dropItem(self.getItemIndex(i.name))
                    break
            self.popup("Caution", "You not have Tresure!")
            return
        if not item.isUse:#if item not in use
            if ((not self.gamedata.isUseWeapon) and item.code == 0) :
                item.isUse = True
                self.gamedata.isUseWeapon = True
                self.gamedata.atk = item.atk
                self.inventory_view.use_button.config(text="Unused")
                
                self.popup("Message", f"You using {item.name}")
            elif (not self.gamedata.isUseDef) and item.code == 1 :
                    item.isUse = True
                    self.gamedata.isUseDef = True
                    self.gamedata.dur = item.dur
                    self.inventory_view.use_button.config(text="Unused")
                    
                    self.popup("Message", f"You using {item.name}")
            else:
                self.popup("Caution", f"You already using item! Please unused it before and try again!")
        else:#if item in use
            item.isUse = False#unused item
            if item.code==0:
                self.gamedata.isUseWeapon = False
                self.gamedata.atk = 0
            if item.code==1:
                self.gamedata.isUseDef = False
                self.gamedata.dur = 1
            self.inventory_view.use_button.config(text="Use")
            self.popup("Message", f"You unused {item.name}!")
    #function to sellItem        
    def sellItem(self, name):
        item = self.getItem(name)
        if item.isUse:
            self.popup("Caution", f"You already using item! Please unused it before and try again!")
        else:
            self.dropItem(self.getItemIndex(name))
            self.gamedata.money += int(item.price*0.6)
            self.popup("Complete" , f"You sell a {item.name}!, Recieve {int(item.price*0.6)}")
    #function to get item
    def getItem(self, name):
        for i in self.inventory:
            if i.name == name:
                return i
    #function to get item index
    def getItemIndex(self, name):
        n = 0
        for i in self.inventory:
            if i.name == name:
                return n
            n+=1
    def setBtn(self, action):
        self.menu_view.inventory_btn.config(state=action)
        self.menu_view.shop_btn.config(state=action)
        self.menu_view.room1_btn.config(state=action)
        self.menu_view.room2_btn.config(state=action)
        self.menu_view.room3_btn.config(state=action)
        self.menu_view.room4_btn.config(state=action)
    #function to run, use when enter the room   
    def run(self):
        if self.decidePopup("Caution", "You wanna run! you will lose points 5 and some money"):
            if self.gamedata.point - 5 >=0:
                self.gamedata.point -= 5
            self.losemoney = random.randint(0,10)
            if self.gamedata.money - self.losemoney >= 0:
                self.gamedata.money -= self.losemoney
            self.room_view.refresh_view(self.roomrun)
            self.room_view.run_btn.config(state="disabled")
            self.room_view.fight_btn.config(state="disabled")
            self.setBtn("normal")
    #function to fight, use when enter the room
    def fight(self):
        if self.decidePopup("Caution", "You wanna fight! if you lose you will lose 3 points"):
            self.curRoom.health -= self.gamedata.atk
            if self.curRoom.health > self.gamedata.atk:
                self.gamedata.health -= int(self.curRoom.damage/self.gamedata.dur)
                self.room_view.refresh_view(self.roomLose)
                if self.gamedata.point - 3 >=0:
                    self.gamedata.point -= 3
                self.gamedata.money += int(self.curRoom.money/4)
            else:
               self.gamedata.health -= int(self.curRoom.damage/self.gamedata.dur)
               self.curRoom.health = self.curRoom.baseHp
               self.gamedata.point += self.currentRoom.point
               self.gamedata.money += int(self.curRoom.money)
               self.room_view.refresh_view(self.roomWin)
               dropItem = [self.addItem(i) for i in self.curRoom.drops]
               self.popup("Message", f"you got a { [f'{i.name}' for i in self.curRoom.drops]}!")
            if(self.gamedata.isUseDef):
                self.gamedata.isUseDef = False
                n = 0
                for i in self.inventory:
                    if i.code ==1:
                        self.useItem(i.name)
                        self.dropItem(n)
                        break
                    n+=1
                self.popup("Caution", "Your armour is broken")
            self.room_view.run_btn.config(state="disabled")
            self.room_view.fight_btn.config(state="disabled")
            self.setBtn("normal")
    #function to check win
    def checkWin(self):
        if self.gamedata.point>=10:
            return 0

        if self.gamedata.health <= 0:
            return 1
    #function to show welcome view, disable other GUI
    def show_welcome_view(self):
        self.menu_view.frame.pack_forget()
        self.inventory_view.frame.pack_forget()
        self.shop_view.frame.pack_forget()
        self.room_view.frame.pack_forget()

        self.welcome_view.frame.pack()
   #function to show in game menu 
    def show_menu_view(self):
        self.welcome_view.frame.pack_forget()

        self.menu_view.frame.pack()
    #function to show inventory
    def show_inventory_view(self):
        self.updateInv()
        self.shop_view.frame.pack_forget()
        self.room_view.frame.pack_forget()

        self.inventory_view.frame.pack()
    #function to show room
    def show_room1_view(self):
        if(self.decidePopup("Caution", "Are you sure to enter this room?")):
            self.setBtn("disabled")
            self.curRoom = self.rooms[random.randint(0, len(self.rooms))-1]
            self.curRoom.content.append(f"Monster Power :{self.curRoom.damage}\n")
            self.curRoom.content.append(f"Monster Health :{self.curRoom.health}/{self.curRoom.baseHp}\n")
            self.room_view.refresh_view(self.curRoom)
            self.shop_view.frame.pack_forget()
            self.inventory_view.frame.pack_forget()
            self.room_view.frame.pack()

    #function to show shop
    def show_shop_view(self):
        self.inventory_view.frame.pack_forget()
        self.room_view.frame.pack_forget()

        self.shop_view.frame.pack()
