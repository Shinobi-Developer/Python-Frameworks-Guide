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


### Copy vs View

copy_arr = second.copy()
view_arr = second.view()

print(copy_arr.base)    # None
print(view_arr.base)    # second array [0, 1, 2, 3, 4]


### Shape

print(third.shape)      # (2, 4)
print(dimension_array.shape)       # (1, 1, 1, 1, 5)


###  Reshape

array_one = np.array([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12])
new_arr = array_one.reshape(4, 3)
print(new_arr)      # [[1, 2, 3], [4, 5, 6], [7, 8, 9], [10, 11, 12]]

reshape = array_one.reshape(2, 3, 2)
print(reshape)      # [[[1, 2], [3, 4], [5, 6]], [[7, 8], [9, 10], [11, 12]]]

# wrong_shape = array_one.reshape(4, 4)     # Error

print(new_arr.reshape(4, 3).base)       # original array so it's view
print(new_arr.reshape(-1))      # [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12]

for x in np.nditer(reshape):
    print(x)                    # 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12
    
for x in np.nditer(second, flags=['buffered'], op_dtypes=['S']):
    print(x)            # b'1', b'2', b'3'
    
    
arr1 = np.array([1, 2, 3])
arr2 = np.array([4, 5, 6])
arr = np.concatenate((arr1, arr2))      # [1, 2, 3, 4, 5, 6]
arr3 = np.array([[1, 2], [3, 4]])
arr4 = np.array([[5, 6], [7, 8]])
axis_arr = np.concatenate((arr3, arr4), axis=1)     # [[1, 2, 5, 6], [3, 4, 7, 8]]
stack_arr = np.stack((arr1, arr2), axis=1)      # [[1, 4], [2, 5], [3, 6]]


### Split

splited_arr = np.array_split(array_one, 4)      # [array([1, 2, 3]), array([4, 5, 6]), array([7, 8, 9]), array([10, 11, 12])]
splited_arr1 = np.array_split(new_arr, 3, axis=1)      # [array([[1], [4], [7], [10]]), array([[2], [5], [8], [11]]), array([[3], [6], [9], [12]])]


### Searching

searched_arr = np.where(array_one == 4)        # 3
seached_arr1 = np.where(array_one%2 == 0)       # array([1, 3, 5, 7, 9, 11],)

x = np.searchsorted(new_arr, 7)         # 6
sorted_arr = np.array([1, 3, 5, 7])
x1 = np.searchsorted(sorted_arr, [2, 4, 6])     # [1 2 3]


### Sorting

x_arr = np.array([3, 2, 0, 1])
print(np.sort(x_arr))       # [0 1 2 3]
x_arr1 = np.array([[3, 2, 4], [5, 0, 1]])
print(np.sort(x_arr1))      # [[2, 3, 4], [0, 1, 5]]


### Filtering

filter_arr = array_one > 7
new_arr3 = array_one(filter_arr)        # [8 9 10 11 12]

