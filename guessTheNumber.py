from random import randint
logo = """  _   _                 _                  ____                     _                ____                      
 | \ | |_   _ _ __ ___ | |__   ___ _ __   / ___|_   _  ___  ___ ___(_)_ __   __ _   / ___| __ _ _ __ ___   ___ 
 |  \| | | | | '_ ` _ \| '_ \ / _ \ '__| | |  _| | | |/ _ \/ __/ __| | '_ \ / _` | | |  _ / _` | '_ ` _ \ / _ \
 | |\  | |_| | | | | | | |_) |  __/ |    | |_| | |_| |  __/\__ \__ \ | | | | (_| | | |_| | (_| | | | | | |  __/
 |_| \_|\__,_|_| |_| |_|_.__/ \___|_|     \____|\__,_|\___||___/___/_|_| |_|\__, |  \____|\__,_|_| |_| |_|\___|
                                                                            |___/                               """

generated_number = randint(1, 100)
print(logo)
print("Welcome to the number guessing game")
print("I am thinking of a number between 1 and 100.")
difficulty_choice = input("Choose a difficulty. Type 'easy' or 'hard': ")
attempts = 5 if difficulty_choice=='hard' else 10
print(f"You have {attempts} remaining to guess the number.")
while(attempts>0):
    guess = int(input("Make a guess: "))
    if(guess>generated_number):
        print("Too high")
        print("Guess again.")
    elif(guess<generated_number):
        print("Too low")
        print("Guess again.")
    else:
        print(f"You got it! The answer was {guess}")
        break
    attempts-=1
    print(f"You have {attempts} attempts remaining to guess the number.")
