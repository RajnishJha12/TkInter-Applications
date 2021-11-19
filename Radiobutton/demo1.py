from tkinter import *

t=Tk()
t.geometry("600x400")
t.resizable(0,0)
s1=IntVar()

#we create the object r1 of Radiobutton class
r1=Radiobutton(text="Male", variable=s1, value=1)
r1.pack()

r2=Radiobutton(text="FeMale", variable=s1, value=2)
r2.pack()

t.mainloop()
