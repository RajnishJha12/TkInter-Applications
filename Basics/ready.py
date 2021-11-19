from tkinter import *

t=Tk()
t.geometry("600x400")
t.resizable(0,0)

l=Label(text="Ready!", bg="crimson", fg="white", font=("Arial",10),
        padx=10,pady=10)
#l.pack(side=LEFT,anchor=NW)
#l.pack(side=LEFT,anchor=SW)
#l.pack(side=RIGHT,anchor=NE)
#l.pack(side=RIGHT,anchor=SE)
l.pack(side="bottom",anchor="s",fill="x")
t.mainloop()
