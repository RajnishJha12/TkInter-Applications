from tkinter import *

#Program 1 :This program will show how to change the bg color of a window on ecah click
#Note: command attribute is only used to handle just click event and not any other event. We even cant use to handle release event by uisng command.

win = Tk()
win.geometry("500x500")
win.resizable(0,0)

x=1
def show():
    global x
    x=x+1
    if(x%2==0):
        win.configure(bg="red")
    else:
        win.configure(bg="blue")


x=1
def show2(b):
    global x
    x=x+1
    if(x%2==0):
        win.configure(bg="green")
    else:
        win.configure(bg="yellow")


x=1
def show3(b):
    global x
    x=x+1
    if(x%2==0):
        win.configure(bg="black")
    else:
        win.configure(bg="cyan")

#x=1
#show4 = lambda e: global x x=x+1 if(x%2==0):  win.configure(bg="black") else:  win.configure(bg="cyan")


        
#Method 1: By using simple command attribute: Without passing any parameter
b1 = Button(win, text="Button1", font=("Arial",20), command=show)
b1.pack()


#Method 2: By using command attribute with LE: By passing parameter i.e. by passing obejct ref b2 to the method call & pass any varaible
#to the defined method to handle click event.
b2 = Button(win, text="Button2", font=("Arial",20), command=lambda: show2(b2))
b2.pack()


#Method 3: By using bind() method: without LE but pass any vaiable to the defined method to hande the event like e or x or b something like that.

b3 = Button(win, text="Button3", font=("Arial",20))
b3.bind("<Button>", show3)
b3.pack()

#Method 4: By using bind() method: With LE but pass any vaiable to the defined method to hande the event like e or x or b something like that.

b4 = Button(win, text="Button4", font=("Arial",20))
b4.bind("<Button>", show4)
b4.pack()







win.mainloop()
