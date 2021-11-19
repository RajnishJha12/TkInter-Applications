from tkinter import *

win = Tk()
win.geometry("400x400")
win.resizable(0,0)
c=1
def show1(b):
    global c
    c=c+1
    if(c%2==0):
        b["text"]="0"
    else:
         b["text"]="X"


b1= Button(win, text="", font=("Arial", 25),width=10, height=5,
           command=lambda:show1(b1))
#b1.bind("<Button>", show1)

b1.grid(row=0,column=0)

b2= Button(win, text="", font=("Arial", 25),width=10, height=5,
           command=lambda:show1(b2))
#b2.bind("<Button>", show1)

b2.grid(row=0,column=1)
    

win.mainloop()
