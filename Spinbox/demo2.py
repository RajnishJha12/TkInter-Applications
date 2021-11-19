from tkinter import *

t=Tk()
t.geometry("600x400")
t.resizable(0,0)
s=StringVar()


def show1():
    t.configure(background=s.get())

s1=Spinbox(values=["red","green","blue","yellow","pink","cyan"],font=("",15), textvariable=s,command=show1)
s1.pack()


t.mainloop()
