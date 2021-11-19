from tkinter import *

#Create a GUI in such a way that when we click on the button then bg color
#of the main window will change.
t = Tk()
t.geometry("500x500")
t.resizable(0,0)

#def show():
    #print("SoftWaves") It will print on the console
    #t.configure(background="red") It will change the bg clour of a main win


def showRed():
    t.configure(bg="red")
    
def showBlue():
    t.configure(bg="blue")

    
def showGreen():
    t.configure(bg="green")

# You have to pass the parameter of any name to handle such event:
def showOrange(e):
    t.configure(bg="orange")


#button = Button(t, text='Button 1' , font=('Arial',15), command=show)
#button.pack()

button1 = Button(t, text='Button 1' , font=('Arial',15), command=showRed)
button1.grid(row=0, column=0, pady=25, padx=25)

button2 = Button(t, text='Button 2' , font=('Arial',15), command=showBlue)
button2.grid(row=0, column=1)

button3 = Button(t, text='Button 3' , font=('Arial',15))
button3.config(command=showGreen)
button3.grid(row=0, column=2, padx=25)

# We can also use bind() method to hande diffenrt events:
# So this shows how to handle events using bind() method:
button4 = Button(t, text="Button 4" , font=("Arial", 15))
button4.bind("<Button>", showOrange)
button4.grid(row=0, column=3)


t.mainloop()
