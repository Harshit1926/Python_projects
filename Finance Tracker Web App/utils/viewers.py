from utils.core import monthly_total, category_summary, sum_transactions

# Return all transactions for a person as a list of dicts
def view_transactions(db, person_index):
    return db[person_index]['Transactions']

# Return all passbook entries for a person as a list of dicts
def view_passbook(db, person_index):
    return db[person_index].get('Passbook', [])

# Return a structured financial summary including totals, category, and monthly breakdowns
def view_summary(db, person_index):
    total_income, total_expense, current_balance = sum_transactions(db, person_index)
    category_summ = category_summary(db, person_index)
    monthly_summ = monthly_total(db, person_index)

    return {
        "TotalIncome": total_income,
        "TotalExpense": total_expense,
        "CurrentBalance": current_balance,
        "CategorySummary": category_summ,
        "MonthlySummary": monthly_summ
    }