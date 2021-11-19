from tkinter import *

win = Tk()
win.geometry("500x500")
win.resizable(0,0)

#How to Handle FocusIn and FocusOut events on Entry: Such that
#It will change the bg color of a window:

x=StringVar()
e1 = Entry(win, font=("Arial", 20), textvariable=x)
e1.pack()

def show():
    #print("SoftWaves")
    #s=e1.get()
    s=x.get()
    print(s)
    x.set("")
    

b1= Button(win, text="Click", font=("Arial", 20), command=show)
b1.pack()



win.mainloop()
