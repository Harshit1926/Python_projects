# PYTHON QUIZ WEB APP

A beginner-friendly, interactive quiz web application built using Flask. This app tests users on Python fundamentals through a series of multiple-choice questions, tracks their score, and provides feedback on incorrect answers. Ideal for learners, educators, and developers exploring Flask session management and web logic.

# FEATURES

-  Randomized Python quiz questions
-  User input validation (name and age)
-  Score tracking and result summary
-  Persistent logging of quiz attempts (data/quizinfo.txt)
-  Session-based state management
-  Feedback with explanations for incorrect answers

# TECH STACK

  #  Layer         Technology
- Backend          Python, Flask
- Frontend         HTML (via Jinja templates)
- Data storage     Local file system (quizinfo.txt)
- Deployment       Localhost (auto-launch in browser)

# PROJECT STRUCTURE

python-quiz-web-app/
├── quiz.py
├── quizReadMe.md
├── templates/
│   ├── home.html
│   ├── quiz.html
│   └── result.html
├── data/
│   └── quizinfo.txt

# HOW IT WORKS

- User enters their name and age on the homepage.
- A randomized set of Python questions is served one by one.
- Each answer is validated and scored.
- Incorrect answers are logged with explanations.
- Final results are displayed and saved locally.

 # NOTES

- All quiz data is stored in memory during the session.
- Results are appended to data/quizinfo.txt for basic persistence.
- Questions are shuffled on each new session

# SAMPLE QUESTION FORMAT

(
  "Which keyword is used for defining a function in Python?",
  ["a) function", "b) func", "c) def", "d) define"],
  "c",
  "'def' is used for defining a function in Python."
)






