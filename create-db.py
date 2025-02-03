import sqlite3

con=sqlite3.connect('data.db')
cursor=con.cursor()

cursor.execute('CREATE TABLE if not exits data ("name TEXT,lastname TEXT,address TEXT,id INTEGRATE PRIMARY KEY, password TEXT ")')

con.commit()
con.close()

