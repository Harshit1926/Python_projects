from flask import Flask, render_template, request, redirect, session, flash
import webbrowser

from utils.core import log_action, recent_transactions, load_data,save_data
from utils.filters import filter_transactions, filter_summary
from utils.viewers import view_transactions, view_passbook, view_summary
from utils.transactions import new_transaction, delete_transaction
from utils.records_update import new_person, update_records, delete_person

app = Flask(__name__)
app.secret_key = "secret123"


# ---------------- HOME / LOGIN ----------------
@app.route("/", methods=["GET", "POST"])
def login():
    if request.method == "POST":
        phone = request.form["phone"]
        password = request.form["password"]

        db = load_data()
        user = next((u for u in db if u["Phone"] == phone and u["Password"] == password), None)

        if user:
            session["phone"] = phone
            session["role"] = user["Role"]

            if user["Role"] == "admin":
                return redirect("/admin")
            elif user["Role"] == "analyst":
                return redirect("/analyst")
            else:
                return redirect("/user")

        flash("Invalid phone number or password.", "danger")
        return render_template("login.html")

    return render_template("login.html")


# ---------------- USER DASHBOARD ----------------
@app.route("/user")
def user_dashboard():
    if "phone" not in session:
        return redirect("/")

    db = load_data()
    user = next(u for u in db if u["Phone"] == session["phone"])
    user_index = db.index(user)

    return render_template(
        "user.html",
        user=user,
        transactions=view_transactions(db, user_index),
        passbook=view_passbook(db, user_index),
        summary=view_summary(db, user_index),
        recent_txns=recent_transactions(db, user_index, n=5)
    )


# ---------------- ADD TRANSACTION ----------------
@app.route("/add_transaction", methods=["POST"])
def add_txn():
    if "phone" not in session:
        return redirect("/")

    db = load_data()
    user = next(u for u in db if u["Phone"] == session["phone"])
    idx = db.index(user)

    category = request.form["Category"]
    amount   = float(request.form["Amount"])
    notes    = request.form.get("Notes", "")
    txn_type = request.form["Type"]
    date     = request.form["Date"]

    new_transaction(db, idx, category, amount, notes, txn_type, date)
    flash("Transaction added successfully!", "success")
    return redirect("/user")


# ---------------- DELETE TRANSACTION ----------------
@app.route("/delete_transaction/<int:txn_id>")
def delete_txn(txn_id):
    if "phone" not in session:
        return redirect("/")

    db = load_data()
    user = next(u for u in db if u["Phone"] == session["phone"])
    idx = db.index(user)

    delete_transaction(db, idx, txn_id)
    flash("Transaction deleted successfully!", "success")
    return redirect("/user")


# ---------------- ADMIN ----------------
@app.route("/admin")
def admin():
    if session.get("role") != "admin":
        return redirect("/")

    db = load_data()
    return render_template("admin.html", users=db)


@app.route("/admin/update", methods=["POST"])
def admin_update():
    if session.get("role") != "admin":
        return redirect("/")

    db = load_data()
    phone = request.form["phone"]
    field = request.form["field"]
    value = request.form["value"]

    user = next((u for u in db if u["Phone"] == phone), None)

    if user is not None:
        idx = db.index(user)
        updated = update_records(field, value, idx, db)
        if updated:
            log_action(db, idx, "Person Updated", f"{field} changed to {value}")
            flash("Person updated successfully!", "success")
        else:
            flash(f"Invalid field '{field}' — no update made.", "danger")
    else:
        flash("Person not found!", "danger")

    return redirect("/admin")                                       


@app.route("/admin/delete", methods=["POST"])
def admin_delete():
    if session.get("role") != "admin":
        return redirect("/")

    db = load_data()
    name = request.form["name"]
    dob = request.form["dob"]
    phone = request.form["phone"]

    person_index = next(
        (i for i, u in enumerate(db) if u["Phone"] == phone),
        None
    )

    if person_index is not None:
        print(f"Stored: '{db[person_index]['Name']}' | '{db[person_index]['DOB']}'")
        print(f"Form:   '{name}' | '{dob}'")
        deleted = delete_person(name, dob, phone, db)
        print(f"Deleted: {deleted}")
        if deleted:
            save_data(db)
            flash("Person deleted successfully!", "success")
        else:
            flash("Name or DOB did not match the phone number on record.", "danger")
    else:
        flash("Person not found!", "danger")

    return redirect("/admin")


@app.route("/admin/create", methods=["POST"])
def admin_create():
    if session.get("role") != "admin":
        return redirect("/")

    db = load_data()
    new_person(
        request.form["name"],
        request.form["dob"],
        request.form["phone"],
        request.form["password"],
        db
    )
    flash("Record created successfully!", "success")
    return redirect("/admin")


# ---------------- ANALYST ----------------
@app.route("/analyst")
def analyst():
    if session.get("role") != "analyst":
        return redirect("/")

    db = load_data()
    return render_template("analyst.html", users=db)


@app.route("/filter", methods=["POST"])
def filter_data():
    if session.get("role") != "analyst":
        return redirect("/")

    db = load_data()
    phone = request.form.get("phone", "").strip()

    if not phone:
        flash("Please enter a phone number to filter.", "danger")
        return render_template("analyst.html", users=db)

    user = next((u for u in db if u["Phone"] == phone), None)

    if not user:
        flash("No user found with that phone number.", "danger")
        return render_template("analyst.html", users=db)

    idx = db.index(user)

    filtered = filter_transactions(
        db, idx,
        request.form.get("start_date"),
        request.form.get("end_date"),
        request.form.get("category"),
        request.form.get("type"),
        formatted=False
    )

    summary = filter_summary(filtered, formatted=False)

    return render_template("analyst.html", filtered=filtered, summary=summary, users=db)


# ---------------- LOGOUT ----------------
@app.route("/logout")
def logout():
    session.clear()
    return redirect("/")


# ---------------- RUN APP ----------------
if __name__ == "__main__":
    webbrowser.open_new("http://127.0.0.1:5000/")
    app.run(debug=True, use_reloader=False)