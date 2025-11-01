# GUESS THE NUMBER GAME - FLASK WEB APP 

A simple and interactive number guessing game built with Flask. The app challenges users to guess a randomly generated number between 1 and 100, tracks their attempts, and awards points based on performance. Perfect for beginners learning Flask, session management, and web logic.

# FEATURES

- Random number between 1 and 100
- Intelligent hints: "Enter a smaller/larger value"
- Points system based on number of attempts
- Option to play again or exit
- Session-based state tracking

# TECH STACK

#    Layer         Technology
- Backend          Python, Flask
- Frontend         HTML (via Jinja templates)
- Deployment       Localhost (auto-launch in browser)

# PROJECT STRUCTURE
Guess-the-Number/
<br>
├── guessthenumber.py
<br>
├── templates/
<br>
│ ├── guess.html
<br>
│ └── thanks2.html
<br>
├── guessthenumberReadMe.md
# HOW IT WORKS

- A random number between 1 and 100 is generated and stored in the session.
- User inputs guesses via a form.
- The app provides feedback: "Enter a smaller/larger value" or "You guessed right!"
- Points start at 100 and decrease by 10 for each attempt beyond 5.
- After guessing correctly, users can choose to play again or exit.

