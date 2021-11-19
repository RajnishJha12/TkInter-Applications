from tkinter import *

root = Tk()
root.geometry("300x300")
root.minsize(300,300)
root.maxsize(300,300)

root.resizable(0,0)

root.title("Example With Grid")

names=["Ram", "Shyam", "Sita"]

#IMPORTANT: If we write same global variable as a local variable inside a method
# then we have to decalre it as global keyword like this:

z=1
def show():
    global z
    for n in names:
        z=z+1
        print(n,z)

b1=Button(root,text="click",command=show)
b1.place(x=100,y=100)

#IMPORTANT: But If we write same global variable as a local variable without method
# then no need to declare it as global keyword like this:

cities=["Bangalore","Hydrabad","Chennei","Pune"]

p=1
for cc in cities:
    p=p+1
    print(cc,p)

colors = ["red","blue","green","yellow","black"]

"""
for c in colors:
    L1 = Label(root, text=c)
    L1.pack()
    E1 = Entry(bg=c)
    E1.pack()


"""
x=1
for c in colors:
    x=x+1
    L1 = Label(root, text=c, relief=RIDGE, width=15)
    L1.grid(row=x, column=0)
    E1 = Entry(bg=c, relief=SUNKEN, width=10)
    E1.grid(row=x,column=1)


root.mainloop()
