#Create Menubar in Python GUI Application
import tkinter as tk
from tkinter import ttk
from tkinter import Menu
from ty import *
def openty():
   t=ty1()
class cse1:
   def __init__(self):
      win = tk.Tk()
      win.title("Python GUI App")

      # Exit action


      def _quit():
         win.quit()
         win.destroy()
         exit()

      # Create Menu Bar
      menuBar = Menu(win)
      win.config(menu=menuBar)
      # File Menu
      fileMenu = Menu(menuBar, tearoff=0)

      fileMenu.add_separator()

      # Help Menu
      helpMenu = Menu(menuBar, tearoff=0)

      # department
      helpMenu = Menu(menuBar, tearoff=0)

      helpMenu.add_command(label="FY")
      helpMenu.add_command(label="SY")
      helpMenu.add_command(label="TY",command=openty)
      helpMenu.add_command(label="BTech")

      menuBar.add_cascade(label="CSE", menu=helpMenu)

      # Calling Main()
      win.mainloop()


