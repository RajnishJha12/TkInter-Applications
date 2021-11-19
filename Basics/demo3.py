from tkinter import *

root = Tk()
root.geometry("600x600")
root.minsize(600,600)
root.maxsize(600,600)
root.resizable(0,0)

var=StringVar()
L1 = Label(root, textvariable=var, font="Arial 30 bold", bg="red", fg="white",
           width=10, height=1, borderwidth=10, relief=RAISED, padx=10, pady=10)
var.set("I am Label")


#To move the widget to the left side uing pack:
#L1.pack( anchor=NW)

#To move the widget to the right side uing pack:
#L1.pack( anchor=NE)


#To move the widget to the botthom of the window to the left side uing pack:
#L1.pack( side=BOTTOM, anchor=W)


#To move the widget to the botthom of the window to the right side uing pack:
L1.pack( side=BOTTOM, anchor=E)

root.mainloop()
