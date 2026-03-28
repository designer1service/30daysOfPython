# statistic

import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

print('numpy: ', np.__version__)
print(dir(np))

# Creating numpy array using
python_list = [1,2,3,4,5]
print(python_list)

two_dimensional_list = [[0,1,2],[3,4,5],[6,7,8]]
print(two_dimensional_list)

numpy_array_from_list = np.array(python_list)
print(type(numpy_array_from_list))
print(numpy_array_from_list)

# Creating float numpy arrays
numy_array_from_list2 = np.array(python_list, dtype=float)
print(numy_array_from_list2)

numpy_bool_array = np.array([0, 1, -1, 0, 0], dtype=bool)
print(numpy_bool_array) 

# Creating multidimensional array using numpy
two_dimensional_list = [[0,1,2], [3,4,5], [6,7,8]]
numpy_two_dimensional_list = np.array(two_dimensional_list)
print(type (numpy_two_dimensional_list))
print(numpy_two_dimensional_list)

# Converting numpy array to list
np_to_list = numpy_array_from_list.tolist()
print(type (np_to_list))
print('one dimensional array:', np_to_list)
print('two dimensional array: ', numpy_two_dimensional_list.tolist())

# Creating numpy array from tuple
python_tuple = (1,2,3,4,5)
print(type (python_tuple)) 
print('python_tuple: ', python_tuple) 

numpy_array_from_tuple = np.array(python_tuple)
print(type (numpy_array_from_tuple)) 
print('numpy_array_from_tuple: ', numpy_array_from_tuple) 

# Shape of numpy array
nums = np.array([1, 2, 3, 4, 5])
print(nums)
print('shape of nums: ', nums.shape)
numpy_two_dimensional_list = np.array([[0,1,2],[3,4,5],[6,7,8]])
print(numpy_two_dimensional_list)
print('shape of numpy_two_dimensional_list: ', numpy_two_dimensional_list.shape)
three_by_four_array = np.array(
    [[0, 1, 2, 3],
    [4,5,6,7],
    [8,9,10,11]]
    )
print(three_by_four_array)
print('shape of three_by_four_array: ', three_by_four_array.shape)

# Data type of numpy array
int_lists = [-3, -2, -1, 0, 1, 2,3]
int_array = np.array(int_lists)
float_array = np.array(int_lists, dtype=float)

print(int_array)
print(int_array.dtype)
print(float_array)
print(float_array.dtype)

# Size of a numpy array
numpy_array_from_list = np.array([1, 2, 3, 4, 5])
two_dimensional_list = np.array([[0, 1, 2],
                              [3, 4, 5],
                              [6, 7, 8]])

print('The size:', numpy_array_from_list.size) # 5
print('The size:', two_dimensional_list.size)  # 3

# Mathematical Operation using numpy
numpy_array_from_list = np.array([1, 2, 3, 4, 5])
print('original array: ', numpy_array_from_list)
ten_plus_original = numpy_array_from_list  + 10
print(ten_plus_original)

ten_minus_original = numpy_array_from_list  - 10
print(ten_minus_original)

ten_times_original = numpy_array_from_list * 10
print(ten_times_original)

ten_times_original = numpy_array_from_list / 10
print(ten_times_original)

ten_times_original = numpy_array_from_list % 3
print(ten_times_original)

ten_times_original = numpy_array_from_list // 10
print(ten_times_original)

ten_times_original = numpy_array_from_list  ** 2
print(ten_times_original)

# Checking data types
numpy_int_arr = np.array([1,2,3,4])
numpy_float_arr = np.array([1.1, 2.0,3.2])
numpy_bool_arr = np.array([-3, -2, 0, 1,2,3], dtype='bool')

print(numpy_int_arr.dtype)
print(numpy_float_arr.dtype)
print(numpy_bool_arr.dtype)

# Multi-dimensional Arrays
two_dimension_array = np.array([(1,2,3),(4,5,6), (7,8,9)])
print(type (two_dimension_array))
print(two_dimension_array)
print('Shape: ', two_dimension_array.shape)
print('Size:', two_dimension_array.size)
print('Data type:', two_dimension_array.dtype)

# Getting items from a numpy array
two_dimension_array = np.array([[1,2,3],[4,5,6], [7,8,9]])
first_row = two_dimension_array[0]
second_row = two_dimension_array[1]
third_row = two_dimension_array[2]
print('First row:', first_row)
print('Second row:', second_row)
print('Third row: ', third_row)

first_column= two_dimension_array[:,0]
second_column = two_dimension_array[:,1]
third_column = two_dimension_array[:,2]
print('First column:', first_column)
print('Second column:', second_column)
print('Third column: ', third_column)
print(two_dimension_array)

# Slicing Numpy array
two_dimension_array = np.array([[1,2,3],[4,5,6], [7,8,9]])
first_two_rows_and_columns = two_dimension_array[0:2, 0:2]
print(first_two_rows_and_columns)
reverse = two_dimension_array[::-1,::-1] # reversing the whole array
print(reverse)

# How to represent missing values ?
print(two_dimension_array)
two_dimension_array[1,1] = 55
two_dimension_array[1,2] =44
print(two_dimension_array)

numpy_zeroes = np.zeros((3,3),dtype=int,order='C')
print(numpy_zeroes)

numpy_ones = np.ones((3,3),dtype=int,order='C')
print(numpy_ones)

twoes = numpy_ones * 2

first_shape  = np.array([(1,2,3), (4,5,6)])
print(first_shape)
reshaped = first_shape.reshape(3,2)
print(reshaped)

flattened = reshaped.flatten()
print(flattened)

np_list_one = np.array([1,2,3])
np_list_two = np.array([4,5,6])
print(np_list_one + np_list_two)
print('Horizontal Append:', np.hstack((np_list_one, np_list_two)))
print('Vertical Append:', np.vstack((np_list_one, np_list_two)))

# Generating Random Numbers
random_float = np.random.random()
print(random_float)

random_floats = np.random.random(5)
print(random_floats)

# Generating a random integers between 0 and 10
random_int = np.random.randint(0, 11)
print(random_int)

random_int = np.random.randint(2,10, size=(3,3))
print(random_int)

#Generationg random numbers
normal_array = np.random.normal(79, 15, 80)
print(normal_array)

sns.set()
plt.hist(normal_array, color="grey", bins=50)

# Matrix in numpy

four_by_four_matrix = np.matrix(np.ones((4,4), dtype=float))
print(four_by_four_matrix)

np.asarray(four_by_four_matrix)[2][2] = 2
print(four_by_four_matrix)

# Numpy numpy.arange()
lst = range(0, 11, 2)
for l in lst:
    print(l)

whole_numbers = np.arange(0, 20, 1)

# Creating sequence of numbers using linspace
np.linspace(1.0, 5.0, num=10)

np.linspace(1.0, 5.0, num=5, endpoint=False)

np.logspace(2, 4.0, num=4)

x = np.array([1,2,3], dtype=np.complex128)
x.itemsize

np_list = np.array([(1,2,3), (4,5,6)])
print('First row: ', np_list[0])
print('Second row: ', np_list[1])
print('First column: ', np_list[:,0])
print('Second column: ', np_list[:,1])
print('Third column: ', np_list[:,2])

# NumPy Statistical Functions with Example
np_normal_dis = np.random.normal(5, 0.5, 100)

## min, max, mean, median, sd
print('min: ', two_dimension_array.min())
print('max: ', two_dimension_array.max())
print('mean: ',two_dimension_array.mean())
# print('median: ', two_dimension_array.median())
print('sd: ', two_dimension_array.std())

print(two_dimension_array)
print('Column with minimum: ', np.amin(two_dimension_array,axis=0))
print('Column with maximum: ', np.amax(two_dimension_array,axis=0))
print('=== Row ==')
print('Row with minimum: ', np.amin(two_dimension_array,axis=1))
print('Row with maximum: ', np.amax(two_dimension_array,axis=1))

# How to create repeating sequences?
a = [1,2,3]

# Repeat whole of 'a' two times
print('Tile:   ', np.tile(a, 2))

# Repeat each element of 'a' two times
print('Repeat: ', np.repeat(a, 2))

# How to generate random numbers?
# One random number between [0,1)
one_random_num = np.random.random()
one_random_in = np.random
print(one_random_num)

r = np.random.random(size=[2,3])
print(r)

print(np.random.choice(['a', 'e', 'i', 'o', 'u'], size=10))

## Random numbers between [0, 1] of shape 2, 2
rand = np.random.rand(2,2)
rand2 = np.random.randn(2,2) # - included

# Random integers between [0, 10) of shape 2,5
rand_int = np.random.randint(0, 10, size=[5,3])

from scipy import stats
np_normal_dis = np.random.normal(5, 0.5, 1000) # mean, standard deviation, number of samples
np_normal_dis
## min, max, mean, median, sd
print('min: ', np.min(np_normal_dis))
print('max: ', np.max(np_normal_dis))
print('mean: ', np.mean(np_normal_dis))
print('median: ', np.median(np_normal_dis))
print('mode: ', stats.mode(np_normal_dis))
print('sd: ', np.std(np_normal_dis))

plt.hist(np_normal_dis, color="grey", bins=21)
plt.show()

# Linear Algebra
### Dot product: product of two arrays
f = np.array([1,2,3])
g = np.array([4,5,6])
### 1*4+2*5 + 3*6
np.dot(f, g)  # 23

# NumPy Matrix Multiplication with np.matmul()
### Matmul: matruc product of two arrays
h = [[1,2],[3,4]]
i = [[5,6],[7,8]]
### 1*5+2*7 = 19
np.matmul(h, i)

np.linalg.det(i) # determinant

Z = np.zeros((8,8))
Z[1::2,::2] = 1
Z[::2,1::2] = 1

new_list = [ x + 2 for x in range(0, 11)]

np_arr = np.array(range(0, 11))
print(np_arr + 2)

temp = np.array([1,2,3,4,5])
pressure = temp * 2 + 5

plt.plot(temp,pressure)
plt.xlabel('Temperature in oC')
plt.ylabel('Pressure in atm')
plt.title('Temperature vs Pressure')
plt.xticks(np.arange(0, 6, step=0.5))
plt.show()

mu = 28
sigma = 15
samples = 100000

x = np.random.normal(mu, sigma, samples)
ax = sns.distplot(x);
ax.set(xlabel="x", ylabel='y')
plt.show()