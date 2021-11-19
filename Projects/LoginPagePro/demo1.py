from tkinter import *
t=Tk() # Now we have created a t object of Tk() class
t.geometry("425x280")

def login():
    f2 = Frame()
    f2.place(x=0,y=0,width=425,height=280)
    e1=Entry(f2)
    e1.pack()
    e2=Entry(f2)
    e2.pack()
    b2=Button(f2,text="back")
    b2.pack()

#Now we will have to create Frame() class object    
f1 = Frame()
f1.place(x=0,y=0,width=425,height=280)
#Now whenver we click on Click!! button then this login() method
#will be call and the content will be displayed on the page.

#Now put or add a button inside/on a Frame like this:
b1=Button(f1,text="Click!!",command=login)
b1.pack()




t.mainloop()

