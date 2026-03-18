# Higher Order Functions


# Function as a Parameter
def sum_numbers(nums):
    return sum(nums)

    # function highjack

def higher_order_function(f,lst):
    summation = f(lst)
    return summation
result = higher_order_function(sum_numbers,[1,2,3,4,5])
print(result)

# Function as a Return Value

def square(x):
    return x**2

def cube(x):
    return x**3

def absolute(x):
    return abs(x)

def higher_order_function(type):
    if(type == 'square'):
        return square
    elif(type == 'cube'):
        return cube
    else:
        return absolute
    
result = higher_order_function('square')
print(result(3))

# Python Closures

def add_ten():
    ten = 10
    def add(num):
        return num+ten
    return add

closure_result = add_ten()
print(closure_result(5))

# Python Decorators

def greeting():
    return 'Welcome to Python'

def uppercase_decorator(function):
    def wrapper():
        func = function()
        make_uppercase = func.upper()
        return make_uppercase
    return wrapper
g = uppercase_decorator(greeting)
print(g()) 

'''This decorator function is a higher order function
that takes a function as a parameter'''
def uppercase_decorator(function):
    def wrapper():
        func = function()
        make_uppercase = func.upper()
        return make_uppercase
    return wrapper
@uppercase_decorator
def greeting():
    return 'Welcome to Python'
print(greeting())   # WELCOME TO PYTHON"""

# g = uppercase_decorator(greeting)
# print(g())

# @uppercase_decorator
# def greeting():
    # return 'Welcome to Python'

# Applying Multiple Decorators to a Single Function

def uppercase_decorator(function):
    def wrapper():
        func = function()
        make_uppercase = func.upper()
        return make_uppercase
    return wrapper

def split_string_decorator(function):
    def wrapper():
        func = function()
        make_split = func.split()
        return make_split
    return wrapper

@split_string_decorator
@uppercase_decorator
def greetings():
    return 'Hello World!'

print(greetings())

# Accepting Parameters in Decorator Functions

def decorator_with_parameters(function):
    def wrapper_accepting_parameters(para1,para2,para3):
        function(para1,para2,para3)
        print("I live in {}".format(para3))
    return wrapper_accepting_parameters
@decorator_with_parameters
def print_full_name(first_name, last_name, country):
    print('I am {} {}. I love to do this.'.format(first_name,last_name))

print_full_name('Luka','Marinkovic','Croatia')

# Built-in Higher Order Functions

# Python - Map Function
numbers = [1,2,3,4,5]
def square(x):
    return x**2
numbers_squared = map(square,numbers)
print(list(numbers_squared))

numbers_str = ["1","2","3","4","5"]
numbers_int = map(int,numbers_str)
print(list(numbers_int))

names = ['Luka','Roko','Marija','Natalie']
def change_toupper(x):
    return x.upper()

numbers_upper = map(change_toupper,names)
print(list(numbers_upper))

names_upper_cased = map(lambda name: name.upper(), names)
print(list(names_upper_cased))  

# Python - Filter Function

numbers = [1,2,3,4,5,6,7,8]
def is_even(numbers):
    if numbers % 2 != 0:
        return False
    return True
even_numbers = filter(is_even,numbers)
print(list(even_numbers))

names = ['Luka','Roko','Marija','Natalie','Noalicker','markolicker']
def is_long_name(names):
    if len(names) > 7:
        return True
    return False
long_names = filter(is_long_name,names)
print(list(long_names))

# Python - Reduce Function

from functools import reduce

numbers_str = ['1', '2', '3', '4', '5']
def add_two_nums(x, y):
    return int(x) + int(y)
total = reduce(add_two_nums, numbers_str)
print(total)  # 15

#  Exercises: Day 14

# Exercises: Level 1
# 1

"""
Difference between map, filter, and reduce:
map()    - applies a function to every element in an iterable (transforms each element)
filter() - selects only elements that meet a condition (returns True/False)
reduce() - combines all elements into a single value
"""

# 2

"""
Explain the difference between higher order function, closure and decorator
Higher order function - A function that takes another function as an argument or returns a function

Closure - A function that remembers variables from its outer (enclosing) scope
even after the outer function has finished execution.

Decorator - A function that wraps another function and adds extra functionality
without changing the original functions code.
"""

# 3
def power_2(x):
    return x**2

def is_zero(num):
    if num == 0:
        return True
    else:
        return False
    
def multi_multiplicator(x,y):
    return int(x)*int(y)

numbers = [1,2,3,4,5]

powered = map(power_2,numbers)
jackpot = filter(is_zero,numbers)
super_calculator = reduce(multi_multiplicator,numbers)
print(list(powered))
print(list(jackpot))
print(super_calculator)

# 4
countries = ['Estonia', 'Finland', 'Sweden', 'Denmark', 'Norway', 'Iceland']
for country in countries:
    print(country)

# 5 
names = ['Asabeneh', 'Lidiya', 'Ermias', 'Abraham']
for name in names:
    print(names)

# 6
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
for number in numbers:
    print(number)

# Exercises: Level 2

# 1
Uppercased_country = map(lambda x:x.upper(), countries)
print(list(Uppercased_country))

# 2 
squared_numbers = map(lambda x:x**2,numbers)
print(list(squared_numbers))

# 3
Uppercased_country = map(lambda x:x.upper(), names)
print(list(Uppercased_country))

# 4
filtered_country = filter(lambda x: True if 'land' in x else False, countries)
print(list(filtered_country))

# 5 
filtered_country_6 = filter(lambda x: True if len(x) == 6 else False, countries)
print(list(filtered_country_6))

# 6 
filtered_country_6_and_more = filter(lambda x: True if len(x) >= 6 else False, countries)
print(list(filtered_country_6_and_more))

# 7 
filtered_country_letter = filter(lambda x: True if x.startswith('E') else False, countries)
print(list(filtered_country_letter))

# 8
chained_operators = filter(lambda x: True if len(x) >= 6 else False, filter(lambda x: True if 'y' in x else False, countries))
print(list(chained_operators))

total = reduce(lambda x, y: x + y,filter(lambda x: x % 2 == 0, map(lambda x: x*2, numbers)))
print(total)

# 9
item_list = [1,True,'Luka','Roko',1.2,'Marija']
def get_string_lists(item):
    if type(item) == str:
        return True
    return False

total = filter(get_string_lists,item_list)
print(list(total))

# 10
def add_two_nums(x,y):
    return int(x)+int(y)
summed = reduce(add_two_nums,numbers)
print(summed)

# 11 
countries = ['Estonia', 'Finland', 'Sweden', 'Denmark', 'Norway', 'Iceland']

def concatenate_countries(countries):
    *rest, last = countries
    body = reduce(lambda acc,cur : acc+', '+cur,rest)
    return f'{body}, and {last} are north European countries'
print(concatenate_countries(countries))

# 12
def categorize_countries(countries):
    body = filter(lambda x: True if 'Den' in x else False,countries)
    return list(body)
print(categorize_countries(countries))

# 13
def dict_country(countries):
    counts = {}
    for country in countries:
        first = country[0]  # prvo slovo imena države
        if first not in counts:
            counts[first] = 0
        counts[first] += 1
    return counts

# 14 
def get_first_ten_countries(countries):
    return list(countries[0:10])

print(get_first_ten_countries(countries))

# 15
def get_last_ten_countries(countries):
    return list(countries[-1:-10:-1])

print(get_last_ten_countries(countries))

# Exercises: Level 3
import countries_data as data
countries_by_name = sorted(data.countries_data_list, key=lambda c: c['name'])

countries_by_capital = sorted(data.countries_data_list, key=lambda c: c['capital'])

countries_by_population = sorted(data.countries_data_list, key=lambda c: c['population'],reverse=True)
print(countries_by_population)

def most_spoken_languages(countries_list,n):
    lang_counter = {}
    for item in countries_list:
        for i in item['languages']:
            if i not in lang_counter:
                lang_counter[i] = 0
            lang_counter[i] += 1
    lang_counter = list(lang_counter.items())
    lang_counter.sort(key=lambda x: x[1], reverse=True)
    return lang_counter[:n]

top_langs = most_spoken_languages(data.countries_data_list, 10)

print('Top 10 spoken languages:')
for lang, count in top_langs:
    print(f'{lang}: {count} countries')

def most_populated_countries(countries_data, top_n=10):
    sorted_countries = sorted(
        countries_data,
        key=lambda c: c['population'],
        reverse=True
    )
    return sorted_countries[:top_n]

top_populated = most_populated_countries(data.countries_data_list, 10)

print('\nTop 10 populated countries:')
for c in top_populated:
    print(f"{c['name']}: {c['population']}")
