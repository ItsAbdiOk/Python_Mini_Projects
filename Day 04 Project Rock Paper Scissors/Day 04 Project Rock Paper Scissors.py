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
user_choice = int(input("What do you choose? Type 0 for Rock , 1 for Paper or 2 for Scissors."))
if user_choice == 0:
    print(rock)
    print("you chose rock ")

elif user_choice == 1:
    print(paper)
    print("you chose paper ")
elif user_choice == 2:
    print(scissors)
    print("you chose scissors ")


Computer_chose = random.randint(0,2)
if Computer_chose == 0:
    print(rock)
    print("Computer chose rock ")

elif Computer_chose == 1:
    print(paper)
    print("Computer chose paper ")

elif Computer_chose == 2:
    print(scissors)
    print("Computer chose scissors ")


if user_choice >= 3 or user_choice < 0: 
  print("You typed an invalid number, you lose!") 
elif user_choice == 0 and Computer_chose == 2:
  print("You win!")
elif Computer_chose == 0 and user_choice == 2:
  print("You lose")
elif Computer_chose > user_choice:
  print("You lose")
elif user_choice > Computer_chose:
  print("You win!")
elif Computer_chose == user_choice:
  print("It's a draw")