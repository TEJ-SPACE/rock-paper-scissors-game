'''
Write a python program capable of playing 'rock, paper, scissors' game with the user.
'''
import random
user_choice = input("Choose rock, paper or scissors: ")

def game(user_choice):
    l = ["rock", "paper", "scissors"] # creates a list containing rock, paper, scissors as separate values
    computer_choice = random.choice(l) # chooses a random value from the list
    if user_choice == computer_choice:
        print(f"The computer chose {computer_choice}. It's a draw!")
    elif user_choice != computer_choice:
        if user_choice == "rock" and computer_choice == "paper":
            print(f"The computer chose {computer_choice}, which covers {user_choice}.")
            print("Computer Wins!")
        elif user_choice == "rock" and computer_choice == "scissors":
            print(f"The computer chose {computer_choice}, which gets destroyed by {user_choice}")
            print("User Wins!")
        elif user_choice == "paper" and computer_choice == "rock":
            print(f"The computer chose {computer_choice}, which gets covered by {user_choice}")
            print("User Wins!")
        elif user_choice == "paper" and computer_choice == "scissors":
            print(f"The computer chose {computer_choice}, which cuts {user_choice}")
            print("Computer Wins!")
        elif user_choice == "scissors" and computer_choice == "rock":
            print(f"The computer chose {computer_choice}, which destroys {user_choice}")
            print("Computer Wins!")
        elif user_choice == "scissors" and computer_choice == "paper":
            print(f"The computer chose {computer_choice}, which gets cut by {user_choice}")
            print("User Wins!")

game(user_choice)



  