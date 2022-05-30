def processOrder(quantity, item_list):
    global total
    if quantity > item_list[2]:
        print("There is not enough stock!")
        pass
    else:
        total += item_list[1] * quantity
        item_list[2] -= quantity

total = 0
A = ["Big Mac", float(2.50), 50], ["Large Fries", float(0.50), 200], ["Vegetarian Burger", float(1.00), 20]

print("Welcome to McDonald's")
print("[1]", A[1][0:2],
      "\n[2]", A[1][0:2],
      "\n[2]", A[1][0:2])

while True:
    choice, quantity = (input("\nWhat would you like?\n")).upper(), int(input("\nHow many would you like?\n"))

    if choice == "BIG MAC":
        processOrder(quantity, A[0])
    elif choice == "LARGE FRIES":
        processOrder(quantity, A[1])
    elif choice == "VEGETARIAN BURGER":
        processOrder(quantity, A[2])
    else:
        print("Invalid Item")

    more_items = (input("Do you want to order more items?")).lower()
    if more_items == "yes":
        #2if more_items =(input)("What do you have ?")).lower()
        
        pass
    else:
        break

print("Thank you for ordering!\nYour total cost is: £" +  str(total))