# Write a program to check whether a string is a palindrome. 

user_input = input("Enter a string: ")

res = ''

for i in user_input:
    res = i + res
if res == user_input:
        print("The string is a palindrome.")
else:
        print("The string is not a palindrome.")

