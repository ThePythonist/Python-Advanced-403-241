import sqlite3


def insert_data(item):
    conn = sqlite3.connect("info.db")
    cur = conn.cursor()

    cur.execute("""
        CREATE TABLE IF NOT EXISTS employees(
        id INTEGER PRIMARY KEY,
        name VARCHAR(50),
        code INT,
        job VARCHAR(70)
        );
        """)

    cur.execute("SELECT * FROM employees;")
    records = cur.fetchall()
    records = [i[1:] for i in records]
    new_record = (item['name'], int(item['code']), item['job'])

    if new_record in records:
        print("Record already exists")
    else:
        query = f"INSERT INTO employees(name,code,job) VALUES {(item['name'], item['code'], item['job'])};"
        cur.execute(query)
        print("Inserted")
        conn.commit()

    conn.close()


def select_table():
    conn = sqlite3.connect("info.db")
    cur = conn.cursor()

    cur.execute("SELECT * FROM employees;")
    records = cur.fetchall()

    for i in records:
        print(i)

    conn.close()


# select_table()
insert_data({"name": "Bahar", "code": "40216", "job": "Civil Engineer"})
