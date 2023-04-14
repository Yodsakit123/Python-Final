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
