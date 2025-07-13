import csv
import os
from datetime import datetime

# Global variables
expenses = []
budget = 0.0
filename = "expenses.csv"

# Load expenses from file
def load_expenses():
    global expenses
    if os.path.exists(filename):
        with open(filename, mode='r', newline='') as file:
            reader = csv.DictReader(file)
            for row in reader:
                try:
                    expense = {
                        'date': row['date'],
                        'category': row['category'],
                        'amount': float(row['amount']),
                        'description': row['description']
                    }
                    expenses.append(expense)
                except Exception as e:
                    print(f"Skipping corrupted row: {row} - Error: {e}")
        print("Expenses loaded successfully.")
    else:
        print("No previous data found. Starting fresh.")

# Save expenses to file
def save_expenses():
    with open(filename, mode='w', newline='') as file:
        fieldnames = ['date', 'category', 'amount', 'description']
        writer = csv.DictWriter(file, fieldnames=fieldnames)
        writer.writeheader()
        for exp in expenses:
            writer.writerow(exp)
    print("Expenses saved successfully.")

# Add a new expense
def add_expense():
    try:
        date = input("Enter the date (YYYY-MM-DD): ")
        datetime.strptime(date, "%Y-%m-%d")  # validate date format
        category = input("Enter the category (e.g., Food, Travel): ")
        amount = float(input("Enter the amount spent: "))
        description = input("Enter a brief description: ")
        expense = {'date': date, 'category': category, 'amount': amount, 'description': description}
        expenses.append(expense)
        print("Expense added successfully.")
    except ValueError:
        print("Invalid input. Please try again.")

# View all expenses
def view_expenses():
    if not expenses:
        print("No expenses recorded yet.")
        return
    print("\n--- Your Expenses ---")
    for exp in expenses:
        if all(k in exp and exp[k] for k in ['date', 'category', 'amount', 'description']):
            print(f"Date: {exp['date']} | Category: {exp['category']} | Amount: ${exp['amount']:.2f} | Description: {exp['description']}")
        else:
            print("Incomplete expense entry found. Skipping.")

# Set and track the budget
def track_budget():
    global budget
    if budget == 0:
        try:
            budget = float(input("Enter your monthly budget: "))
        except ValueError:
            print("Invalid input. Please enter a number.")
            return

    total_expense = sum(exp['amount'] for exp in expenses)
    remaining = budget - total_expense

    print(f"\nTotal spent so far: ${total_expense:.2f}")
    if total_expense > budget:
        print("⚠️ You have exceeded your budget!")
    else:
        print(f"✅ You have ${remaining:.2f} left for the month.")

# Interactive menu
def main_menu():
    load_expenses()
    while True:
        print("\n==== Personal Expense Tracker ====")
        print("1. Add Expense")
        print("2. View Expenses")
        print("3. Track Budget")
        print("4. Save Expenses")
        print("5. Exit")
        choice = input("Choose an option (1-5): ")

        if choice == '1':
            add_expense()
        elif choice == '2':
            view_expenses()
        elif choice == '3':
            track_budget()
        elif choice == '4':
            save_expenses()
        elif choice == '5':
            save_expenses()
            print("Goodbye! Your expenses have been saved.")
            break
        else:
            print("Invalid option. Please choose a number from 1 to 5.")

# Start the program
if __name__ == "__main__":
    main_menu()
