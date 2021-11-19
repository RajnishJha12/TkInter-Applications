#Now we will start creating anothe view of our project called regis page:
from tkinter import *
t=Tk()
t.geometry("485x400")  #Try 485x400 Earlier it was: "485x280"
t.resizable(0,0)
t.configure(bg="black")

#f1=Frame(bg="blue")
#f1.place(x=0,y=20,width=485,height=200)
#b1=Button(f1,text="Login",bg="blue",fg="white",activebackground="red",
          #activeforeground="yellow")
#b1.place(x=160,y=50,width=80,height=40)


def login():
   # label=Label(text="I am login page!!") #This code by defualt will appear on the main window screen itself.
   # label.pack()
   #Whenever we create a frame for each new view component then set the size of a fame like as your main window size to hide the content and use place()
   #instead on pack() otherwise if we use pack() then content will apear on the main screen only insetead of a frame.
   f3=Frame(bg="blue") # f3=Frame()
   f3.place(x=0,y=20, width=485,height=280) # x=0 n y=0 fro no margin through x n y axis   place(x=0,y=0, width=485,height=400)

   # Label(text="I am login page!!",font=("Arail",20))
   label=Label(text="I am Login page!!",font=("Arial"),bg="blue",fg="white",activebackground="red",
              activeforeground="yellow")  
   #label.pack()
   label.place(x=210,y=30)

   un=Label(text="Enter Name",bg="blue",fg="white")
   un.place(x=150,y=70)
   e1=Entry()
   e1.place(x=240,y=70)

   up=Label(text="Enter Pass",bg="blue",fg="white")
   up.place(x=150,y=100)
   e2=Entry(show="*")
   e2.place(x=240,y=100)


   b1=Button(text="Login", bg="blue",fg="white",activebackground="red",
              activeforeground="yellow")
   b1.place(x=220,y=150,width=80,height=40)

   b2=Button(text="Home", command=home , bg="blue",fg="white",activebackground="red",
              activeforeground="yellow")
   b2.place(x=10,y=250,width=80,height=40)  # b2.place(x=10,y=350,width=80,height=40)

   b3=Button(text="Regis",command=show ,bg="blue",fg="white",activebackground="red",
              activeforeground="yellow")
   b3.place(x=390,y=250,width=80,height=40)
   
   

def show():
    f2=Frame(bg="blue")
    f2.place(x=0,y=20,width=485,height=280)#x=0,y=0 means no margin from both x n y axis across win border: Try height=380 : Earlier it was: height=200
    l=Label(f2,text="I am registration page!!",font=("Arial"),bg="blue",fg="white",activebackground="red",
              activeforeground="yellow")
    #l.pack()
    l.place(x=180,y=5)
    l1=Label(f2,text="Enter Name",bg="blue",fg="white")
    l1.place(x=130,y=60)
    e1=Entry(f2)
    e1.place(x=210,y=60)
    
    l2=Label(f2,text="Enter Pass",bg="blue",fg="white")
    l2.place(x=130,y=120)
    e2=Entry(f2,show="*")
    e2.place(x=210,y=120)

    l3=Label(f2,text="Enter C.Pass",bg="blue",fg="white")
    l3.place(x=130,y=180)
    e3=Entry(f2)
    e3.place(x=210,y=180)

    b3=Button(f2,text="Registration",bg="blue",fg="white",activebackground="red",
              activeforeground="yellow")
    b3.place(x=200, y=220,width=80,height=40)

    #b4=Button(f2,text="Back",command=home,bg="blue",fg="white",activebackground="red",
             # activeforeground="yellow")
    #b4.place(x=0,y=0)

    b4=Button(f2,text="Home",command=home,bg="blue", fg="white",activebackground="red",
              activeforeground="yellow")
    b4.place(x=10,y=230, width=80,height=40)

    
    b5=Button(f2,text="Login",command=login,bg="blue", fg="white",activebackground="red",
              activeforeground="yellow")
    b5.place(x=400,y=230, width=80,height=40)


#f2=Frame()
#f2.place(x=0,y=0,width=485,height=280)#x=0,y=0 means no margin from both x n y axis across win border

#b2=Button(f1,text="Regis.",bg="blue",fg="white",activebackground="red",
          #activeforeground="yellow", command=show)
#b2.place(x=260,y=50,width=80,height=40)






def home():
    f1=Frame(bg="blue")
    f1.place(x=0,y=20,width=485,height=280) # Earlier it was like: width=485,height=200
    b1=Button(f1,text="Login", command=login, bg="blue",fg="white",activebackground="red",
              activeforeground="yellow")
    b1.place(x=160,y=50,width=80,height=40)

    b2=Button(f1,text="Regis.",bg="blue",fg="white",activebackground="red",
              activeforeground="yellow", command=show)
    b2.place(x=260,y=50,width=80,height=40)

#Since the above code inside one method called home() so who will call it? So for that we have to cwrire like this below to call it automatically:
home()

t.mainloop()

