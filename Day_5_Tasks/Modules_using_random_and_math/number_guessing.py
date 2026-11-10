'''  Create a Number Guessing Game where: 
● The program generates a random number between 1 and 50 using random. 
● The user has 5 attempts to guess the number. 
● After each guess, calculate the absolute difference using math.fabs() and 
display how far the guess is from the correct number.
'''

import random
import math

# Generates a random number between 1 and 50
secret_number = random.randint(1,50)
attempts = 5

print("Welcome to Number Guessing Game!")
print("You have to pick a number between 1 to 50")
print(f"You have {attempts} attempts to guess the number")
print("\n-------------------------------------------")

for i in range(1, attempts+ 1):
    guess = int(input("Enter a number to guess:"))

    if guess == secret_number:
        print(f"\nCongratulations! You guess the number {secret_number} in {attempts} attempts!")
        break

    # Calculate absolute difference 
    difference = math.fabs(secret_number-guess)
    print(f"Wrong guess! You are {difference} away from the correct number.\n")

else:
    print(f"Game Over ! You have used all your attempts")
    print(f"The correct number was {secret_number}")

    




