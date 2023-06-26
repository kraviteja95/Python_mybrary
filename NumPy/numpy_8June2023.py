"""We can also perform Slicing and Dicing on NumPy arrays"""
import numpy as np

np_array = np.array([1, 2, 3, 4, 5, 6, 7, 8, 9])
print(np_array[2:7])
print(np_array[2:7:2])

np_array1 = np.array([5, 2, 7, 4, 1, 8, 11, 15, 25, 17])
print(np_array1)
print(len(np_array1))
print(np_array1[2::3][::-1])
print(np_array1[-2:-9:-3])
