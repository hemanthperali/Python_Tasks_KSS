#  Write a program to remove duplicate characters from a string. 

s = input("Enter a string: ")
res = ""

for char in s:
    if char not in res:
        res += char

print(res)