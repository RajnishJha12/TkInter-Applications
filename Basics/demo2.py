#Get or import the widgets from the tkinter
from tkinter import *

# with the help of this basic window is creating: Now create an instance of a Tk() class
win = Tk()

#Then set the size of the tkinter main window or ecreen or editor using these methods
win.geometry("300x300")
win.minsize(300,300)
win.maxsize(900,900)
# With this window wont be resiable:
win.resizable(0,0)

#Create a Lable widget on the tkinter window

label = Label(win, text="Hello\nRajnish\nBangalore", font=('Edwardian Script ITC', 19),
              bg='red',fg='yellow', width="15", height=3)

#height=1 indicates 1 row and so on. If text has 3 rows so we have to set height=3 rows also
#width attribute indicates that how many characters we can display on any text inputs at a time

#Then place the widget on the main tkinter window using pack() method
label.pack()
#label.grid(column=2, row=2)

#Entry Widget:
#width attribute indicates how many no. of characters will be displayed at one time and
#height attribute indicates the no. of rows. So if text is wriiten in single line then set height=1 and iftext is wriiten in two lines then set height=2
#So it doesn't matter even if we increase the font size. There is no relation b/w them.

entry = Entry(win,bg='yellow', font=("Arial",30),fg='red', width="10")
entry.pack()

#Button Widget:
button = Button(win, text="ClickMe!!",bg='blue', fg='green', font=('Arail',15,'bold'),
                width=10,height=1)
button.pack()

#start the event loop
win.mainloop()
