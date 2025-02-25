# Task-4
# Rock-Paper-Scissors Game

import random

choices = ["rock", "paper", "scissors"]
win_logic = {"rock": "scissors", "scissors": "paper", "paper": "rock"}
score = {"You": 0, "Computer": 0}

while True:
    user = input("Rock, Paper, or Scissors? ").lower()
    if user not in choices:
        print( "Oops! That's not in the game. Pick rock, paper, or scissors!")
        continue

    comp = random.choice(choices)
    print(f"Computer chose: {comp}")

    if user == comp:
        print("It's a tie!")
    else:
        winner = "You" if win_logic[user] == comp else "Computer"
        print(f"{winner} win!")
        score[winner] += 1

    print(f"Score - You: {score['You']}, Computer: {score['Computer']}")

    if input("Play again? (y/n): ").lower() != "y":
        print("Hope you had fun! See you next time!")
        break
