from tkinter import *

win = Tk()
win.geometry("500x500")
win.resizable(0,0)

x=IntVar()
y=IntVar()
z=IntVar()


def show(op):
    a=x.get()
    b=y.get()
    if(op==1):
        c=a+b
        z.set(c)
        x.set("")
        y.set("")
    if(op==2):
        c=a-b
        z.set(c)
        x.set("")
        y.set("")
    if(op==3):
        c=a*b
        z.set(c)
        x.set("")
        y.set("")

    
e1 = Entry(win, font=("Arial", 20), textvariable=x)
e1.pack()

e2 = Entry(win, font=("Arial", 20), textvariable=y)
e2.pack()

b1= Button(win, text="+", font=("Arial", 20), command=lambda:show(1))
b1.pack()

b2= Button(win, text="-", font=("Arial", 20), command=lambda:show(2))
b2.pack()

b3= Button(win, text="*", font=("Arial", 20), command=lambda:show(3))
b3.pack()

e3 = Entry(win, font=("Arial", 20), textvariable=z)
e3.pack()
    

win.mainloop()
