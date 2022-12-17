import tkinter
import mysql.connector
from tkinter import Tk

mydb = mysql.connector.connect(
    host="localhost",
    user="root",
    passwd="root@123",
    database="student"

)

def openNewWindow2():
    import time
    from PIL import Image
    while (True):
        im = Image.open('qrcode.png')
        im.show()
        time.sleep(60)


def openNewWindow():
    import tkinter as tk

    try:
        from Tkinter import Label
        from ttk import Style
        from tkFont import Font, nametofont
    except ImportError:
        from tkinter import Label
        from tkinter.ttk import Style
        from tkinter.font import Font, nametofont

    def get_background_of_widget(widget):
        try:
            # We assume first tk widget
            background = widget.cget("background")
        except:
            # Otherwise this is a ttk widget
            style = widget.cget("style")

            if style == "":
                # if there is not style configuration option, default style is the same than widget class
                style = widget.winfo_class()

            background = Style().lookup(style, 'background')

        return background

    class Link_Button(Label, object):
        def __init__(self, master, text, background=None, font=None, familiy=None, size=None, underline=True,
                     visited_fg="#551A8B", normal_fg="#0000EE", visited=False, action=None):
            self._visited_fg = visited_fg
            self._normal_fg = normal_fg

            if visited:
                fg = self._visited_fg
            else:
                fg = self._normal_fg

            if font is None:
                default_font = nametofont("TkDefaultFont")
                family = default_font.cget("family")

                if size is None:
                    size = default_font.cget("size")

                font = Font(family=family, size=size, underline=underline)

            Label.__init__(self, master, text=text, fg=fg, cursor="hand2", font=font)

            if background is None:
                background = get_background_of_widget(master)

            self.configure(background=background)

            self._visited = visited
            self._action = action

            self.bind("<Button-1>", self._on_click)

        @property
        def visited(self):
            return self._visited

        @visited.setter
        def visited(self, is_visited):
            if is_visited:
                self.configure(fg=self._visited_fg)
                self._visited = True
            else:
                self.configure(fg=self._normal_fg)
                self._visited = False

        def _on_click(self, event):
            if not self._visited:
                self.configure(fg=self._visited_fg)

            self._visited = True

            if self._action:
                self._action()

    if __name__ == "__main__":
        import webbrowser

        try:
            from Tkinter import Tk, Frame
        except ImportError:
            from tkinter import Tk, Frame

        def callback3():
            webbrowser.open_new("xyz.html")

        def callback():
            webbrowser.open_new(
                r"https://docs.google.com/forms/d/1yhUPqOea5yj-IzgrmQbUkNbjs6mwi3ulQzkZ9fYYCgY/edit")


        root = Tk()
        frame = Frame(root, bg="pink")
        frame.pack(expand=True, fill="both")

        link = Link_Button(frame, text="Home", action=callback3)
        link.pack(padx=10, pady=10)

        link = Link_Button(frame, text="Open Excel Sheet", action=callback)
        link.pack(padx=20, pady=10)

        link = Link_Button(frame, text="Open QR Code", action =openNewWindow2)
        link.pack(padx=30, pady=10)

        root.mainloop()

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

        self.buttonLogin = tkinter.Button(self.parent, text="LOGIN", font="Arial 8 bold",  command = openNewWindow)
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
