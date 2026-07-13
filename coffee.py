import time
import pprint
Prices={"coffee 8oz":2.5,
        "coffee 16oz":3,
        "coffee 20oz":5,
        "latte 8oz":4, 
        "latte 16oz":5, 
        "coffee 20oz":6, 
        "espresso 8oz": 5, 
        "hotchoclate 8oz": 4, 
        "hotchoclate 16oz":5, 
        "hotchoclate 20oz":6, 
        "sandwhiches":9, 
        "croissants ": 5, 
        "yogurt": 2, 
        "cookie":3, 
        "brownie": 5 
    }
global stuff_ordered
stuff_ordered = []
def take_order():
    print("Hello!")
    time.sleep(0.5)
    print("Welcome to the Python Cafe!")
    time.sleep(0.5)
    global menu_choice
    global total
    pprint.pprint(Prices)
    menu_choice = input("What would you like to order today? (enter your order as [drink] [size], just like on the menu) ")
    total = 0
    total = total + Prices.get(menu_choice)
    print(f"Your current total is {total}")
    keep_going = input("Would you like to keep ordering? (yes or no) ")
    stuff_ordered.append(menu_choice)
    orders = 0
    if keep_going == "yes":
            while orders<11:
                pprint.pprint(Prices)
                menu_choice = input("What would you like to order today? (enter your order as [drink] [size], just like on the menu) ")
                total = total + Prices.get(menu_choice)
                print(f"Your current total is {total}")
                stuff_ordered.append(menu_choice)
                keep_going = input("Would you like to keep ordering? (yes or no, MAKE SURE TO NOT CAPITALIZE) ")
                if keep_going == "yes":
                    orders+=1
                    continue
                elif keep_going=="no":
                    break
                else:
                    print("you did not say yes or no")
                    print("the cafe self-destructs")
                    exit()
            if orders > 9:
                print("You have reached the max order amount")

def calculate_total():
     print("Thank you for coming to our cafe")
     time.sleep(0.5)
     print(f"Your total is {total}")
def print_receipt():
     global stuff_ordered
     print("You ordered:")
     for item in stuff_ordered:
        print(item)
     print(f"And that all came up to a price of {total}")
     

take_order()   
calculate_total()
print_receipt()