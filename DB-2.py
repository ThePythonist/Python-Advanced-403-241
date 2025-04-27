import sqlite3

students = [
    {"name": "Amirali", "code": "40211", "job": "Backend Developer"},
    {"name": "Parsa", "code": "40212", "job": "Frontend Developer"},
    {"name": "Mehrzad", "code": "40213", "job": "Security Engineer"},
    {"name": "Mohammad Mehdi", "code": "40214", "job": "DevOps Engineer"},
    {"name": "Bahar", "code": "40215", "job": "Civil Engineer"},
]


def create_table():
    con = sqlite3.connect('info.db')
    cur = con.cursor()

    cur.execute("""
    CREATE TABLE IF NOT EXISTS employees(
    id INTEGER PRIMARY KEY,
    name VARCHAR(50),
    code INT,
    job VARCHAR(70)
    );
    """)

    con.commit()
    con.close()


def insert(item):
    con = sqlite3.connect('info.db')
    cur = con.cursor()

    command2 = f"INSERT INTO employees(name,code,job) VALUES {(item['name'], item['code'], item['job'])};"
    # print(command2)
    cur.execute(command2)

    con.commit()
    con.close()


def select(table):
    con = sqlite3.connect('info.db')
    cur = con.cursor()

    command = f"SELECT * FROM {table};"
    cur.execute(command)
    records = cur.fetchall()
    for i in records:
        # if i[0] == 4:
        print(i)


# create_table()

# for i in students:
#     insert(i)

# insert({"name": "Bahar", "code": "40215", "job": "Civil Engineer"})

select("employees")
