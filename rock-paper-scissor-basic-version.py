print("Hello, Welcome to Rock! Paper! Scissor!")
print("You have three options - rock, paper and scissor.")

user_1 = input("Enter Player 1's Choice: ")

user_2 = input("Enter Player 2's Choice: ")


# For Player 1 to win
if user_1 == "rock" and user_2 == "scissor":
    print("Player 1 Wins!")
elif user_1 == "paper" and user_2 == "rock":
    print("Player 1 Wins!")
elif user_1 == "scissor" and user_2 == "paper":
    print("Player 1 Wins!")

# For Player 2 to win
if user_1 == "rock" and user_2 == "paper":
    print("Player 2 Wins!")
elif user_1 == "paper" and user_2 == "scissor":
    print("Player 2 Wins!")
elif user_1 == "scissor" and user_2 == "rock":
    print("Player 2 Wins!")
# Play Again
if user_1 == user_2:
    print("Play Again!")