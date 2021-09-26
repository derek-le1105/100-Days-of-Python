import rock_paper_scissors
import random

symbols = [rock_paper_scissors.rock, rock_paper_scissors.paper, rock_paper_scissors.scissors]
player = int(input("Type 0 for rock, 1 for paper, and 2 for scissors. "))
print(symbols[player])

computer = random.randint(0, 2)
print("Computer chooses: ")
print(symbols[computer])

if player > computer:
    if player == 2 and computer == 0:
        print("You lose!")
    else:
        print("You win!")
elif player == computer:
    print("Tie!")
elif player < computer:
    if player == 0 and computer == 2:
        print("You win!")
    else:
        print("You lose!")