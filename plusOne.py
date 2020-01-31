'''
Given a non-empty array where each element represents a digit of a non-negative integer, add one to the integer. 
The most significant digit is at the front of the array and each element in the array contains only one digit. 
Furthermore, the integer does not have leading zeros, except in the case of the number '0'.

Example:

Input: [2,3,4]
Output: [2,3,5]

class Solution():
  def plusOne(self, digits):
    # Fill this in.

num = [2, 9, 9]
print(Solution().plusOne(num))
# [3, 0, 0]
'''
from functools import reduce

class Solution():
    def plus_one(self, digits):
        add_one = reduce(lambda x, y: x*10 + y, digits) + 1
        return [int(x) for x in str(add_one)]


num = [2, 9, 9]
print(Solution().plus_one(num))
