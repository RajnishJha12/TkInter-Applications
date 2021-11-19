from tkinter import *

win = Tk()
win.geometry("500x500")
win.resizable(0,0)

def show(b):
    b1["text"]="reset"
    


b1= Button(win, text="Click", font=("Arial", 20), command=lambda:show(b1))
#b1= Button(win, text="Click", font=("Arial", 20), command=lambda:show())
b1.pack()

    

win.mainloop()
