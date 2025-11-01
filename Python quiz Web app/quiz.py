from flask import Flask,render_template,redirect,session,flash,request,url_for
import webbrowser
import random
import os
app=Flask(__name__)
app.secret_key="MYSECRETKEY"

questions = [
    ("Which of the following is the correct extension of a Python file?",
     ["a) .py", "b) .p", "c) .python", "d) none of the above"], "a",
     "Python files use the .py extension."),

    ("Which keyword is used for defining a function in Python?",
     ["a) function", "b) func", "c) def", "d) define"], "c",
     "'def' is used for defining a function in Python."),

    ("What will be the output of the following code:\n\nx = 'abcd'\nfor i in x:\n    print(i.upper())",
     ["a) abcd", "b) error", "c) a\n   b\n   c\n   d", "d) A\n   B\n   C\n   D"], "d",
     "The loop iterates over each character, converting each one to uppercase."),

    ("Which arithmetic operator cannot be used with strings in Python?",
     ["a) +", "b) -", "c) *", "d) all of the above"], "b",
     "The + operator concatenates strings, and * repeats them, but - is not valid for string operations."),

    ("What will be the output of the following code:\n\nx = 'abcDEF'\nprint(x.capitalize())",
     ["a) Abcdef", "b) ABCDEF", "c) abc.Def", "d) none of the above"], "a",
     "The .capitalize() method makes the first letter uppercase while making the rest lowercase."),

    ("Which statement is used to create an empty set in Python?",
     ["a) {}", "b) ()", "c) set()", "d) []"], "c",
     "{} creates an empty dictionary, whereas set() correctly initializes an empty set."),

    ("Which of the following is a Python tuple?",
     ["a) (1,2,3,4)", "b) [1,2,3,4]", "c) {1,2,3,4}", "d) [1,2,3,4]"], "a",
     "Tuples are defined using parentheses (). Lists [] and sets {} are different data types."),

    ("What will be the output of the following Python code:\n\nx = 'abcd'\nfor i in range(len(x)):\n    print(x)",
     ["a) 0 1 2 3", "b) 1 2 3 4", "c) None of the Above", "d) a b c d"], "c",
     "The code prints 'abcd' four times because the loop runs for the string's length."),

    ("Which of the following Python statements will result in the output 6?\n\nA = [[1,2,3]\n[4,5,6]\n[7,8,9]]",
     ["a) A[2][1]", "b) A[1][2]", "c) A[3][2]", "d) A[2][3]"], "b",
     "In Python, lists are zero-indexed. A[1] refers to [4,5,6], and A[1][2] gives 6."),

    ("Which of the following is not a core data type in Python?",
     ["a) Tuple", "b) List", "c) Dictionary", "d) Class"], "d",
     "Python has core data types like tuples, lists, and dictionaries. Classes exist but are not core data types."),
]

@app.route("/", methods=["GET", "POST"])
def home():
    if request.method == "POST":
        name = request.form.get("name")
        age = request.form.get("age")

        if not name or not age:
            flash("Required fields can't be empty")
            return redirect(url_for('home'))

        if not name.isalpha():
            flash("Name should be in alphabets")
            return redirect(url_for('home'))

        if not age.isdigit():
            flash("Age should be an integer")
            return redirect(url_for('home'))

        session["name"] = name
        session["age"] = age
        session["score"] = 0
        session["q_idx"] = 0
        session["incorrect"] = []
        session["questions"] = random.sample(questions, len(questions))

        return redirect(url_for('quiz'))

    return render_template("home.html")

@app.route("/quiz", methods=["GET", "POST"])
def quiz():
    q_idx = session.get("q_idx", 0)
    # returns 0 if q_idx is missing
    questions_list = session.get("questions")

    if q_idx >= len(questions_list):
        return redirect(url_for("result"))

    question, options, correct, exp = questions_list[q_idx]

    if request.method == "POST":
        ans = request.form.get("answer")
        if ans == correct:
            session["score"] += 1
        else:
            session["incorrect"].append((question, exp))

        session["q_idx"] += 1

        if session["q_idx"] >= len(questions_list):
            return redirect(url_for("result"))
        return redirect(url_for("quiz"))

    return render_template("quiz.html", question=question, options=options, index=q_idx + 1)

@app.route("/result")
def result():
    name = session.get("name")
    age = session.get("age")
    incorrect = session.get("incorrect")
    score = session.get("score")

    os.makedirs("data", exist_ok=True)
    with open("data/quizinfo.txt", "a") as f:
        f.write(f"Name={name}\nAge={age}\nScore={score}/{len(questions)}\n")
        f.write("=" * 40 + "\n")

    return render_template("result.html", name=name, age=age, incorrect=incorrect, score=score, total=len(questions))

if __name__ == "__main__":
    webbrowser.open("http://127.0.0.1:5000")
    app.run(debug=True, host="127.0.0.1", port=5000, use_reloader=False)
