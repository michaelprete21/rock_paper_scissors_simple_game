"""Rock Paper Scissors Game"""

import random

rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''

rps = [rock, paper, scissors]
computer_choice_int = random.randint(0,2)

my_choice = input("Do you choose rock, paper, or scissors?").lower()
print("\nPlayer 1\n")
if my_choice == "rock":
    print(rps[0])
    my_choice_int = 0
elif my_choice == "paper":
    print(rps[1])
    my_choice_int = 1
elif my_choice == "scissors":
    print(rps[2])
    my_choice_int = 2
else:
    print("\nPlease choose a valid choice\n")
    my_choice_int = 10

print("Computer\n")
print(rps[computer_choice_int])

if my_choice_int == computer_choice_int:
    print("This is a draw!")
elif my_choice_int == 0 and computer_choice_int == 1:
    print("Paper beats rock, you lose!")
elif my_choice_int == 1 and computer_choice_int == 0:
    print("Paper beats rock, you win!")
elif my_choice_int == 0 and computer_choice_int == 2:
    print("Rock beats scissors, you win!")
elif my_choice_int == 2 and computer_choice_int == 0:
    print("Rock beats scissors, you lose!")
elif my_choice_int == 1 and computer_choice_int == 2:
    print("Scissors beat paper, you lose!")
elif my_choice_int == 2 and computer_choice_int == 1:
    print("Scissors beat paper, you win!")
else:
    print("Please check your input. You did not enter a valid response. \nBe "
          "sure to leave out any spaces.")

