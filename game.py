import random


RPS = ["rock","paper","scissor"]

def play():
    computer_choice = random.choice(RPS)
    player_choice = input("rock paper or scissor? \n").lower()
    
    if computer_choice == player_choice:
        print(f"Its a draww!! {computer_choice} was computer choice")
    elif (computer_choice == "rock" and player_choice == "scissor") or (computer_choice == "scissor" and player_choice == "paper") or (computer_choice == "paper" and player_choice == "rock"):
        print(f"you Loose! {computer_choice} was computer choice")
    elif (computer_choice == "scissor" and player_choice == "rock") or (computer_choice == "paper" and player_choice == "scissor") or (computer_choice == "rock" and player_choice == "paper"):
        print(f"You Winn!! {computer_choice} was computer choice")
    else:
        print(f"might be an invalid input {computer_choice} was computer choice")
    
play()