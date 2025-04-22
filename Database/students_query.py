import sqlite3

conn = sqlite3.connect('univ.db')
cur = conn.cursor()
#rows = cur.execute('select distinct deptno from students')
rows = cur.execute("select name from students where city in(select city from students where name = 'Ajay') " )

#print(rows.fetchall())
allrows = rows.fetchall()
print(allrows)
cur.close()
conn.close()
