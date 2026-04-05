from utils.core import update_passbook, save_data
from datetime import datetime

# Create a new person record if phone number isn't already registered, then persist to disk
def new_person(name, DOB, phone_number, password, db):
    for user in db:
        if user["Phone"] == phone_number:
            return "User already exists"
    person = {
        "Name": name,
        "DOB": DOB,
        "Phone": phone_number,
        "Password": password,
        "Role": "viewer",
        "Transactions": [],
        "Summary": {
            "TotalIncome": 0,
            "TotalExpenses": 0,
            "CurrentBalance": 0,
            "CategoryBreakdown": {},
            "MonthlyTotals": {},
            "RecentActivity": []
        },
        "Passbook": [{
            "Timestamp": datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
            "Action": "Person Created",
            "Details": f"{name} registered"
        }]
    }

    db.append(person)
    save_data(db)
    return person


# Update a single allowed field (name, dob, phone) for a person by index and log the change
def update_records(choice, new_value, index, db):
    field_map = {"name": "Name", "dob": "DOB", "phone_number": "Phone"}
    col = field_map.get(choice.lower())

    if col:
        db[index][col] = new_value
        update_passbook(db, "Record Updated", index, f"{col} changed to {new_value}")
        save_data(db)
        return True

    return False


# Delete a person matched by name, DOB, and phone; log the deletion before removing
def delete_person(name, dob, phone, db):
    for i, person in enumerate(db):
        if person["Name"] == name and person["DOB"] == dob and person["Phone"] == phone:
            update_passbook(db, "Record Deleted", i, f"{name} with DOB {dob} and phone {phone} deleted")
            db.pop(i)
            save_data(db)
            return True
    return False