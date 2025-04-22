import sqlite3

conn = sqlite3.connect('univ.db')
cur = conn.cursor()
#rows = cur.execute('select distinct deptno from students')
#cur.execute('update Dept set dname="ISE" where dname="ECE"')
#cur.execute('update Students set City="Hubli" where Roll=15')
cur.execute('Delete from Dept where deptno=40')

#print(rows.fetchall())

conn.commit()
cur.close()
conn.close()