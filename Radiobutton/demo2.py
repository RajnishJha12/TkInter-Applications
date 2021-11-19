from tkinter import *

t=Tk()
t.geometry("600x400")
t.resizable(0,0)
s1=IntVar()
s2=StringVar()
s3=StringVar()

def show1(m):
    s2.set(m)
    #print("click")
    

#we create the object r1 of Radiobutton class
r1=Radiobutton(text="Male", variable=s1, value=1, command=lambda:show1("Male"))
r1.pack()

def show2(f):
    s3.set(f)
r2=Radiobutton(text="FeMale", variable=s1, value=2, command=lambda:show2("FeMale"))
r2.pack()

e1=Entry(textvariable=s2)
e1.pack()

e2=Entry(textvariable=s3)
e2.pack()

t.mainloop()
