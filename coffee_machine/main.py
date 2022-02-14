coffees = {
    "espresso": {
        "water": 50,
        "coffee": 18,
        "milk": 0,
        "price": 1.5,
    },
    "latte": {
        "water": 200,
        "coffee": 24,
        "milk": 150,
        "price": 2.5,
    },
    "cappuccino": {
        "water": 250,
        "coffee": 24,
        "milk": 100,
        "price": 3.0,
    }
}

resources = {
    "water": 300,
    "coffee": 100,
    "milk": 200,
    "money": 0.0,
}

game_continue = True

while game_continue:
    a_coffee = input("What would you like? (espresso/latte/cappuccino): ")
    if a_coffee == "report":
        print(f"Water: {resources['water']}ml")
        print(f"Milk: {resources['milk']}ml")
        print(f"Coffee: {resources['coffee']}g")
        print(f"Money: ${resources['money']}")
    elif a_coffee == "off":
        game_continue = False
    else:
        if a_coffee == "latte" or a_coffee == "cappuccino" or a_coffee == "espresso":
            water_check = resources["water"] >= coffees[a_coffee]["water"]
            coffee_check = resources["coffee"] >= coffees[a_coffee]["coffee"]
            milk_check = resources["milk"] >= coffees[a_coffee]["milk"]
            if water_check and coffee_check and milk_check:
                quarters = int(input("How many quarters?: "))
                dimes = int(input("How many dimes?: "))
                nickles = int(input("How many nickles?: "))
                pennies = int(input("How many pennies?: "))
                sum_inserted = quarters * 0.25 + dimes * 0.10 + nickles * 0.05 + pennies * 0.01
                if sum_inserted >= coffees[a_coffee]["price"]:
                    sum_inserted -= coffees[a_coffee]["price"]
                    resources["money"] += coffees[a_coffee]["price"]
                    print(f"Here is ${sum_inserted} in change.")
                    print(f"Here is your {a_coffee} ☕ Enjoy!")
                    for key in resources:
                        if key == "money":
                            pass
                        else:
                            resources[key] -= coffees[a_coffee][key]
                else:
                    print("Sorry  that's not enough money. Money refunded")
            else:
                if not water_check:
                    print("Sorry there is not enough water")
                if not coffee_check:
                    print("Sorry there is not enough coffee")
                if not milk_check:
                    print("Sorry there is not enough milk")
        else:
            print("Sorry, there is no such coffee.")
