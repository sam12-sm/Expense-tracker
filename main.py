expenses = []

def add_expense():
    amount = float(input("Enter amount: "))
    category = input("enter category")
    description = input("description")

    expense = {
        "amount": amount,
        "category": category,
        "description": description
    }

    expenses.append(expense)
    print("Expense added successfully")

def view_expense():
    if not expenses:
        print("No expenses found")
        return
    for exp in expenses:
        print(f"{exp['amount']} | {exp['category']} | {exp['description']}")

while True:
    print("/n1. Add Expense")
    print("2. View expense")
    print("3. Exit")

    choice = input("Enter your choice: ")

    if choice == "1":
        add_expense()
    elif choice == "2":
        view_expense()
    elif choice == "3":
        break
    else:
        print("Invalid choice")