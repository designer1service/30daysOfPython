
# Creating a string
letter = 'p'
print(letter)
print(len(letter))
greeting = 'Hello, World!'
print(greeting)
print(len(greeting))
sentence = 'My name is Luka and I like to study'
print(sentence)

multiline_strings = '''I am a teacher and enjoy teching.
I did not fint anything as rewarding as empowering people.''' # can be done with single and double quotes
print(multiline_strings)

# String concatenation
first_name = 'luka'
last_name = 'marinkovic'
space = ' '
full_name = first_name + space + last_name
print(full_name)
print(len(first_name))
print(len(last_name))
print(len(first_name) > len(last_name))
print(len(full_name))

# Escape sequences in Strings
# \n new line
# \t tab (8 spaces)
# \\ back slash
# \' single quote
# \" double quote

print('my name is luka.\n I study computer science')
print('Days\tTopics\tExercises\t')
print('Day 1\t5\t5')
print('Day 2\t6\t20')
print('Day 3\t5\t23')
print('Day 4\t1\t35')
print('This is a backslash symbol (\\)')
print('In every pg language it starts with \"Hello World\"')

# String formatting
# %s - string
# %d - integers
# %f - float
# %.number of digitsf - %.3f - 3 decimal spaces

first_name = 'luka'
last_name = 'marinkovic'
language = 'python'
formated_string = 'I am %s %s. I teach %s' %(first_name,last_name,language)
print(formated_string)

radius = 10
pi = 3.14
area = pi * radius ** 2
formated_string1 = 'The area of cricle is %.2f with radius of %d' %(area,radius)
print(formated_string1)

# Second way of doing it
formated_string2 = 'I am a {} {}. I teach {}'.format(first_name,last_name,language)
print(formated_string2)

a = 3
b = 4
print('{} + {} = {}'.format(a,b, a+b))
print('{} - {} = {}'.format(a,b, a-b))
# we can do that with all operators

# Third way of doing it
formated_string3 = 'The area of a circle is {:.2f} with radius of {}'.format(area,radius)
print(formated_string3)

# String interpolation
a = 4
b = 3
print(f'{a} + {b} = {a+b}')
print(f'{a} // {b} = {a//b}')
# we can do that with all operators

# Python Strings as Sequences
word = 'Kodak'
a,b,c,d,e = word
print(a)
print(b)
print(c)
print(d)
print(e)

first_letter = word[0]
print(first_letter)
second_letter = word[1]
print(second_letter)
last_index = len(word)-1
last_letter = word[last_index]
print(last_letter)

# We can also go backwards with negative indexing -1 last letter
third_letter = word[-3]
print(third_letter)

# Slicing strings
first_three = word[0:3]
print(first_three)
last_three = word[3:6]
print(last_three)

# Reversing a string
reversed_word = word[::-1]
print(reversed_word)

# Skipping Characters while slicing
skip = word[0:4:3]
print(skip)


# String Methods
challange = 'thirty days of python'
print(challange.capitalize())
print(challange.count('y'))
print(challange.count('th'))
print(challange.count('y',7,14))
print(challange.endswith('on'))
print(challange.endswith('dr'))

challange1 = 'thirty\tdays\tof\tpython'
print(challange1.expandtabs(10)) # Defalut is 8

print(challange.find('y')) # Finds first that matches and returns index
print(challange.find('th'))

print(challange.rfind('y')) # Same but reversed
print(challange.rfind('th'))

sub_string = 'da'
print(challange.index(sub_string)) # 7 
print(challange.index('y',10)) # 16 - 10 is the starting index from where search begins

print(challange.rindex(sub_string)) 
print(challange.rindex('y',10)) # 10 is still starting index

challange2 = 'thirtydaysofpython'
print(challange2.isalnum()) # True
print(challange1.isalnum()) # False - it has tabs
print(challange.isalnum())  # False - it has spaces

num = '123'
print(challange.isalpha()) # True
print(num.isalpha()) # False - isalpha check if the characters are a-z not numbers

superscript = '\u00B2'
print(challange.isdigit()) # False
print(num.isdigit()) # True - spaces not allowed
print(superscript.isdigit()) # True - superscript and subscripts included

print(challange.isdecimal()) # False
print(num.isdecimal()) # True - spaces not allowed
print(superscript.isdecimal()) # false - superscript and subscripts not included

# isdecimal is strict about only including 0-9 digits and isdigit allows them

num = "10"
num1 = "10.5"
print(num.isnumeric())
print(num1.isnumeric()) # false - no decimal num

string_lower = 'luka'
string_upper = 'LUKA'
print(string_lower.lower()) # True
print(string_upper.lower()) # False
print(string_lower.upper()) # True
print(string_upper.upper()) # Flase

web_tech = ['Html' , 'CSS' , 'JavaScript' , 'React']
result = ' '.join(web_tech) #Html CSS JavaScript React
print(result)
result = '# '.join(web_tech) # Html# CSS# JavaScript# React
print(result)

remove_text = 'thirty days of pythooonnn'
print(remove_text.strip('noth')) # works only at beginning and end of the string

print(remove_text.replace('pythooonnn','coding'))

print(remove_text.split()) # ['thirty', 'days', 'of', 'python']
print(remove_text.split(' ', 2)) # splits into 2 sections
print(remove_text.split('y')) # splits at y 

print(string_lower.swapcase())
print(string_upper.swapcase())

print(remove_text.startswith('thir')) # True
print(remove_text.startswith('days')) # False

# Exercises - Day 4

# 1 Concatenate the string 'Thirty', 'Days', 'Of', 'Python' to a single string, 'Thirty Days Of Python'.
string_list = ['Thirty', 'Days', 'Of', 'Python']
result = ' '.join(string_list)
print(result)

# 2 Concatenate the string 'Coding', 'For' , 'All' to a single string, 'Coding For All'.
string_list1 = ['Coding', 'For' , 'All']
result1 = ' '.join(string_list1)
print(result1)

# 3 Declare a variable named company and assign it to an initial value "Coding For All".
company = "Coding For All"

# 4 Print the variable company using print().
print(company)

# 5 Print the length of the company string using len() method and print().
print(len(company))

# 6 Change all the characters to uppercase letters using upper() method.
print(company.upper())

# 7 Change all the characters to lowercase letters using lower() method.
print(company.lower())

# 8 Use capitalize(), title(), swapcase() methods to format the value of the string Coding For All.
print(company.capitalize())
print(company.title())
print(company.swapcase())

# 9 Cut(slice) out the first word of Coding For All string.
print(company[0:6])

# 10 Check if Coding For All string contains a word Coding using the method index, find or other methods.
print(company.index('Coding'))
text = 'Coding'
if text in company:
    print('it contains')
else:
    print('it does not contain')

# 11 Replace the word coding in the string 'Coding For All' to Python.
print(company.replace('Coding','Python'))

# 12 Change "Python for Everyone" to "Python for All" using the replace method or other methods.
company1 = "Python for Everyone"
print(company1.replace('for Everyone','for All'))

# 13 Split the string 'Coding For All' using space as the separator (split()).
print(company.split())

# 14 "Facebook, Google, Microsoft, Apple, IBM, Oracle, Amazon" split the string at the comma.
big_comp = "Facebook, Google, Microsoft, Apple, IBM, Oracle, Amazon"
print(big_comp.split(', '))

# 15 What is the character at index 0 in the string Coding For All.
print(company[0])

# 16 What is the last index of the string Coding For All.
print(company[-1])
temp = len(company) - 1
print(company[temp])

# 17 What character is at index 10 in "Coding For All" string.
print(company[10]) 

# 18 Create an acronym or an abbreviation for the name 'Python For Everyone'.
company_split = company1.split()
result = ''.join(word[0] for word in company_split)
print(result.upper())

# 19 Create an acronym or an abbreviation for the name 'Coding For All'.
company_split1 = company.split()
result = ''.join(word[0] for word in company_split1)
print(result.upper())

# 20 Use index to determine the position of the first occurrence of C in Coding For All.
print(company.index('C'))

# 21 Use index to determine the position of the first occurrence of F in Coding For All.
print(company.index('F'))

# 22 Use rfind to determine the position of the last occurrence of l in Coding For All People.
company_people = "Coding For All People"
print(company_people.rfind('l'))

# 23 Use index or find to find the position of the first occurrence of the word 'because' in the 
# following sentence: 'You cannot end a sentence with because because because is a conjunction'
sentence = 'You cannot end a sentence with because because because is a conjunction'
print(sentence.index('because'))

# 24 Use rindex to find the position of the last occurrence of the word because in the 
# following sentence: 'You cannot end a sentence with because because because is a conjunction'
print(sentence.rfind('because'))

# 25 Slice out the phrase 'because because because' in the following sentence: 
# 'You cannot end a sentence with because because because is a conjunction'
start = sentence.index('because')
end = sentence.index('because') + len('because because because')
print(sentence[start:end])

# 26 Find the position of the first occurrence of the word 'because' in the following sentence: 
# 'You cannot end a sentence with because because because is a conjunction'
print(sentence.index('because'))

# 27 Slice out the phrase 'because because because' in the following sentence: 
# 'You cannot end a sentence with because because because is a conjunction'
start = sentence.index('because')
end = sentence.index('because') + len('because because because')
print(sentence[start:end])

# 28 Does 'Coding For All' start with a substring Coding?
print(company.startswith('Coding'))

# 29 Does 'Coding For All' end with a substring coding?
print(company.endswith('coding'))

# 30 '   Coding For All      '  , remove the left and right trailing spaces in the given string.
print(company.strip(' '))

# 31 Which one of the following variables return True when we use the method isidentifier():
# 30DaysOfPython
# thirty_days_of_python

print('30DaysOfPython'.isidentifier())
print('thirty_days_of_python'.isidentifier())

# 32 The following list contains the names of some of python libraries: 
# ['Django', 'Flask', 'Bottle', 'Pyramid', 'Falcon']. Join the list with a hash with space string.
lib_list = ['Django', 'Flask', 'Bottle', 'Pyramid', 'Falcon']
result = '# '.join(lib_list)
print(result)

# 33 Use the new line escape sequence to separate the following sentences.
print('I am enjoying this challenge.\nI just wonder what is next.')

# 34 Use a tab escape sequence to write the following lines.
print('Name\t\tAge\tCountry\tCity\nAsabeneh\t250\tFinland\tHelsinki')

# 35 Use the string formatting method to display the following:
radius = 10
area = 3.14 * radius ** 2
print("The area of a circle with radius %d is %d meters square." %(radius,area))

# 36 Make the following using string formatting methods:
a = 8
b = 6
print(f"{a} + {b} = {a+b}")
print(f"{a} - {b} = {a-b}")
print(f"{a} * {b} = {a*b}")
print(f"{a} / {b} = {(a/b):.2f}")
print(f"{a} % {b} = {a%b}")
print(f"{a} // {b} = {a//b}")
print(f"{a} ** {b} = {a**b}")

