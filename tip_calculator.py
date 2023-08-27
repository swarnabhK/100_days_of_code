#If the bill was $150.00, split between 5 people, with 12% tip. 

#Each person should pay (150.00 / 5) * 1.12 = 33.6
#Format the result to 2 decimal places = 33.60
#Tip: There are 2 ways to round a number. You might have to do some Googling to solve this.💪

#Write your code below this line 👇

bill = input("What is the total bill amount(in $)?\n")
tip = input("What percentage tip would you like to give? 10, 12 or 15?\n")
people = input("How many people is this bill divided into?\n")

split_per_person = round(((int(tip)/100)*float(bill)+float(bill))/int(people),2)
print("Each person should pay: {:.2f}".format(split_per_person))