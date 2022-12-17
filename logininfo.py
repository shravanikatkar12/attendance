import tkinter
import mysql.connector
from tkinter import Tk

mydb = mysql.connector.connect(
    host="localhost",
    user="root",
    passwd="root@123",
    database="student"

)

class lo1:
    def __init__(self):

class Form(tkinter.Frame):

    def __init__(self, parent):
        tkinter.Frame.__init__(self, parent)
        self.parent = parent
        self.initialize_interface()

    def initialize_interface(self):
        self.parent.title("login")  # title of the form
        self.parent.config(background="lavender")  # background color
        self.parent.geometry("300x100")  # size of the form
        self.parent.resizable(False, False)  # disables resize of hegiht and width

        global username  # our variables
        global password  # we use global for the other function to use it

        username = tkinter.StringVar()  # we indicate what type of variables we declared
        password = tkinter.StringVar()  # which is string type

        self.labelUser = tkinter.Label(self.parent, text="Username: ", background="dark slate gray", foreground="White",
                                       font="Arial 8 bold")
        self.labelUser.place(x=25, y=25)

        self.entryUser = tkinter.Entry(self.parent, textvariable=username)
        self.entryUser.place(x=100, y=25)

        self.labelPass = tkinter.Label(self.parent, text="Password: ", background="dark slate gray", foreground="White",
                                       font="Arial 8 bold")
        self.labelPass.place(x=25, y=50)

        self.entryPass = tkinter.Entry(self.parent, textvariable=password)
        self.entryPass.place(x=100, y=50)

        self.buttonLogin = tkinter.Button(self.parent, text="LOGIN", font="Arial 8 bold", command=logs)
        self.buttonLogin.place(height=45, width=60, x=230, y=25)


def logs():
    mycursor = mydb.cursor()
    sql = "SELECT * FROM login WHERE BINARY username = '%s' AND BINARY password = '%s'" % (
    username.get(), password.get())

    mycursor.execute(sql)

    if mycursor.fetchone():

        print("Successfully")

    else:

        print("Invalid Username And Password! Please try again......")


def main():
    root = tkinter.Tk()
    b = Form(root)
    b.mainloop()


if __name__ == "__main__":
    main()
