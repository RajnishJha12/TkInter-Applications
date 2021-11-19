from tkinter import *

#This program shows how many differnt ways are available to handle click events in tkinter:

win = Tk()
win.geometry("500x500")
win.resizable(0,0)

#1. First program will show how to change the window BG color by diffretn ways
#2. Second program will show how to change the button text once we click on it
#3. Third program will show how to display the message which is wriiten on entry to the console when we click on the button
#4  Fourth program will show how to display the message which is wriiten on one entry to the another entry when we click on the button]
#5. Fifth program will show how to display the message which is wriiten on an entry to the main window screen ITSELF.

def show(b):
    win.configure(bg="red")
   
#Method 1: By using command attribute which is frequently used: without passing any parameters :
#command attribute does not take event parameters if we need to use then better to use use lambda expression with it


b1 = Button(win, text="Click Me!!", font=("Arial", 20), command=show)
b1.pack()

#Method 2: By using command attribute and config this is rarely used and I'm not a big fan of this approach. As its just similar to first one

b1 = Button(win, text="Click Me!!", font=("Arial", 20))
b1.config(command=show)
b1.pack()

#Method 3: By using command attribute with lambda expression:
#We use it when we need to handle the event for this we need to pass the parameter of that class object reference for which we are handling the event in
# this case we are passing this Button class object reference b2 to the corresponding method call and inside the method definition
#we can pass any name parameter like b or e or soemthing else

b2 = Button(win, text="Click Me!!", font=("Arial", 20), command=lambda: show(b2))
#b2.config(command=show)
b2.pack()

#Method 4: By using bind() method one of my favourite and also frequently used: It always work with parameter
#but at the time of calling we should't pass any parameter like this.
b3 = Button(win, text="Button3", font=("Arial",20))
b3.bind("<Button>", show)
b3.pack()

#Method 5: By using lamda expression: It is similar to Method 4 only. Here we will only change the enire function and rewrire in LE
b4 = Button(win, text="Button4", font=("Arial",20))
b4.bind("<Button>", lambda e: win.configure(bg="blue"))
b4.pack()

win.mainloop()
