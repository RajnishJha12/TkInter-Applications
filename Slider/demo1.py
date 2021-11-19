from tkinter import *
from tkinter import ttk

t=Tk()
t.geometry("600x400")
t.resizable(0,0)
t.title('Sacale, Tabs, Table Example')

def getValue(value):
    print(value)


def getValue2(value):
    print(scale2.get())
    
#This is a way to create a slider in Tkinter
scale1=Scale(t,from_=1,to=100,label="Simple Slide",
            fg="white", bg="green", activebackground="red", troughcolor="orange", command=getValue)

scale1.pack(fill=X)
#Now creating a Horizontal Slider

scale2=Scale(t,from_=1,to=100,label="Simple Slide",
            fg="white", bg="green", activebackground="red",
             troughcolor="orange", orient="horizontal", command=getValue2)

scale2.pack(fill=X) #scale2.pack(fill="x")

#Now creating fames for showing tabs
f1=Frame(t)
f1.pack(fill="both")
n=ttk.Notebook(f1)
n.add(f1,text="tab 1")




t.mainloop()
