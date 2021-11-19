#First we need to create a ins table in the rajnish.db db. In order to do this
#This is a program:
import sqlite3
db=sqlite3.connect('rajnish.db')
cr=db.cursor()
cr.execute('create table ins(URNO text, UNAME text,UPHY text, UCHE text, UMaths text)')
db.commit()
db.close()
print('table create')
