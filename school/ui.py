import  tkinter as tk
from tkinter import messagebox
from tkinter import ttk
from crud import add_user,get_all_users,delete
def clear():
    answer=messagebox.askyesno("warning","Are you sure?")
    if answer:
        delete()
        messagebox.showinfo("Success", "User has been deleted")
        load_users()
def adduser():
    username = entry_username.get()
    password = entry_password.get()
    role = entry_role.get()
    if not username or not password or not role:
        messagebox.showerror("eror", "Please enter username and password and role")
        return
    add_user(username, password, role)
    messagebox.showinfo("Success", "User created successfully")
    entry_username.delete(0, tk.END)
    entry_password.delete(0, tk.END)
    entry_role.delete(0, tk.END)
    load_users()
root = tk.Tk()
root.geometry("500x400")
root.resizable(False, False)
root.title("school")
font = ("Arial", 20, "bold")
title = tk.Label(root, text="School manegement", font=font, fg="black")
title.pack(side=tk.TOP)
frame1 = tk.Frame(root)
frame1.pack(pady=10)
tk.Label(frame1, text="Enter username", font=font, fg="black").grid(row=1)
entry_username = tk.Entry(frame1)
entry_username.grid(row=1, column=1)
tk.Label(frame1, text="Enter password", font=font).grid(row=2)
entry_password = tk.Entry(frame1)
entry_password.grid(row=2, column=1)
tk.Label(frame1, text="Enter role", font=font).grid(row=3)
entry_role = tk.Entry(frame1)
entry_role.grid(row=3, column=1)
tk.Button(frame1, text="Add user", command=adduser).grid(row=4, column=1)
tk.Button(frame1, text="delete user", command=clear).grid(row=5, column=1)
columns = ("id", "username", "role")
tree = ttk.Treeview(root, columns=columns, show="headings")
tree.heading("id", text="ID")
tree.heading("username", text="Username")
tree.heading("role", text="Role")
tree.pack(fill="both", expand=True, padx=10, pady=10)
def load_users():
    for row in tree.get_children():
        tree.delete(row)

    users = get_all_users()
    for user in users:
        tree.insert("", tk.END, values=user)
load_users()
root.mainloop()