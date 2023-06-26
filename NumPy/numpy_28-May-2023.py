import numpy as np

# Define a list
list_a = [5, 2, 7, 4, 1]
print(list_a)
print(type(list_a))

# Convert list into an array
array_a = np.array(list_a)
print(array_a)
print(type(array_a))

# Min and Max functions of matrix
print(min(array_a))
print(max(array_a))

# Reshaping of a matrix
''' It's upto us how to provide the order of the matrix. But, the # of elements of matrix should be the same. '''

matrix_a = np.array([
    [5, 2, 7, 4, 1],
    [11, 8, 25, 17, 15]])

reshaped_matrix_a = matrix_a.reshape(5, 2)
print(reshaped_matrix_a)

# Transpose of a matrix using .T and .transpose
print(matrix_a.shape)
transposed_matrix_a = matrix_a.T
"""transposed_matrix_a = matrix_a.transpose()"""
print(transposed_matrix_a)
print(transposed_matrix_a.shape)

# arange -> Array range

'''
    We already know the below items in list.
'''

array_range_list = list(range(0, 11))
array_range_list1 = list(range(2, 11))
array_range_list2 = list(range(2, 11, 2))

print(array_range_list)
print(array_range_list1)
print(array_range_list2)


'''
    The same thing in arrange will return in array. That's it 
'''

a_range = np.arange(1, 11, 3)
print(a_range)
'''
    In this output , the spaces are not empty spaces, they are just white spaces. 
    If you calculate length of it, you will get the correct length for sure.
'''

# Zeros matrix -> Used in Deep Learning
zeros_matrix = np.zeros([5, 5])
print(zeros_matrix)
print(zeros_matrix.shape)

# Ones matrix -> Used in Deep Learning
ones_matrix = np.ones([5, 5])
print(ones_matrix)
print(ones_matrix.shape)

# Diagonal matrix
diag_matrix = np.diag([1, 2, 3, 4, 5])
print(diag_matrix)
print(diag_matrix.shape)

# Identity matrix
identity_matrix = np.diag([1, 1, 1, 1, 1])
print(identity_matrix)
print(identity_matrix.shape)

# Zeros matrix
zeros_matrix = np.zeros([5, 5])
print(zeros_matrix)
print(zeros_matrix.shape)



