# Write a program to count the frequency of each character in a string.

s = input("Enter a string: ")
count = {}

for char in s:
    if char in count:
        count[char] += 1
    else:
        count[char] = 1
        
print(count)  