from enum import Enum
import random
import sys

class RPS(Enum):
    ROCK = 1
    PAPER = 2
    SISSORS = 3

print("")
playerchoice = input("Please enter...\n1 for Rock,\n2 for Paper,\n3 for Sissors\n\n")
player = int(playerchoice)
computerchoice = random.choice("123")
computer = int(computerchoice)

print("You chose: " + str(RPS(player)).replace("RPS.",""))
print("Computer chose: " + str(RPS(computer)).replace("RPS.",""))

if player > 3 | player < 1:
    sys.exit("Please enter only 1, 2 or 3")

if player == 1 and computer == 3:
    print("Taylor wins")
elif player == 2 and computer == 1:
    print("Taylor wins")
elif player == 3 and computer == 2:
    print("Taylor wins")
elif player == computer:
    print("Tie game!")
else:
    print("Computer wins")
