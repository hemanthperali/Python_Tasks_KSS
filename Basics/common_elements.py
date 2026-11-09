''' Given two lists:
 
    ```python
    list1 = [1, 2, 3, 4, 5]
    list2 = [3, 4, 5, 6, 7]
    ```
  Find:

* Common elements.
* Elements present only in the first list.
* All unique elements from both lists.'''

list1 = [1,2,3,4,5]
list2 = [3,4,5,6,7]

# Find common elements
common_elements = list(set(list1) & set(list2))

# Find elements present only in the first list
only_in_list1 = list(set(list1) - set(list2))

# Find all unique elements from both lists
all_unique_elements = list(set(list1) | set(list2))

print("Common elements:", common_elements)
print("Elements present only in the first list:", only_in_list1)
print("All unique elements from both lists:", all_unique_elements)
