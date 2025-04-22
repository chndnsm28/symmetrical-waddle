import sqlite3

conn = sqlite3.connect('univ.db')
cur = conn.cursor()
#cur.execute('create table Dept(deptno int primary key, dname text)')
#cur.execute('create table Students(roll int primary key, name text, city text, deptno int, foreign key(deptno) references Dept(deptno))')
#cur.execute('insert into Dept values(10, "CSE")')
#cur.execute('insert into Dept(dname, deptno) values("ECE", 20)')
deptno = int(input("enter deptno"))
dname = input("department name")
cur.execute(f'insert into Dept values({deptno},"{dname}")')
conn.commit()
cur.close()
conn.close()

import sqlite3

conn = sqlite3.connect('shop.db')
cur = conn.cursor()
for i in range(12):
    ordno = int(input("enter ordno"))
    custid =int(input("enter custid"))
    prodno= input("enter prodno")
    qty = int(input("enter quantity"))
    cur.execute(f'insert into order values({ordno},{custid},"{prodno}",{qty})')

conn.commit()
cur.close()
conn.close()