'''
Hi, here's your problem today. This problem was recently asked by LinkedIn:

Write a function that reverses the digits a 32-bit signed integer, x. Assume that the environment can only store integers within the 32-bit signed integer range, [-2^31, 2^31 - 1]. The function returns 0 when the reversed integer overflows.

Example:

Input: 123
Output: 321

class Solution:
  def reverse(self, x):
    # Fill this in.

print(Solution().reverse(123))
# 321
print(Solution().reverse(2**31))
# 0
'''


class Solution(object):
    @staticmethod
    def reverse(x):
        # return int(str(x)[::-1]) if -2**31 <= x < 2**31 else 0
        
        if not -2**31 <= x < 2**31:
            return 0

        reverse = 0
        while x > 0:
            reverse = reverse * 10 + x % 10
            x //= 10
        return reverse


print(Solution.reverse(123))
# 321
print(Solution.reverse(2**31))
# 0
