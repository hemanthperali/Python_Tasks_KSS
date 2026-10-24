# 7. Store a price in a variable and add tax to it.  

price = float(input("Enter the price of the item: "))
tax = float(input("Enter the tax : "))

total_price = price + (price * tax)

print("Original Price :",price)
print("Tax Amount :",price * tax)
print("Total Price :",total_price)