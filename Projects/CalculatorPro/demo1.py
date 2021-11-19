from tkinter import *

win = Tk()
win.geometry("500x500")
win.resizable(0,0)

x=IntVar()
y=IntVar()
z=IntVar()

def show():
    s=x.get()
    s2=y.get()
    #a=x.get()
    #b=y.get()
    #c=a+b
    #z=set(c)
    z.set(s+s2)
    x.set("")
    y.set("")
    
def show2():
    s=x.get()
    s2=y.get()
    #a=x.get()
    #b=y.get()
    #c=a+b
    #z=set(c)
    z.set(s-s2)
    x.set("")
    y.set("")

def show3():
    s=x.get()
    s2=y.get()
    z.set(s*s2)
    x.set("")
    y.set("")
    
e1 = Entry(win, font=("Arial", 20), textvariable=x)
e1.pack()

e2 = Entry(win, font=("Arial", 20), textvariable=y)
e2.pack()

b1= Button(win, text="+", font=("Arial", 20), command=show)
b1.pack()

b2= Button(win, text="-", font=("Arial", 20), command=show2)
b2.pack()

b3= Button(win, text="*", font=("Arial", 20), command=show3)
b3.pack()

e3 = Entry(win, font=("Arial", 20), textvariable=z)
e3.pack()
    

win.mainloop()
