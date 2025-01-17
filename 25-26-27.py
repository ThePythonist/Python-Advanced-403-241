import sqlite3

conn = sqlite3.connect("info.db")
cur = conn.cursor()

# cur.execute("CREATE TABLE customers (name,city,phone);")

# cur.execute("INSERT INTO customers VALUES ('ahmad javid','mashhad','09396740119');")
# cur.execute("INSERT INTO customers VALUES ('sina keykavoos','yazd','09122220189');")
# cur.execute("INSERT INTO customers VALUES ('sahand teymori','oromieh','09306740267');")

cur.execute("SELECT * FROM customers;")

records = cur.fetchall()

for i in records:
    print(i[-1])

conn.commit()
conn.close()
