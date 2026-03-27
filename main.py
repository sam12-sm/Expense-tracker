from database import create_table

expenses = []

def add_expense():
    try:
        amount = float(input("Enter amount: "))
    except ValueError:
        print("Invalid amount. Try again.")
        return

    category = input("Enter category: ")
    description = input("Enter description: ")

    expense = {
        "amount": amount,
        "category": category,
        "description": description
    }

    expenses.append(expense)
    print("Expense added successfully!")

def view_expenses():
    if not expenses:
        print("No expenses found.")
        return

    print("\n--- Expenses ---")
    for exp in expenses:
        print(f"{exp['amount']} | {exp['category']} | {exp['description']}")

def main():
    create_table()   # database + table created here

    while True:
        print("\n1. Add Expense")
        print("2. View Expenses")
        print("3. Exit")

        choice = input("Enter choice: ")

        if choice == "1":
            add_expense()
        elif choice == "2":
            view_expenses()
        elif choice == "3":
            print("Exiting program...")
            break
        else:
            print("Invalid choice")

if __name__ == "__main__":
    main()