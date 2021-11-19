from tkinter import *

t=Tk()
t.geometry("600x400")
t.resizable(0,0)
s=StringVar()

s1=Spinbox(from_=1,to=15, font=("",15), textvariable=s)
s1.pack()

def show1():
    print(s.get())
    #if(s.get()=)
   

b1=Button(text="Click",font=("",15),command=show1)
b1.pack()


t.mainloop()
