from tkinter import *

win = Tk()
win.geometry("400x400")
win.resizable(0,0)
c=1
def show1(b):
    global c
    c=c+1
    if(c%2==0):
        if(b["text"]==""):
            b["text"]="0"
    else:
        if(b["text"]==""):
             b["text"]="X"
    if(b1["text"]=="0" and b2["text"]=="0" and b3["text"]=="0"):
        print("player 1 is a winner!!")
    elif(b1["text"]=="X" and b2["text"]=="X" and b3["text"]=="X" ):
         print("Player 2 is a winner!!")


b1= Button(win, text="", font=("Arial", 15),width=10, height=5,
           command=lambda:show1(b1))
#b1.bind("<Button>", show1)

b1.grid(row=0,column=0)

b2= Button(win, text="", font=("Arial", 15),width=10, height=5,
           command=lambda:show1(b2))
#b2.bind("<Button>", show1)

b2.grid(row=0,column=1)

b3= Button(win, text="", font=("Arial", 15),width=10, height=5,
           command=lambda:show1(b3))
b3.grid(row=0,column=2)

b4= Button(win, text="", font=("Arial", 15),width=10, height=5,
           command=lambda:show1(b4))
b4.grid(row=1,column=0)

b5= Button(win, text="", font=("Arial", 15),width=10, height=5,
           command=lambda:show1(b5))
b5.grid(row=1,column=1)

b6= Button(win, text="", font=("Arial", 15),width=10, height=5,
           command=lambda:show1(b6))
b6.grid(row=1,column=2)

b7= Button(win, text="", font=("Arial", 15),width=10, height=5,
           command=lambda:show1(b7))
b7.grid(row=2,column=0)

b8= Button(win, text="", font=("Arial", 15),width=10, height=5,
           command=lambda:show1(b8))
b8.grid(row=2,column=1)

b9= Button(win, text="", font=("Arial", 15),width=10, height=5,
           command=lambda:show1(b9))
b9.grid(row=2,column=2)
    

win.mainloop()
