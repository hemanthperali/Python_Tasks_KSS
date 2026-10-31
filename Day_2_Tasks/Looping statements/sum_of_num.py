#  Write a program to find the sum of numbers from 1 to N using a loop. 

n = int(input("Enter a number:"))
sum = 0
i = 1

while i <= n:
    sum += i
    i+=1
    print(sum)