from tkinter import *

#Program 3 : This program will show how to change the text and reset of the button once we click on it
#Note: command attribute is only used to handle just click event and not any other event. We even cant use to handle release event by uisng command.

win = Tk()
win.geometry("500x500")
win.resizable(0,0)

y=1
def show():
    global y
    y=y+1
    if(y%2==0):
        b1["text"]="Rajnish"
    else:
        b1["text"]="Button1"


y=1
def show2(b):
    global y
    y=y+1
    if(y%2==0):
        b2["text"]="Kumar"
    else:
        b2["text"]="Button2"

y=1
def show3(e):
    global y
    y=y+1
    if(y%2==0):
        x="Jha"
    else:
        x="Button3"


#Method 1: Using command attribute: Without LE i.e. without any parameters
b1 = Button(win, text="Button1", font=("Arial", 20), command=show)
#b1.config(command=show)
b1.pack()

#Method 2: Using command attribute: With LE i.e. with object ref as parameter
b2 = Button(win, text="Button2", font=("Arial", 20), command=lambda:show2(b2))
b2.pack()

x=StringVar()
x.set("Button3")
#Method 3: Using bind() method: Without LE i.e. without any parameters being passed to the callinf function but any parameter need to be passed with defined fun
b3 = Button(win, textvariable=x, font=("Arial", 20))
b3.bind("<Button>",show3)
b3.pack()


#NOTE: Dont know how to use LE in tkinter which takes = sign
"""
#Method 4: Using bind() method: With LE i.e. with object ref as parameter
b4 = Button(win, text="Button4", font=("Arial", 20))
b4.bind("<Bitton>",lambda e:)
b4.pack()
"""

win.mainloop()
