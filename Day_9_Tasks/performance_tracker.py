'''A software team wants to track how long functions take to execute. Create a decorator
that measures and prints the execution time of a function.'''


import time

def calculate_time(func):
    def wrapper():
        start = time.time()
        func()
        end = time.time()
        print("Execution Time:", end - start, "seconds")
    return wrapper


@calculate_time
def display():
    for i in range(10):
        pass


# Calling function
display()
