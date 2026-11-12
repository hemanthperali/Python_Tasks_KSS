import math_operations as m
import string_operations as s

sum = m.add(5, 3)
product = m.multiply(5, 3)

text = input("Enter a string: ")
upper_string = s.to_uppercase(text)
char_count = s.count_characters(text)

print("Sum:", sum)
print("Product:", product)
print("Uppercase String:", upper_string)
print("Character Count:", char_count)
