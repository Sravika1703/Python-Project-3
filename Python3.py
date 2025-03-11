import json
import os
from datetime import datetime

class ExpenseTracker:
    def __init__(self):
        self.expenses = []
        self.filename = "expenses.json"
        self.load_data()

    def load_data(self):
        if os.path.exists(self.filename):
            with open(self.filename, "r") as file:
                self.expenses = json.load(file)
        else:
            print("No previous expense data found. Starting fresh.")

    def save_data(self):
        with open(self.filename, "w") as file:
            json.dump(self.expenses, file, indent=4)

    def add_expense(self, amount, category, description):
        date = datetime.now().strftime("%Y-%m-%d")
        expense = {
            "amount": amount,
            "category": category,
            "description": description,
            "date": date
        }
        self.expenses.append(expense)
        self.save_data()

    def view_expenses(self):
        if not self.expenses:
            print("No expenses recorded.")
        else:
            print("\nExpenses:")
            for expense in self.expenses:
                print(f"Date: {expense['date']} | Amount: ${expense['amount']} | "
                      f"Category: {expense['category']} | Description: {expense['description']}")

    def category_summary(self, category):
        category_expenses = [exp for exp in self.expenses if exp['category'] == category]
        if category_expenses:
            total = sum(exp['amount'] for exp in category_expenses)
            print(f"Total spent on {category}: ${total}")
        else:
            print(f"No expenses recorded under {category}.")

    def monthly_summary(self):
        current_month = datetime.now().strftime("%Y-%m")
        monthly_expenses = [exp for exp in self.expenses if exp['date'].startswith(current_month)]

        if not monthly_expenses:
            print(f"No expenses recorded for the month {current_month}.")
        else:
            total = sum(exp['amount'] for exp in monthly_expenses)
            print(f"Total expenses for {current_month}: ${total}")

def show_menu():
    print("\nExpense Tracker")
    print("1. Add Expense")
    print("2. View All Expenses")
    print("3. View Category Summary")
    print("4. View Monthly Summary")
    print("5. Exit")

def get_valid_amount():
    while True:
        try:
            amount = float(input("Enter the amount spent: $"))
            if amount <= 0:
                print("Amount should be a positive number. Please try again.")
            else:
                return amount
        except ValueError:
            print("Invalid input. Please enter a valid amount (numeric value).")

def get_valid_category():
    categories = [
        "Food", "Entertainment", "Water Bill", "Electricity", "Grocery", 
        "Traveling", "EMI", "Rent", "Fees", "Personal"
    ]
    while True:
        print("\nAvailable categories:")
        for idx, category in enumerate(categories, 1):
            print(f"{idx}. {category}")
        
        try:
            choice = int(input("Choose a category by number: "))
            if 1 <= choice <= len(categories):
                return categories[choice - 1]
            else:
                print("Invalid choice. Please choose a valid category.")
        except ValueError:
            print("Invalid input. Please enter a valid number.")

def main():
    tracker = ExpenseTracker()

    while True:
        show_menu()
        choice = input("Choose an option (1-5): ")

        if choice == "1":
            while True:
                amount = get_valid_amount()
                category = get_valid_category()
                description = input("Enter a brief description of the expense: ")
                tracker.add_expense(amount, category, description)
                print(f"Expense of ${amount} in category '{category}' added.")

                another_expense = input("Do you have another expense to enter? (yes/no): ").lower()
                if another_expense != "yes":
                    break

        elif choice == "2":
            tracker.view_expenses()

        elif choice == "3":
            category = input("Enter the category to view: ").capitalize()
            tracker.category_summary(category)

        elif choice == "4":
            tracker.monthly_summary()

        elif choice == "5":
            print("Exiting program. Goodbye!")
            break

        else:
            print("Invalid choice. Please select a valid option.")

if __name__ == "__main__":
    main()
