from tkinter import *

win = Tk()
win.geometry("1200x800")
win.minsize(1200,800)
win.maxsize(1200,800)
win.title("My First Project")



# Frame:
F1 = Frame(win,bg="blue")   
#F1.grid(row=0,column=0)
#F1.pack(fill=X)
F1.place(x=0,y=0) 

# Heading

H1 = Label(F1, text="EDITION:", font="Arial 10", background="#363130", foreground="#f5f5f5")
H1.grid(row=0,column=0)

H2 = Label(F1, text="IND", font="proximanova 10 bold", background="#363130", foreground="#f5f5f5")
H2.grid(row=0,column=1, padx=25)

H3 = Label(F1, text="|", font="proximanova 10",foreground="#f5f5f5", bg="red")
H3.grid(row=0,column=2, padx=25)

H4 = Label(F1, text="MON, NOV 30, 2020 | UPDATED 06.31PM IST", font="proximanova 10 bold", background="#363130", foreground="#f5f5f5")
H4.grid(row=0,column=3, padx=25)

H5 = Label(F1, text="SIGN IN", font="proximanova 10 bold", background="#363130", foreground="#f5f5f5")
H5.grid(row=0,column=4, padx=500, pady=10)



# Frame:
F2 = Frame(win, bg="green")
#F2.grid(row=1,column=0)
#F2.pack(fill=X, padx=100)
F2.pack(fill=X)
F2.grid(columnspan=5)

label=Label(F2,text="Hello", font="Arial 20 bold", fg="white")
label.pack()


#H6 = Label(F2, text="THE TIMES OF INDIA", font="proximanova 10 bold", bg="black", fg="white")
#H6.grid(row=1,column=0)


H6 = Label(win, text="THE TIMES OF INDIA", font="proximanova 40 bold", foreground="white", bg="black")
H6.place(x=500, y=100,anchor = CENTER)
#H6.grid(row=1,column=0, padx=50, pady=50)


# Images:
"""
photo1 = PhotoImage(file="C:/Users/Admin/Desktop/NewsPaperPro/images/image4.png")

label = Label(image=photo1)
label.grid(column=0,row=2)


photo2 = PhotoImage(file="C:/Users/Admin/Desktop/NewsPaperPro/images/text1.png")

label2 = Label(image=photo2)
label2.grid(column=1,row=2)

"""



win.mainloop()
