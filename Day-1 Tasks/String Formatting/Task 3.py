# . Use **f-strings** to print a sentence with variables.  

item = input("Enter the name of the item:")
price = float(input("Enter the price:"))
quantity = int(input("Enter quantity:"))

sentence = f"The total cost of {quantity} {item}(s) is: ${price * quantity:.2f}"

print(sentence)