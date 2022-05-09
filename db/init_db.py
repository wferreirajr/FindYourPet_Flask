import sqlite3

connection = sqlite3.connect('findyourpet.db')


with open('schema.sql') as f:
    connection.executescript(f.read())

cur = connection.cursor()

cur.execute("INSERT INTO account (fullname, user, passwd, type) VALUES (?, ?, ?, ?)",
            ('Wilson', 'wilson.f.jr@gmail.com', 'vai123', 'admin')
            )

connection.commit()
connection.close()