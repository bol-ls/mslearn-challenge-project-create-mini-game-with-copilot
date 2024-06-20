# Rock, paper scissors game - A game played through the terminal
    
# Import random module
import random

# Initialize players score
player_score = 0

# Start loop
while True:
    # Create a list of play options
    play = ["rock", "paper", "scissors"]

    # Assign a random play to the computer
    computer = random.choice(play)

    # Prompt the user to select rock, paper, or scissors
    player = input("Rock, Paper, Scissors? ").lower()

    # Check if the player choose a valid option
    if player not in play:
        print("Invalid choice. Please try again.")
        continue

    # Find out who won
    if player == computer:
        print("Tie!")
    elif player == "rock":
        if computer == "scissors":
            print("You win! Rock smashes scissors.")
            player_score += 1
        else:
            print("You lose! Paper covers rock.")
    elif player == "paper":
        if computer == "rock":
            print("You win! Paper covers rock.")
            player_score += 1
        else:
            print("You lose! Scissors cuts paper.")
    elif player == "scissors":
        if computer == "paper":
            print("You win! Scissors cuts paper.")
            player_score += 1
        else:
            print("You lose! Rock smashes scissors.")

    # Ask the player if they want to play again
    play_again = input("Do you want to play again? (yes/no) ").lower()

    # Check if the player wants to play again
    if play_again != "yes":
        print(f"Thanks for playing! Your score is {player_score}.")
        break


