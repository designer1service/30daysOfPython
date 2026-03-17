# List Comprehension

# [expression for i in iterable if condition]

language = 'Python'
lst = list(language)
print(type(lst))
print(lst)

lst = [i for i in language]
print(type(lst))
print(lst)

numbers = [i for i in range(11)]
print(numbers)

squares = [i*i for i in range(11)]
print(squares)

numbers = [(i,i*i) for i in range(11)]
print(numbers)

even_number = [i for i in range(21) if i % 2 == 0]
print(even_number)

odd_number = [i for i in range(21) if i % 2 != 0]
print(odd_number)

numbers = [-8, -7, -3, -1, 0, 1, 3, 4, 5, 7, 6, 8, 10]
positive_even_numbers = [i for i in numbers if i % 2 == 0 and i > 0]
print(positive_even_numbers)

list_of_lists = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
flattened_list = [number for row in list_of_lists for number in row]
print(flattened_list)

# Lambda Function

# x = lambda param1, param2, param3: param1 + param2 + param3
# print(x(arg1, arg2, arg3))

# Creating a Lambda Function
def add_two_nums(a,b):
    return a + b
print(add_two_nums(1,2))

add_two_nums = lambda a,b : a+b
print(add_two_nums(1,2))

print((lambda a,b: a+b)(2,5))

square = lambda x : x*x
print(square(5))

multiple_variable = lambda a,b,c : a**2 - 3*b + 4*c
print(multiple_variable(1,2,3))

# Lambda Function Inside Another Function

def power(x):
    return lambda n: x**n
cube= power(2)(3)
print(cube)

# Exercises: Day 13

# 1 Filter only negative and zero in the list using list comprehension

numbers = [-4, -3, -2, -1, 0, 2, 4, 6]
nums = [num for num in numbers if num <= 0]
print(nums)

# 2 Flatten the following list of lists of lists to a one dimensional list :
list_of_lists =[[1, 2, 3], [4, 5, 6], [7, 8, 9]]
flattened_list = [i for rows in list_of_lists for i in rows]
print(flattened_list)

# 3 Using list comprehension create the following list of tuples:
square_list = [(i,i**0,i**1,i**2,i**3,i**4,i**5) for i in range(11)]
print(square_list)

# 4 Flatten the following list to a new list:
countries = [[('Finland', 'Helsinki')], [('Sweden', 'Stockholm')], [('Norway', 'Oslo')]]
flattened_tuple = [[country.upper(), country[:3].upper(), capital.upper()] for rows in countries for (country,capital) in rows]
print(flattened_tuple)

# 5 Change the following list to a list of dictionaries:
countries = [[('Finland', 'Helsinki')], [('Sweden', 'Stockholm')], [('Norway', 'Oslo')]]
flattened_dict = [{'country':country , 'city' :capital} for rows in countries for (country,capital) in rows]
print(flattened_dict)

# 6 Change the following list of lists to a list of concatenated strings:
names = [[('Asabeneh', 'Yetayeh')], [('David', 'Smith')], [('Donald', 'Trump')], [('Bill', 'Gates')]]
full_name_list = [first + ' ' + last for rows in names for (first,last) in rows]
print(full_name_list)

# 7 Write a lambda function which can solve a slope or y-intercept of linear functions.
slope = lambda x0,y0,x1,y1 : (y1-y0)/(x1-x0)
y_intercept = lambda x0, y0, x1, y1: y0 - slope(x0, y0, x1, y1) * x0
print(slope(1,3,2,6))
print(y_intercept(1, 3, 2, 6))