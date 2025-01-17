import sqlite3

students = [
    {"name": "mina", "major": "riazi", "grade": "18.75"},
    {"name": "pedram", "major": "olom computer", "grade": "16.98"},
    {"name": "kiana", "major": "mohandesi omran", "grade": "17.33"},
    {"name": "mohsen", "major": "mohandesi computer", "grade": "17.47"},
]


def create_table():
    conn = sqlite3.connect("info.db")
    cur = conn.cursor()

    query = "CREATE TABLE students (name,major,grade);"
    cur.execute(query)

    conn.commit()
    conn.close()


def insert(student):
    conn = sqlite3.connect("info.db")
    cur = conn.cursor()

    query = f"INSERT INTO students VALUES {(student['name'], student['major'], student['grade'])};"
    cur.execute(query)

    conn.commit()
    conn.close()


def select():
    conn = sqlite3.connect("info.db")
    cur = conn.cursor()

    query = "SELECT * FROM students;"
    cur.execute(query)

    records = cur.fetchall()
    for i in records:
        print(i)

    conn.commit()
    conn.close()


# create_table()

# for i in students:
#     insert(i)

select()
