from tkinter import *
t = Tk()
t.geometry("1200x1000")
t.resizable(0,0)


#Home Page:
f1=Frame(t,bg="blue")
f1.place(x=0,y=0,width=1200,height=40) #Utill widgets will be not places on the frame, widgets wont displayed on the frame.

#Now to display the widgets on the created frame f1 we have to place on it.


b1=Button(f1,text="EDITIONS", fg="white", bg="black", activebackground="seagreen",
          activeforeground="yellow")
b1.place(x=20,y=5,width=80,height=30)

b2=Button(f1,text="IND",fg="white", bg="black", activebackground="seagreen",
          activeforeground="yellow")
b2.place(x=120,y=5, width=80,height=30)

b3=Label(f1,text="|", bg="blue", fg="white", width=100,height=100)
b3.place(x=240,y=5)

b4=Label(f1,text="MON,NOV 30,2020|UPDATED 06:31PM IST",bg="blue", fg="white")
b4.place(x=280,y=5, width=300,height=30)

b5=Button(text="SIGN IN",fg="white", bg="black", activebackground="seagreen",
          activeforeground="yellow")
b5.place(x=1000,y=5, width=80,height=30)

label=Label(text="THE TIMES OF INDIA", font=("Algerian",50),fg="black")
label.place(x=330,y=100)

#Pictures and News


photo1 = PhotoImage(file="C:/Users/Admin/Desktop/TkInter Projects/NewsPaperPro/images/image1.png")

label = Label(image=photo1)
label.place(x=200,y=200)


photo2 = PhotoImage(file="C:/Users/Admin/Desktop/TkInter Projects/NewsPaperPro/images/image2.png")

label2 = Label(image=photo2)
label2.place(x=180,y=400, width=400)

photo3 = PhotoImage(file="C:/Users/Admin/Desktop/TkInter Projects/NewsPaperPro/images/image1.png")

label3 = Label(image=photo3)
label3.place(x=200,y=600)




#colors = ["red","blue","green","yellow","black"]

"""
x=1
for c in colors:
    x=x+900
    L1 = Label(t, text=c, relief=RIDGE, width=5)
    L1.grid(row=x,column=800)
    E1 = Entry(t,bg=c, relief=SUNKEN, width=10)
    E1.grid(row=x,column=800)

"""    
t.mainloop()
