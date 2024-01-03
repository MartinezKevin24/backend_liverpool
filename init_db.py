import sqlite3
from flask import current_app

connection = sqlite3.connect('./databases/liverpool.db')

with open('./schemas/init_tables.sql') as f:
    connection.executescript(f.read())
    
connection.commit()
connection.close()