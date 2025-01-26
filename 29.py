import sqlite3


def select(table):
    con = sqlite3.connect('info.db')
    cur = con.cursor()

    command = f"SELECT * FROM {table};"
    cur.execute(command)
    records = cur.fetchall()
    for i in records:
        # if i[0] == 4:
        print(i)

    con.commit()
    con.close()


def insert(item):
    con = sqlite3.connect('info.db')
    cur = con.cursor()

    query1 = f"SELECT * FROM employees;"
    cur.execute(query1)
    records = cur.fetchall()

    records = [i[1:] for i in records]
    new_record = tuple(item.values())

    if not new_record in records:
        query2 = f"INSERT INTO employees(name,code,job) VALUES {new_record}"
        cur.execute(query2)
        print("Inserted New Record")
        con.commit()
        con.close()
        return

    print("Inserted No Record")


select("employees")
# r = {"name": "Nima", "code": 40215, "job": "Computer Engineer"}
# insert(r)
