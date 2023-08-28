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

#Write your code below this line 👇
game_images = [rock,paper,scissors]
user_choice=int(input("What do you want to choose? 0 for Rock, 1 for paper, 2 for scissors\n"))
print(game_images[user_choice])
computer_choice = random.randint(0,2)
print(f"Computer chose : {computer_choice}")
print(game_images[computer_choice])

# if(user_choice==0):
#     if(computer_choice==0):
#         print("Draw")
#     elif(computer_choice==1):
#         print("computer win")
#     else:
#         print("user win")
# elif(user_choice==1):
#     if(computer_choice==0):
#         print("User win")
#     elif(computer_choice==1):
#         print("draw")
#     else:
#         print("computer win")
# else:
#     if(computer_choice==0):
#         print("computer win")
#     elif(computer_choice==1):
#         print("user win")
#     else:
#         print("draw")

#User win options - 10, 0 2 , 2 1
#computer win options - 01, 12, 20

if(user_choice==0 and computer_choice==2):
    print("You win")
elif(computer_choice==0 and user_choice==2):
    print("You lose")
elif(user_choice> computer_choice):
    print("You win")
elif(computer_choice> user_choice):
    print("You lose")
elif(computer_choice==user_choice):
    print("It's a draw")
elif(user_choice>2 or user_choice<0):
    print("Invalid number added")
