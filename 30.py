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
        pass
    elif operation == "3":
        name = input("Enter table name : ")
        selectTable(name)
    else:
        print("Bye 👍")
