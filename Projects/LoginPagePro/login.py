from tkinter import *
t=Tk() # Now we have created a t object of Tk() class
t.geometry("425x280")

def login():
    f2=Frame()
    f2.place(x=0,y=0,width=425,height=280)
    e1=Entry(f2)
    e1.pack()
    e2=Entry(f2)
    e2.pack()
    b3=Button(f2,text="back", command=back)
    b3.pack()

def regis():
    f3=Frame()
    f3.place(x=0,y=0,width=425,height=280)
    e1=Entry(f3)
    e1.pack()
    e2=Entry(f3)
    e2.pack()
    e3=Entry(f3)
    e3.pack()
    b3=Button(f3,text="back", command=back)
    b3.pack()

def back():
    f1=Frame()
    f1.place(x=0,y=0,width=425,height=280)
    b1=Button(f1,text="Login", command=login)
    b1.pack()
    b2=Button(f1,text="Regis",command=regis)
    b2.pack()

back()




t.mainloop()
