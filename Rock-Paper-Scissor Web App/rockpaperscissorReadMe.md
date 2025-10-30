# ROCK-PAPER-SCISSOR WEB APP

A Flask-powered Rock-Paper-Scissors game where the player competes against the computer in a best-of-three format. The game features interactive web-based gameplay, session-based score tracking, and dynamic result rendering.

# FEATURES

  Web-based interactive gameplay using Flask

  Session management to track rounds and scores

  Randomized computer moves for fairness

  Score tracking across three rounds

  Replay option after each match

  Session reset after game completion


# HOW TO PLAY

- Run the app:
    python rockpaperscissor.py
    The game will auto-launch in your browser at http://127.0.0.1:5002.

- Choose your move:
    - Rock
    - Paper
    - Scissors

- Play three rounds:
    - Each round compares your move with the computer's.
    - Scores are updated after each round.

- View final result:
    - After round 3, the game declares the winner.
    - You can choose to play again or exit.

# TECH STACK
- Python 3
- Flask
- HTML Templates (game.html, result2.html, final.html, thanks.html)
- Session API for stateful gameplay


# NOTES
- The app uses session.clear() to reset game state after completion.
- Secret key (IamBatman) is used for session encryption — replace it in production.
- Port 5002 is used for local hosting.
