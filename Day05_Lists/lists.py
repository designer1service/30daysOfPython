# Lists

lst = list()

empty_lst = list()
print(len(empty_lst))

lst = []
empty_lst1 = []
print(len(empty_lst1))

fruits = ['banana', 'orange', 'mango', 'lemon']
vegetables = ['Tomato', 'Potato', 'Cabbage','Onion', 'Carrot']    
animal_products = ['milk', 'meat', 'butter', 'yoghurt']
web_techs = ['HTML', 'CSS', 'JS', 'React','Redux', 'Node', 'MongDB']
countries = ['Finland', 'Estonia', 'Denmark', 'Sweden', 'Norway']

print('Fruits:', fruits)
print('Number of fruits:', len(fruits))
print('Vegetables:', vegetables)
print('Number of vegetables:', len(vegetables))
print('Animal products:',animal_products)
print('Number of animal products:', len(animal_products))
print('Web technologies:', web_techs)
print('Number of web technologies:', len(web_techs))
print('Countries:', countries)
print('Number of countries:', len(countries))

lst = ['luka',250,True, {'country':'croatia','city':'zagreb'}]

# Accessing List Items Using Positive Indexing

fruits = ['banana', 'orange', 'mango', 'lemon']
first_fruit = fruits[0]
print(first_fruit)
second_fruit = fruits[1]
print(second_fruit)

last_fruit = fruits[3]
print(last_fruit)

last_fruit_index = len(fruits) - 1
print(fruits[last_fruit_index])

# Accessing List Items Using Positive Indexing

fruits = ['banana', 'orange', 'mango', 'lemon']
first_fruit = fruits[-4]
print(first_fruit)
last_fruit = fruits[-1]
print(last_fruit)

# Unpacking List Items

lst = ['item1','item2','item3', 'item4', 'item5']
first_item, second_item, third_item, *rest = lst
print(first_item)
print(second_item)
print(third_item)
print(rest)

first,second,third,*rest, tenth = [1,2,3,4,5,6,7,8,9,10]
print(first)
print(second)
print(third)
print(rest)
print(tenth)

countries = ['Germany', 'France','Belgium','Sweden','Denmark','Finland','Norway','Iceland','Estonia']
gr, fr, bg, sw, *scandic, es = countries
print(gr) 
print(fr)
print(bg)
print(sw)
print(scandic)
print(es)

# Slicing items from a List

fruits = ['banana', 'orange', 'mango', 'lemon']
all_fruits = fruits[0:4] # all_fruits = fruits[0:] it goes to the end
print(all_fruits)
orange_and_mango  = fruits[1:3]
print(orange_and_mango)
orange_mango_lemon = fruits[1:4]
print(orange_mango_lemon)
reverse_fruits = fruits[::-1]
print(reverse_fruits)

# Modifying Lists
fruits = ['banana', 'orange', 'mango', 'lemon']
fruits[0] = 'avocado'
print(fruits)
fruits[1] = 'apple'
print(fruits)
last_fruit_index = len(fruits) - 1
fruits[last_fruit_index] = 'lime'
print(fruits)

# Checking Items in a List
fruits = ['banana', 'orange', 'mango', 'lemon']
does_exist = 'banana' in fruits
print(does_exist)

# Adding Items to a List
fruits = ['banana', 'orange', 'mango', 'lemon']
fruits.insert(2,'apple')
print(fruits)
fruits.insert(3,'lime')
print(fruits)

# Removing Items froma a List
fruits = ['banana', 'orange', 'mango', 'lemon']
fruits.remove('banana')
print(fruits)
fruits.remove('lemon')
print(fruits)

# Removing Items Using Pop
fruits = ['banana', 'orange', 'mango', 'lemon']
fruits.pop()
print(fruits)
fruits.pop(0)
print(fruits)

# Removing Items Using Del
fruits = ['banana', 'orange', 'mango', 'lemon', 'kiwi', 'lime']
del fruits[0]
print(fruits)
del fruits[1]
print(fruits)
del fruits[2:4]
print(fruits)

# Clearing List Items
fruits = ['banana', 'orange', 'mango', 'lemon']
fruits.clear()
print(fruits)

# Copying a List
fruits = ['banana', 'orange', 'mango', 'lemon']
fruits2 = fruits.copy()
print(fruits2)

# Joining Lists
positive_numbers = [1,2,3,4,5]
zero = [0]
negative_numbers = [-5,-4,-3,-2,-1]
integers = negative_numbers + zero + positive_numbers
print(integers)

list1 = [0,1,2]
list2 = [3,4,5]
list1.extend(list2)
print(list1)

# Counting Items in a List
fruits = ['banana', 'orange', 'mango', 'lemon','orange']
print(fruits.count('orange'))
ages = [22, 19, 24, 25, 26, 24, 25, 24]
print(ages.count(24)) 

# Finding Index of an Item
fruits = ['banana', 'orange', 'mango', 'lemon']
print(fruits.index('banana'))
ages = [22, 19, 24, 25, 26, 24, 25, 24]
print(ages.index(25)) 

# Reversing a List
fruits = ['banana', 'orange', 'mango', 'lemon']
fruits.reverse()
print(fruits)

# Sorting List Items
fruits = ['banana', 'orange', 'mango', 'lemon']
fruits.sort() # alphabetical order
print(fruits) 
fruits.sort(reverse= True) # reversed
print(fruits) 

ages = [22, 19, 24, 25, 26, 24, 25, 24]
ages.sort()
print(ages)
ages.sort(reverse=True)
print(ages)

# sorted is not modifying the original
fruits = ['banana', 'orange', 'mango', 'lemon']
print(sorted(fruits))   # ['banana', 'lemon', 'mango', 'orange']
fruits = sorted(fruits,reverse=True)
print(fruits)     # ['orange', 'mango', 'lemon', 'banana']

# Exercises: Day 5

# 1 Declare an empty list
lst = []
lst = list()

# 2 Declare a list with more than 5 items
components = ['ram','hdd','cpu','gpu','psu']

# 3 Find the length of your list
print(len(components))

# 4 Get the first item, the middle item and the last item of the list
print(components[0])
print(components[2])
last_index = len(components) - 1
print(components[last_index])

# 5 Declare a list called mixed_data_types, put your(name, age, height, marital status, address)
mixed_data_types = ['luka', 21 , 180 , False , 'fake adress 101']

# 6 Declare a list variable named it_companies and assign initial values Facebook, Google, Microsoft, Apple, IBM, Oracle and Amazon.
companies = ["Facebook", "Google", "Microsoft", "Apple", "IBM", "Oracle", "Amazon"]

# 7 Print the list using print()
print(companies)

# 8 Print the number of companies in the list
print(len(companies))

# 9 Print the first, middle and last company
print(companies[0])
print(companies[3])
last_index = len(companies) - 1
print(companies[last_index])

# 10 Print the list after modifying one of the companies
companies[0] = 'zivotna firma'
print(companies)

# 11 Add an IT company to it_companies
it_companies = []
it_companies.insert(1,'OPENAI')
print(it_companies)

# 12 Insert an IT company in the middle of the companies list
companies.insert(3,it_companies[0])
print(companies)

# 13 Change one of the it_companies names to uppercase (IBM excluded!)
companies[0] = companies[0].upper()
print(companies)

# 14 Join the it_companies with a string '#;  '
result = '#; '.join(companies)
print(result)

# 15 Check if a certain company exists in the it_companies list.
does_exist = 'OPENAI' in companies
print(does_exist)

# 16 Sort the list using sort() method
companies.sort(reverse=False)
print(companies)

# 17 Reverse the list in descending order using reverse() method
companies.sort(reverse=True)
print(companies)

# 18 Slice out the first 3 companies from the list
print(companies[0:4])

# 19 Slice out the last 3 companies from the list
print(companies[5:])

# 20 Slice out the middle IT company or companies from the list
print(companies[3])

# 21 Remove the first IT company from the list
companies.pop(0)
print(companies)

# 22 Remove the middle IT company or companies from the list
companies.pop(3)
print(companies)

# 23 Remove the last IT company from the list
last_index = len(companies) - 1
companies.pop(last_index)
print(companies)

# 24 Remove all IT companies from the list
companies.clear()
print(companies)

# 25 Destroy the IT companies list
del it_companies

# 26 Join the following lists:
front_end = ['HTML', 'CSS', 'JS', 'React', 'Redux']
back_end = ['Node','Express', 'MongoDB']
stack = front_end + back_end

# 27 After joining the lists in question 26. Copy the joined list and assign it to a variable full_stack, then insert Python and SQL after Redux.
full_stack = stack.copy()
full_stack.insert(5,'Python')
full_stack.insert(6,'SQL')
print(full_stack)

# Exercises: Level 2

# The following is a list of 10 students ages:
ages = [19, 22, 19, 24, 20, 25, 26, 24, 25, 24]

# Sort the list and find the min and max age
ages.sort()
last_index_ages = len(ages) - 1
print(f'min {ages[0]} max {ages[last_index_ages]}')

# Add the min age and the max age again to the list
ages.insert(0,min(ages))
last_index_ages = len(ages) - 1
ages.insert(last_index_ages,max(ages))
print(ages)

# Find the median age (one middle item or two middle items divided by two)
print(len(ages))
median = (ages[6] + ages[7]) / 2
print(median)

# Find the average age (sum of all items divided by their number )
average = sum(ages) / len(ages)
print(average)

# Find the range of the ages (max minus min)
age_range = max(ages) - min(ages)
print(age_range)

# Compare the value of (min - average) and (max - average), use abs() method
print( abs(min(ages) - average) > abs(max(ages) - average)) 

# Find the middle country(ies) in the countries list
countries = [] # Here list is empty because the real one is git and it is to long for it to be here
middle_index = len(countries) // 2
print(countries[middle_index])

# Divide the countries list into two equal lists if it is even if not one more country for the first half.
middle_index = (len(countries) + 1) // 2 
first_part = countries[:middle_index]
second_part = countries[middle_index:]
print(first_part)
print('\n')
print(second_part)

# ['China', 'Russia', 'USA', 'Finland', 'Sweden', 'Norway', 'Denmark']. Unpack the first three countries and the rest as scandic countries.
specific_countries = ['China', 'Russia', 'USA', 'Finland', 'Sweden', 'Norway', 'Denmark']
first_three, rest = specific_countries[:3], specific_countries[3:]
print(first_three)
print(rest)

