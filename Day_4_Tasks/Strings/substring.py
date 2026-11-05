# Write a program to check whether a substring exists in a string.
 
Str = input("Enter a string:")

sub_string = input("Enter a substring to check:")

if sub_string in Str:
        print("True! The substring is exists in the given string.")

else:
        print("Substring does not exists in the  given string.")