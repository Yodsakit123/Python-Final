#Main file
from tkinter import *
from controller import UserController
#Class App, use to create an object to start the program
class App:
    #constructor
    def __init__(self, master):
        self.master = master #set object equal to the input object (Tk)
        self.master.geometry("500x800") #set the GUI to be 500x500
        self.master.resizable(False, False) 
        self.master.title("My Game") #set title
        self.controller = UserController(self.master) #called UserController class and input Tk()
        self.controller.show_welcome_view() #function to show the welcome GUI

root = Tk() #set root = Tk()
app = App(root) #called App class input Tk()
root.mainloop() #start GUI
