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
game_images=[rock,paper,scissors]
user_choose=int(input("What do you choose? Type 0 for Rock, 1 for Paper or 2 for Scissors.\n"))
computer_choose=random.randint(0,2)
if(user_choose>=3 or user_choose<0):
    print("You typed an invalid number, you lose!")
else:
    print(game_images[user_choose])

    print(f"Computer chose:")
    print(game_images[computer_choose])

    if(user_choose==0 and computer_choose==2):
        print("You win!")
    elif(computer_choose>user_choose):
        print("You lose")
    elif(user_choose>computer_choose):
        print("You win!")
    elif(computer_choose==user_choose):
        print("It's a draw")
    elif(computer_choose==0 and user_choose==2):
        print("You lose")
