#First we need to create a regis table in the rajnish.db db. In order to do this
#This is a program:
import sqlite3
db=sqlite3.connect('rajnish.db')
cr=db.cursor()
cr.execute('create table regis(UNAME text, UPASS text, UCN text)')
db.commit()
db.close()
print('table create')
