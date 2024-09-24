print("Welcome To Our Restaurants Management System.")
menu = {
    'Pizza': 120,
    'Pasta': 60,
    'Burger': 80,
    'Salad': 40,
    'Tea': 20,
    'Coffee': 50,
}

print("Pizza: 120 Rs\nPasta: 60 Rs\nBurger: 80 Rs \nSalad: 40 Rs\nTea: 20 Rs\nCoffee: 50 Rs")

order_total = 0
while True:
    item1 = input("Enter The Name Of Item You Want To Order = ").title()
    if item1 in menu:
        order_total += menu[item1]
        print(f"Your Item {item1} Has Been Added To Your Order")
        break

    else:
        print(f"Sorry, We Don't Have {item1} In Our Menu")

while True:
    another_order = input("Do You Want To Add Another Item? (Yes/No) ")
    if another_order == "Yes":
        item2 = input("Enter The Name Of Item You Want To Order = ").title()
        if item2 in menu:
            order_total += menu[item2]
            print(f"Your Item {item2} Has Been Added To Your Order")
        else:
            print(f"Sorry, We Don't Have {item2} In Our Menu")
    elif another_order == "No":
        print("-----------------------------------------------------")
        print(f"Your Total Amount To Be Payed Is {order_total} Rs")
        print("-----------------------------------------------------")
        break
    else:
        print("Invalid Input. Please Enter Yes or No")
