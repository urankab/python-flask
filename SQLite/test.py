import sqlite3

connection = sqlite3.connect('data.db')

cursor = connection.cursor()

create_table = 'CREATE TABLE users (id int, username text, password text)'
cursor.execute(create_table)

# Insert single item
user = (1, 'Jon', 'asdf')
insert_query = 'INSERT INTO users VALUES (?, ?, ?)'
cursor.execute(insert_query, user)

# Insert multiple items
users = [
    (2, 'Rolf', '1234'),
    (3, 'Dave', 'doggy')
]
cursor.executemany(insert_query, users)
select_query = 'SELECT * FROM users'

for row in cursor.execute(select_query):
    print(row)

connection.commit()

connection.close()