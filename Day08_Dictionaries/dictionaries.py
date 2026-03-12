# Dictionaries

empty_dict = {}
dct = {'key1':'value1','key2':'value2','key3':'value3'}

person = {
    'first_name' : 'Luka',
    'last_name' : 'Marinkovic',
    'age' : 21,
    'country' : 'Croatia',
    'isMarried' : False,
    'skills' : ['HTML','CSS','JS','Kotlin','C#'],
    'adress' : {
        'street' : 'fake adress 101',
        'zipcode' : '10000'
    }
}

print(len(dct))
print(len(person))

# Accessing Dictionary Items
print(dct['key1'])
print(dct['key3'])

print(person['age'])
print(person['skills'])
print(person['adress']['street'])

# accessing the key that doesn't exist raises an error thats why we use .get

print(person.get('first_name'))
print(person.get('city')) # none

# Adding Items to a Dictionary
dct['key4'] = 'value4'
print(dct)

person['job_title'] = 'None'
person['skills'].append('C') # only for lists
person['adress']['city'] = 'Osijek' 
print(person)

# Modifying Items in a Dictionary
dct['key1'] = 'value-one'

# Checking Keys in a Dictionary
print('key1' in dct)
print('key11' in dct)

# Removing Key and Value Pairs from a Dictionary
dct.pop('key1')
dct.popitem() # last item
del dct['key2']
print(dct)

person.pop('first_name')
person.popitem()
del person['isMarried']
print(person)

# Changing Dictionary to a List of Items
dct = {'key1':'value1', 'key2':'value2', 'key3':'value3', 'key4':'value4'}
print(dct.items())
print(list(dct.items()))

# Clearing a Dictionary
print(dct.clear())

# Deleting a Dictionary
del dct

# Copy a Dictionary
dct = {'key1':'value1', 'key2':'value2', 'key3':'value3', 'key4':'value4'}
dct_copy = dct.copy()

# Getting Dictionary Keys as a List
print(dct.keys())

# Getting Dictionary Values as a List
print(dct.values())

# Exercises: Day 8

# 1 Create an empty dictionary called dog
dog = {}

# 2 Add name, color, breed, legs, age to the dog dictionary
dog = {'color':'brown', 'breed':'brown_dog', 'legs':4, 'age':21}

# 3 Create a student dictionary and add first_name, last_name, gender, age, 
# marital status, skills, country, city and address as keys for the dictionary

student = {
    'first_name' : 'Luka',
    'last_name' : 'Marinkovic',
    'gender' : 'male',
    'age' : 21,
    'country' : 'Croatia',
    'isMarried' : False,
    'skills' : ['HTML','CSS','JS','Kotlin','C#'],
    'adress' : 'fake adress 101',
    'city' : 'Osijek'
}

# 4 Get the length of the student dictionary
print(len(student))

# 5 Get the value of skills and check the data type, it should be a list
print(student['skills'])
print(type(student['skills']))

# 6 Modify the skills values by adding one or two skills
student['skills'].extend(['C','Python'])

# 7 Get the dictionary keys as a list
print(student.keys())

# 8 Get the dictionary values as a list
print(student.values())

# 9 Change the dictionary to a list of tuples using items() method
print(student.items())

# 10 Delete one of the items in the dictionary
student.pop('city')
print(student)

# Delete one of the dictionaries
del dog
