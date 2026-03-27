import sqlite3

def connect_db():
    return sqlite3.connect("expenses.db")

def create_table():
    conn = connect_db()
    cursor = conn.cursor()

    cursor.execute("""
    CREATE TABLE IF NOT EXISTS expenses (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        amount REAL,
        category TEXT,
        description TEXT
    )
    """)

    conn.commit()
    conn.close()

def insert_expense(amount, category, description):
    conn = connect_db()
    cursor = conn.cursor()

    cursor.execute("""
    INSERT INTO expenses (amount, category, description)
    VALUES (?, ?, ?)
    """, (amount, category, description))

    conn.commit()
    conn.close()

def fetch_expenses():
    conn = connect_db()
    cursor = conn.cursor()

    cursor.execute("SELECT * FROM expenses")
    rows = cursor.fetchall()

    conn.close()
    return rows

def delete_expense(expense_id):
    conn = connect_db()
    cursor = conn.cursor()

    cursor.execute("DELETE FROM expenses WHERE id = ?", (expense_id,))

    conn.commit()
    conn.close()

def update_expense(expense_id, amount, category, description):
    conn = connect_db()
    cursor = conn.cursor()

    cursor.execute("""
    UPDATE expenses
    SET amount = ?, category = ?, description = ?
    WHERE id = ?
    """, (amount, category, description, expense_id))

    conn.commit()
    conn.close()