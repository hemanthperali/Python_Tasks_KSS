'''Create a generator function that continuously generates even numbers starting from
2. The program should print the first N even numbers using this generator.'''

def even_numbers():
    i = 2
    while True:
        yield i
        i += 2

N = int(input("Enter N: "))

count = 0
for num in even_numbers():
    print(num)
    count += 1
    if count == N:
        break