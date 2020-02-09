'''
You are given a list of numbers, and a target number k. Return whether or not there are two numbers in the list that add up to k.

Example:
Given [4, 7, 1 , -3, 2] and k = 5,
return true since 4 + 1 = 5.

def two_sum(list, k):
  # Fill this in.

print two_sum([4,7,1,-3,2], 5)
# True
'''

def two_sum(list_, k):
    for i in range(length := len(list_)):
        for j in range(i, length):
            if list_[i] + list_[j] == k:
                return True
    return False

print(two_sum([4,7,1,-3,2], 5))
