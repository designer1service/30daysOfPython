# Conditionals

# If Condition
a=3
if a>0:
    print('A is positive number')

# If Else
a=3
if a<0:
    print('A is negative number')
else:
    print('A is positive number')

# If Elif Else
a = 0
if a > 0 :
    print('A is a positive number')
elif a < 0 :
    print('A is a negative number')
else:
    print('A is zero')

# Short Hand
a = 3
print('A is positive') if a > 0 else print('A is negative')

# Nested Conditions
a = 0
if a > 0:
    if a % 2 == 0:
        print('A is even number')
    else:
        print('A is odd number')
elif a == 0:
    print('A is zero')
else:
    print('A is negative number')

# If Condition and Logical Operators
a = 0
if a > 0 and a % 2 == 0:
    print('A is even adn positive')
elif a > 0 and a % 2 != 0:
    print('A is odd and positive')
elif a == 0:
    print('A is zero')
else:
    print('A is negative')

# If and Or Logical Operators
user = 'James'
access_level = 3
if user == 'admin' or access_level >= 4:
    print('Access granted')
else:
    print('Access denied')
"""

# Exercises: Level 1

# 1

"""
age = int(input('Enter your age: '))
if age >= 18:
    print('You are old enough to learn to drive.')
else:
    print(f'You need {18-age} more years to learn to drive.')

# 2

age = int(input('Enter your age: '))
my_age = 21
if age > my_age:
    if abs(age-my_age == 1):
        print('You are 1 year older than me.')
    else:
        print(f'You are {abs(age-my_age)} years older than me.')
else:
    if abs(my_age-age == 1):
       print('You are 1 year younger than me.')
    else:
        print(f'You are {abs(my_age-age)} years younger than me.')

# 3
number_one = int(input('Enter number one: '))
number_two = int(input('Enter number two: '))
if number_one > number_two:
    print(f'{number_one} is greater than {number_two}')
elif number_one < number_two:
    print(f'{number_two} is greater than {number_one}')
else:
    print('Numbers are equal')

# Exercises: Level 2

# 1
while True:
    grade = int(input('Enter grade between 0-100: '))
    if grade >= 0 and grade <= 100:
        break
if grade >= 90 and grade <= 100:
    print('A')
elif grade >= 80 and grade <= 89:
    print('B')
elif grade >= 70 and grade <= 79:
    print('C')
elif grade >= 60 and grade <= 69:
    print('D')
elif grade >= 0 and grade <= 59:
    print('F')

# 2
month = input('Enter a month to get a season: ').lower()
if month == 'september' or month == 'october' or month == 'november':
    print('Autumn')
elif month == 'december' or month == 'january' or month == 'february':
    print('Winter')
elif month == 'march' or month == 'april' or month == 'may':
    print('Spring')
else:
    print('Summer')

# 3

fruits = ['banana', 'orange', 'mango', 'lemon']
fruit_input = input('Enter fruit: ').lower()
if fruit_input in fruits:
    print('That fruit already exist in the list')
else:
    fruits.append(fruit_input)
    print(fruits)

# Exercises: Level 3

person={
    'first_name': 'Asabeneh',
    'last_name': 'Yetayeh',
    'age': 250,
    'country': 'Finland',
    'is_married': True,
    'skills': ['JavaScript', 'React', 'Node', 'MongoDB', 'Python'],
    'address': {
        'street': 'Space street',
        'zipcode': '02210'
    }
}
if 'skills' in person:
    middle_index = (len(person['skills']) // 2)
    print(person['skills'][middle_index])
else:
    print('No skills key')

if 'skills' in person:
    if 'Python' in person['skills']:
        print('True')
    else:
        print('False')
else:
    print('No skills key')

skills = set(person['skills'])

if skills == {'JavaScript', 'React'}:
    print('He is a front end developer')
elif skills == {'Node', 'Python', 'MongoDB'}:
    print('He is a backend developer')
elif skills == {'React', 'Node', 'MongoDB'}:
    print('He is a fullstack developer')
else:
    print('unknown title')

if person['is_married']:
    if person['country'] == 'Finland':
        print(f'{person['first_name']} {person['last_name']} lives in {person['country']}. He is married')