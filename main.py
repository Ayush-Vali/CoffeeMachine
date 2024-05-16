

#machine needs to have a report

#seperated menu cause it will help in selecting those item easily

ingredients = {
    "Milk": 500,
    "Water": 800,
    "Coffee_powder": 30,
}

espresso = {
    "Milk": 0,  # cause function findleft is common for every coffee
    "Water": 50,
    "Coffee_powder": 18,
    "Coins": 1.5,
}

latte = {
    "Water": 200,
    "Milk": 150,
    "Coffee_powder": 24,
    "Coins": 2.5,
}

cappuccino = {
    "Water": 250,
    "Milk": 100,
    "Coffee_powder": 24,
    "Coins": 3.0
}

#converting string to variables
coffee = {
    "espresso": espresso,
    "latte": latte,
    "cappuccino": cappuccino,
}


# loop through ingredients
def loop_ing():
    for i in ingredients:
        if i == "Coffee_powder":
            print(f"{i}: {ingredients[i]}gm")
            break
        print(f"{i}: {ingredients[i]}ml")


# returns ingredients left after using machine # TODO:1 Could have done this in loop
def calc_ing(coffee_type):
    ingredients["Milk"] = ingredients["Milk"] - coffee_type["Milk"]
    ingredients["Water"] = ingredients["Water"] - coffee_type["Water"]
    ingredients["Coffee_powder"] = ingredients["Coffee_powder"] - coffee_type["Coffee_powder"]
    return ingredients


# # which resources are not enough
# def print_enough():
#     """ prints ingredients status and returns true if not enough ingredients"""
#     for i in ingredients:
#         if ingredients[i] < 0:
#             print(f"Less {i}, ")
#
#     for i in ingredients:
#         if ingredients[i] < 0:
#             return True  # return true if less ingredients

def print_enough():  # it does the same as above function but doesn't specify which ingredients and in lesser steps
    """ prints ingredients status and returns true if not enough ingredients"""
    if not any(ingredients.values()):
        print("Not enough ingredients")
        return True # return true if less ingredients


def get_money():
    quarters = 0.25
    dimes = 0.10
    nickles = 0.05
    pennies = 0.01

    print("Please insert coins:")
    q = int(input("quarters = "))
    d = int(input("dimes = "))
    n = int(input("nickles = "))
    p = int(input("pennies = "))

    quarters = quarters * q
    dimes = dimes * d
    pennies *= p
    nickles *= n

    return quarters+dimes+pennies+nickles


machine = True
while machine:

    enter = input("What coffee do you want ('report' if want to know what we have),\nespresso/latte/cappuccino:")
    if enter == "report":
        loop_ing()
        continue

    c_type = coffee[enter]

    # now calculate ingredients as per the choice
    calc_ing(c_type)

    # check after calculating is there enough ingredients
    print_enough()

    if print_enough():  # since is_enough will be 'none' when ingredients are enough it will be false at that time
        print("please refill the mentioned ingredients")

    else:
        coins = get_money()
        # TODO: 2 Could have made check_money function
        if coins < c_type["Coins"]:
            print("Not enough coins")
            print("\n . \n . \n . \n .")
            continue
        elif coins > c_type["Coins"]:
            extra_coins = coins - c_type['Coins']
            print(f"Here's your extra change {round(extra_coins,3)}")  # rounded the money
        else:
            pass  # just give them their coffee
        print(f"AAnd, Here's your {enter} ☕\n")






