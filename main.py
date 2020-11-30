
menu = {
    "espresso": {
        "ingredients": {
            "water": 50,
            "milk": 0,
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
    "money": 0,
}




# TODO 4. Check resources sufficient?


def check(client):

    r_water = resources["water"]
    r_milk = resources["milk"]
    r_coffee = resources["coffee"]

    u_water = menu[client]["ingredients"]["water"]
    u_milk = menu[client]["ingredients"]["milk"]
    u_coffee = menu[client]["ingredients"]["coffee"]
    if r_water > u_water:

        if r_milk > u_milk:
            if r_coffee > u_coffee:

                # TODO 5. Process coins.
                print("Please insert coins")
                quarters = float(input("How many quarters? :"))
                dimes = float(input("How many dimes? :"))
                nickles = float(input("How many nickles? :"))
                pennies = float(input("How many pennies? :"))
                total = (quarters*0.25)+(dimes*0.1)+(nickles*0.05)+(pennies*0.01)
                # TODO 6. Check transaction successful?

                if total < menu[client]["cost"]:
                    print("Sorry that is not enough money. Money refunded")
                    start()

                # TODO 7. Make Coffee

                else:
                    changes = total-menu[client]["cost"]
                    print(f"Here is ${round(changes,2)} in change.")
                    print(f"Here is your {client} ☕ Enjoy!")
                    resources["water"] -= u_water
                    resources["coffee"] -= u_coffee
                    resources["milk"] -= u_milk
                    resources["money"] += menu[client]["cost"]
                    start()
            else:
                print("Sorry there is no enough coffee.")
                should_continue = False
        else:
            print("Sorry there is no enough milk.")
            should_continue = False
    else:
        print("Sorry there is no enough water.")
        should_continue = False

# TODO 1.  Prompt user by asking “What would you like? (espresso/latte/cappuccino


def start():
    should_continue = True
    while should_continue:
        client = input("What would you like? (espresso/latte/cappuccino):  ")
# TODO 2.  Turn off the Coffee Machine by entering “off” to the prompt.
        if client == "off".lower():
            should_continue = False

# TODO 3. Print report
        elif client == "report".lower():
            print(resources)
        elif client == "espresso".lower():
            check(client)
        elif client == "latte".lower():
            check(client)
        elif client == "cappuccino".lower():
            check(client)
















# TODO 7. Make Coffee


start()