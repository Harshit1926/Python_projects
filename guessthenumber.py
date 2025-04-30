title=("WELCOME TO THE GAME GUESS THE NUMBER")
print(title.center(50))

rules = """ 
RULES FOR THE GAME
1. If you guess the number in 5 or fewer attempts, you will get 100 points.
2. If you take more than 5 attempts, every extra attempt will reduce 10 points.
3. Minimum points are 0.
"""
print(rules)

import random
while True:
    number=random.randint(1,100)
    guess=None
    attempts=0
    max_points=100
    while (guess!=number):
        try: 
            guess=int(input("\nEnter your guess:"))
            
        except ValueError:
            print("Enter a valid number.")
            continue
        attempts +=1
        if (guess>number):
            print("Enter a smaller value.")
        elif(guess<number):
            print("Enter a greater value.")
        else:
            print(" Congratulations! You guessed the number!")

            if (attempts<=5):
                points=max_points
            else:
                points=min(100,max(0,100-(attempts-5)*10))
            print(f"you scored {points} points.")
            print(f" You took {attempts} attempts.") 
            
    next_round=input("do you want to play another round (yes/no):").lower()
    if (next_round!="yes"):
        print("thank you for playing.")
        break


