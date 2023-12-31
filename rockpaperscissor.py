from random import randint

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

scissor = '''
      ____
  / __ \
 ( (__) |___ ___
  \________,'   """""----....____
   _______<  () dd       ____----'
  / __   __`.___-----""""
 ( (__) |
  \____/

'''

game_images = [rock, paper, scissor]
user_choice = int(input("What do you choose? Type 0 for Rock, 1 for Paper or 2 for Scissors "))
computer_choice = randint(0, 2)
if user_choice >= 0 and user_choice <= 2:
  print(game_images[user_choice])
  print("computer_choice chose:")
  print(game_images[computer_choice])
else:
  print("game_images does not exist!")


if user_choice >= 3 and user_choice < 0:
  print("You typed an invalid number, you lose!")
elif user_choice == 0 and computer_choice == 2:
  print("You win!")
elif user_choice == 2 and computer_choice == 0:
  print("You lose!")
elif computer_choice > user_choice:
  print("You lose!")
elif user_choice > computer_choice:
  print("You win!")
elif user_choice == computer_choice:
  print("It's a draw.")
