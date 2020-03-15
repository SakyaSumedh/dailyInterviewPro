'''
Reshaping a matrix means to take the same elements in a matrix but change the row and column length. 
This means that the new matrix needs to have the same elements filled in the same row order as the old matrix.
Given a matrix, a new row size x and a new column size y, reshape the matrix.
If it is not possible to reshape, return None.

Here's an example and some starter code.

def reshape_matrix(mat, x, y):
  # Fill this in.

print(reshape_matrix([[1, 2], [3, 4]], 1, 4))
# [[1, 2, 3, 4]]

print(reshape_matrix([[1, 2], [3, 4]], 2, 3))
# None
'''

def reshape_matrix(matrix, x, y):
    if not ((len(matrix) * len(matrix[0])) == (x * y)):
        return None

    matrix_elem = []
    for row in matrix:
        matrix_elem += row

    return [[matrix_elem.pop(0) for _ in range(y)] for _ in range(x)]


print(reshape_matrix([[1, 2], [3, 4]], 1, 4))
print(reshape_matrix([[1, 2], [3, 4]], 4, 1))
print(reshape_matrix([[1, 2], [3, 4]], 2, 3))
print(reshape_matrix([[1, 2], [3, 4], [5, 6]], 1, 6))
