# Python_projects

# FIRST PROJECT

Python Quiz Game

A simple Python-based quiz application designed to test programming knowledge through interactive multiple-choice questions. This project features randomized questions, answer validation, score tracking, and explanations for incorrect answers, making it both engaging and educational.

# FEATURES

1. Randomized Questions: Shuffles questions dynamically for varied gameplay.

2. Multiple-Choice Format: Offers four answer options for each question.

3. Answer Validation & Scoring: Provides instant feedback and tracks correct responses.

4. Explanation for Mistakes: Displays the correct answer and reasoning when an incorrect response is given.

5. User-Friendly Interaction: Simple text-based interface allowing smooth user input handling

# HOW TO PLAY

1. Run the script in a Python environment
  
2. Answer each question by typing a, b, c, or d.
   
3. Get immediate feedback correct answers increase your score, while incorrect answers include explanations.
   
4. At the end, see your Final score and review your mistakes.



------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

# SECOND PROJECT

Secret Code Generator & Decoder

A Python program that encrypts and deciphers text using a simple character manipulation technique. Words are transformed based on their length, ensuring a unique encoding pattern. The project demonstrates proficiency in string manipulation, conditional logic, and user interaction.

# FEATURES

1. Custom Encoding & Decoding: Encrypts text using predefined logic and restores it accurately.

2. Word-Based Transformation: Adjusts structure based on word length for added complexity.

3. User-Friendly Input Handling: Allows interactive text encryption and decryption.

# ENCODING RULES

Words with 3 or more letters are modified:
  
  1. A prefix (ghf) is added.
  
  2. The first letter moves to the end.
  
  3. A suffix (hhv) is added.
  
  4. Example: "hello" → "ghfellohhv".
  
  5. Short words are reversed.

#  DECODING RULES

1. The transformation is reversed for encoded words

2. Short words are flipped back to their original form.

# HOW TO USE

1. Run the script.
   
2. Choose:
     1 to encode a message.
     2 to decode a message.
   
3. Enter the text.
   
4. The program converts and displays the result.

------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

# THIRD PROJECT

Rock-Paper-Scissors Game

A Python-based Rock-Paper-Scissors game where the player competes against the computer in a best-of-three format. The game implements input validation, a loop for multiple rounds, and score tracking.

# FEATURES

1. Interactive gameplay with user input validation

2. Randomized computer moves

3. Score tracking for both the player and computer

4. Replay option for continuous gameplay

# HOW TO PLAY

1. Run the script in a Python environment.

2. Choose your move:
    1 for Rock
    2 for Paper
    3 for Scissors
   
4. The game runs three rounds, determining the final winner.

5. You can play again after finishing a match.
   
------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

# FOURTH PROJECT

Number Guessing Game

This is a number-guessing game where the player tries to guess a randomly generated number between 1 and 100. Here's a breakdown to help you upload it with a well-structured GitHub README:

# FEATURES

1. Hints to guide the player (higher or lower)

2. Scoring System that rewards quick guesses

3. Replay Option for continuous gameplay

4. Error Handling for invalid inputs

# RULES

1. You will get 100 points if guessed within 5 attempts.

2. If more than 5 attempts are taken, the score is adjusted using:

python
points = min(100, max(0, 100 - (attempts - 5) * 10))

# HOW TO PLAY

1. Run the script in a Python environment.

2. Enter a number between 1 and 100.

3. The game will provide hints (higher or lower) to refine your guesses.

4. Your score depends on the number of attempts taken.

5. Play multiple rounds if you wish!

------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

# FIFTH PROJECT

Unit Convereter in Python

A simple yet powerful Python-based unit converter that allows users to convert length, weight, and temperature units interactively via the console.

# FEATURES

1. Converts between multiple units of:
   
2. Length: meters, kilometers, miles, feet, centimeters

3. Weight: grams, kilograms, pounds, ounce, short ton

4. Temperature: Celsius, Fahrenheit, Kelvin

# HOW IT WORKS

1. Upon running the program, you’re greeted with a neat title and menu to choose the type of conversion.
   
2. The program takes your input value along with source and target units.
   
3. It performs internal mapping using dictionaries (for length & weight) and well-defined formulas (for temperature).
   
4. Final result is printed in a readable format.

------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

# SIXTH PROJECT
 
 Multi-Stock Price Visualizer with Moving Average

This Python project fetches historical data for multiple stocks (AAPL, META, TSLA) using `yfinance`, and visualizes both their closing prices and 20-day moving averages over time.

# FEATURES

1. Uses yfinance to collect daily stock data between user-defined dates

2. Calculates a 20-day simple moving average for each stock
   
3. Plots both closing prices and trendlines with Matplotlib
   
4. Assigns distinct color schemes for better visual differentiation
   
5. Prints latest closing vs average prices for a quick market snapshot

# TECH STACK
1. Python (3.11.3)
   
2. pandas (2.2.2)
  
3. yfinance (0.2.37)

4. matplotlib (3.8.4)

# OUTPUT

The plot includes labeled trendlines, legends, and a clean layout, making it suitable for presentation or financial analysis dashboards.


# ABBREVIATIONS

   COMPANY    -   TICKER SYMBOL
   
1.  Apple     -      AAPL
              
2.  Meta      -        META  
              
3.  Tesla     -        TSLA
