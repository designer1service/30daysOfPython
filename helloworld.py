# Comments example

# Multiline comment
"""
Multiline comment 
takes a lot to write
but it is like a paragraph
"""

# Print
print("Hello World!")


# Data Types
integer = 0
integer1 = 3
integer2 = -1

floatinteger = 2.2
floatinteger1 = 0.0
floatinteger1 = -1.0

string = 'Luka'
string1 = 'Multiple words at once'

boolean = True
boolean2 = False


# Lists
list1 = [0,1,2,3,4,5] # List with the same data types
list2 = ['banana','orange','apple'] # List of strings
list3 = ['banana',1,False,9.81] # List with different data types


# Dictionary
# Key-value pairs
dict1 = {'name':'Luka','Surename':'Marinkovic','age':21,'isMarried':False}


# Tuple
# Ordered collection of different data, cannot be modified after creation
tupl = ('Luka','Marija','Roko')


# Set
# Collection of unordered data that stores unique values
set1 = {3.14,12.2,11.2}


# EXERCISE 1
A = 3
B = 4

Add = A + B
print(f"{A} + {B} is {Add}") # String interpolation one way

Sub = A - B
SubString = 'Sub of ' + str(A) + '-' + str(B) + ' is equal to ' + str(Sub) # String interpolation the other way
print(SubString)

Multply = A * B
print(Multply)

print('Division of A and B is', A / B) # Returns a decimal

Modulus = B % A
print(f"Modulus is {Modulus}") # Remainder of the division

Expo = A ** B
print(Expo)

FloorDivisionOperation = 25 // 4
print(FloorDivisionOperation)


# There is a way to do math directly inside the print function
print(3+2)
print(A//B)
print(A/2)


# Data type checks
print(type(2))
print(type('Luka'))
print(type([1,2,3,4,5]))
print(type(['banana',9.1,1,True]))
print(type(('Luka','Roko','Marija')))
print(type({3.1,3.2,3.3}))
print(type({'Name':'Luka','age':21}))
print(type(True))
