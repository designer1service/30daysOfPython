# Loops

# While Loop
count = 0
while count < 5:
    print(count)
    count += 1

count = 0
while count < 5:
    print(count)
    count += 1
else:
    print('Loop is done')

# Break and Continue - Part 1
count = 0
while count < 5:
    print(count)
    count += 1
    if count == 3:
        break

# skips number 3
count = 0
while count < 5:
    if count == 3:
        count += 1
        continue
    print(count)
    count += 1

# For Loop
numbers = [0,1,2,3,4,5]
for number in numbers:
    print(number)

language = 'Python'
for letter in language:
    print(letter)

for i in range(len(language)):
    print(language[i])

# tuple iteration
numbers = (0, 1, 2, 3, 4, 5)
for number in numbers:
    print(number)

# dict iteration
person = {
    'first_name':'Asabeneh',
    'last_name':'Yetayeh',
    'age':250,
    'country':'Finland',
    'is_marred':True,
    'skills':['JavaScript', 'React', 'Node', 'MongoDB', 'Python'],
    'address':{
        'street':'Space street',
        'zipcode':'02210'
    }
}
for key in person:
    print(key)

for key, value in person.items():
    print(key, value) # this way we get both keys and values printed out

# set iteration
it_companies = {'Facebook', 'Google', 'Microsoft', 'Apple', 'IBM', 'Oracle', 'Amazon'}
for company in it_companies:
    print(company)

# Break and Continue - Part 2
numbers = (0,1,2,3,4,5)
for number in numbers:
    print(number)
    if number == 3:
        break

numbers = (0,1,2,3,4,5)
for number in numbers:
    print(number)
    if number == 3:
        continue
    print('Next number should be: ', number + 1) if number != 5 else print('Loops end')
print('outside the loop')

# when iteration reaches number 3 the rest of code gets skipped thats why number 4 doen't have a message

# Range Function
lst = list(range(11))
print(lst)

st  = set(range(1,11))
print(st)

lst = list(range(0,11,2))
print(lst)

lst = list(range(11,0,-2))
print(lst)

for number in range(11):
    print(number) # doen't include 11

# Nested For Loop
person = {
    'first_name': 'Asabeneh',
    'last_name': 'Yetayeh',
    'age': 250,
    'country': 'Finland',
    'is_marred': True,
    'skills': ['JavaScript', 'React', 'Node', 'MongoDB', 'Python'],
    'address': {
        'street': 'Space street',
        'zipcode': '02210'
    }
}

for key in person:
    if key == 'skilss':
        for skill in person['skills']:
            print(skill)

# For Else
for number in range(11):
    print(number)
else:
    print('Loop endend')

# Pass
for number in range(6):
    pass # serves as a place holder to avoid errors


# Exercises: Level 1

# 1 Iterate 0 to 10 using for loop, do the same using while loop.
for number in range(11):
    print(number)

counter = 0
while counter < 11:
    print(counter)
    counter += 1

# 2 Iterate 10 to 0 using for loop, do the same using while loop.
for number in range(10,0,-1):
    print(number)

counter = 10
while counter > 0:
    print(counter)
    counter -= 1

# 3 Write a loop that makes seven calls to print(), so we get on the output the following triangle:
counter = '#'
for number in range(0,7):
    print(counter)
    counter += '#'

# 4 Use nested loops to create the following:
for number0 in range(8):
    for number1 in range(8):
        print('# ',end='')
    print()

# 5 Print the following pattern:
counter = 0
for number in range(11):
    print(f'{counter} x {counter} = {counter*counter}')
    counter += 1

# 6 Iterate through the list, ['Python', 'Numpy','Pandas','Django', 'Flask'] 
# using a for loop and print out the items.
languages = ['Python', 'Numpy','Pandas','Django', 'Flask'] 
for items in languages:
    print(items)

# 7 Use for loop to iterate from 0 to 100 and print only even numbers
for numbers in range(101):
    if numbers % 2 == 0:
        print(numbers)

# 8 Use for loop to iterate from 0 to 100 and print only odd numbers
for numbers in range(101):
    if numbers % 2 == 1:
        print(numbers)

# Exercises: Level 2

# 1 Use for loop to iterate from 0 to 100 and print the sum of all numbers.
total = 0
for numbers in range(101):
    total += numbers
print(total)

# 2 Use for loop to iterate from 0 to 100 and print the sum of all evens and the sum of all odds.
total_even = 0
total_odd = 0
for numbers in range(101):
    if numbers % 2 == 0:
      total_even += numbers
    else:
        total_odd += numbers
print(total_odd)
print(total_even)

# Exercises: Level 3

# 1 Go to the data folder and use the countries.py file. Loop through the countries and extract all the countries containing the word land.
countries = []
for country in countries:
    if 'land' in country:
        print(country)

# 2 This is a fruit list, ['banana', 'orange', 'mango', 'lemon'] reverse the order using loop.
fruits = ['banana', 'orange', 'mango', 'lemon']
last_index = len(fruits) - 1
fruit = 0
while fruit < len(fruits)//2:
    temp = fruits[fruit]
    fruits[fruit] = fruits[last_index]
    fruits[last_index] = temp
    fruit += 1
    last_index -= 1
    if fruit == last_index:
        break
print(fruits)

# 3 

# What are the total number of languages in the data
countries_data = []

language = set()
for country in countries_data:
    for lang in country['languages']:
        language.add(lang)

print(len(language))

# Find the ten most spoken languages from the data
new_dict = {}
counter = 1
for country in countries_data:
    for lang in country['languages']:
        if lang not in new_dict:
            new_dict.update({lang:counter})
        else:
            new_dict[lang] += 1
list_dict = list(new_dict.items())
sorted_languages = sorted(list_dict, key=lambda x: x[1], reverse=True)
for lang, count in sorted_languages[:10]:
    print(f"{lang} - {count}")


# Find the 10 most populated countries in the world
new_dict1 = {}
counter = 10
for country in countries_data:
        new_dict1.update({country['name']:country['population']})
list_dict1 = list(new_dict1.items())
sorted_list = sorted(list_dict1, key=lambda x: x[1], reverse=True)
for w,c in sorted_list[:10]:
    print(f'{w}-{c}')