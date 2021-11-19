# This program is actually a core cocepts which shows how we can handle two
#diffrent events by using single method instead of wrting two diffrent methods
#to handle the two differnt events.

"""
x=100
def show():
    x=x+10
    print(x)
show()
"""
#OUTPUT:  UnboundLocalError: local variable 'x' referenced before assignment

"""
x=100
def show():
    global x
    x=x+10
    print(x)
show()
OUTPUT: 110
"""

"""
x=100
def show():
    global x
    x=x+1
    print("ram")
show()
show()
show()
OUTPUT: ram ram ram .....
"""

x=1

def show():
    global x
    x=x+1 #x becomes 2
    if(x%2==0):
        print("ram")
    else:
        print("sita")
        
show() #ram
show() #sita
show() #ram
show() #sita
show() #ram

