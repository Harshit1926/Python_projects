import random
title="ROCK PAPER SCISSORS"
print(title.center(50))
moves="""
1. CHOOSE 1 FOR ROCK
2. CHOOSE 2 FOR PAPER
3. CHOOSE 3 FOR SCISSORS
"""
print(moves)

def start_game():
    choices=[1,2,3]
    computer_choice=random.randint(1,3)

    while True:
        try:
            user_choices=int(input("Enter your move:"))
            if (user_choices not in [1,2,3]):
                print("Enter a valid number from [1,2,3].")
                continue
            break
        except ValueError:
            print("Enter a valid number")
       
    print(f"Computer chooses {computer_choice}")
    if(user_choices==computer_choice):
        print("It is a draw")
        return None
    elif(user_choices==1 and computer_choice==3 or\
        user_choices==2 and computer_choice==1 or\
        user_choices==3 and computer_choice==2):
        print("You Won!")
        return "user"
    else:
        print("Computer Won!")
        return "computer"
def win():
    user_win=0
    computer_win=0

    for round_win in range (1,4):
        print(f"Round {round_win}")
        winner=start_game()
        if (winner is None):
            continue
        if (winner=="user"):
            user_win+=1
        elif(winner=="computer"):
            computer_win+=1
        
    print("\nFINAL RESULT:")   
     
    if(user_win>computer_win):
        print("Congratulations! You Won the Game")
    elif(computer_win>user_win):
        print("Computer Won the Game!")
    elif(user_win==computer_win):
        print("It's a Draw")

while True:
    win()
    another_round = input("Do you want to play another round (yes/no): ").lower()
    if another_round != "yes":
        print("Thank you for playing this game.")
        break
