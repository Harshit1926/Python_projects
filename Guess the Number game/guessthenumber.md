# GUESS THE NUMBER GAME

This is a number-guessing game where the player tries to guess a randomly generated number between 1 and 100. Here's a breakdown to help you upload it with a well-structured GitHub README:

# FEATURES

1. Hints to guide the player (higher or lower)

2. Scoring System that rewards quick guesses

3. Replay Option for continuous gameplay

4. Error Handling for invalid inputs

# RULES

1. You will get 100 points if guessed within 5 attempts.

2. If more than 5 attempts are taken, the score is adjusted using:

3. python points = min(100, max(0, 100 - (attempts - 5) * 10))

# HOW TO PLAY

1. Run the script in a Python environment.

2. Enter a number between 1 and 100.

3. The game will provide hints (higher or lower) to refine your guesses.

4. Your score depends on the number of attempts taken.

5. Play multiple rounds if you wish!