from tkinter import *


# This program shows how to handle click & release events on the button by using normal methods
win = Tk()

win.geometry("500x500")
win.resizable(0,0)

button = Button(win, text="Click Me!!", font=("Arial",15))

# And if we want to change the bg color of a main window After handling the event:
#Then this is a way to configure it:
def show1(e):
    win.configure(bg="blue")


def show2(e):
    win.configure(bg="yellow")

#How to Handle click event on the button: By using Button event and by using bind()
button.bind("<Button>", show1)
button.bind("<ButtonRelease>", show2)
button.pack()

win.mainloop()
