import json
import os
from datetime import datetime

DATA_PATH = "data.json"

# Return empty list if file doesn't exist, else load and return JSON data
def load_data(file_path=DATA_PATH):
    if not os.path.exists(file_path):
        return []
    with open(file_path, 'r') as file:
        return json.load(file)

# Write data to JSON file with indentation
def save_data(data, file_path=DATA_PATH):
    with open(file_path, 'w') as file:
        json.dump(data, file, indent=4)

# Build a timestamped log entry and append it to the person's passbook
def update_passbook(db, action, person_index, details=""):
    entry = {
        "Timestamp": datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
        "Action": action,
        "Details": details
    }
    db[person_index].setdefault("Passbook", []).append(entry)

# Tally total income and expenses, return both along with net balance
def sum_transactions(db, person_index):
    income, expense = 0, 0
    for txn in db[person_index]['Transactions']:
        amt = abs(txn['Amount'])
        if txn['Type'].lower() == 'income':
            income += amt
        else:
            expense += amt
    return income, expense, income - expense

# Aggregate net amounts per category (positive = income, negative = expense)
def category_summary(db, person_index):
    summary = {}
    for txn in db[person_index]['Transactions']:
        amt = abs(txn['Amount'])
        if txn['Type'].lower() == 'income':
            summary[txn['Category']] = summary.get(txn['Category'], 0) + amt
        else:
            summary[txn['Category']] = summary.get(txn['Category'], 0) - amt
    return summary

# Group net transaction amounts by month (YYYY-MM)
def monthly_total(db, person_index):
    monthly = {}
    for txn in db[person_index]['Transactions']:
        month = txn['Date'][:7]
        amt = abs(txn['Amount'])
        if txn['Type'].lower() == 'income':
            monthly[month] = monthly.get(month, 0) + amt
        else:
            monthly[month] = monthly.get(month, 0) - amt
    return monthly

# Return the n most recent transactions sorted by date descending
def recent_transactions(db, person_index, n=3):
    txns = sorted(
        db[person_index]['Transactions'],
        key=lambda x: x['Date'],
        reverse=True
    )
    return txns[:n]

# Recompute and overwrite the person's full financial summary
def refresh_summary(db, person_index):
    income, expense, balance = sum_transactions(db, person_index)
    db[person_index]["Summary"] = {
        "TotalIncome": income,
        "TotalExpenses": expense,
        "CurrentBalance": balance,
        "CategoryBreakdown": category_summary(db, person_index),
        "MonthlyTotals": monthly_total(db, person_index),
        "RecentActivity": recent_transactions(db, person_index)
    }

# Record an action in the passbook and persist to disk
def log_action(db, index, action, details):
    update_passbook(db, action, index, details)
    save_data(db)
