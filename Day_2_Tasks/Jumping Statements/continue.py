# Write a program using continue to skip printing the number 3 in a loop from 1 to 10.

i = 0

while i < 10:
    i+=1
    if i==3:
        continue
    print(i)
