from __future__ import print_function

import cx_Oracle

connection = cx_Oracle.connect("user", "password", "10.0.0.18:1521/db")

print(connection.version)
cursor = connection.cursor()

# sql语句不能以;结尾
cursor.execute("""
    SELECT table_name
    FROM user_tables""")

row = cursor.fetchall()
for row in row:
    print(row)

cursor.execute('''insert into tb(col1) values ('val')''')
connection.commit()

connection.close()
