
groceries = {
    'milk (1gal)': 4.95,
    'hamburger (1lb)': 3.99,
    'tomatoes (ea.)': .35,
    'asparagus (12lbs)': 7.25,
    'water (1oz)': .01,
    'single use plastic bag': 3.00,
}
# cart_total = 0
sub_total = 0
# cart = [["Total =", cart_total]]
cart = []

def shopping_cart():
    print("\n")
    response = input("Would you like to 'show'/'add'/'delete' or 'quit'?:")
    # return response, cart, cart_total, sub_total
    return response, cart

def add_items():
    for key,value in groceries.items():
        print(f"{key} : ${value}")
    choice = input("Select from these items:")
    try:
        sub_total = groceries[choice]
        # cart_total += sub_total
        cart.append([choice, sub_total])
        # cart[len(cart)-1][1] = [[cart_total]]
    except: 
        print("Please only select an item in the list, typed EXACTLY as it appears")   

def delete_items():
    for i in cart:
        print(f"{i[0]} : ${i[1]}")
    choice = input("Select from these items:")
    try:
        sub_total = groceries[choice]
        # cart_total -= sub_total
        cart.remove([choice, sub_total])
        # cart[len(cart)-1][1] = [[cart_total]]
    except: 
        print("Please only select an item in the list, typed EXACTLY as it appears")

def show_cart():
    for i in cart:
        print(f"{i[0]} : ${i[1]}")
