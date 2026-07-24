Menu={
    "latte":{"ingredients":{
        "water":200,
        "milk":150,
        "coffee":24
    },
    "cost":150
    },
    "espresso":{"ingredients":{
            "water":50,
            "coffee":18
        },
        "cost":100
    },
     "cappuccino":{"ingredients":{
                "water":250,
                "milk":100,
                "coffee":24
            },
            "cost":200
        }
}
profit=0
resources={
    "water":500,
    "milk":200,
    "coffee":100
}
def check_resources(order_ingredients):
    for item in order_ingredients:
        if order_ingredients[item]>resources[item]:
            print(f"sorry there is not enough {item}")
            return False
        return True
def process_coins():
    print("please insert coins:")
    total=0
    coins_five=int(input("how many 5rs coins? "))
    coins_tens=int(input("how many 10rs coins? "))
    coins_twenty=int(input("how many 20rs coins? "))
    total=coins_five*5+coins_tens*10+coins_twenty*20
    return total
def is_payment_successfull(money_received,coffee_cost):
    if money_received>=coffee_cost:
        global profit
        profit+=coffee_cost
        change=money_received-coffee_cost
        print(f"Here is your Rs{change} in change.")
        return True
    else:
        print("Sorry that's not enough money. Money refunded")
        return False
def make_coffee(coffee_name,coffee_ingredients):
    for item in coffee_ingredients:
        resources[item]-=coffee_ingredients[item]
    print(f"Here's your {coffee_name} ☕... Enjoy!!")
is_on=True
while is_on:
    choice=input("what would you like to have? (latte/espresso/cappuccino):")
    if choice=="off":
        is_on=True
    elif choice=="report":
        print(f"water={resources['water']}ml")
        print(f"water={resources['milk']}ml")
        print(f"water={resources['coffee']}g")
    else:
        coffee_type=Menu[choice]
        print(coffee_type)
        if check_resources(coffee_type['ingredients']):
            payment=process_coins()
            if is_payment_successfull(payment,coffee_type['cost']):
                make_coffee(choice,coffee_type["ingredients"])
        