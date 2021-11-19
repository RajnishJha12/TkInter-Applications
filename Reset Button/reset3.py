from tkinter import *

win = Tk()
win.geometry("500x500")
win.resizable(0,0)

def show1(e):
    b1["bg"]="black"
    b1["fg"]="white"
    b1["width"]=10
    b1["height"]=5
    b1["text"]="reset"


b1= Button(win, text="Click", font=("Arial", 20))
b1.bind("<Button>", show1)

b1.pack()

    

win.mainloop()
