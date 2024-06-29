
import random

def play_again():
  while True:
    answer = input("Do you want to play again? (yes/no): ").lower()
    if answer in ("yes", "no"):
      return answer == "yes"
    else:
      print("Invalid input. Please enter 'yes' or 'no'.")

def main():
  user_score = 0
  computer_score = 0

  while True:
    
    user_choice = input("Choose rock, paper, or scissors: ").lower()
    valid_choices = ["rock", "paper", "scissors"]
    if user_choice not in valid_choices:
      print("Invalid choice. Please choose rock, paper, or scissors.")
      continue

   
    computer_choice = random.choice(valid_choices)

    if user_choice == computer_choice:
      print(f"You chose {user_choice} and computer chose {computer_choice}. It's a tie!")
    elif (user_choice == "rock" and computer_choice == "scissors") or \
         (user_choice == "paper" and computer_choice == "rock") or \
         (user_choice == "scissors" and computer_choice == "paper"):
      print(f"You chose {user_choice} and computer chose {computer_choice}. You win!")
      user_score += 1
    else:
      print(f"You chose {user_choice} and computer chose {computer_choice}. You lose.")
      computer_score += 1

   
    print(f"Your score: {user_score}, Computer score: {computer_score}")

    if not play_again():
      break

  print("Thanks for playing!")

if __name__ == "__main__":
  main()

