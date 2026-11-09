# Given a string `"programming"`, create a dictionary that counts how many times each character appears.
 
s = "Programming"

# Initialize an empty dictionary to store character counts
count = {}

# Loop through each character in the string
for i in s:
    # Check if the character is already in the dictionary
    if i in count:
        # If the character is already in the dictionary, increment its count by 1
        count[i]+=1
    else:
        # If the character is not in the dictionary, add it with a count of 1
        count[i] = 1

print(count)