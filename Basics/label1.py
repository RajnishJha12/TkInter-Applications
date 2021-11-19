from tkinter import *

root = Tk()
root.title("Label Example")
root.geometry("300x300")
root.minsize(300,300)
root.maxsize(300,300)

root.resizable(0,0)



l1 = Label(root, text="Red",bg="red", fg="white")
l1.pack(side=LEFT,anchor=NW, padx=5)

l2 = Label(root, text="Blue",bg="blue", fg="white")
l2.pack(side=LEFT,anchor=NW, padx=5)


l3 = Label(root, text="Green",bg="green", fg="white")
l3.pack(side=LEFT, anchor=NW, padx=5)



#If we change LEFT to RIGHT in the previous example,
#we get the colours in reverse order:

L1 = Label(root, text="Red",bg="red", fg="white")
L1.pack(side=RIGHT,anchor=NW, padx=5)

L2 = Label(root, text="Blue",bg="blue", fg="white")
L2.pack(side=RIGHT,anchor=NW, padx=5)


L3 = Label(root, text="Green",bg="green", fg="white")
L3.pack(side=RIGHT, anchor=NW, padx=5)

root.mainloop()
