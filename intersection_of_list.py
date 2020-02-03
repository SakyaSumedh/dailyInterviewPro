'''
Given 3 sorted lists, find the intersection of those 3 lists.

Here's an example and some starter code.

def intersection(list1, list2, list3):
  # Fill this in.
  
print(intersection([1, 2, 3, 4], [2, 4, 6, 8], [3, 4, 5]))
# [4]
'''

def intersection(list1, list2, list3):
    return list(set(list1).intersection(set(list2), set(list3)))

print(intersection([1, 2, 3, 4], [2, 4, 6, 8], [3, 4, 5]))
