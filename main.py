MENU = {
    "espresso": {
        "ingredients": {
            "water": 50,
            "coffee": 18,
        },
        "cost": 5,
    },
    "latte": {
        "ingredients": {
            "water": 200,
            "milk": 150,
            "coffee": 24,
        },
        "cost": 7,
    },
    "cappuccino": {
        "ingredients": {
            "water": 250,
            "milk": 100,
            "coffee": 24,
        },
        "cost": 10,
    }
}

resources = {
    "water": 500,
    "milk": 200,
    "coffee": 100,
}

money = 0


def resource_sufficient(drink):
    for ingredient, required_amount in MENU[drink]["ingredients"].items():

        if resources[ingredient] < required_amount:
            return f"Sorry, there is not enough {ingredient}"
    return "enough"


def process_payment():
    print('please insert coins.')
    bank = int(input("how many 50 groszy?: ")) * 0.50
    bank += int(input("how many 1 złoty?: ")) * 1
    bank += int(input("how many 2 złoty?: ")) * 2
    bank += int(input("how many 5 złoty?: ")) * 5
    return bank


def is_transaction_successful(money_received, drink_cost):
    """Return True when the payment is accepted, or False if money is insufficient."""
    if money_received >= drink_cost:
        change = round(money_received - drink_cost, 2)
        print(f"Here is ${change} in change.")
        global money
        money += drink_cost
        return True    # Transakcja udana, zwracamy reszte
    else:
        print("Sorry that's not enough money. Money refunded.")
        return False   # Transakcja nieudana, zwracamy otrzymane pieniądze


def make_coffee(name_coffe, drink):
    for item in drink:
        resources[item] -= drink[item]
    print(f"Here is your {name_coffe} ☕️. Enjoy!")


is_on = True

while is_on:
    choose = input("What would you like? (espresso/latte/cappuccino): ")
    if choose == "off":
        is_on = False
    elif choose == "report":
        print(f"Water: {resources['water']}ml")
        print(f"Milk: {resources['milk']}ml")
        print(f"Coffee: {resources['coffee']}g")
        print(f"Money: ${money}")
    elif choose in MENU:  # Sprawdzamy, czy wybrano napój
        drink = MENU[choose]
        resource_check = resource_sufficient(choose)
        if resource_check == "enough":
            payment = process_payment()
            if is_transaction_successful(payment, drink["cost"]):
                make_coffee(choose, drink["ingredients"])
        else:
            print(resource_check)


    else:
        print("Sorry, that is not a valid choice.")  # Obsługa nieprawidłowego wyboru