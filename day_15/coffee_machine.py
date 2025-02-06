import art
print(art.logo)



MENU = {
    "espresso": {
        "ingredients": {
            "water": 50,
            "coffee": 18,
            "milk":0,
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

ORDER = True

def coin_box(coffee_type,pennies,nickles,dimes,quarters):
    pennies = 0.01 * pennies
    nickles = 0.05 * nickles
    dimes = 0.10 * dimes
    quarters = 0.25 * quarters
    all_cash = pennies + nickles + dimes + quarters
    if coffee_type in ['espresso','latte','cappuccino']:
        a
   


def resource_mgmt(coffee_type,materials,menu):
    if coffee_type in ['espresso','latte','cappuccino']:
        water_cal = materials['water'] - menu[coffee_type]['ingredients']['water']
        coffee_cal = materials['coffee'] - menu[coffee_type]['ingredients']['coffee']
        milk_cal = materials['milk'] - menu[coffee_type]['ingredients']['milk']
    leftover_resource = {'water':water_cal,'coffee':coffee_cal,'milk':milk_cal}
    return leftover_resource
    

# while ORDER == True:
what_want = input("What would you like?\n 1.Espresso \n 2.Latte \n 3.Cappuccino\n").lower()
#     coin_pennies = float(input("How many pennies?: "))
#     coin_nickles = float(input("How many nickles?: "))
#     coin_dimes = float(input("How many dimes?: "))
#     coin_quarters = float(input("How many quarters?: "))
#     coinless = coin_box(coffee_type=what_want,pennies=coin_pennies,nickles=coin_nickles,dimes=coin_dimes,quarters=coin_quarters)

resources = resource_mgmt(coffee_type=what_want,materials=resources,menu=MENU)
