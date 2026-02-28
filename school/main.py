from DBrun import create_table
from crud import add_user,get_all_users

if __name__ == '__main__':
    create_table()
    print("database successfully created")
users = get_all_users()
for i in users:
    print(dict(i))