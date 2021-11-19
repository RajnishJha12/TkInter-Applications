from tkinter import *

# This program shows how to handle click & release events on a single button
# using lambda expression
win = Tk()

win.geometry("500x500")
win.resizable(0,0)

button = Button(win, text="Click Me!!", font=("Arial",15))
#How to Handle click event on the main window: By using Button event like this:
#win.bind("<Button>", lambda e: win.configure(bg="red"))

#How to Handle click event on the button: By using Button event like this:
button.bind("<Button>", lambda e: win.configure(bg="red"))


#How to Handle click event release on the windows: By using ButtonRelease event like this:
button.bind("<ButtonRelease>", lambda e: win.configure(bg="blue"))
button.pack()


win.mainloop()
