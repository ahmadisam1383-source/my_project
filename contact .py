from tkinter import *
from tkinter import messagebox
import sqlite3


DB_NAME = "none"


class Mokhatab:
    def __init__(self):
        self.win = Tk()
        self.win.title("Contacts")
        self.win.geometry("300x250")
        self.win.resizable(False, False)
        self.widgets()
        self.win.mainloop()

    def db_exec(self, query, params=(), fetch=False):
        with sqlite3.connect(DB_NAME) as conn:
            cur = conn.cursor()
            cur.execute(query, params)
            return cur.fetchall() if fetch else None

    def widgets(self):
        frm = Frame(self.win, padx=10, pady=10)
        frm.pack()

        Label(frm, text="Name").grid(row=0, column=0, pady=5)
        Label(frm, text="Number").grid(row=1, column=0, pady=5)

        self.ent_name = Entry(frm, width=20, justify="center")
        self.ent_num = Entry(frm, width=25, justify="center")

        self.ent_name.grid(row=0, column=1)
        self.ent_num.grid(row=1, column=1)

        btns = Frame(self.win)
        btns.pack(pady=10)

        Button(btns, text="Add", width=8, command=self.add).grid(row=0, column=0, padx=5)
        Button(btns, text="Delete", width=8, command=self.delete).grid(row=0, column=1, padx=5)
        Button(btns, text="Search", width=8, command=self.search).grid(row=1, column=0, columnspan=2, pady=5)

    def add(self):
        name, num = self.ent_name.get(), self.ent_num.get()
        if not name or not num:
            return messagebox.showwarning("Error", "Enter name and number")

        self.db_exec(
            "INSERT INTO users (name, number) VALUES (?, ?)",
            (name, num)
        )
        messagebox.showinfo("Done", "Contact added")

    def delete(self):
        num = self.ent_num.get()
        if not num:
            return messagebox.showwarning("Error", "Enter number")

        self.db_exec("DELETE FROM users WHERE number=?", (num,))
        messagebox.showinfo("Done", "Contact deleted")

    def search(self):
        name = self.ent_name.get()
        if not name:
            return messagebox.showwarning("Error", "Enter name")

        result = self.db_exec(
            "SELECT * FROM users WHERE name=?",
            (name,),
            fetch=True
        )

        messagebox.showinfo("Result", result or "Not found")


Mokhatab()
