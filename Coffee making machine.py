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
    "money": 0,
}
def machine(coffee,):
    print("Please insert coins.")
    q = int(input("how many quarters?: "))
    d = int(input("how many dimes?: "))
    n = int(input("how many nickles?: "))
    p = int(input("how many pennies?: "))
    total = (q*0.25)+(d*0.10)+(n*0.05)+(p*0.01)
    if total > MENU[coffee]["cost"]:
        change = total - MENU[coffee]["cost"]
        resources["money"]+=(total-change)
        print(f"Here is ${change.__round__(2)} in change.")
        print(f"Here is your {coffee} ☕️. Enjoy!")
    else:
        print("Sorry that's not enough money. Money refunded.")
def revaluting_resource(cofee):
    for item in MENU[cofee]["ingredients"]:
        resources[item] -= MENU[cofee]["ingredients"][item]

order = input("What would you like? (espresso/latte/cappuccino):").lower()
while order =="espresso" or order =="latte" or order =="cappuccino" or order =="report":
    if order == "report":
        print("Water:",resources["water"])
        print("Milk:",resources["milk"])
        print("Coffee:",resources["coffee"])
        print("Money:",resources["money"])
    elif resources["water"] >= MENU[order]["ingredients"]["water"]:
        if resources["coffee"] >= MENU[order]["ingredients"]["coffee"]:
            if order == "espresso":
                machine(order)
                revaluting_resource(order)
            elif resources["milk"] >= MENU[order]["ingredients"]["coffee"]:
                machine(order)
                revaluting_resource(order)
            else:
                print("Sorry there is not enough milk.")
        else:
            print("Sorry there is not enough coffee.")
    else:
        print("Sorry there is not enough water.")
    order = input("What would you like? (espresso/latte/cappuccino):").lower()