# Write a program to check whether a number is a Palindrome.

n = int(input("Enter a number:"))
rev = 0
num = n

while n>0:
    digit = n%10
    rev = rev * 10 + digit
    n//=10

if rev == num:
    print(f"{num} is a Palindrome Number.")
else:
    print(f"{num} is not a Palindrome Number.")