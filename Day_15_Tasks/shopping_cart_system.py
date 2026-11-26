'''Scenario: A user adds items to a shopping cart.
Task:
● Store items in a list
● Convert to set to remove duplicates
● Use loop + condition to calculate total cost
● Handle invalid input using try-except'''


#  Store shopping items in a list
cart = []

try:
    n = int(input("Enter the number of items: "))

    for i in range(n):
        item = input("Enter item name: ")
        cart.append(item)

    print("\nShopping Cart:", cart)

    #  Convert list into set to remove duplicates
    unique_items = set(cart)

    print("Items after removing duplicates:", unique_items)

    #  Calculate total cost using loop and condition
    total = 0

    for item in unique_items:
        price = float(input("Enter price of " + item + ": "))

        if price >= 0:
            total += price
        else:
            print("Invalid price for", item)

    print("\nTotal Shopping Cost:", total)

except ValueError:
    print("Invalid input! Please enter valid numbers.")

