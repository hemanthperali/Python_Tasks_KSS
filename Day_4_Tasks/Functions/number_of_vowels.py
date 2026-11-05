#  Write a function that takes a string as input and returns the number of vowels. 

def vowel_count(string):
    vowels = "aeiouAEIOU"
    count = 0
    for char in string:
        if char in vowels:
            count += 1
    return count

result = vowel_count("Hello, World!")
print("Number of vowels:", result)