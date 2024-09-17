import random

def game():

    choices = ["rock", "paper", "scissors"]
    outcomes = {
        "rock" : "scissors", # rock beats scissors
        "paper" : "rock", # paper beats rock
        "scissors" : "paper" # scissors beat paper
    }

    user_choice = input("Choose rock, paper or scissors: ").lower() # .lower() converts everything to lower case to match up with the choices in the list

    if user_choice not in choices:
        print("Invalid choice. Please choose rock, paper or scissors.")
        return
    
    computer_choice = random.choice(choices)
    print(f"The computer chose: {computer_choice}")

    if user_choice == computer_choice:
        print("It's a draw!")
    
    elif outcomes[user_choice] == computer_choice:
        print("You win!")

    else:
        print("Computer wins!")

game()
