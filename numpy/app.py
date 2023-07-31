import numpy as np

arr = np.array([1, 2, 3, 4, 5])

print(type(arr))            # numpy:ndarray

###  Dimension Array

first = np.array(42)    # 0-D array
second = np.array([0, 1, 2, 3, 4])      # 1-D array
third = np.array([[0, 1, 2], [3, 4, 5]])        # 2-D array
fourth = np.array([[[1, 2, 3], [4, 5, 6]], [[1, 2, 3], [4, 5, 6]]])     # 3-D array

# Create array with dimension
dimension_array = np.array([1, 2, 3, 4], ndmin=5)
print(dimension_array)  # [[[[[1, 2, 3, 4]]]]


### Indexing

print(second[0])     # 0
print(third[0, 1])      # 1
print(fourth[0, 1, 2])      # 6


### Slicing

print(second[1:4])      # 1, 2, 3
print(second[2:])       # 2, 3, 4


print(third[1, 1:])     # 4, 5
print(third[0:2, 2])    # 2, 5


### Data Type
# i = integer
# b = boolean
# u = unsigned integer
# f = float
# c = complex float
# m = timedelta
# M = datetime
# O = object
# S = string
# U = unicode string
# V = fixed chunk of memory for other type ( void )

print(second.dtype)     # i

new_arr = np.array([1, 2, 3, 4], dtype='S')