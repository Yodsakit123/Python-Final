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
#InventoryView class, GUI of the inventory
class InventoryView:
    #Constructor
    def __init__(self, master, controller):
        self.master = master#master = Tk()
        self.controller = controller#controller = obejct
        self.frame = Frame(self.master, width=400, height=400)#set up inventory GUI grid
        self.frame.pack(padx=10, pady=30)

        self.items = self.controller.inventory #get player's items

        self.border_frame = Frame(self.frame, bd=5, relief=GROOVE)#set up frame
        self.border_frame.pack(side=TOP, fill=BOTH, expand=True)

        self.heading_label = Label(self.border_frame, text='My Inventory')#label
        self.heading_label.pack(side=TOP, pady=10)

        self.listbox = Listbox(self.border_frame, selectmode=SINGLE)#Listbox to show items and can be select
        self.listbox.pack(side=LEFT, fill=BOTH, expand=True)

        for item in self.items:#add items to listbox
            self.listbox.insert(END, item.name)

        self.card_frame = Frame(self.frame, bd=5, relief=GROOVE)#set up item detail frame
        self.card_frame.pack(side=BOTTOM, fill=BOTH, expand=True)

        # Create labels for displaying details
        self.item_name_label = Label(self.card_frame, text='Item Name:')#item name label
        self.item_name_label.grid(row=0, column=0, padx=10, pady=5, sticky=W)

        self.item_desc_label = Label(self.card_frame, text='Description:')#item description label
        self.item_desc_label.grid(row=1, column=0, padx=10, pady=5, sticky=W)

        self.item_desc_label = Label(self.card_frame, text='Price:')#Price label
        self.item_desc_label.grid(row=2, column=0, padx=10, pady=5, sticky=W)


        self.selected_item_name = StringVar()#set to be string
        self.selected_item_desc = StringVar()
        self.selected_item_price = StringVar()

        self.selected_item_name_label = Label(self.card_frame, textvariable=self.selected_item_name)
        self.selected_item_name_label.grid(row=0, column=1, padx=10, pady=5, sticky=W)#selected item label

        self.selected_item_desc_label = Label(self.card_frame, textvariable=self.selected_item_desc, wraplength=300)
        self.selected_item_desc_label.grid(row=1, column=1, padx=10, pady=5, sticky=W)#selected item desciption

        self.selected_item_price_label = Label(self.card_frame, textvariable=self.selected_item_price, wraplength=300)
        self.selected_item_price_label.grid(row=2, column=1, padx=10, pady=5, sticky=W)#selected item price

        self.listbox.bind('<<ListboxSelect>>', self.show_item_details)#if press of item in listbox, call function to show the item details

        # Create a button frame for the use and sell buttons
        self.button_frame = Frame(self.card_frame)
        self.button_frame.grid(row=3, column=1, pady=10)

        # Create a use button
        self.use_button = Button(self.button_frame, text='Use', command=self.use_item)
        self.use_button.pack(side=LEFT, padx=5)

        # Create a sell button
        self.drop_button = Button(self.button_frame, text='Sell', command=self.drop_item)
        self.drop_button.pack(side=LEFT, padx=5)
    #Function to update inventory
    def update(self, inventory):
        self.items = self.controller.inventory
        #Get current scroll position
        cur_scroll_pos = self.listbox.yview()
        #Update inventory listbox
        self.listbox.delete(0, END)
        for item in inventory:
            self.listbox.insert(END, item.name)
        #Restore scroll position
        self.listbox.yview_moveto(cur_scroll_pos[0])

   #function to show selected item details, event to prevent from error
    def show_item_details(self,event):
        selection = self.listbox.curselection()#listbox function to get the index of item

        if selection:#if true, show the item detail

            index = selection[0]
            
            itemName = self.listbox.get(index)#get item name
            itemDesc=""#create item description variable
            itemPrice=""#create item price variable
            for i in self.items:#check item
                if (i.name==itemName):
                    itemDesc = i.desc#get item description
                    itemPrice = int(i.price*0.6)#get item price and decrease item sell price
                    if i.isUse:
                        self.use_button.config(text="Unused")
                    else:
                        self.use_button.config(text="Use")
                    break
                    

            self.selected_item_name.set(itemName)#show item name
            self.selected_item_desc.set(itemDesc)#show item description
            self.selected_item_price.set(itemPrice)#show item price
    def use_item(self):#function to use item
        selection = self.listbox.curselection()
        if selection:
            index = selection[0]
            name = self.listbox.get(index)
            self.controller.useItem(name)
                    
    def drop_item(self):#function to sell item
        if self.controller.decidePopup("Confirm Action", "Are you sure ?"):
            selection = self.listbox.curselection()

            if selection:
                index = selection[0]
                name = self.listbox.get(index)
                self.controller.sellItem(name)
                #ShopView class, GUI of shop
class ShopView:
    #Constructor
    def __init__(self, master, controller):
        self.master = master#master = Tk()
        self.controller = controller#controller = object
        self.frame = Frame(self.master, width=400, height=400)
        self.frame.pack(padx=10, pady=30)

        self.items = []#shop item list
        self.items.append(Item("Knife", "Good for begining damage 10", 50, 0, 10 ))
        self.items.append(Item("Rifle", "Medium range! Damage 30", 150, 0, 30))
        self.items.append(Item("Pistol", "You are cowboy! damage 20", 100, 0, 20))
        self.items.append(Item("Bomb", "Boom!", 300, 0, 50))
        self.items.append(Item("Sniper", "Long range! 40 power", 250, 0, 40))
        self.items.append(Item("Key", "for open treasure", 100, 0, 0, 9))
        self.items.append(Item("Healing Pad", "health +50", 30, 5, 50, 8))
        self.items.append(Item("Armour1", "increase defense 2", 200, 2, 0, 1))
        self.items.append(Item("Armour2", "increase defense 3", 300, 3, 0, 1))

        self.border_frame = Frame(self.frame, bd=5, relief=GROOVE)
        self.border_frame.pack(side=TOP, fill=BOTH, expand=True)

        self.heading_label = Label(self.border_frame, text='Shop')
        self.heading_label.pack(side=TOP, pady=10)

        self.listbox = Listbox(self.border_frame, selectmode=SINGLE)#shop listbox
        self.listbox.pack(side=LEFT, fill=BOTH, expand=True)

        for item in self.items:#insert item in shop list into listbox
            self.listbox.insert(END, item.name)

        self.card_frame = Frame(self.frame, bd=5, relief=GROOVE)
        self.card_frame.pack(side=BOTTOM, fill=BOTH, expand=True)

        # Create labels for displaying details
        self.item_name_label = Label(self.card_frame, text='Item Name:')
        self.item_name_label.grid(row=0, column=0, padx=10, pady=5, sticky=W)

        self.item_desc_label = Label(self.card_frame, text='Description:')
        self.item_desc_label.grid(row=1, column=0, padx=10, pady=5, sticky=W)

        self.item_desc_label = Label(self.card_frame, text='Price:')
        self.item_desc_label.grid(row=2, column=0, padx=10, pady=5, sticky=W)

        self.selected_item_name = StringVar()#convert to string
        self.selected_item_desc = StringVar()
        self.selected_item_price = StringVar()

        self.selected_item_name_label = Label(self.card_frame, textvariable=self.selected_item_name)
        self.selected_item_name_label.grid(row=0, column=1, padx=10, pady=5, sticky=W)

        self.selected_item_desc_label = Label(self.card_frame, textvariable=self.selected_item_desc, wraplength=300)
        self.selected_item_desc_label.grid(row=1, column=1, padx=10, pady=5, sticky=W)

        self.selected_item_price_label = Label(self.card_frame, textvariable=self.selected_item_price, wraplength=300)
        self.selected_item_price_label.grid(row=2, column=1, padx=10, pady=5, sticky=W)

        self.listbox.bind('<<ListboxSelect>>', self.show_item_details)#call function to show item detail

        # Create a button frame for buy buttons
        self.button_frame = Frame(self.card_frame)
        self.button_frame.grid(row=3, column=1, pady=10)

        # Create a buy button
        self.use_button = Button(self.button_frame, text='Buy', command=self.use_buy)
        self.use_button.pack(side=RIGHT, padx=5)#call function buy item when the btn is press

    #show item detail in shop, event to prevent from error
    def show_item_details(self,event):
        selection = self.listbox.curselection()

        if selection:
            index = selection[0]
            
            itemName = self.listbox.get(index)
            itemDesc=""
            itemPrice=""
            for i in self.items:
                if (i.name==itemName):
                    itemDesc = i.desc
                    itemPrice = i.price
                    break
                    

            self.selected_item_name.set(itemName)
            self.selected_item_desc.set(itemDesc)
            self.selected_item_price.set(itemPrice)
    #buy item
    def use_buy(self):
        selection = self.listbox.curselection()

        if selection:
            index = selection[0]
            name = self.listbox.get(index)
            for i in self.items:
                if (i.name==name):
                    self.controller.buyItem(i)
                    break
#RoomView class, GUI of room
class RoomView:
    #Constructor
    def __init__(self, master, controller):
        self.master = master
        self.controller = controller
        self.frame = Frame(self.master, width=600, height=400, padx=20, pady=20)
        self.frame.pack()


        # Frame to display title and content
        title_frame = Frame(self.frame)
        title_frame.pack(side=TOP)

        # Label to display title
        self.title_label = ttk.Label(title_frame, text=self.controller.currentRoom.title, font=("Helvetica", 18, "bold"))
        self.title_label.pack(side=LEFT, padx=10, pady=10)

        # Frame to display buttons
        button_frame = Frame(self.frame)
        button_frame.pack(side=BOTTOM, pady=10)

        # Run button
        self.run_btn = ttk.Button(button_frame, text="Run", command=self.controller.run)
        self.run_btn.pack(side=LEFT, padx=10)

        # Fight button
        self.fight_btn = ttk.Button(button_frame, text="Fight", command=self.controller.fight)
        self.fight_btn.pack(side=LEFT, padx=10)

        # Frame to display content
        self.content_frame = Frame(self.frame, relief=None, bd=0)
        self.content_frame.pack(side=LEFT)

        # Text widget to display room content
        self.content_text = Text(self.content_frame, font=("Helvetica", 12), wrap=WORD, bg="white", height=200)
        self.content_text.pack(side=LEFT, padx=10, pady=10)
        for i in self.controller.currentRoom.content:
            self.content_text.insert(END, i)
        self.content_text.config(state=DISABLED)
    #refresh GUI
    def refresh_view(self, room):
        self.title_label.config(text=room.title)
        self.content_text.config(state=NORMAL)
        self.content_text.delete("1.0", END)
        self.run_btn.config(state="normal")
        self.fight_btn.config(state="normal")
        for i in room.content:
            self.content_text.insert(END, i)
        self.content_text.config(state=DISABLED)
