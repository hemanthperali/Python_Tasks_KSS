'''A shop has prices:
prices = [100, 200, 300, 400]
Scenario:
● Apply a 10% discount only if price > 200.
Task:
● Use list comprehension with condition to create updated price list'''

prices = [100,200,300,400]

new_list = [price * 0.9 if price > 200 else price for price in prices]

print("Updated_prices:",new_list)