import numpy as np

# Function to create a 1D array using NumPy
one_d_array = np.array([10, 20, 30, 40, 50])
print(one_d_array)

# v.shape will check the # of rows and # of columns of a matrix/array
print(one_d_array.shape)

# Function to create a 2D array using NumPy
two_d_array_1 = np.array([
    [10, 20, 30],
    [40, 50, 60],
    [70, 80, 90]])
print(two_d_array_1)
print(two_d_array_1.shape)

two_d_array_2 = np.array([
    [11, 21, 31],
    [41, 51, 61],
    [71, 81, 91]])

print(two_d_array_2)
print(two_d_array_2.shape)

# Matrix Multiplication using .matmul
matrix_multiplication = np.matmul(two_d_array_1, two_d_array_2)
print(matrix_multiplication)

# Matrix Multiplication using .dot (nothing but the dot product)
matrix_multiplication = np.dot(two_d_array_1, two_d_array_2)
print(matrix_multiplication)

# Mean
print(np.mean(two_d_array_1))

# Median
''' Median returns the mid-element of matrix/set/list of elements by sorting in ascending order
For odd number of elements, median = (n+1/2)
For even number of elements, median = 0.5*((n/2) + ((n/2)+1)) '''

list_for_median = [1, 2, 3, 4, 5, 6, 7, 8]
print(np.median(list_for_median))
print(np.median(two_d_array_1))

# Standard Deviation
print(np.std(two_d_array_1))

# Variance
print(np.var(two_d_array_1))
