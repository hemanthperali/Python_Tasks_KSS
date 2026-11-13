# Write a program to check whether a number is a Perfect number.

# Get the user input
n = int(input("Enter a number:"))
sum = 0

if n > 1:
    # Loop through each number less than n to find its factors
    for i in range(1, n):
        if n % i == 0:
            sum += i

    # Check if the sum of factors is equal to the original number
    if sum == n:
        print(f"{n} is a Perfect Number.")
    else:
        print(f"{n} is not a Perfect Number.")

