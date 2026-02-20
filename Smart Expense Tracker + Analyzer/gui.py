import tkinter as tk
from tkinter import messagebox, ttk
from database import createTable, addExpense, get_all_expenses

class AppExpense:
    def __init__(self, root):
        self.root = root
        self.root.title("Expense Tracker + Analyzer")
        self.root.geometry("700x500")

        createTable()
        self.create_widget()
        self.load_expenses()

    def create_widget(self):
        self.frame = tk.Frame(self.root)
        self.frame.pack(pady=10)

        tk.Label(self.frame, text="Amount").grid(row=0, column=0)
        tk.Label(self.frame, text="Category").grid(row=0, column=1)
        tk.Label(self.frame, text="Description").grid(row=0, column=2)
        tk.Label(self.frame, text="Date").grid(row=0, column=3)

        self.amount = tk.Entry(self.frame, width=10)
        self.category = tk.Entry(self.frame, width=15)
        self.description = tk.Entry(self.frame, width=20)
        self.date = tk.Entry(self.frame, width=10)

        self.amount.grid(row=1, column=0)
        self.category.grid(row=1, column=1)
        self.description.grid(row=1, column=2)
        self.date.grid(row=1, column=3)

        tk.Button(self.frame, text="Add", command=self.add).grid(row=1, column=4, padx=5)

        self.tree = ttk.Treeview(
            self.root,
            columns=("id", "amount", "category", "description", "date"),
            show="headings"
        )

        for col in self.tree["columns"]:
            self.tree.heading(col, text=col)

        self.tree.pack(expand=True, fill="both", pady=10)

    def add(self):
        try:
            addExpense(
                float(self.amount.get()),
                self.category.get(),
                self.description.get(),
                self.date.get()
            )

            self.clear_entries()
            self.load_expenses()

        except ValueError:
            messagebox.showerror("Error", "Amount must be a number")

    def load_expenses(self):
        for row in self.tree.get_children():
            self.tree.delete(row)

        for expense in get_all_expenses():
            self.tree.insert("", "end", values=expense)

    def clear_entries(self):
        self.amount.delete(0, tk.END)
        self.category.delete(0, tk.END)
        self.description.delete(0, tk.END)
        self.date.delete(0, tk.END)



