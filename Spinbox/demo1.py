from tkinter import *

t=Tk()
t.geometry("600x400")
t.resizable(0,0)
s=StringVar()

s1=Spinbox(values=["red","green","blue","yellow","pink","cyan"],font=("",15), textvariable=s)
s1.pack()

def show1():
    #if(s.get()=)
    t.configure(bg=s.get())

b1=Button(text="Click",font=("",15),command=show1)
b1.pack()


t.mainloop()
