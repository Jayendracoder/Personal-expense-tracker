# Personal-expense-tracker
A simple and user-friendly Python-based Personal Expense Tracker created by me. It helps users log, manage, and analyze their daily expenses with features like category-wise tracking, total spending summary, and basic insights for better budgeting.
Personal Expense Tracker in Python Problem Statement: In today's fast-paced world, effectively managing personal finances is essential. This project aims to build a personal expense tracker that allows users to log daily expenses, categorize them, monitor spending habits, and compare expenditures against a monthly budget. The tracker also includes file handling to persist user data.

Objectives: Design and implement a personal expense tracker in Python.

Enable users to categorize expenses and define monthly budgets.

Save and load expenses using CSV files.

Provide an interactive, menu-driven interface for ease of use.

Project Description:

Add Expense Users are prompted to enter the date, category, amount, and description.
Entries are stored as dictionaries inside a list for structured data management.

View Expenses All expenses are displayed with validation checks to skip incomplete entries.
This gives users clear visibility into their spending patterns.

Budget Tracking Users can define a monthly budget.
The application calculates the total expenses and compares it to the set budget.

Alerts are given if the user exceeds their budget or shows the remaining balance.

File Handling Expenses are stored in a CSV file (expenses.csv).
When the program is restarted, previous data is loaded automatically to continue tracking without data loss.

Interactive Menu A user-friendly, menu-driven interface guides users through the functionalities:
Add expense

View expenses

Track budget

Save expenses

Exit

Tools & Technologies Used: Language: Python 3

File Format: CSV

Libraries: csv, os, datetime

What I Learned: Python Fundamentals:

Conditionals, loops, functions, and error handling.

Working with lists and dictionaries for data organization.

File Handling:

Reading from and writing to CSV files.

Handling data persistence using file I/O operations.

User Interaction:

Designing menu-driven console applications.

Validating user input for reliability.

Data Validation:

Ensuring data consistency and completeness before processing.

Budget Management Logic:

Understanding how to implement financial logic and calculations in a real-world context.

Conclusion: This project simulates a real-world use case and strengthens core Python programming skills. It integrates logical thinking, user interface design, and file handling — essential components for many software applications. This hands-on experience helped in understanding not only Python as a language but also how to build structured, scalable solutions to common problems.
