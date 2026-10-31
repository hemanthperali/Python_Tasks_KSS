# Write a program that uses pass inside a loop. 

n = int(input("Enter a number: "))

for i in range(n):
    if i == 4:
        pass
    else:
        print(i)