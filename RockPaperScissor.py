from random import random

game_images = ["rock", "paper", "scissors"]

user_choice = int(input("What dou oy choose? Type 0 for Rock, 1 for paper or 2 for scissors\n"))
print(game_images[user_choice])

computer_choice = random.randint(0, 2)
print(f"Computer chose: ")
print(game_images[computer_choice])

if user_choice >= 3 or user_choice < 0:
    print("You typed an invalid number. You lose!")
elif user_choice == 0 and computer_choice == 2:
    print("You won!")
elif user_choice == 0 and computer_choice == 2:
    print("You lost!")
elif computer_choice > user_choice:
    print("You lost!")
elif computer_choice < user_choice:
    print("You won!")
elif computer_choice == user_choice:
    print("It is draw")
