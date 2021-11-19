from tkinter import *
t=Tk() # Now we have created a t object of Tk() class
t.geometry("425x280")

def show():
    f2=Frame()
    f2.place(x=0,y=0,width=425,height=280)
    e1=Entry(f2)
    e1.pack()
    e2=Entry(f2)
    e2.pack()
   
    b2=Button(f2,text="back",command=home)
    b2.pack()

def home():
    #show()
    #I have created a frame of same size of a main windows  to move from one window to another window    
    f1=Frame()
    f1.place(x=0,y=0,width=425,height=280)
    #Now add a button on a f1 frame. NOw same process we will repeat for anottger button and entry.
    b1=Button(f1,text="Clickme!!",command=show)
    b1.pack()

#Once program will be executed then by defulat home() method will be called because of below code:    
home()





t.mainloop()

