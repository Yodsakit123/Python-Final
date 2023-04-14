#View file, all the GUI are in this file
from tkinter import *
from tkinter import ttk
from model import Item

#WelcomeView class, the welcome view GUI and ask for the player's name
class WelcomeView:
    #Constructor of WelcomeView class
    def __init__(self, master, controller):
        self.master = master #master = Tk()
        self.controller = controller#controller = object, input from the controller
        self.frame = Frame(self.master, width=500, height=600, padx=20, pady=20) #Set GUI grid
        self.frame.pack()

        self.name_label = Label(self.frame, text="Game", font=("Helvetica", 48))#game name label
        self.name_label.grid(row=0, column=0, columnspan=2, padx=10, pady=40, sticky="n")

        self.name_label = Label(self.frame, text="Enter your name:", font=("Helvetica", 14))#enter name label
        self.name_label.grid(row=1, column=0, padx=10, pady=10)

        self.name_entry = Entry(self.frame, font=("Helvetica", 14), bg="white")#enter name box
        self.name_entry.grid(row=1, column=1, padx=10, pady=10)

        play_button = Button(self.frame, text="Play", font=("Helvetica", 14), command=lambda: self.start_game(self.name_entry.get()), bg="#4CAF50", fg="white", padx=20, pady=10)
        play_button.grid(row=2, column=0, columnspan=2, padx=10, pady=10)#play button, press to start the game and get player's name

    #function to start game, use in the play button
    def start_game(self, name):
        self.controller.gamedata.name = name #deliver player's name to the model
        self.controller.show_menu_view() #call the function to show the in game menu GUI
#MenuView class, in game main menu GUI
class MenuView:
    #COnstructor
    def __init__(self, master, controller):
        self.master = master #master = TK()
        self.controller = controller #controller = object
        self.frame = Frame(self.master, width=500, height=300) #set up GUI grid
        self.frame.pack(padx=10, pady=10)

        # Player information
        player_info_frame = Frame(self.frame, relief=SOLID, bd=1)#set up player info frame
        player_info_frame.pack(side=LEFT, padx=20)

        player_label = ttk.Label(player_info_frame, text="Player", font=("Helvetica", 18, "bold"), anchor="center")#label
        player_label.pack(pady=5)

        self.name_label = ttk.Label(player_info_frame, text=f"Name: {self.controller.gamedata.name}", font=("Helvetica", 14))#player name label
        self.name_label.pack(pady=5)

        self.damage_label = ttk.Label(player_info_frame, text=f"Damage: {self.controller.gamedata.atk} Defense: {self.controller.gamedata.dur}", font=("Helvetica", 14))
        self.damage_label.pack(pady=5)#player;s damage label
        self.health_label = ttk.Label(player_info_frame, text=f"Health: {self.controller.gamedata.health}", font=("Helvetica", 14))
        self.health_label.pack(pady=5)#player's health label

        self.money_label = ttk.Label(player_info_frame, text=f"Money: {self.controller.gamedata.money}", font=("Helvetica", 14))
        self.money_label.pack(pady=5)#player's money label

        self.point_label = ttk.Label(player_info_frame, text=f"Point: {self.controller.gamedata.point}", font=("Helvetica", 14))
        self.point_label.pack(pady=5)#player's point label

        # Buttons
        button_frame = Frame(self.frame)#set up button gui frame
        button_frame.pack(side=RIGHT)

        self.inventory_btn = ttk.Button(button_frame, text="Inventory", command=self.controller.show_inventory_view, width=20)
        self.inventory_btn.pack(pady=5)#inventory button, press to call function to show inventory GUI

        self.shop_btn = ttk.Button(button_frame, text="Shop", command=self.controller.show_shop_view, width=20)
        self.shop_btn.pack(pady=5)#shop button, press to call function to show shop GUI

        self.room1_btn = ttk.Button(button_frame, text="Room 1", command=self.controller.show_room1_view, width=20)
        self.room1_btn.pack(pady=5)#room1 btn, press to call function to enter room

        self.room2_btn = ttk.Button(button_frame, text="Room 2", command=self.controller.show_room1_view, width=20)
        self.room2_btn.pack(pady=5)#room2 btn, press to call function to enter room

        self.room3_btn = ttk.Button(button_frame, text="Room 3", command=self.controller.show_room1_view, width=20)
        self.room3_btn.pack(pady=5)#room3 btn, press to call function to enter room

        self.room4_btn = ttk.Button(button_frame, text="Room 4", command=self.controller.show_room1_view, width=20)
        self.room4_btn.pack(pady=5)#room4 btn, press to call function to enter room
