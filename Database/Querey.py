import sqlite3

conn = sqlite3.connect('univ.db')
cur = conn.cursor()
rows = cur.execute('select *from Dept')
#print(rows.fetchone())
#print(rows.fetchmany(3))
print(rows.fetchall())

cur.close()
conn.close()
