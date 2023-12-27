MENU = {
    "espresso": {
        "ingredients": {
            "water": 50,
            "coffee": 18,
        },
        "cost": 1.5,
    },
    "latte": {
        "ingredients": {
            "water": 200,
            "milk": 150,
            "coffee": 24,
        },
        "cost": 2.5,
    },
    "cappuccino": {
        "ingredients": {
            "water": 250,
            "milk": 100,
            "coffee": 24,
        },
        "cost": 3.0,
    }
}

resources = {
    "water": 300,
    "milk": 200,
    "coffee": 100,
}

money = 0

def print_report():
    global resources,money
    print(f"Water: {resources['water']}")
    print(f"Milk: {resources['milk']}")
    print(f"Coffee: {resources['coffee']}")
    print(f"Money: ${money}")


def trans_happened(water,milk,coffee):
    global resources
    resources['water']-=water
    resources['milk']-=milk
    resources['coffee']-=coffee

def trans(type):
    global money, MENU, resources
    water = MENU[type]['ingredients']['water']
    milk = MENU[type]['ingredients']['milk'] if(type!='espresso') else 0
    coffee = MENU[type]['ingredients']['coffee']
    if(resources['water']<water):
        print("Sorry there is not enough water!")
        return
    elif(type!='espresso' and resources['milk']<milk):
        print("Sorry there is not enough milk!")
        return
    elif(resources['coffee']<coffee):
        print("Sorry there is not enough coffee!")
        return
    print("Please insert coins.")
    quarters = int(input("how many quarters?: "))
    dimes = int(input("how many dimes?: "))
    nickles = int(input("how many nickels?: "))
    pennies = int(input("how many pennies?: "))
    m = quarters*0.25+dimes*0.1+nickles*0.05+pennies*0.01
    cost_esp = MENU[type]['cost']
    change = m - cost_esp
    if(change>=0):
        money+=cost_esp
        print(f"Here is your change ${round(change,2)}")
        print(f"Here is your {type}. Enjoy!")
        trans_happened(water,milk,coffee)
    else:
        print(f"Here is your change ${round(m,2)}")
        print("Sorry Not enough coins.")

def add_ingredient(ingredient):
    global resources
    amount = input(f"How much {ingredient} do you want to add(100/200/300...)? ")
    resources[ingredient]+=int(amount)

while(True):
  choice = input("What would you like? (espresso/latte/cappuccino/report/quit/add_milk,add_coffee,add_water)")
  if(choice=='report'):
      print_report()
  elif(choice=='quit'):
      exit(1)
  elif(choice=='add_milk' or choice=='add_coffee' or choice=='add_water'):
      add_ingredient(choice.split('_')[1])
  else:
      trans(choice)