#  Write a recursive function to calculate the sum of digits of a number. 

def sum_of_digits(n):
    if n==0:
        return 0
    else:
        digit = n%10
        n //=10
        return digit + sum_of_digits(n)

num = int(input("Enter a number:"))
res = sum_of_digits(num)
print(f"Sum of digits:{res}")
