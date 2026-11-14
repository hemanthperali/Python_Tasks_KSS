''' A user wants to save grocery items in a file grocery.txt. Write a Python program that
takes multiple items from the user and writes them into the file, with each item on a
new line.'''

# Open the file in write mode
with open("grocery.txt", "w") as file:

    # Take multiple grocery items from the user
    while True:
        item = input("Enter grocery item : ")

        if item.lower() == "stop":
            break

        # Write each item on a new line
        file.write(item + "\n")

print("Grocery items saved successfully!")