from tkinter import *

#This program shows how to handle click & release events on a single button
#by uisng single method only.

win = Tk()
win.geometry("500x500")
win.resizable(0,0)

button = Button(win, text="Click Me!!", font=("Arial", 20))

x=1
def show(e):
    global x
    x=x+1
    if(x%2==0):
        win.configure(background="red")
    else:
         win.configure(background="blue") 
    
#How to Handle click & release events on Button to change the bg color of a Window:

"""
button.bind("<Button>", show)
button.bind("<ButtonRelease>", show)
"""
button.bind("<Motion>", show)
button.pack()


win.mainloop()
