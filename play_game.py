import random

def play_game():
  
  user_choice = input("Rock, paper, or scissors? ")

  
  computer_choice = random.choice(["rock", "paper", "scissors"])

  
  if user_choice == computer_choice:
    print("Tie!")
  elif user_choice == "rock" and computer_choice == "scissors":
    print("You win!")
  elif user_choice == "paper" and computer_choice == "rock":
    print("You win!")
  elif user_choice == "scissors" and computer_choice == "paper":
    print("You win!")
  else:
    print("Computer wins!")


play_game()
