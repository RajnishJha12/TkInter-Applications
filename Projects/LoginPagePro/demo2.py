from tkinter import *
t=Tk() # Now we have created a t object of Tk() class
t.geometry("425x350")

def login():
    f2 = Frame(bg="#091e42")
    f2.place(x=0,y=0,width=425,height=350)
    u=Label(f2,text="Login Page",font="Arial 20", bg="#091e42", fg="white")
    #u.place(x=160,y=20)
    u.place(x=150,y=10)
    
    u1=Label(f2,text="Enter Name", bg="#091e42", fg="white" )
    u1.place(x=100,y=80)
    e1=Entry(f2, font="'',12")
    e1.place(x=200,y=80,width=120)

    u2=Label(f2,text="Enter Pass",  bg="#091e42", fg="white")
    u2.place(x=100,y=130)
    e2=Entry(f2, font="'',12",show="*")
    e2.place(x=200,y=130,width=120)

    b3=Button(f2,text="Login")
    b3.place(x=150,y=200,width=80,height=40)

    b2=Button(f2,text="<-",command=home)
    b2.place(x=2,y=3)

def regis():
    f3 = Frame(bg="#0e2140")
    f3.place(x=0,y=0,width=425,height=350)

    u=Label(f3,text="Registration Page",font="Arial 20",  bg="#091e42", fg="white")
    u.place(x=150,y=10)

    u1=Label(f3,text="Enter Name",  bg="#091e42", fg="white")
    u1.place(x=100,y=80)
    e1=Entry(f3, font=("Arial",10))
    e1.place(x=200,y=80)

    u2=Label(f3,text="Enter Pass",  bg="#091e42", fg="white")
    u2.place(x=100,y=130)
    e2=Entry(f3, font=("Arial",10),show="*")
    e2.place(x=200,y=130)

    u3=Label(f3,text="Enter C.Pass",  bg="#091e42", fg="white")
    u3.place(x=100,y=180)
    e3=Entry(f3, font=("Arial",10),show="*")
    e3.place(x=200,y=180)
    
 
    b2=Button(f3,text="back", command=home)
    b2.place(x=0,y=0)
    b3=Button(f3  ,text="Registration", font=("Arial",10))
    b3.place(x=180,y=230,width=80,height=40)

def home(bg="#0e2140"):
    #Now we will have to create Frame() class object    
    f1 = Frame( bg="#091e42")
    f1.place(x=0,y=0,width=425,height=350)
    #Now whenver we click on Click!! button then this login() method
    #will be call and the content will be displayed on the page.

    #Now put or add a button inside/on a Frame like this:
    b1=Button(f1,text="Login",command=login)
    b1.place(x=100,y=50,width=80,height=40)
    b2=Button(f1,text="Regis",command=regis)
    b2.place(x=200,y=50,width=80,height=40)
home()




t.mainloop()

