from tkinter import Tk #First we will impot Tk() class from Tool Kit Interface
from tkinter import Entry
from tkinter import Button
from tkinter import StringVar
t=Tk() #Then we will create object of Tk() class
t.title("Rajnish")
t.geometry("425x280")
t.resizable(0,0)
t.configure(background="black")

a=StringVar()
e1=Entry(font=("",30),justify="right",textvariable=a)
e1.place(x=0,y=0, width=425, height=50)

def show(b):
    a.set(a.get()+b)


def equ():
    exp=a.get()
    a.set(eval(exp))
    
def clr():
    a.set("")

#create an array of 16 Buttons
b=[Button()]*16
data=["7","8","9","+","4","5","6","-","1","2","3","*","C","0","=","/",]
x=5
y=55
k=0

for i in range(4):
    for j in range(4):
        b[k]=Button(text=data[k], font=("",25),bg="gray",fg="white",activebackground="dodgerblue",activeforeground="red")
        b[k].place(x=x,y=y, width=100, height=50)
        k=k+1
        x=x+105
    x=5
    y=y+55
#Now add events on every butons
b[0].configure(command=lambda:show(data[0]))
b[1].configure(command=lambda:show(data[1]))
b[2].configure(command=lambda:show(data[2]))
b[3].configure(command=lambda:show(data[3]))
b[4].configure(command=lambda:show(data[4]))
b[5].configure(command=lambda:show(data[5]))
b[6].configure(command=lambda:show(data[6]))
b[7].configure(command=lambda:show(data[7]))
b[8].configure(command=lambda:show(data[8]))
b[9].configure(command=lambda:show(data[9]))
b[10].configure(command=lambda:show(data[10]))
b[11].configure(command=lambda:show(data[11]))
b[12].configure(command=clr)
b[13].configure(command=lambda:show(data[13]))
b[14].configure(command=equ)
b[15].configure(command=lambda:show(data[15]))




t.mainloop() # Then we will create eventloop
