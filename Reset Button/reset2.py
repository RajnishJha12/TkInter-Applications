from tkinter import *

win = Tk()
win.geometry("500x500")
win.resizable(0,0)

def show1(e):
    b1["text"]="reset"


b1= Button(win, text="Click", font=("Arial", 20))
b1.bind("<Button>", show1)

b1.pack()

    

win.mainloop()
