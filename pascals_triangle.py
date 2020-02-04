'''
Pascal's Triangle is a triangle where all numbers are the sum of the two numbers above it. Here's an example of the Pascal's Triangle of size 5.
    1
   1 1
  1 2 1
 1 3 3 1
1 4 6 4 1
Given an integer n, generate the n-th row of the Pascal's Triangle.

Here's an example and some starter code.

def pascal_triangle_row(n):
  # Fill this in.

print(pascal_triangle_row(6))
# [1, 5, 10, 10, 5, 1]
'''
import time
from math import factorial


def combination(n, r):
    if r == 0 or n == r:
        return 1
    return int(factorial(n) / (factorial(r) * factorial(n-r)))


def pascal_triangle_row(n):
    '''
    each element of pascal triangle row is given by:
    C(n,k) = n!/(k!(n-k)!) , where n is row-index and k is element-index
    '''
    return [combination(n-1, r) for r in range(n)]    

start = time.time()
print(pascal_triangle_row(10))
print(time.time() - start)