import random

scissors = """
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
"""

rock = """
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
"""

paper = """
     _______
---'    ____)____
           ______)
          _______)
         _______)
---.__________)
"""

correct_guess = 0
total_guess = 0

while True:
    mychoice = input("scissors, rock, paper！")
    if mychoice == "end":
        break

    total_guess = total_guess + 1
    computer_choice = random.choice(["scissors", "rock", "paper"])

    if computer_choice == "scissors":
        print(scissors)
    elif computer_choice == "rock":
        print(rock)
    else:
        print(paper)

    if mychoice == computer_choice:
        print("this is a draw\n")
        continue
		
    win = False
    if mychoice == "scissors":
        if computer_choice == "paper":
            win = True
    elif mychoice == "rock":
        if computer_choice == "scissors":
            win = True
    elif mychoice == "paper":
        if computer_choice == "rock":
            win = True
    else:
        print("plese only chose：scissors、rock、paper、end\n")
        continue

    if win:
        correct_guess = correct_guess + 1
        print("you've win！\n")
    else:
        print("you've losed！\n")

print("you've win{0}times！your winning rate{1}%。".format(correct_guess, correct_guess / total_guess * 100.0))
