from flask import Flask, redirect, request, session, url_for, flash, render_template
import webbrowser
import random

app = Flask(__name__)
app.secret_key = "your_secret_key"  # Required for session

@app.route("/", methods=["GET", "POST"])
def guess():
    if "number" not in session:
        session["number"] = random.randint(1, 100)
        session["max_point"] = 100
        session["user_points"] = 0
        session["attempts"] = 0

    inst = None
    points = session["user_points"]
    attempts = session["attempts"]
    guess = None

    if request.method == "POST":
        raw_guess = request.form.get("guess")
        if not raw_guess or not raw_guess.isdigit():
            flash("Please enter a valid number between 1 and 100.")
            return redirect(url_for("guess"))

        guess = int(raw_guess)
        if guess < 1 or guess > 100:
            flash("Enter a number between 1 and 100.")
            return redirect(url_for("guess"))

        number = session["number"]

        if guess > number:
            inst = "Enter a smaller value."
        elif guess < number:
            inst = "Enter a larger value."
        if guess == number:
            inst = "You guessed right!"
        session["attempts"] += 1
        attempts = session["attempts"]

        if attempts <= 5:
            points = 100
        else:
            points = max(0, 100 - (attempts - 5) * 10)

        session["user_points"] = points
    return render_template("guess.html", inst=inst, points=points, attempts=attempts, guess=guess)

@app.route("/again", methods=["POST"])
def again():
    if request.form.get("action") == "play again":
        session.clear()
        return redirect(url_for("guess"))
    else:
        return render_template("thanks2.html")
    

if __name__ == "__main__":
    webbrowser.open("http://127.0.0.1:5001")
    app.run(debug=True, host="127.0.0.1", port=5001,use_reloader=False)
    