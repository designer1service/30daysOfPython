# Functions

# Function without Parameters

def generate_full_name():
    first_name = 'luka'
    last_name = 'marinkovic'
    space = ' '
    full_name = first_name + space + last_name
    print(full_name)
generate_full_name()

def add_two_numbers ():
    num_one = 2
    num_two = 3
    total = num_one + num_two
    print(total)
add_two_numbers()

# Function Returning a Value - Part 1

def generate_full_name():
    first_name = 'luka'
    last_name = 'marinkovic'
    space = ' '
    full_name = first_name + space + last_name
    return full_name
generate_full_name()

def add_two_numbers ():
    num_one = 2
    num_two = 3
    total = num_one + num_two
    return total
add_two_numbers()

# Function with Parameters

def greetings (name):
    message = name + ', welcome to Python'
    return message
print(greetings('luka'))

def add_10(num):
    ten = 10
    return num+ten
print(add_10(90))

def square_number(x):
    return x*x
print(square_number(2))

def area_of_circle(r):
    PI = 3.14
    area = PI * r ** 2
    return area
print(area_of_circle(10))

def sum_of_numbers(n):
    total = 0
    for i in range(n+1):
        total += i
    return total
print(sum_of_numbers(10))

# Function with Two Parameters

def generate_full_name (first_name, last_name):
    space = ' '
    full_name = first_name + space + last_name
    return(full_name)
print(generate_full_name('luka','marinkovic'))

def sum_two_numbers(num_one,num_two):
    sum = num_one + num_two
    return sum
print(sum_two_numbers(2,3))

def calculate_age(current_year,birth_year):
    age = current_year - birth_year
    return age
print(calculate_age(2026,2004))

def weight_of_object (mass, gravity):
    weight = str(mass*gravity)+'N'
    return weight
print(weight_of_object(85,9.81))

# Passing Arguments with Key and Value

def print_full_name (first_name, last_name):
    space = ' '
    full_name = first_name + space + last_name
    return(full_name)
print(generate_full_name(first_name='luka',last_name='marinkovic'))

# Function Returning a Value - Part 2

def is_even(n):
    if n % 2 == 0:
        return True
    return False
print(is_even(10))
print(is_even(7))

def find_even_numbers(n):
    evens = []
    for i in range(n+1):
        if i % 2 == 0:
            evens.append(i)
    return evens
print(find_even_numbers(10))

# Function with Default Parameters

def generate_full_name (first_name = 'Asabeneh', last_name = 'Yetayeh'):
    space = ' '
    full_name = first_name + space + last_name
    return full_name

print(generate_full_name())
print(generate_full_name('David','Smith'))

def calculate_age (birth_year, current_year = 2021):
    age = current_year - birth_year
    return age
print(calculate_age(2004))
print(calculate_age(2004,2026))

# Arbitrary Number of Arguments
# when we don't know number of arguments we pass to func

def sum_all_nums(*nums):
    total = 0
    for num in nums:
        total += num
    return total
print(sum_all_nums(2,3,4,5))

# Default and Arbitrary Number of Parameters in Functions

def generate_groups (team,*args):
    print(team)
    for i in args:
        print(i)
print(generate_groups('Team-1','luka','roko','marija'))

# Dictionary unpacking

def greet(name,location):
    print(name,location)
greet(name='luka',location='Croatia')
my_dict = {'name':'luka','location':'Croatia'}
greet(**my_dict)

# Arbitrary Number of Named Arguments
my_dict1 = {'name':'luka','location':'Croatia','age':21}
def arbitrary_named_args(**args):
    for k, v in args.items():
        print(" * key:", k, "value:", v)

arbitrary_named_args(**my_dict1)

# Function as a Parameter of Another Function
def square_num(n):
    return n*n
def do_something(f,x):
    return f(x)
print(do_something(square_num,3))


# Exercises: Level 1

# 1 Declare a function add_two_numbers. It takes two parameters and it returns a sum.

def add_two_numbers (num_one,num_two):
    sum = num_one + num_two
    return sum

# 2 Area of a circle is calculated as follows: area = π x r x r. Write a function that calculates area_of_circle.

def area_of_circle(r):
    PI = 3.14
    area = PI * r * r
    return area

# 3 Write a function called add_all_nums which takes arbitrary number of arguments and sums all the arguments. 
# Check if all the list items are number types. If not do give a reasonable feedback.

def add_all_nums (*args):
    total = 0 
    for num in args:
        if type(num) is not int:
            print('Not a number')
            continue
        else:
            total += num
    return total
print(add_all_nums(2,3,4,5))

# 4 convert_celsius_to_fahrenheit

def convert_celsius_to_fahrenheit(C):
    F = (C * 9/5) + 32
    return F

# 5 check-season

def check_season(month):
    lower_month = month.lower()
    if lower_month == 'september' or lower_month == 'october' or lower_month == 'november':
        print('Autumn')
    elif lower_month == 'december' or lower_month == 'january' or lower_month == 'february':
        print('Winter')
    elif lower_month == 'march' or lower_month == 'april' or lower_month == 'may':
        print('Spring')
    else:
        print('Summer')
check_season('March')

# 6 calculate_slope

def calculate_slope(x0, y0, x1, y1):
    slope = (y1 - y0) / (x1 - x0)
    return slope

print(calculate_slope(1, 2, 3, 6))

# 7 solve_quadratic_eqn
from math import sqrt

def solve_quadratic_eqn(a, b, c):
    D = b**2 - 4*a*c
    if D > 0:
        x1 = (-b + sqrt(D)) / (2*a)
        x2 = (-b - sqrt(D)) / (2*a)
        return x1, x2
    elif D == 0:
        x = -b / (2*a)
        return x
    else:
        return "No real solutions"
    
# 8 print_list

nums_list = [1,2,3,4,5]
def print_list(nums):
    for num in nums:
        print(num)

# 9 reverse_list

def reverse_list(item_list):
    for item in item_list[::-1]:
        item_list.append(item)
    for item in item_list:
        item_list.remove(item)
    return item_list

print(reverse_list([1, 2, 2, 3]))
print(reverse_list(["A", "A", "B", "C"]))

print(reverse_list([1, 2, 3, 4, 5]))
print(reverse_list(["A", "B", "C"]))

# 10 capitalize_list_items

item_list = ['luka','roko','marija']
def capitalize_list_items(item_list):
    for item in item_list:
       item_list[item_list.index(item)] = item.capitalize()
    print(item_list)
capitalize_list_items(item_list)

# 11 add_item
food_stuff = ['Potato', 'Tomato', 'Mango', 'Milk']
numbers = [2, 3, 7, 9]
def add_item(item_list,new_item):
    item_list.append(new_item)
    print(item_list)

print(add_item(food_stuff, 'Meat'))   
print(add_item(numbers, 5))   

# 12 remove_item

food_stuff = ['Potato', 'Tomato', 'Mango', 'Milk']
numbers = [2, 3, 7, 9]
def remove_item(item_list,r_item):
    item_list.remove(r_item)
    print(item_list)

print(remove_item(food_stuff, 'Mango'))  
print(remove_item(numbers, 3))

# 13 sum_of_numbers

def sum_of_numbers(num):
    sum = 0
    for i in range(num+1):
        sum += i
    return sum
print(sum_of_numbers(5))  # 15
print(sum_of_numbers(10)) # 55
print(sum_of_numbers(100)) # 5050

# 14 sum_of_odds
def sum_of_odds(nums):
    sum = 0
    for i in range(nums+1):
        if i % 2 == 1:
            sum += i
    return sum
print(sum_of_odds(100))

# 15 sum_of_evens
def sum_of_evens(nums):
    sum = 0
    for i in range(nums+1):
        if i % 2 == 0:
            sum += i
    return sum
print(sum_of_evens(100))

# Exercises: Level 2

# 1 evens_and_odds

def evens_and_odds(num):
    even_counter = 0
    odd_counter = 0
    for i in range(num+1):
        if i % 2 == 0:
            even_counter += 1
        else:
            odd_counter += 1
    print(even_counter,odd_counter)
print(evens_and_odds(100))

# 2 recursion
def factorial(n):
    if n <= 1:
        return 1
    else:
        return n*factorial(n-1)
print(factorial(3))

# 3
number_list = [2, 4, 4, 5, 7, 9]
def calculate_mean(number_list):
    return (sum(number_list)/len(number_list))

def calculate_median(number_list):
    sorted_list = sorted(number_list)
    n = len(sorted_list)
    middle_index = n // 2
    if n % 2 == 0:
        return (sorted_list[middle_index - 1] + sorted_list[middle_index]) / 2
    else: 
        return sorted_list[middle_index]
    
def calculate_mode(number_list):
    mode_dict = {}
    for num in number_list:
        if num not in mode_dict:
            mode_dict[num] = 1
        else:
            mode_dict[num] += 1
    max_count = max(mode_dict.values())
    modes = []
    for number, count in mode_dict.items():
        if count == max_count:
            modes.append(number)
    return modes

def calculate_range(number_list):
    num_range = max(number_list) - min(number_list)
    return num_range

def calculate_variance(number_list):
    for num in number_list:
        num_sum += pow(num-calculate_mean(number_list),2)
        variance = num_sum/len(number_list)
        return variance
    
def calculate_std(number_list):
    std = sqrt(calculate_variance(number_list))
    return std

# 4
def greet(name = 'Guest'):
    print(f'Hello, {name}!')
greet()
greet('Luka')


def show_args(**args):
    arg_strings = [f"{key}: {value}" for key, value in args.items()]
    print('Received:',", ".join(arg_strings))

show_args(name="Alice", age=30, city="New York")
show_args(name="Bob", pet="Fluffy, the bunny")

# Exercises: Level 3

# 1
def is_prime(n):
    if n <= 1: return False
    if n == 2: return True
    if n % 2 == 0: return False

    for i in range(3,int(sqrt(n))+1,2):
        if n % i == 0:
            return False
    return True
print(is_prime(29))

# 2
item_list = ['luka','roko','marija','luka']
def is_unique(item_list):
    item_set = set()
    for item in item_list:
        item_set.add(item)
    if len(item_set) == len(item_list):
        print('All items unique')
    else:
        print('items not unique')
print(is_unique(item_list))

def is_unique(item_list):
    for i in range(len(item_list)):
        for j in range(i+1, len(item_list)):
            if item_list[i] == item_list[j]:
                print("items not unique")
                break

def is_unique(item_list):
    return(len(item_list)) == len(set(item_list))
print(is_unique(item_list))

# 3
item_list = [1,2,3,4,5,'luka']
def is_unique_data(item_list):
    for i in range(len(item_list)):
        for j in range(i+1, len(item_list)):
            if type(item_list[i]) != type(item_list[j]):
                print("items not the same data")
            break
print(is_unique_data(item_list))

# 4
def valid_variable(name):
    if name.isidentifier():
        return True
    else:
        return False
print(valid_variable('name'))

# 5 
countries_data = []
def most_spoken_languages(countries_data):
    new_dict = {}
    for country in countries_data:
        for lang in country['languages']:
            if lang not in new_dict:
                new_dict[lang] = 1
            else:
                new_dict[lang] += 1
    list_dict = new_dict.items()
    sorted_languages = sorted(list_dict, key=lambda x: x[1], reverse=True)
    return sorted_languages[:10]


def most_populated_countries(countries_data):
    new_dict1 = {}
    for country in countries_data:
            new_dict1.update({country['name']:country['population']})
    # pop_dict = {country['name']:country['population'] for country in countries_data}
    list_dict1 = new_dict1.items()
    sorted_list = sorted(list_dict1, key=lambda x: x[1], reverse=True)
    return sorted_list[:10]