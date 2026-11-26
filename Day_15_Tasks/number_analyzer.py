'''Scenario:
A system generates random numbers for testing.
Task:
● Use random to generate 10 numbers
● Store in a list
● Use loop + condition to count even/odd numbers
● Use set to remove duplicates'''

import random

# Generate 10 random numbers
nums = []
for i in range(10):
    n = random.randint(1,100)
    nums.append(n)
print("Generated Numbers:",nums)

# Count even/odd numbers
even_count = 0
odd_count = 0

for n in nums:
  if n%2==0:
    even_count+=1
  else:
    odd_count+=1

print("\nEven Numbers Count:", even_count)
print("Odd Numbers Count:", odd_count)

# Remove duplicates
unique_nums = set(nums)

print("\nNumbers after removing duplicates:")
print(unique_nums)


