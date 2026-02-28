import sqlite3
def get_db():
    db = sqlite3.connect('school.db')
    db.row_factory = sqlite3.Row
    db.execute("PRAGMA foreign_keys = ON;")
    return db