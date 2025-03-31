from tkinter import *

login = Tk()

#!Centering Code
w = 300
h = 200
ws = login.winfo_screenwidth()
hs = login.winfo_screenheight()
x = (ws/2)-(w/2)
y = (hs/2)-(h/2)
login.geometry("%dx%d+%d+%d"%(w,h,x,y))

#!Configuring the window
login.title("Login")
login.configure(bg="slateblue2")

#!Displaying on the window
#\Labels
login_lbl = Label(login, text = "Login", width = 10, font=("Arial 12 bold"), fg = "black", bg = "slateblue2", justify = "center")
username_lbl = Label(login, text = "Username", width = 10, font=("Arial 12 bold"), fg = "black", bg = "slateblue2", justify = "center")
password_lbl = Label(login, text = "Password", width = 10, font=("Arial 12 bold"), fg = "black", bg = "slateblue2", justify = "center")

#!Function
def login_in():
    username = username_txt.get()
    password = password_txt.get()
    if username == "admin" and password == "admin":
        top = Toplevel(login)
        top.geometry("100x100")
        top.title("Successful login")
        Label(top, text = "Logged in", font = ("Arial 12 bold"))
        username_txt.text = ""
        password_txt.text = ""
    else:
        top = Toplevel(login)
        top.geometry("100x100")
        top.title("Try again")
        Label(top, text = "Incorrect username/password", font = ("Arial 12 bold"))
        username_txt.text = ""
        password_txt.text = ""



#\Textbox
username_txt = Entry(login, width = 10, font=("Arial 12 bold"), fg = "black", bg = "slateblue1")
password_txt = Entry(login, width = 10, font=("Arial 12 bold"), fg  = "black", bg = "slateblue1")

#\Button
login_btn = Button(login, width = 10, text = "Login", font=("Arial 12 bold"), fg = "black", bg = "slateblue1", command = login_in)

#!Pack
login_lbl.pack()
username_lbl.pack()
username_txt.pack()
password_lbl.pack()
password_txt.pack()
login_btn.pack()

login.mainloop()
