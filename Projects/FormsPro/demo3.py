#Now we will start creating view of our project: SO first we will create Home page:
from tkinter import *
t=Tk()
t.geometry("485x280")
t.resizable(0,0)
t.configure(bg="black")

f1=Frame(bg="blue")
f1.place(x=0,y=20,width=485,height=200)
b1=Button(f1,text="Login",bg="blue",fg="white",activebackground="red",
          activeforeground="yellow")
b1.place(x=160,y=50,width=80,height=40)
b2=Button(f1,text="Regis.",bg="blue",fg="white",activebackground="red",
          activeforeground="yellow")
b2.place(x=260,y=50,width=80,height=40)

t.mainloop()

