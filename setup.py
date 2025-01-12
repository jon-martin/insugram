#!/bin/python3

import sqlite3

db_name = 'data.db'
db_create = 'tables.sql'
db_content = ''

with open(db_create, 'r') as f:
    for line in f:
        db_content += line

connection = sqlite3.connect(db_name)
cursor = connection.cursor()

cursor.executescript(db_content)

connection.commit()
connection.close()
