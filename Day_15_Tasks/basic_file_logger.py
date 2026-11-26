'''Scenario:
A system logs user actions.
Task:
● Take user input
● Store logs in a file
● Use loop to allow multiple entries
● Handle file errors using exception handling'''


try:
    # Open file in append mode
    file = open("user_logs.txt", "a")

    # Loop to allow multiple entries
    while True:
        action = input("Enter user action (or 'exit'): ")

        if action.lower() == "exit":
            break

        # Store action in file
        file.write(action + "\n")

    file.close()

    print("User logs saved successfully!")

except FileNotFoundError:
    print("Error: File not found!")

except PermissionError:
    print("Error: Permission denied!")

