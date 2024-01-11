import sqlite3
link= sqlite3.connect("Database.db")
cursor=link.cursor()

cursor.execute('''
            CREATE TABLE IF NOT EXISTS users (
                username TEXT NOT NULL PRIMARY KEY,
                password TEXT NOT NULL
            )
    ''')

cursor.execute('''
            CREATE TABLE IF NOT EXISTS user_info (
                username TEXT NOT NULL,
                Fname TEXT,
                gender TEXT NOT NULL,
                phone INTEGER NOT NULL UNIQUE,
                address TEXT,
                company TEXT
            )      
    ''')
