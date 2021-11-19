from tkinter import *

#Program 2 : This program will show how to change the button text once we click on it
#Note: command attribute is only used to handle just click event and not any other event. We even cant use to handle release event by uisng command.

win = Tk()
win.geometry("500x500")
win.resizable(0,0)

def show():
    b1["text"]="Rajnish"

def show2(b):
    b2["text"]="Kumar"

def show3(b):
    b3["text"]="Jha"

#show4 = lambda e: b4["text"]="Bangalore"
    
#Method 1: By using command attribute: Without passing any parameters
b1 = Button(win, text="Button1", font=("Arial",20), command=show)
#b1.config(command=show)
b1.pack()


#Method 2: By using command attribute: By passing parameter with LE: Pass object ref of the Button b2 on which we want to handle the event to the call function
b2 = Button(win, text="Button2", font=("Arial",20), command=lambda:show2(b2))
b2.pack()

#Method 3: By using bind() method: Without LE
b3 = Button(win, text="Button3", font=("Arial",20))
b3.bind("<Button>", show3)
b3.pack()

#Method 4: By using bind() method: With LE
b4 = Button(win, text="Button4", font=("Arial",20))
#b4.bind("<Button>", lambda e:b4["text"]="Bangalore")
b4.pack()

#NOTE: In order to use LE the expression shouldn't contains = sign otherwise the statement brocke.

win.mainloop()
