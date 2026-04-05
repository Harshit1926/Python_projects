from datetime import datetime

# Try parsing a date string against known formats; raise ValueError if none match
def parse_date(date_str):
    for fmt in ("%Y-%m-%d %H:%M:%S", "%Y-%m-%d"):
        try:
            return datetime.strptime(date_str, fmt)
        except ValueError:
            continue
    raise ValueError(f"Unrecognised date format: {date_str}")

def filter_transactions(db, person_index, start_date=None, end_date=None, category=None, txn_type=None, formatted=False):
    txns = db[person_index]['Transactions']
    if not isinstance(txns, list) or not txns:
        return "No transactions found." if formatted else []

    results = list(txns)

    # Date filters
    if start_date:
        start_dt = parse_date(start_date)
        results = [t for t in results if parse_date(t['Date']) >= start_dt]

    if end_date:
        end_dt = parse_date(end_date)
        results = [t for t in results if parse_date(t['Date']) <= end_dt]

    # Category filter
    if category and category.strip():
        results = [t for t in results if t['Category'].lower() == category.strip().lower()]

    # Type filter
    if txn_type and txn_type.strip():
        results = [t for t in results if t['Type'].lower() == txn_type.strip().lower()]

    # Handle empty results
    if not results:
        return "No transactions found for given filters." if formatted else []

    # Optional formatted output
    if formatted:
        result = "Index | Amount | Type | Category | Date | Notes\n"
        result += "-" * 70 + "\n"
        for txn in results:
            result += f"{txn.get('TxnIndex', '?')} | {txn['Amount']} | {txn['Type']} | {txn['Category']} | {txn['Date']} | {txn['Notes']}\n"
        return result

    return results

# Summarize income, expense, and balance from a transaction list;
# returns a formatted string if formatted=True, else a raw dict
def filter_summary(txns, formatted=True):
    if not txns:
        return "No transactions found for summary." if formatted else {
            "TotalIncome": 0,
            "TotalExpense": 0,
            "Balance": 0
        }

    total_income  = sum(abs(t['Amount']) for t in txns if t['Type'].lower() == 'income')
    total_expense = sum(abs(t['Amount']) for t in txns if t['Type'].lower() == 'expense')
    balance       = total_income - total_expense

    if formatted:
        return (
            f"Total Income: {total_income}\n"
            f"Total Expense: {total_expense}\n"
            f"Balance: {balance}"
        )
    else:
        return {
            "TotalIncome": total_income,
            "TotalExpense": total_expense,
            "Balance": balance
        }