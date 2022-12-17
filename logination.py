import tkinter
import mysql.connector
from tkinter import Tk

mydb = mysql.connector.connect(
    host="localhost",
    user="root",
    passwd="root@123",
    database="student"

)

def openqr():
    from PIL import Image
    from matplotlib import pyplot as plt
    import time

    # create figure
    fig = plt.figure(figsize=(10, 7))

    # setting values to rows and column variables
    rows = 2
    columns = 2

    # reading images
    im1 = Image.open('SE.png')
    im2 = Image.open('HCI.png')
    im3 = Image.open('TOC.png')
    im4 = Image.open('DBMS.png')
    im5 = Image.open('Miniproject.png')
    im6 = Image.open('BC.png')

    # Adds a subplot at the 1st position
    fig.add_subplot(rows, columns, 1)

    # showing image
    im1.show()
    plt.axis('off')
    plt.title("DB")
    time.sleep(60)

    # Adds a subplot at the 2nd position
    fig.add_subplot(rows, columns, 2)

    # showing image
    im2.show()
    plt.axis('off')
    time.sleep(60)

    # Adds a subplot at the 3rd position
    fig.add_subplot(rows, columns, 3)

    # showing image
    im3.show()
    plt.axis('off')
    plt.title("HCI")
    time.sleep(60)

    # Adds a subplot at the 4th position
    fig.add_subplot(rows, columns, 4)

    # showing image
    im4.show()
    plt.axis('off')
    plt.title("DB")
    time.sleep(60)

    im5.show()
    plt.axis('off')
    plt.title("SE Tutorial")
    time.sleep(60)

    im6.show()
    plt.axis('off')
    plt.title("BC")
    time.sleep(60)

def openhome():
    import tkinter
    import webbrowser
    def open():
        webbrowser.open("https://docs.google.com/forms/d/19K5dJdd7FxAXg7IbsiXcThGwmRrh8iUwYpwuoFQKMvk/edit")

    def open1():
        webbrowser.open('https://mail.google.com/mail/u/0/?tab=rm&ogbl#inbox')

    def open3():
        webbrowser.open('timetable2.xlsx')
    def open4():
        webbrowser.open("about.html")

    master = tkinter.Tk()
    master.title("place() method")
    master.geometry("450x350")
    master.configure(bg='cyan')

    button2 = tkinter.Button(master, text="Open Excel Sheet", command=open)
    button2.place(x=25, y=100)


    button3 = tkinter.Button(master, text="Submit attendance",command=openqr)
    button3.place(x=200, y=100)
    button4 = tkinter.Button(master, text="Contact Me", command=open1)
    button4.place(x=400, y=100)
    button4 = tkinter.Button(master, text="Timetable",command=open3)
    button4.place(x=550, y=100)
    button5 = tkinter.Button(master, text="About Us",command=open4)
    button5.place(x=700, y=100)

    master.mainloop()


class Form(tkinter.Frame):

    def __init__(self, parent):
        tkinter.Frame.__init__(self, parent)
        self.parent = parent
        self.initialize_interface()

    def initialize_interface(self):
        self.parent.title("Login")  # title of the form
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

        self.buttonLogin = tkinter.Button(self.parent, text="LOGIN", font="Arial 8 bold", command=openhome)
        self.buttonLogin.place(height=45, width=60, x=230, y=25)


def logs():
    mycursor = mydb.cursor()
    sql = "SELECT * FROM login WHERE BINARY username = '%s' AND BINARY password = '%s'" % (
    username.get(), password.get())

    mycursor.execute(sql)

    if mycursor.fetchone():

        print("Successfully")

    else:

        print("Invalid Credentials")


def main():
    root = tkinter.Tk()
    b = Form(root)
    b.mainloop()


if __name__ == "__main__":
    main()
