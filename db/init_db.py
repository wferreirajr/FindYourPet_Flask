import sqlite3

connection = sqlite3.connect('findyourpet.db')

with open('schema.sql') as f:
    connection.executescript(f.read())

cur = connection.cursor()

cur.execute("INSERT INTO accounts (NomeCompleto, Email, Tipo, Senha) VALUES (?, ?, ?, ?)",
            ('Wilson', 'wilson.f.jr@gmail.com', 'admin', 'Password123')
            )

connection.commit()
connection.close()