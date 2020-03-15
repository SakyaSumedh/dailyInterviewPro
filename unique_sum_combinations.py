'''
This problem was recently asked by Twitter:

Given a list of numbers and a target number, 
find all possible unique subsets of the list of numbers that sum up to the target number.
The numbers will all be positive numbers.

Here's an example and some starter code.

def sum_combinations(nums, target):
  # Fill this in.

print(sum_combinations([10, 1, 2, 7, 6, 1, 5], 8))
# [(2, 6), (1, 1, 6), (1, 2, 5), (1, 7)]
'''

def sum_combinations(nums, target):
    def sum_generator(nums_list, target, elem=[]):
        if target <= 0:
            return
        for i in range(len(nums_list)):
            if nums_list[i] > target:
                continue
            
            nums_i = nums_list[:i] + nums_list[i+1:]
            remainder = target - nums_list[i]
            if remainder in nums_i:
                combinations.add(tuple(sorted(elem + [nums_list[i], remainder])))
            
            sum_generator(nums_i, remainder, elem=[nums_list[i], *elem])
        
    combinations = set()
    sum_generator(nums, target)
    return list(combinations)


print(sum_combinations([10, 1, 2, 7, 6, 1, 5], 8))
print(sum_combinations([5, 8, 4, 5, 1, 12, 2, 3], 10))
print(sum_combinations([5, 8, 4, 3, 5, 1, 12, 2, 3, 6], 15))