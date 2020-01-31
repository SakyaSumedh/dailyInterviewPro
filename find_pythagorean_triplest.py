'''
Given a list of numbers, find if there exists a pythagorean triplet in that list. A pythagorean triplet is 3 variables a, b, c where a^2 + b^2 = c^2

Example:

Input: [3, 5, 12, 5, 13]
Output: True

Here, 5^2 + 12^2 = 13^2.

def findPythagoreanTriplets(nums):
	# Fill this in.

print findPythagoreanTriplets([3, 12, 5, 13])
# True
'''
import time

def find_pythagorean_triplets(nums):
	length = len(nums)
	for i in range(length - 1):
		for j in range(1, length):
			square_root = (nums[i] ** 2 + nums[j] ** 2) ** (1/2)
			if square_root in nums:
				return True
	return False

start = time.time()
print(find_pythagorean_triplets([15, 8, 6, 10]))
print(time.time() - start)
