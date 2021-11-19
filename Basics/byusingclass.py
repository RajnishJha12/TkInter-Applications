from tkinter import *

class myApp:
    def __init__(self,t):
        self.t=t
        self.t.geometry("900x700+0+0")
        self.t.title("My Title")



t=Tk()
obj=myApp(t)
t.mainloop()
