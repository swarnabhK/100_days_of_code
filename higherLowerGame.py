from art import logo,vs
from gameData import data
import random

def highLow(a,b):
  #print the initial logo
  print(logo)
  #variable to track the final score.
  score = 0
  while(True):
      print(f"Compare A: {a['name']}, a {a['description']}, from {a['country']}.")
      print(vs)
      print(f"Compare B: {b['name']}, a {b['description']}, from {b['country']}.")
      choice = input("Who has more followers? Type 'A' or 'B': ")
      if(choice=='A' and a['follower_count']>b['follower_count']):
          score+=1
          print(f"You are right! Current score: {score}")
      elif(choice=='B' and b['follower_count']>a['follower_count']):
          score+=1
          print(f"You are right! Current score: {score}")
      else:
          print(f"Sorry that's wrong! Your final score is {score}")
          break
      
      #When answer is right and we need new A and B
      a = b

      #while loop to make sure that a and b aren't the same.
      while(b==a):
          b = data[random.randint(0,49)]
        

#two initial random A and B
rn = random.sample(range(50), 2)
a = data[rn[0]]
b = data[rn[1]]
highLow(a,b)