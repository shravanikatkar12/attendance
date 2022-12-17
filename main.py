#Create Menubar in Python GUI Application
import tkinter as tk
from tkinter import ttk
from tkinter import Menu
from cse import *
win = tk.Tk()
win.title("Python GUI App")
#Exit action
def opencse():
    c=cse1()
def openlogin():
    l=login1()
def _quit():
   win.quit()
   win.destroy()
   exit()
#Create Menu Bar
menuBar=Menu(win)
win.config(menu=menuBar)
#File Menu
fileMenu= Menu(menuBar, tearoff=0)

fileMenu.add_separator()
menuBar.add_cascade(label="Home", menu=fileMenu)
#Help Menu
helpMenu= Menu(menuBar, tearoff=0)

menuBar.add_cascade(label="About Us", menu=helpMenu)
# department
helpMenu= Menu(menuBar, tearoff=0)
helpMenu.add_command(label="CSE",command=opencse)

helpMenu.add_command(label="IT")
helpMenu.add_command(label="ENTC")
helpMenu.add_command(label="Civil")
menuBar.add_cascade(label="Departments", menu=helpMenu)
#login
helpMenu= Menu(menuBar, tearoff=0)
menuBar.add_cascade(label="Login", menu=helpMenu)
#Calling Main()
win.mainloop()
