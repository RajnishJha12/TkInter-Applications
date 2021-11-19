from tkinter import *

win = Tk()
win.title("Login Page - GUI")
win.configure(bg="darkblue")

# First set the size of a window screen to 900x700 using geometry():
#win.geometry("900x700")
win.geometry("500x500")

# Then Second set the size of the window screen not resizable also using resizable():
win.resizable(0,0)

#userName = Label(win, text='User Name:', font=('Arial',15,'bold'))

#userName = Label(win, text='Enter Name', font=('Arial',20), pady=25)
userName = Label(win, text='Enter Name', font=('Arial',20), bg="white")
userName.grid(row=0,column=0,pady=25, sticky=W)

entry1 = Entry(win,font=('Arial',20))
entry1.grid(row=0,column=1,pady=25)


password = Label(win, text='Enter Password', font=('Arial',20), bg="white")
password.grid(row=1,column=0, pady=25)

entry2 = Entry(win,font=('Arial',20), show="*")
entry2.grid(row=1,column=1,pady=25)

button = Button(win, text="Login", font=('Arial',20) )
#columnspan attribute takes entire column based on no. of columns and place the widgets in middle.
#Likewise rowspan attribute is used to span the text across the given rows.
button.grid(row=2, column=0, columnspan="2")









win.mainloop()




