import tkinter as tk
from tkinter import ttk, messagebox
import pandas as pd
from datetime import datetime
import os

class ExpenseTracker:
    def __init__(self, root):
        self.root = root
        self.root.title("Shweta's Smart Expense Tracker 🚀")
        self.root.geometry("450x500")
        self.root.configure(bg="#f0f0f0")

        # 1. Path Setup: Ye line file ko usi folder mein banayegi jahan code hai
        base_path = os.path.dirname(os.path.abspath(__file__))
        self.filename = os.path.join(base_path, "expenses.csv")

        # 2. Excel File Initialization (Check if exists)
        if not os.path.exists(self.filename):
            df = pd.DataFrame(columns=["Date", "Category", "Amount", "Notes"])
            df.to_csv(self.filename, index=False)

        # --- UI Design (Front-end) ---
        tk.Label(root, text="EXPENSE TRACKER", font=('Arial', 18, 'bold'), bg="#f0f0f0", fg="#333").pack(pady=20)

        # Amount Entry
        tk.Label(root, text="Amount (₹):", bg="#f0f0f0").pack()
        self.amt_ent = tk.Entry(root, font=('Arial', 12))
        self.amt_ent.pack(pady=5)

        # Category Dropdown
        tk.Label(root, text="Category:", bg="#f0f0f0").pack()
        self.cat_box = ttk.Combobox(root, values=["Food", "Travel", "Shopping", "Bills", "Fees", "Others"], font=('Arial', 10))
        self.cat_box.pack(pady=5)

        # Note Entry
        tk.Label(root, text="Note/Description:", bg="#f0f0f0").pack()
        self.note_ent = tk.Entry(root, font=('Arial', 12))
        self.note_ent.pack(pady=5)

        # Add Button
        tk.Button(root, text="SAVE EXPENSE", command=self.add_expense, bg="#28a745", fg="white", font=('Arial', 12, 'bold'), width=20).pack(pady=20)

        # Summary Button
        tk.Button(root, text="SHOW TOTAL SPEND", command=self.show_summary, bg="#007bff", fg="white", font=('Arial', 10), width=20).pack()

    # --- Logic (Back-end) ---
    def add_expense(self):
        amt = self.amt_ent.get()
        cat = self.cat_box.get()
        note = self.note_ent.get()
        date = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

        if amt and cat:
            try:
                # Direct entry into CSV
                new_row = pd.DataFrame([[date, cat, amt, note]], columns=["Date", "Category", "Amount", "Notes"])
                new_row.to_csv(self.filename, mode='a', header=False, index=False)
                
                messagebox.showinfo("Done!", f"Successfully added ₹{amt} for {cat}")
                self.amt_ent.delete(0, tk.END)
                self.note_ent.delete(0, tk.END)
                self.cat_box.set('')
            except Exception as e:
                messagebox.showerror("Error", f"Could not save: {e}")
        else:
            messagebox.showwarning("Input Missing", "Please enter Amount and Category!")

    def show_summary(self):
        try:
            df = pd.read_csv(self.filename)
            total = pd.to_numeric(df['Amount']).sum()
            messagebox.showinfo("Report", f"Your Total Expense: ₹{total}")
        except:
            messagebox.showwarning("Empty", "No data found yet!")

if __name__ == "__main__":
    root = tk.Tk()
    app = ExpenseTracker(root)
    root.mainloop()