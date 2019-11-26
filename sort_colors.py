'''
Given an array with n objects colored red, white or blue, sort them in-place so that objects of the same color are adjacent, with the colors in the order red, white and blue.

Here, we will use the integers 0, 1, and 2 to represent the color red, white, and blue respectively.

Note: You are not suppose to use the library’s sort function for this problem.

Can you do this in a single pass?

Example:

Input: [2,0,2,1,1,0]
Output: [0,0,1,1,2,2]

Here's a starting point:

class Solution:
    def sortColors(self, nums):
        # Fill this in.

nums = [0, 1, 2, 2, 1, 1, 2, 2, 0, 0, 0, 0, 2, 1]
print("Before Sort: ")
print(nums)
# [0, 1, 2, 2, 1, 1, 2, 2, 0, 0, 0, 0, 2, 1]

Solution().sortColors(nums)
print("After Sort: ")
print(nums)
# [0, 0, 0, 0, 0, 1, 1, 1, 1, 2, 2, 2, 2, 2]
'''

# Shell Sort

class Solution:
    def sort_colors(self, nums):
        n = len(nums)
        print('n -> ', n)

        gap = n // 2 
        print('gap -> ', gap)
        while gap > 0:
            print('gap', gap)
            for i in range(gap, n):
                temp = nums[i]
                j = i
                while j >= gap and nums[j - gap] > temp:
                    nums[j] = nums[j - gap]
                    j -= gap
                nums[j] = temp
            gap = gap // 2

import time
start = time.time()
nums = [0, 1, 2, 2, 1, 1, 2, 2, 0, 0, 0, 0, 2, 1]

print("Before Sort: ")
print(nums)

Solution().sort_colors(nums)
print("After Sort: ")
print(nums)
print('Execution Time: ', time.time() - start)