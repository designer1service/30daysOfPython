# Exploration of functions

# Min, Max, Sum 
num = min([1,2,3,4,5,6])
num1 = min(['luka',str(1),'marija'])
print(num1)

num2 = max([1,2,3,4,5,6])
num3 = max(['luka',str(1),'marija'])
print(num2)
print(num3)

num4 = sum([1,2,3,4,5])
print(num4)


# Print and len
first_name = 'luka' # snake_case style of naming variables
print('First name is',first_name) # print() takes an infinite amount of arguments
print('First',"name",'is',first_name) 
print(len(first_name)) # length


# Multiline declaration
first_name1, last_name, age, is_Student = 'luka','marinkovic',21,True
print(first_name1)
print(len(last_name))
print(age)
print(is_Student)


# User input
name = input('Input your name: ')
age = input('Input your age: ') # We can also cast this to prevent the user from inputting a string instead of a number
age = int(input('Input your age: ')) # We can cast it into any data type
age = int(age) # We can also cast it like this


# Data types
first_name = 'luka'     
last_name = 'marinkovic'      
country = 'croatia'        
city= 'vukovar'            
age = 21

print(type('luka'))
print(type(first_name))
print(type(2))
print(type(2.2))
print(type(2+2j))
print(type(True))
print(type([1,2,3,4,5]))
print(type({'name':'luka','age':21}))
print(type({'marija','roko','luka'}))
print(type((1,2,3,4,5)))
print(type(zip([1,2],[3,4])))


# Casting types
number1 = 10
print(number1) # 10
number1 = float(number1)
print(number1) # 10.1

gravity = 9.81
print(int(gravity)) # 9

string1 = '10'
string1 = int(string1)
print(string1)
number2 = 10
print(str(number2))

rnd_name = 'marko'
name_to_list = list(rnd_name) # ['m','a','r','k','o']
print(name_to_list)


# Exercises: Level 1

first_name_1 = 'luka'
last_name_1 = 'marinkovic'
full_name = first_name1 + ' ' + last_name_1
print(full_name)
full_name_1 = 'luka marinkovic'
country_1 = 'Croatia'
city_1 = 'vukovar'
age_1 = 21
year = 2026
is_married = False # soon
is_true = True
is_light_on = True

favorite_food, favorite_place, favorite_movie = 'pizza','bed','orient express'


# Exercises: Level 2
print(type(first_name_1))
print(type(last_name_1))
print(type(country_1))
print(type(age_1))
print(type(year))
print(type(is_married))
print(type(full_name))

print(len(first_name_1))
print(len(last_name_1))

if len(first_name1) > len(last_name_1):
    print(first_name_1)
else:
    print(last_name_1)

num_one = 5
num_two = 4
Total = num_one + num_two
Diff = num_two - num_one
Product = num_one * num_two
Division = num_one / num_two
Remainder = num_two % num_one
Exp = num_two ** num_one
Floor_division = num_one // num_two

radius = 30
area_of_circle = (30**2) * 3.14
circum_of_circle = 2*30*3.14

first_name_2 = input('first name ')
last_name_2 = input('last name ')
country_2 = input('country ')
age_2 = input('age ')
