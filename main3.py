from tkinter import *
from PIL import ImageTk  #pip install pillow
from  tkinter import messagebox
import mysql.connector
from tkinter import Tk
from home import *
mydb = mysql.connector.connect(
    host="localhost",
    user="root",
    passwd="root@123",
    database="student"

)
class Login:
    def __init__(self,root):
        self.root = root
        self.root.title("Login")
        self.root.geometry("1199x700+200+100")

        #Background image
        self.bg=ImageTk.PhotoImage(file="C:\shravani/1.jpg")
        self.bg_image=Label(self.root,image=self.bg).place(x=0,y=0,relwidth=1,relheight=1)

        #Login Frame

        Frame_login = Frame(self.root,bg="pink")
        Frame_login.place(x=330,y=150,width=500,height=400)

        # title & subtitle
        title= Label(Frame_login,text="Login Here",font=("Impact",35,"bold"),fg="#6162FF",bg="pink").place(x=120,y=30)
        subtitle = Label(Frame_login, text="Members Login Area", font=("Goudy old style", 15, "bold"), fg="#1d1d1d", bg="pink").place(x=120,
                                                                                                           y=100)
        # Username
        lbl_user = Label(Frame_login, text="Username", font=("Goudy old style", 15, "bold"), fg="grey",bg="pink").place(x=120,y=140)
        self.username = Entry(Frame_login, text="Username", font=("Goudy old style", 15), bg="#E7E6E6")
        self.username.place(x=120, y=170,width=320,height=35)

        # password
        lbl_password = Label(Frame_login, text="Password", font=("Goudy old style", 15, "bold"), fg="grey", bg="pink").place(x=120, y=210)
        self.password = Entry(Frame_login, text="Password", font=("Goudy old style", 15), bg="#E7E6E6")
        self.password.place(x=120, y=240, width=320, height=35)
        #Button
        forget = Button(Frame_login, text="Forget Password?", bd=0, cursor="hand2", font=("Goudy old style", 12),fg="#6162FF", bg="pink").place(x=120, y=280)
        submit = Button(Frame_login,command = self.logs, cursor="hand2",text="Login?", bd=0, font=("Goudy old style", 15), bg="#6162FF",fg="pink").place(x=120, y=320,height=40,width=188)

    #def check_function(self):

     #   if self.username.get()==""or self.password.get()=="":
      #      messagebox.showerror("Error","All fields are required",parent=self.root)
       # elif self.username.get()!="" or self.password.get()!="":
        #    messagebox.showerror("Error", "Invalid username or password", parent=self.root)
        #else:
         #   messagebox.showinfo("Welcome", f"Welcome {self.username.get()}")

def logs(self):
    mycursor = mydb.cursor()
    sql = "SELECT * FROM login WHERE BINARY username = '%s' AND BINARY password = '%s'" % (
    username.get(), password.get())

    mycursor.execute(sql)

    if mycursor.fetchone():

        print("Successfully")

    else:

        print("Invalid Username And Password! Please try again......")




root = Tk()
obj = Login(root)
root.mainloop()