import sqlite3
conn = sqlite3.connect('univ.db')
cur = conn.cursor()
for i in range(1):

    roll = int(input("enter roll no :"))
    name = input("enter name :")
    city = input("enter city :")
    depno = int(input("enter depno :"))
    cur.execute(f'insert into students values({roll},"{name}","{city}",{depno})')

conn.commit()
cur.close()
conn.close()


