from tkinter import *

root = Tk()
root.geometry("300x300")
root.minsize(300,300)
root.maxsize(300,300)

root.resizable(0,0)

root.title("Example GUI")

L1 = Label(root, text="red")
L1.grid(row=0,column=0, padx=20)
E1= Entry(root, bg="red")
E1.grid(row=0,column=1)

L2 = Label(root, text="blue")
L2.grid(row=1,column=0)
E2= Entry(root, bg="blue")
E2.grid(row=1,column=1)


L3 = Label(root, text="green")
L3.grid(row=2,column=0)
E3= Entry(root, bg="green")
E3.grid(row=2,column=1)


L4 = Label(root, text="yellow")
L4.grid(row=3,column=0)
E4= Entry(root, bg="yellow")
E4.grid(row=3,column=1)


L5 = Label(root, text="black")
L5.grid(row=4,column=0)
E5= Entry(root, bg="black")
E5.grid(row=4,column=1)


root.mainloop()
