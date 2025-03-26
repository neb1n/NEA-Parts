from tkinter import *

main = Tk()

#!Centering Code
w = 300
h = 200
ws = main.winfo_screenwidth()
hs = main.winfo_screenheight()
x = (ws/2)-(w/2)
y = (hs/2)-(h/2)
main.geometry("%dx%d+%d+%d"%(w,h,x,y))

#!Configuring the window
main.title("Main Menu")
main.configure(bg="slateblue2")

#!Displaying on the window
#\ Labels

welcome_lbl = Label(main, text = "Welcome!", width = 10, font = ("Arial 12 bold"), fg = "black", bg = "slateblue2", justify = "center")

#!Function

def login_pressed():
    login()

#\Buttons

login_btn = Button(main, text = "Login", font=("Arial 15"), width = 10, bg = "mediumpurple1", command = login_pressed)
edit_btn = Button(main, text = "Edit", font=("Arial 15"), width = 10, bg = "mediumpurple1")
bookings_btn = Button(main, text = "Bookings", font=("Arial 15"), width = 10, bg = "mediumpurple1")

#!Function
def login():
    login_btn.pack_forget()
    edit_btn.pack()
    bookings_btn.pack()
    
#!Pack
welcome_lbl.pack()
login_btn.pack()
edit_btn.pack_forget()
bookings_btn.pack_forget()

main.mainloop()
