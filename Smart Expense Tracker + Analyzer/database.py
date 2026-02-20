import sqlite3
db_name = 'exp.db'
def connect():
    return sqlite3.connect(db_name)


def createTable():
    conn = connect()
    cursor = conn.cursor()
    cursor.execute("""CREATE TABLE IF NOT EXISTS expense(
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    amount REAL NOT NULL,
    category TEXT NOT NULL,
    description TEXT ,
    date TEXT NOT NULL
    )
    """)
    conn.commit()
    conn.close()

def addExpense(amount, category, description, date):
    conn = connect()
    cursor = conn.cursor()
    cursor.execute("""INSERT INTO expense(amount, category, description, date)
    VALUES(?,?,?,?)""", (amount, category, description, date))
    conn.commit()
    conn.close()
def get_all_expenses():
    conn = connect()
    cursor = conn.cursor()
    cursor.execute("""SELECT * FROM expense ORDER BY amount""")
    expenses = cursor.fetchall()
    conn.close()
    return expenses