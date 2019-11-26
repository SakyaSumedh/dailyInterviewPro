'''
You are given an array of integers. Return the smallest positive integer that is not present in the array. The array may contain duplicate entries.

For example, the input [3, 4, -1, 1] should return 2 because it is the smallest positive integer that doesn't exist in the array.

Your solution should run in linear time and use constant space.

Here's your starting point:

def first_missing_positive(nums):
    # Fill this in.

print first_missing_positive([3, 4, -1, 1])
# 2
'''

import time

def first_missing_positive(nums):
    i = 1
    while True:
        if not i in nums:
            return i
        i += 1

start = time.time()
print(first_missing_positive([3, 2, 7, -1, 1, 4, 5, 9]))
print(time.time() - start)
