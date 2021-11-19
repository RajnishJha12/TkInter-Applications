from tkinter import *

win = Tk()
win.geometry("500x500")
win.resizable(0,0)

x=StringVar()
y=StringVar()
e1 = Entry(win, font=("Arial", 20), textvariable=x)
e1.pack()

def show():
    #print("Rajnish")
    s=x.get()
    y.set(s)
    x.set("")
    
    #print(s)  

b1= Button(win, text="Click", font=("Arial", 20), command=show)
b1.pack()

e2 = Entry(win, font=("Arial", 20),textvariable=y)
e2.pack()
    

win.mainloop()
