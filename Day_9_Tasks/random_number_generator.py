'''A program is needed to generate numbers for testing purposes. Create a generator
function that produces numbers from 1 to N and prints them one by one when iterated'''

import random

def calculate(n):
    for i in range(1,n+1):
        yield random.randint(1,n)
        
    
r = calculate(10)

for i in r:
    print("Random Number:",i)
    break
