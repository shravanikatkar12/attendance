import tkinter as tk
from tkinter import ttk
from tkinter import Menu
class ty1:
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

      helpMenu.add_command(label="Add student")
      helpMenu.add_command(label="remove student")
      helpMenu.add_command(label="Attendance")

      menuBar.add_cascade(label="TY", menu=helpMenu)

      # Calling Main()
      win.mainloop()


