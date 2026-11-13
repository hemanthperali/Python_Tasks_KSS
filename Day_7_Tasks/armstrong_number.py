# Write a program to check whether a given number is an Armstrong number or not.

# Get the user input
n = int(input("Enter a number:"))
sum = 0
length_n = len(str(n))
temp = n

# Calculate the sum of cubes of digits
while temp>0:
    digit = temp%10
    sum+=digit**length_n
    temp//=10

# Check if the sum equals to the original number
if sum == n:
    print(f"{n} is an Armstrong number.")
else:
    print(f"{n} is not an Armstrong number.")
    

