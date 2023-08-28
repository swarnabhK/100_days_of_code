# 🚨 Don't change the code below 👇
print("Welcome to the Love Calculator!")
name1 = input("What is your name? \n")
name2 = input("What is their name? \n")
# 🚨 Don't change the code above 👆

#Write your code below this line 👇

#Method 1
print("Method 1 of calculating the score")
combo = (name1+name2).lower().replace(" ","")
total1 = 0
total2 = 0
for s in combo:
    if(s in "TRUE".lower()):
          total1+=1
    if(s in "LOVE".lower()):
          total2+=1
score = int(str(total1)+str(total2))
if(score<10 or score>90):
     print(f"Your score is {score}, you go together like coke and mentos.")
elif(score>=40 and score<=50):
     print(f"Your score is {score}, you are alright together.")
else:
     print(f"Your score is {score}")


## Method 2
print("Method 2 of calculating the score")
total1 = name1.lower().count("t") + name1.lower().count("r") + name1.lower().count("u")+ name1.lower().count("e") + name2.lower().count("t") + name2.lower().count("r") + name2.lower().count("u")+ name2.lower().count("e")
total2 = name1.lower().count("l") + name1.lower().count("o") + name1.lower().count("v")+ name1.lower().count("e") + name2.lower().count("l") + name2.lower().count("o") + name2.lower().count("v")+ name2.lower().count("e")
score = int(str(total1)+str(total2))

if(score<10 or score>90):
     print(f"Your score is {score}, you go together like coke and mentos.")
elif(score>=40 and score<=50):
     print(f"Your score is {score}, you are alright together.")
else:
     print(f"Your score is {score}")