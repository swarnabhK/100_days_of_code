# Generate random word, create as many blanks as the number of letters in the word, initalize the number of lives
# ask the user to guess a letter, check if letter is present in the word, if present replace blanks with the letter, check if the blanks are over if yes, they won
# if letter is guessed wrong, deduct a life, check if the no of lives have been exhausted, if exhausted lose.

import random

def read_words_from_file():
    words = []
    with open("wordlist.txt", "r") as grilled_cheese:
      lines = grilled_cheese.readlines()
      for word in lines:
         words.append(word.split("\n")[0])
    return words

def hangMan():
  stages = ['''
  +---+
  |   |
  O   |
 /|\  |
 / \  |
      |
=========
''', '''
  +---+
  |   |
  O   |
 /|\  |
 /    |
      |
=========
''', '''
  +---+
  |   |
  O   |
 /|\  |
      |
      |
=========
''', '''
  +---+
  |   |
  O   |
 /|   |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
  |   |
      |
      |
=========
''', '''
  +---+
  |   |
  O   |
      |
      |
      |
=========
''', '''
  +---+
  |   |
      |
      |
      |
      |
=========
''']
  word_list = read_words_from_file()
  chosen_word = word_list[random.randint(0,len(word_list)-1)]
  blank_word = ['-']*len(chosen_word)
  no_blanks = len(blank_word)
  lives = 7
  print(blank_word)
  print("The chosen word is: ",chosen_word)
  seen_letters = set()
  while(True):
    guess = input("Guess a letter: ").lower()
    if(guess in chosen_word and guess not in seen_letters):
        indices_list = []
        seen_letters.add(guess)
        indices_list = [(guess,i) for i,a in enumerate(chosen_word) if a==guess]
        for word in indices_list:
            blank_word[word[1]] = word[0]
            no_blanks-=1
        print(blank_word)
        print("No of blanks is: ",no_blanks)
        if(no_blanks==0):
            return "Congratulations! You won the game."
    else:
        lives-=1
        print(f"You guessed wrong! You have {lives} lives left ")
        print(stages[lives])
        if(lives==0):
            return "Sorry but you lost the game!"
    

print(hangMan())
