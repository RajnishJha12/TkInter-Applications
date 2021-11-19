from tkinter import *

win = Tk()
win.geometry("500x500")
win.resizable(0,0)

x=IntVar()

def show():
   a= x.get()
   for i in range(1,11):
       print(a*i)
       #print(a)
    
e1 = Entry(win, font=("Arial", 20), textvariable=x)
e1.pack()


b1= Button(win, text="Click", font=("Arial", 20), command=show)
#b1= Button(win, text="Click", font=("Arial", 20), command=lambda:show())
b1.pack()

    

win.mainloop()
