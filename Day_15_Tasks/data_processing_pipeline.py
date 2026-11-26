'''Scenario:
A system processes numeric data from file.
Task:
● Read numbers from a file
● Use NumPy for calculations (mean, std)
● Convert results to Pandas DataFrame
● Use exception handling for bad data
● Use a generator to stream data
● Apply decorator to measure execution time'''

import numpy as np
import pandas as pd
import time

#  Generator to read numbers from file
def read_numbers(numbers):
    with open(numbers, 'r') as file:
        for line in file:
            try:
                yield float(line.strip())
            except ValueError:
                print("Invalid data:", line.strip())


#  Decorator to measure execution time
def calculate_time(func):
    def wrapper():
        start = time.time()
        func()
        end = time.time()
        print("\nExecution Time:", end - start, "seconds")
    return wrapper


#  Apply decorator
@calculate_time
def process_data():

    numbers = []

    #  Read and process data using generator
    for num in read_numbers("numbers.txt"):
        numbers.append(num)

    #  NumPy calculations
    if len(numbers) > 0:
        mean_value = np.mean(numbers)
        std_value = np.std(numbers)

        # Convert results into Pandas DataFrame
        df = pd.DataFrame({
            'Calculation': ['Mean', 'Standard Deviation'],
            'Result': [mean_value, std_value]
        })

        print("\nOriginal Numbers:")
        print(numbers)

        print("\nProcessed Results:")
        print(df)

    else:
        print("No valid numbers found!")


#  Call function
process_data()