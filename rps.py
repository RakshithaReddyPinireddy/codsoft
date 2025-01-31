import random
def determine_winner(user_choice, computer_choice):
    if user_choice == computer_choice:
        return "It's a tie!"
    elif (user_choice == 'rock' and computer_choice == 'scissors') or(user_choice == 'scissors' and computer_choice == 'paper') or  (user_choice == 'paper' and computer_choice == 'rock'):
        return "You win!"
    else:
        return "Computer wins!"
choices = ['rock', 'paper', 'scissors']
user_score = 0
computer_score = 0
while True:
    user_choice = input("Choose rock, paper, or scissors: ").lower()
    if user_choice not in choices:
        print("Invalid choice. Please choose rock, paper, or scissors.")
        continue
    computer_choice = random.choice(choices)
    print(f"You chose: {user_choice}")
    print(f"Computer chose: {computer_choice}")
    result = determine_winner(user_choice, computer_choice)
    print(result)
    if result == "You win!":
        user_score += 1
    elif result == "Computer wins!":
        computer_score += 1
    play_again = input("Do you want to play again? (yes/no): ")
    if play_again.lower() != 'yes':
        print(f"Final Scores - You: {user_score}, Computer: {computer_score}")
        break

