#  Write a recursive function to reverse a string.

def reverse_string(s):
    if len(s)<=1:
        return s
    else:
        return s[-1] + reverse_string(s[:-1])

s1 = input("Enter a string:")
res = reverse_string(s1)
print(f"Reverse of the string is: {res}")