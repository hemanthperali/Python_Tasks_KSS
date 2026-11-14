''' A writer saves an article in a file called article.txt. Write a Python program that:
● Opens and reads the file
● Counts the number of words, lines, and characters in the file
● Displays the results'''

# Open and read the file
with open("article.txt", "r") as file:
    data = file.read()

# Count words, lines and characters
words = len(data.split())  #separate the text into words
lines = len(data.splitlines())  # separate the text into lines
characters = len(data)

# Display the results
print("Number of Words:", words)
print("Number of Lines:", lines)
print("Number of Characters:", characters)