from random import randint
# welcome message

print("Rock...")
print("Paper...")
print("Scissors...")

player = input("(Enter your choice): ").lower()
computer = randint(0, 2)
if computer == 0:
    computer = "rock"
elif computer == 1:
    computer = "paper"
else:
    computer = "scissors"

print(f"The computer plays: {computer}")

if player == computer:
    print("It's a tie!")
elif player == "rock":
    if computer == "scissors":
        print("Player 1 wins!")
    elif computer == "paper":
        print("Computer wins!")
elif player == "paper":
    if computer == "rock":
        print("Player 1 wins!")
    elif computer == "scissors":
        print("Computer wins!")
elif player == "scissors":
    if computer == "paper":
        print("Player 1 wins!")
    elif computer == "rock":
        print("Computer wins!")
else:
    print("Something went wrong, please try again.")