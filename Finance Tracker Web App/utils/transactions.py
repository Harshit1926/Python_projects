from utils.core import save_data, update_passbook, refresh_summary

# Add a new transaction, normalize amount sign by type, log it, and refresh the summary
def new_transaction(db, person_index, category, amount, notes, txn_type, date):

    if txn_type.lower() == "expense":
        amount = -abs(amount)
    else:
        amount = abs(amount)

    txns = db[person_index]['Transactions']
    txn = {
        "TxnIndex": len(txns) + 1,
        "Amount": amount,
        "Type": txn_type,
        "Category": category,
        "Date": date,
        "Notes": notes
    }

    txns.append(txn)

    update_passbook(db, "Transaction Added", person_index, f"{category}: {amount}")
    refresh_summary(db, person_index)
    save_data(db)

    return txn


# Remove a transaction by index, reindex remaining entries, log the deletion, and refresh the summary
def delete_transaction(db,person_index,txn_index):
    txns = db[person_index]['Transactions']

    for i, txn in enumerate(txns):
        if txn['TxnIndex'] == txn_index:
            removed = txns.pop(i)

            # reindex
            for j, t in enumerate(txns, start=1):
                t['TxnIndex'] = j

            update_passbook(db, "Transaction Deleted", person_index, f"Removed {txn_index}")
            refresh_summary(db, person_index)
            save_data(db)

            return removed

    return None