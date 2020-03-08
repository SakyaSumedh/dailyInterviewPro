'''
This problem was recently asked by Apple:

Given a sorted list of size n, with m unique elements (thus m < n), modify the list such that the first m unique elements in the list will be sorted, ignoring the rest of the list.
Your solution should have a space complexity of O(1).
Instead of returning the list (since you are just modifying the original list), you should return what m is.

Here's an example and some starter code.

def remove_dups(nums):
  # Fill this in.

nums = [1, 1, 2, 3, 4, 4, 4, 4, 4, 5, 5, 6, 7, 9]
print(remove_dups(nums))
# 8
print(nums)
# [1, 2, 3, 4, 5, 6, 7, 9]

nums = [1, 1, 1, 1, 1, 1]
print(remove_dups(nums))
print(nums)
# 1
# [1]
'''

def remove_dups(nums):
    i = 0
    while i < len(nums) - 1:
        while (i + 1) < len(nums) and nums[i] == nums[i+1]:
            nums.pop(i+1)
        i += 1
    return len(nums)

nums = [1, 1, 2, 3, 4, 4, 4, 4, 4, 5, 5, 6, 7, 9, 9, 10, 11, 11, 11, 11, 15, 15, 15, 15, 15, 15, 15, 15]
print(remove_dups(nums))
print(nums)
