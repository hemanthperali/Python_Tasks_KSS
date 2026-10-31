#  Write a program using break to stop printing numbers when the number reaches 5. 

n = int(input("Enter a number: "))

for i in range(n):
    if i == 5:
        break
    print(i)

