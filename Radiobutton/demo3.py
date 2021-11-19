from tkinter import *

t=Tk()
t.geometry("600x400")
t.resizable(0,0)

a=IntVar()
s=StringVar()
def show1():
    if (a.get()==1):
        s.set("Male")
    if(a.get()==2):
        s.set("FeMale")

    

#Now we create an object of Radiobutton class
r1=Radiobutton(text="Male", variable=a, value=1, command=show1)
r1.pack()

r2=Radiobutton(text="FeMale", variable=a, value=2, command=show1)
r2.pack()

e=Entry(textvariable=s)
e.pack()

t.mainloop()
