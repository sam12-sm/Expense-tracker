from database import create_table, insert_expense, fetch_expenses, delete_expense, update_expense

def add_expense():
    try:
        amount = float(input("Enter amount: "))
    except ValueError:
        print("Invalid amount. Try again.")
        return

    category = input("Enter category: ")
    description = input("Enter description: ")

    insert_expense(amount, category, description)
    print("Expense added successfully!")

def view_expenses():
    expenses = fetch_expenses()

    if not expenses:
        print("No expenses found.")
        return

    print("\n--- Expenses ---")
    for exp in expenses:
        print(f"{exp[0]} | {exp[1]} | {exp[2]} | {exp[3]}")

def delete_expense_ui():
    try:
        expense_id = int(input("Enter expense ID to delete: "))
    except ValueError:
        print("Invalid ID.")
        return

    delete_expense(expense_id)
    print("Expense deleted successfully!")

def update_expense_ui():
    try:
        expense_id = int(input("Enter expense ID to update: "))
        amount = float(input("Enter new amount: "))
    except ValueError:
        print("Invalid input.")
        return

    category = input("Enter new category: ")
    description = input("Enter new description: ")

    update_expense(expense_id, amount, category, description)
    print("Expense updated successfully!")

def main():
    create_table()   # VERY IMPORTANT

    while True:
        print("\n1. Add Expense")
        print("2. View Expenses")
        print("3. Delete Expense")
        print("4. Update Expense")
        print("5. Exit")

        choice = input("Enter choice: ")

        if choice == "1":
            add_expense()
        elif choice == "2":
            view_expenses()
        elif choice == "3":
            delete_expense_ui()
        elif choice == "4":
            update_expense_ui()
        elif choice == "5":
            print("Exiting program...")
            break

if __name__ == "__main__":
    main()