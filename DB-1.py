import sqlite3

conn = sqlite3.connect("info.db")  # baraye etesal be db
cur = conn.cursor()  # baraye dastoor dadan

# cur.execute("CREATE TABLE countries (name,capital,language);")

# cur.execute("INSERT INTO countries VALUES ('iran','tehran','farsi');")
# cur.execute("INSERT INTO countries VALUES ('germany','berlin','deutsch');")
# cur.execute("INSERT INTO countries VALUES ('belgium','brussels','deutsch');")
# cur.execute("INSERT INTO countries VALUES ('Austria ','vienna','deutsch');")
# cur.execute("INSERT INTO countries VALUES ('afghanistan','kabul','farsi');")

# cur.execute("DELETE FROM countries")  # deletes all records
# cur.execute("DELETE FROM countries WHERE language='deutsch';")  # deletes specific record

# cur.execute("DROP TABLE countries;") # deletes the table

cur.execute("SELECT * FROM countries;")
cur.execute("SELECT * FROM countries WHERE language='deutsch';")

records = cur.fetchall()
print(records)

conn.commit()
conn.close()
