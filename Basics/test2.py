from tkinter import *

win = Tk()
win.title("Rajnish-GUI")
win.geometry("500x400")
win.resizable(0,0)

lablel1 = Label(win,text="Jupiter", font="Arial 19" , bg="red", fg="yellow")
lablel1.pack(pady=10, anchor=E, padx=50)

label = Label(win, text="I'm Ready!", font=('Arial',10), background="red",
              foreground="white", padx=20, pady=10, width=10, height=1)
#colspan attribute span all the text across all the given columns.
label.pack(side=BOTTOM, anchor=W)


win.mainloop()
