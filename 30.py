import sqlite3


def createTable(name):
    conn = sqlite3.connect("info.db")
    cur = conn.cursor()

    fields = input("Enter table columns : ").split(",")

    query = f"CREATE TABLE IF NOT EXISTS {name} {tuple(fields)};"

    cur.execute(query)
    print(f"Table {name} create successfully")

    conn.commit()
    conn.close()


def insertTable(name):
    conn = sqlite3.connect("info.db")
    cur = conn.cursor()

    query = f"PRAGMA table_info({name});"  # baraye peyda kardane esme soton ha
    cur.execute(query)
    column_names = [i[1] for i in cur.fetchall()]  # esme soton ha dar index 1 hastand
    values = []

    for i in column_names:
        values.append(input(f"Enter {i} : "))

    query = f"INSERT INTO {name} VALUES {tuple(values)};"
    cur.execute(query)

    print("Insert Was Successful")
    conn.commit()
    conn.close()


def selectTable(name):
    conn = sqlite3.connect("info.db")
    cur = conn.cursor()

    query = f"SELECT * FROM {name};"
    cur.execute(query)
    data = cur.fetchall()

    for i in data:
        print(i)

    conn.commit()
    conn.close()


while True:
    operation = input("""
    1 : Create a table
    2 : Insert into a table
    3 : Display a table
: """)

    if operation == "1":
        name = input("Enter table name : ")
        createTable(name)
    elif operation == "2":
        name = input("Enter table name : ")
        insertTable(name)
    elif operation == "3":
        name = input("Enter table name : ")
        selectTable(name)
    else:
        print("Bye 👍")
