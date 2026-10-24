#  Print a table row using formatted strings.

name = input("Enter a name: ")
age = int(input("Enter an age: "))
stream = input("Enter a stream: ")
percentage = float(input("Enter a percentage: "))

print(f"| {name:^10} | {age:^5} | {stream:^10} | {percentage:^10.2f} |")