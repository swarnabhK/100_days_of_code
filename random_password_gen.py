#Password Generator Project
import random
letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

print("Welcome to the PyPassword Generator!")
nr_letters= int(input("How many letters would you like in your password?\n")) 
nr_symbols = int(input(f"How many symbols would you like?\n"))
nr_numbers = int(input(f"How many numbers would you like?\n"))

#Eazy Level - Order not randomised:
#e.g. 4 letter, 2 symbol, 2 number = JduE&!91
let = ''
sym=''
num = ''

iter = max(nr_letters,nr_symbols,nr_numbers)
for i in range(0,iter):
    if(i<=nr_letters-1):
      rand_ind = random.randint(0,len(letters)-1)
      let+=letters[rand_ind]
    if(i<=nr_symbols-1):
      rand_ind = random.randint(0,len(symbols)-1)
      sym+=symbols[rand_ind]
    if(i<=nr_numbers-1):
      rand_ind = random.randint(0,len(numbers)-1)
      num+=numbers[rand_ind]

combined = let+sym+num
print("Easy password is: ",combined)

#Hard Level - Order of characters randomised:
#e.g. 4 letter, 2 symbol, 2 number = g^2jk8&P

randomized_password = list(combined)
random.shuffle(randomized_password)
print("Hard level password :"+"".join(randomized_password))