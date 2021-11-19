from tkinter import *

"""
Button is a widget which is interacted by a user so when user inreract with a button
then based on interaction by the user on the button event occurs i.e. we decide
the events and handle it.
"""

t = Tk()

t.geometry("500x500")
t.resizable(0,0)

#This proram shows different types of events occuring on a tkinter main tdow
# By using bind() method and lambda expression
t.bind("<Enter>", lambda e: t.configure(background="cyan"))
t.bind("<Leave>", lambda e: t.configure(background="seagreen"))

"""
def show(e):
    t.configure(bg="pink")
    
def show2(e):
    t.configure(bg="red")

def show3(e):
    t.configure(bg="yellow")


def show4(e):
    t.configure(bg="black")

def show5(e):
    t.configure(bg="green")
"""


#This program show diffrent types of events ocuuring on a single button 
show = lambda e: t.configure(bg="pink")

show2 = lambda e: t.configure(bg="red")

show3 = lambda e: t.configure(bg="yellow")

show4 = lambda e: t.configure(bg="black")

show5 = lambda e: t.configure(bg="green")

#show6 = lambda e: t.configure(bg="blue")

#Click Event:
button = Button(t, text="Click!!!", font=("Arial",20))
button.pack()
button.bind("<Button-1>", show) #L
button.bind("<Button-2>", show2) #Scroll
button.bind("<Button-3>", show3) #R

#Double Event:
button.bind("<Double-1>", show4) #L
button.bind("<Double-2>", show4) #Scroll
button.bind("<Double-3>", show4) #R

#Enter Event: When Enter event takes place: Means when hover over the mouse on the Button
button.bind("<Enter>", show5)

#Leave Event: When Leave event takes place: Means when move out of the mouse on the Button
button.bind("<Leave>", lambda e: t.configure(bg="blue"))


button.bind("<ButtonRelease>", lambda e: button.configure(bg="white"))

#Key Events on main tdow:
t.bind("<Key-a>", lambda e: t.configure(background="orange"))
t.bind("<Key-b>", lambda e: t.configure(background="slateblue"))
t.bind("<Key-c>", lambda e: t.configure(background="lightblue"))

# We can also use Key events without Key keyword like this:
t.bind("<d>", lambda e: t.configure(background="dodgerblue"))

# Functions like F1, F2 Events:
t.bind("<F1>", lambda e: t.configure(background="orange"))
t.bind("<F2>", lambda e: t.configure(background="slateblue"))
t.bind("<F3>", lambda e: t.configure(background="lightblue"))
t.bind("<Delete>", lambda e: t.configure(background="dodgerblue"))

#To Handle Number Events like 1 to 9 use it without <> angular bracket: like this:
t.bind("1", lambda e: t.configure(background="red"))
t.bind("2", lambda e: t.configure(background="blue"))
t.bind("3", lambda e: t.configure(background="green"))

#To Handle Shift+arrow keys events on main tdows:
t.bind("<Shift-Up>", lambda e: t.configure(bg="red"))
t.bind("<Shift-Down>", lambda e: t.configure(bg="blue"))
t.bind("<Shift-Left>", lambda e: t.configure(bg="green"))
t.bind("<Shift-Right>", lambda e: t.configure(bg="orange"))

#To Handle Alt+arrow keys events on main tdows:
t.bind("<Alt-Up>", lambda e: t.configure(bg="red"))
t.bind("<Alt-Down>", lambda e: t.configure(bg="blue"))
t.bind("<Alt-Left>", lambda e: t.configure(bg="green"))
t.bind("<Alt-Right>", lambda e: t.configure(bg="orange"))


#To Handle Ctrl+arrow keys events on main tdows:
t.bind("<Control-Up>", lambda e: t.configure(bg="red"))
t.bind("<Control-Down>", lambda e: t.configure(bg="blue"))
t.bind("<Control-Left>", lambda e: t.configure(bg="green"))
t.bind("<Control-Right>", lambda e: t.configure(bg="orange"))


t.mainloop()
