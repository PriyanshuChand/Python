
print("Hello, Welcome to Rock! Paper! Scissor!")
print("You have three options - rock, paper and scissor.")

user_1 = input("Enter Player 1's Choice: ")

user_2 = input("Enter Player 2's Choice: ")

# Player 1 and Player 2 choose same option.
if user_1 == user_2:
    print("Play Again!")

# If Player 1 Chooses rocks
elif user_1 == "rock": 
    if user_2 == "scissor":
        print("Player 1 Wins!")
    elif user_2 == "paper":
        print("Player 2 Wins!")
    else:
        print("Please Player 2, enter correct choice.")

# If Player 1 Chooses paper
elif user_1 == "paper":
    if user_2 == "scissor":
        print("Player 2 Wins!")
    elif user_2 == "rock":
        print("Player 1 Wins!")
    else:
        print("Please Player 2, enter correct choice.")

# If Player 1 Chooses scissor
elif user_1 == "scissor":
    if user_2 == "paper":
        print("Player 1 Wins!")
    elif user_2 == "rock":
        print("Player 2 Wins!")
    else:
        print("Please Player 2, enter correct choice.")


# If Players enter anything else other than correct options.

else:
    print("Please Player 1, enter correct choice.")