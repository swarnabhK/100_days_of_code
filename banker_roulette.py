# Import the random module here
import random
# Split string method
names_string = input("Give me everybody's names, separated by a comma. ")
names = names_string.split(", ")
# 🚨 Don't change the code above 👆

#Write your code below this line 👇
index_picked = random.randint(0,len(names)-1)
print(f"{names[index_picked]} is going to buy the meal today!")