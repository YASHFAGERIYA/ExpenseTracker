import json
import os
from datetime import datetime

FILE_NAME = os.path.join(os.path.dirname(os.path.abspath(__file__)), "expenses.json")


def load_expenses():
    if not os.path.exists(FILE_NAME):
        return []

    with open(FILE_NAME, "r") as file:
        return json.load(file)


def save_expenses(expenses):
    with open(FILE_NAME, "w") as file:
        json.dump(expenses, file, indent=4)


def add_expense(expenses):
    name = input("Enter expense name: ")
    amount = float(input("Enter amount: "))
    category = input("Enter category: ")

    expense = {
        "name": name,
        "amount": amount,
        "category": category,
        "date": datetime.now().strftime("%Y-%m-%d")
    }

    expenses.append(expense)
    save_expenses(expenses)

    print("Expense added successfully!")
    print("Saved to:", FILE_NAME)


def view_expenses(expenses):
    if not expenses:
        print("No expenses found.")
        return

    for i, expense in enumerate(expenses, 1):
        print(
            f"{i}. {expense['name']} | "
            f"₹{expense['amount']} | "
            f"{expense['category']} | "
            f"{expense['date']}"
        )


def search_expense(expenses):
    keyword = input("Enter name or category: ")
    found = False

    for expense in expenses:
        if keyword.lower() in expense["name"].lower() or keyword.lower() in expense["category"].lower():
            print(
                f"{expense['name']} | "
                f"₹{expense['amount']} | "
                f"{expense['category']} | "
                f"{expense['date']}"
            )
            found = True

    if not found:
        print("No matching expense found.")


def show_total(expenses):
    total = sum(expense["amount"] for expense in expenses)
    print(f"Total spending: ₹{total}")


def main():
    expenses = load_expenses()

    while True:
        print("\n============================")
        print("   PERSONAL EXPENSE TRACKER")
        print("============================")
        print("1. Add Expense")
        print("2. View Expenses")
        print("3. Search Expense")
        print("4. Show Total Spending")
        print("5. Exit")

        choice = input("Enter choice: ")

        if choice == "1":
            add_expense(expenses)
        elif choice == "2":
            view_expenses(expenses)
        elif choice == "3":
            search_expense(expenses)
        elif choice == "4":
            show_total(expenses)
        elif choice == "5":
            break
        else:
            print("Invalid choice.")


if __name__ == "__main__":
    main()