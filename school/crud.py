from db import get_db
import sqlite3

def delete():
    db = get_db()
    cursor = db.cursor()
    cursor.execute(
        "delete from users ",
    )
    db.commit()
    cursor.close()
def add_user(username, password,role):
    db = get_db()
    cursor = db.cursor()
    try:
        cursor.execute("""
            INSERT INTO users (username , password , role)
            VALUES (?,?,?)
            """, (username, password, role))
        db.commit()
        print("user created successfully")
    except sqlite3.IntegrityError as e:
        print(e)
    finally:
        cursor.close()
def get_all_users():
    db = get_db()
    cursor = db.cursor()
    cursor.execute("SELECT id,username,password,role FROM users")
    rows = cursor.fetchall()
    users = [tuple(row) for row in rows]
    db.close()
    return users
