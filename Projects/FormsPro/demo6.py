#Now our next step is to insert data from our registration page
#and it will be stored in our regis table DB.
#So we need to fetch the data from the entry fields of the regis button and insurt in regis table db. To do that we need to take three variables:

#Now my next job is to when we click on the login button then it should either come with message like "Login succeful" or "Not successful" with error message:
#In order to do that at first we also need  create two variables and link it with these two entries to grab/fetch the data from these 2 entries and then we need to define a method
# called longin1 
from tkinter import *
from tkinter import messagebox
from tkinter import ttk
import sqlite3
t=Tk()
t.geometry("600x400")
t.resizable(0,0)
f55=None

def login():
    f2=Frame(bg="#091e42")
    f2.place(x=0,y=0,width=600,height=400)
    
    g1=StringVar()
    g2=StringVar()
    
    un=Label(f2,text="Enter Name",font=("",11),bg="#091e42", fg="white")
    un.place(x=200,y=50)
    e1=Entry(f2,font=("",11),textvariable=g1)
    e1.place(x=300,y=50,width=130)

    up=Label(f2,text="Enter Pass",font=("",11),bg="#091e42", fg="white")
    up.place(x=200,y=100)
    e2=Entry(f2,font=("",11),show="*",textvariable=g2)
    e2.place(x=300,y=100,width=130)

    def login1():
        db=sqlite3.connect("rajnish.db")
        cr=db.cursor()
        #r=cr.execute("SELECT * FROM regis WHERE UNAME='"+g1.get()+"'AND UPASS='"+g2.get()+"'  ")
        r=cr.execute("SELECT * FROM regis WHERE UNAME='"+g1.get()+"'AND UPASS='"+g2.get()+"'  ")
        #if un==g1.set("rajnish") and up==g2.set("123"):
            #messagebox.showinfo('Title', 'Your UN & Pwd are correct')
        #else:
            #messagebox.showinfo('Title', 'Your UN & Pwd are not correct')
        for r1 in r:
            #messagebox.showinfo("Title","Your UN and PWD are correct")
            #Now my next job is to display a new welcome page when I click on login button instead of showing correct UN & PWD in messagebox 

            #f4=Frame(bg="yellow")
            #f4.place(x=0,y=0,width=600,height=400)
            mymenu()
            break
        else:
            messagebox.showinfo("Title","Your UN and PWD are NOT correct")
        db.commit()
        db.close()
        g1.set("")
        g2.set("")


        
        
    b1=Button(f2,text="Login", command=login1)
    b1.place(x=260,y=160,width=100,height=40)

    b2=Button(f2,text="Home",command=home)
    b2.place(x=15,y=340,width=100,height=40)

    b3=Button(f2,text="Regis",command=regis)
    b3.place(x=480,y=340,width=100,height=40)

def mymenu():
    n=ttk.Notebook()
    n.place(x=0,y=0,width=600,height=400)
    insertdata(n)
    showalldata(n)
    searchdata(n)
    updatedata(n)
    deletedata(n)
    logoutdata(n)
     
#Now our next job is to create a view for the Insert tab. This is our Insert page view
def insertdata(n):
    f4=Frame(bg="yellow")
    n.add(f4,text="Insert")
    s1=StringVar()
    s2=StringVar()
    s3=StringVar()
    s4=StringVar()
    s5=StringVar()

    u1=Label(f4,text="Enter RNO.", bg="yellow", fg="black", font=("",11))
    u1.place(x=200,y=50)
    e1=Entry(f4,font=("",11),textvariable=s1)
    e1.place(x=300,y=50,width=130)

    u2=Label(f4,text="Enter Name", bg="yellow", fg="black", font=("",11))
    u2.place(x=200,y=100)
    e2=Entry(f4,font=("",11),textvariable=s2)
    e2.place(x=300,y=100,width=130)

    u3=Label(f4,text="Enter Phy", bg="yellow", fg="black", font=("",11))
    u3.place(x=200,y=150)
    e3=Entry(f4,font=("",11),textvariable=s3)
    e3.place(x=300,y=150,width=130)

    u4=Label(f4,text="Enter Che", bg="yellow", fg="black", font=("",11))
    u4.place(x=200,y=200)
    e4=Entry(f4,font=("",11),textvariable=s4)
    e4.place(x=300,y=200,width=130)

    u5=Label(f4,text="Enter Maths", bg="yellow", fg="black", font=("",11))
    u5.place(x=200,y=250)
    e5=Entry(f4,font=("",11),textvariable=s5)
    e5.place(x=300,y=250,width=130)

    def insertdemo1():
        db=sqlite3.connect("rajnish.db")
        cr=db.cursor()
        cr.execute("INSERT INTO ins values('"+s1.get()+"','"+s2.get()+"', '"+s3.get()+"','"+s4.get()+"','"+s5.get()+"' ) ")

        db.commit()
        db.close()
        messagebox.showinfo('Title', 'Insert Data')
        s1.set("")
        s2.set("")
        s3.set("")
        s4.set("")
        s5.set("")

        showalldata1(f55)

    b1=Button(f4,text="Insert",command=insertdemo1)
    b1.place(x=260,y=330,width=80,height=40)





def showalldata1(f5):
    u1=Label(f5,text="RNO.",font=("",11),bg="red",fg="white")
    u1.place(x=0,y=0,width=120)
    u2=Label(f5,text="Name",font=("",11),bg="red",fg="white")
    u2.place(x=120,y=0,width=120)
    u3=Label(f5,text="Phy",font=("",11),bg="red",fg="white")
    u3.place(x=240,y=0,width=120)
    u4=Label(f5,text="Che",font=("",11),bg="red",fg="white")
    u4.place(x=360,y=0,width=120)
    u5=Label(f5,text="Maths",font=("",11),bg="red",fg="white")
    u5.place(x=480,y=0,width=120)

    db=sqlite3.connect("rajnish.db")
    cr=db.cursor()
    r=cr.execute("SELECT * FROM ins ")
    x=0
    y=40
    for r1 in r:
        l=Label(f5,text=r1[0],font=("",11), bg="yellow", fg="red").place(x=x,y=y,width=120)
        x+=120
        l=Label(f5,text=r1[1],font=("",11), bg="yellow", fg="red").place(x=x,y=y,width=120)
        x+=120
        l=Label(f5,text=r1[2],font=("",11), bg="yellow", fg="red").place(x=x,y=y,width=120)
        x+=120
        l=Label(f5,text=r1[3],font=("",11), bg="yellow", fg="red").place(x=x,y=y,width=120)

        x+=120
        l=Label(f5,text=r1[4],font=("",11), bg="yellow", fg="red").place(x=x,y=y,width=120)

        #l.place(x=x,y=y,width=120)
        y+=40
        x=0
    db.commit()
    db.close()
    
    #print('Show all data')
    
def showalldata(n):
    f5=Frame(bg="blue")
    n.add(f5,text="ShowAll")
    global f55  # Since f55 is a global variable so it can be accessed anywhere throughut program.
    f55=f5
    #showalldata1()  We can also use by passing without parameter
    #showalldata1(n)  We can also use by passing with Notebook object as parameter
    showalldata1(f5)  # We can also use by passing with Frame object as parameter
    # NOTE: If we use ttk module then we cant use command attribute in order to call a method like this: n.add(f5,text="ShowAll",command=showalldatademo1)


   
    
def searchdata(n):
    f6=Frame(bg="pink")
    n.add(f6,text="Search")
    s1=StringVar()

    u1=Label(f6,text="Enter RNO.", font=("",11),bg="black", fg="white")
    u1.place(x=100,y=50)
    e1=Entry(f6,text="Enter RNO.", font=("",11),textvariable=s1)
    e1.place(x=200,y=50,width=130)
    
    def searchdata1():
        db=sqlite3.connect("rajnish.db")
        cr=db.cursor()
        r=cr.execute("SELECT * FROM ins WHERE URNO='"+s1.get()+"'  ")
        for r1 in r:
              u3=Label(f6,text="Name Is", font=("",11),bg="black", fg="white")
              u3.place(x=200,y=100)
              u4=Label(f6,text=r1[1], font=("",11),bg="black", fg="white")
              u4.place(x=300,y=100)

              u5=Label(f6,text="Phy Marks Is", font=("",11),bg="black", fg="white")
              u5.place(x=200,y=150)
              u6=Label(f6,text=r1[2], font=("",11),bg="black", fg="white")
              u6.place(x=300,y=150)

              u7=Label(f6,text="Che Marks Is", font=("",11),bg="black", fg="white")
              u7.place(x=200,y=200)
              u8=Label(f6,text=r1[3], font=("",11),bg="black", fg="white")
              u8.place(x=300,y=200)

              u9=Label(f6,text="Maths Marks Is", font=("",11),bg="black", fg="white")
              u9.place(x=200,y=250)
              u10=Label(f6,text=r1[4], font=("",11),bg="black", fg="white")
              u10.place(x=300,y=250)
              break

        db.commit()
        db.close()
        #messagebox.showinfo('Title', 'Insert Data')
        s1.set("")


        
        #print('I am searching...')

    b1=Button(f6,text="Search",font=("",11), command=searchdata1)
    b1.place(x=350,y=50,height=25)

   

    
def updatedata(n):
    f7=Frame(bg="red")
    n.add(f7,text="Update")

    
def deletedata(n):
    f8=Frame(bg="black")
    n.add(f8,text="Delete")

    
def logoutdata(n):
    f9=Frame(bg="green")
    n.add(f9,text="LogOut")
    
    
    
    

#This is our regis page
def regis():
    f3=Frame(bg="#091e42")
    f3.place(x=0,y=0,width=600,height=400)
    
    r1=StringVar()
    r2=StringVar()
    r3=StringVar()
    
    un=Label(f3,text="Enter Name",font=("",11),bg="#091e42", fg="white")
    un.place(x=200,y=50)
    e1=Entry(f3,font=("",11), textvariable=r1)
    e1.place(x=300,y=50,width=130)

    up=Label(f3,text="Enter Pass",font=("",11),bg="#091e42", fg="white")
    up.place(x=200,y=100)
    
    e2=Entry(f3,font=("",11),show="*", textvariable=r2)
    e2.place(x=300,y=100,width=130)

    
    uc=Label(f3,text="Enter C.N.",font=("",11),bg="#091e42", fg="white")
    uc.place(x=200,y=150)

    e3=Entry(f3,font=("",11), textvariable=r3)
    e3.place(x=300,y=150,width=130)

    def regis1():
        db=sqlite3.connect("rajnish.db")
        cr=db.cursor()
        cr.execute("INSERT INTO regis values('"+r1.get()+"', '"+r2.get()+"', '"+r3.get()+"')")
        db.commit()
        db.close()
        messagebox.showinfo('Title', 'User Registered')
        r1.set("")
        r2.set("")
        r3.set("")

        #print("data inserted...")
        #print("Registration data goes here!")
    
    b1=Button(f3,text="Regis",command=regis1)
    b1.place(x=260,y=210,width=100,height=40)

    b2=Button(f3,text="Home",command=home)
    b2.place(x=15,y=340,width=100,height=40)

    b3=Button(f3,text="Login",command=login)
    b3.place(x=480,y=340,width=100,height=40)

"""
def hello():
    print("Hello Hi Here!!")
"""

def home():
    f1=Frame(bg="#091e42")
    f1.place(x=0,y=0,width=600,height=400)
    b1=Button(f1,text="Login",command=login)
    b1.place(x=220,y=100,width=80,height=40)
    b2=Button(f1,text="Regis",command=regis)
    b2.place(x=310,y=100,width=80,height=40)

home()


t.mainloop()


#NOTE: We will use regis table for both login and registration data

