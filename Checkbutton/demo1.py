from tkinter import *

t=Tk()
t.geometry("600x400")
t.resizable(0,0)

a=IntVar()
b=IntVar()
s=StringVar()


#Now we will create object of Checkbutton() class: Checkbutton ka c1 object bana diya: RB class ka object banakar taiyaar kar liya
c1=Checkbutton(text="PYTHON",variable=a,  font=("",15))
c1.pack()

c2=Checkbutton(text="JAVA",variable=b, font=("",15))
c2.pack()

#Now my next job is to when I click on any above checkbox button then that button
#text should be sisplayed in the console also

def show1():
    s1=""
    if(a.get()==1):
        s1+="PYTHON"
        #print(s.set(s1))
    if(b.get()==1):
        s1+="JAVA"
        #print(s.set(s1))
    s.set(s1)

        

b1=Button(text="Click", font=("",15),command=show1)
b1.pack()

e1=Entry(textvariable=s)
e1.pack()


t.mainloop()
