from tkinter import *

# This program again shows how to handle click event on entry
win = Tk()
win.geometry("500x500")
win.resizable(0,0)

#How to Handle FocusIn and FocusOut events on Entry: Such that
#It will change the bg color of a window:
e1 = Entry(win, font=("Arial", 20))
e1.bind("<FocusIn>", lambda e: win.configure(bg="red"))
e1.bind("<FocusOut>", lambda e: win.configure(bg="blue"))

e2 = Entry(win, font=("Arial", 20))

e1.pack()
e2.pack()



win.mainloop()
