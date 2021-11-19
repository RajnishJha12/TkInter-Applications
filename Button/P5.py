from tkinter import *

#Program 5 : Fifth program will show how to display the message which is wriiten on an entry to the main window screen ITSELF.
#Note: command attribute is only used to handle just click event and not any other event. We even cant use to handle release event by uisng command.

win = Tk()
win.geometry("500x500")
win.resizable(0,0)

x=StringVar()
x.set("Input Your Name")
L1 = Label(win, textvariable=x, font=("Arial",10,"bold"))
L1.pack(side=LEFT, anchor=N)

x=StringVar()
E1 = Entry(win,textvariable=x)
E1.pack()

s=StringVar()
def show():
    s=x.get()
    #print(s)
    win.configure(textvariable=s)
    


def show2(b):
    s=x.get()
    #print(s)
    y.set(s)
    #print("Rajnish")

def show3(b):
    s=x.get()
    #print(s)
    y.set(s)
    x.set("")
    #print("Rajnish")

#Method 1: By using command attribute: Without parameters
B1 = Button(win,text="Button1",font=("Arial",10,"bold"), command=show )
B1.pack()

#Method 2: By using command & config attributes less used!: Without parameters
B2 = Button(win,text="Button2",font=("Arial",10,"bold") )
B2.config(command=show)
B2.pack()

#Method 3: By using command attribute: With LE
B3 = Button(win,text="Button3",font=("Arial",10,"bold"), command=lambda:show2(B3) )
B3.pack()

#Method 4: By using bind() method: Without LE
B4 = Button(win,text="Button4",font=("Arial",10,"bold"))
B4.bind("<Button>",show3)
B4.pack()

#Method 5: By using bind() method: With LE : Dont know how to write expression using LE here
B5 = Button(win,text="Button5",font=("Arial",10,"bold"))
#B5.bind("<Button>",lambda e: expressions)
B5.pack()



win.mainloop()
