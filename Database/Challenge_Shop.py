import sqlite3

conn = sqlite3.connect('shop.db')
cur = conn.cursor()
#cur.execute('create table product(prodno int primary key, pname text, price int)')
cur.execute('create table orders (ordno int, custid int, foreign key(custid) references customer(custid), prodno text, foreign key(prodno) references product(prodno), qty int')
#cur.execute('''create table order(orderno int,
#            custid int, foreign key(custid) references customer(custid),
#            prodno int, foreign key(prodno) references product(prodno), qty int )''' )

conn.commit()
cur.close()
conn.close()

