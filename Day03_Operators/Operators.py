from math import sqrt,pow
# Operators

# Boolean
var = True
var2 = False
print(var)

# Assigment operators
a,b,c,d,e,f = 0,0,0,0,0,0
a = 1 # operator =
b += 1 # operator += // can be - , * , / , % , // , **
c &= 1 # AND operator compares bits of each numbers and sets result to 1 if both bits are 0
d |= 1 # OR operator compares bits of each numbers and sets result to 1 if one of them is 1
e ^= 1 # XOR exclusevly OR 
f >>= 2 # Shift f to right by 2 bits, there is also <<

# Arithmetic operators
# +,-,*,/,%,//,**
# Integers

print('Addition: ', 1 + 2)        
print('Subtraction: ', 2 - 1)  
print('Multiplication: ', 2 * 3)  
print ('Division: ', 4 / 2)       # 2.0  Division in Python gives floating number
print('Division: ', 6 / 2)        # 3.0         
print('Division: ', 7 / 2)        # 3.5
print('Division without the remainder: ', 7 // 2)  
print ('Division without the remainder: ',7 // 3)   
print('Modulus: ', 3 % 2)         # 1, Gives the remainder
print('Exponentiation: ', 2 ** 3) # 8 it means 2 * 2 * 2

# Floats
print('Floating Point Number, PI',3.14)
print('Floating Point Number, Gravity', 9.81)

# Complex numbers
print('Complex Numbers: ', 1+1j)
print('Multiplying complex numbers: ', (1+1j)*(1+1j))

# Calculating Area of circle
radius = 10
area_of_circle = 3.14 * radius ** 2
print(area_of_circle)

# Calculating Area of rectangle
length = 10
width = 20
area_of_rectangle = length * width
print(area_of_rectangle)

# Calculating a weight of an object
mass = 75
gravity = 9.81
weight = 9.81 * 75
print(weight)

# Calculate in density of a liquid
mass1 = 75
volume = 0.075 # cubic meter
density = mass / volume
print(density)

# Comparison operators
# == equal x == y x== 'example'
# != not equal x != y 
# > greater than x>y
# < less than x<y
# >= greater or equal x >= y
# <= less or equal x <= y

print(3 > 2)     
print(3 >= 2)    
print(3 < 2)     
print(2 < 3)     
print(2 <= 3)    
print(3 == 2)   
print(3 != 2)    
print(len('mango') == len('avocado'))  
print(len('mango') != len('avocado')) 
print(len('mango') < len('avocado'))   
print(len('milk') != len('meat'))    
print(len('milk') == len('meat'))     
print(len('tomato') == len('potato'))  
print(len('python') > len('dragon'))   

# Comparing something gives either a True or False
print('True == True: ', True == True)
print('True == False: ', True == False)
print('False == False:', False == False)

# Bonus comparison operators
# is, is not, in, not in
print(1 is 1)
print(1 is not 2)
print('A' in 'Ana')
print('T' not in 'Banana')
print(4 is 2**2)

# Logical operators
# and, or, not // && , || , !

print(3>2 and 4>3)
print(3>2 or 3>4)
print(not 3>2)
print(not not False)

# Exercises
# 1. Declare your age as integer variable
age = 21
# 2. Declare your height as a float variable
my_height = 180.0
# 3. Declare a variable that store a complex number
complex_number = 1+1j

# 4. enter base and height of the triangle and calculate an area
base = float(input('Enter base of Triangle: '))
height = float(input('Enter height of Triangle: '))
area_of_triangle = 0.5 * base * height
print(f'area of triangle is {area_of_triangle}cm^2')

# 5. enter side a, side b, and side c of the triangle. Calculate the perimeter of the triangle
side_a = float(input('Enter side a: '))
side_b = float(input('Enter side b: '))
side_c = float(input('Enter side c: '))
perimeter = side_a+side_b+side_c
print(f'perimeter is {perimeter}cm')

# 6. Get length and width of a rectangle. Calculate its area and perimeter
rectangle_length = float(input('Enter length: '))
rectangle_width = float(input('Enter width: '))
rectangle_area = rectangle_length*rectangle_width
rectangle_perimeter = 2 * (rectangle_width + rectangle_length)
print(f'Area of rectangle is {rectangle_area} and perimeter is {rectangle_perimeter}')

# 7. Get radius of a circle using prompt. Calculate the area and circumference
circle_radius = float(input('Enter radius: '))
circle_area = 3.14 * circle_radius ** 2
circle_circumference = 2 * 3.14 * circle_radius
print(f'circle area is {circle_area} and circumference is {circle_circumference}')


# 8. Calculate the slope, x-intercept and y-intercept of y = 2x -2
# y intercept
x = 0
y = 2*x - 2
print(y)
# x intercept
y = 0 
x = int((y + 2)/2)
print(x)
# slope 
x0,y0 = 0,-2
x1,y1 = 1,0
m = (y1 - y0)/(x1 - x0)
print(m)


# 9. Slope is (m = y2-y1/x2-x1). 
# Find the slope and Euclidean distance between point (2, 2) and point (6,10)
x1,y1 = 2,2
x2,y2 = 6,10
slope = (y2 - y1)/(x2-x1)
print(slope)
# from math import sqrt,pow ->> on top
Euclidean_distance = sqrt(pow((x2-x1),2)+pow((y2-y1),2))

# 10. Compare the slopes in tasks 8 and 9.  == slopes are the same

# 11. Calculate the value of y (y = x^2 + 6x + 9). 
# Try to use different x values and figure out at what x value y is going to be 0.
a = 1
b = 6
c = 9
x0 = (-b + sqrt(b**2 - 4*a*c))/(2*a)
x1 = (-b - sqrt(b**2 - 4*a*c))/(2*a)
print(x0,x1)
# They are the same
y = a*x0**2 + b*x0 + c
print(y)
# y is 0 when x is -3


# 12. Find the length of 'python' and 'dragon' and make a falsy comparison statement.
print(len('python'))
print(len('dragon'))
print(len('python') > 7)

# 13. Use and operator to check if 'on' is found in both 'python' and 'dragon'
print('on' in 'python' and 'on' in 'dragon')

# 14. I hope this course is not full of jargon. Use in operator to check if jargon is in the sentence.
string = 'I hope this course is not full of jargon.'
print('jargon' in  string)

# 15. There is no 'on' in both dragon and python
print('on' not in 'python' and 'on' not in 'dragon')

# 16. Find the length of the text python and convert the value to float and convert it to string
string_text = 'python'
text_num = str(float(len(string_text)))
print(type(text_num))

# 17. check if a number is even or not 
number = int(input('Enter Number: '))
if number%2 == 0:
    print('number is even')
else:
    print('number is odd')

# 18. Check if the floor division of 7 by 3 is equal to the int converted value of 2.7.
conv_num = int(2.7)
print(conv_num)
floor_num = 7 // 3
print(floor_num)
# it is the same

# 19. Check if type of '10' is equal to type of 10
# it is not equal one is string and other one integer

# 20. Check if int('9.8') is equal to 10
print(int(9.8)==10) #false

# 21. enter hours and rate per hour. Calculate pay of the person? 
# float or int idc
rate = float(input('enter rate: '))
hours = float(input('enter hours: '))
total = rate * hours
print(total)

# 22. enter number of years calculate the number of seconds 
years = int(input('Enter years: '))
years_into_seconds = years * 365 * 24 * 60 * 60
print(years_into_seconds)

# 23. Write a Python script that displays the following table
for i in range(1,6):
    print(f'{i} {i**0} {i**1} {i**2} {i**3}')