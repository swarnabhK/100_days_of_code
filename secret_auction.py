import os
#HINT: You can call clear() to clear the output in the console.
logo = '''
                         ___________
                         \         /
                          )_______(
                          |"""""""|_.-._,.---------.,_.-._
                          |       | | |               | | ''-.
                          |       |_| |_             _| |_..-'
                          |_______| '-' `'---------'` '-'
                          )"""""""(
                         /_________\\
                       .-------------.
                      /_______________\\
'''
print(logo)
print("Welcome to the secret auction program")
bidders = {}
while (True):
    name = input("What is your name?: ")
    bid = input("What is your bid?: ")
    bidders[name] = int(bid)
    choice = input("Are there any other bidders? Type 'yes' or 'no': ")
    if (choice == 'yes'):
        os.system('cls')
        continue
    elif (choice == 'no'):
        os.system('cls')
        max_bid = 0
        winner = ""
        for bidder in bidders:
            if (int(bidders[bidder]) > max_bid):
                max_bid = bidders[bidder]
                winner = bidder
        print(f"The winner is {winner} with a bid of ${max_bid}")
        break