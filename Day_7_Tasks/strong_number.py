#Write a program to check whether a given number is a Strong number.

# Get the user input
n = int(input("Enter a number:"))
sum = 0

# Create a temporary variable 
temp = n

# Loop through each digit of the number
while temp>0:
    digit = temp%10

    # Calculate the factorial of the extracted digit
    fact = 1
    for i in range(1,digit+1):
        fact*=i

    # Add the calculated factorial to the sum
    sum+=fact

    # Remove the last digit from the temporary variable 
    temp//=10

# Check if the sum equals to original number
if sum == n:
    print(f"{n} is a strong number.")
else:
    print(f"{n} is not a strong number.")