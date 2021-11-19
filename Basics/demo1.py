#First Get or import the widgets from the tkinter
from tkinter import *

#Then second create the instance of the Tk() class
win = Tk()

#Then set the size of the main tkinter window or screen or editor
#by using these diffrent methods
win.geometry("400x400")
win.minsize(400,400)
win.maxsize(400,400)

#Then disable the maximise button by using this method
win.resizable(0,0)

#Then create a Label widget or class on the main tkinter window
label = Label(win, text="Hello World!", font=("Arial", 20, "bold"), bg="red",
              fg="blue", width=10, height=1, padx=10, pady=10, borderwidth=10,
              relief=SUNKEN)
#Now place the Lable widget on the main tkinter window using pack() method
label.pack(pady=10)






#Finally start the event loop
win.mainloop()
