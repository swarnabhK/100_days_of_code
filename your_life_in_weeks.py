# 🚨 Don't change the code below 👇
age = input("What is your current age? ")
# 🚨 Don't change the code above 👆

#Write your code below this line 👇

days_left = 90*365 - int(age)*365
weeks_left = 90*52 - int(age)*52
months_left = 90*12 - int(age)*12

print(f"You have {days_left} days, {weeks_left} weeks, and {months_left} months left.")