# Tuple
empty_tuple = ()
empty_tuple = tuple()

tpl = ('item1','item2','item3')
fruits = ('banana','orange','mango','lemon')

print(len(tpl))

# Accessing Tuple Items

tpl = ('item1','item2','item3')
first_item = tpl[0]
second_item = tpl[1]
last_index = len(tpl) - 1
last_item = tpl[last_index]

first_item = tpl[-3]
second_item = tpl[-2]

# Slicing Tuples

tpl = ('item1','item2','item3','item4')
all_items = tpl[0:4] # or [0:] 
middle_two = tpl[1:3]
# can be done with negative indexing 


# Changing Tuples to Lists

fruits = ('banana','orange','mango','lemon')
fruits = list(fruits)
fruits.insert(0,'Lime')
print(fruits)
fruits.pop(0)
print(fruits)

# Checking an Item in a Tuple
tpl = ('item1', 'item2', 'item3','item4')
print('item2' in tpl)

# Joining Tuples
tpl1 = ('item1', 'item2', 'item3')
tpl2 = ('item4', 'item5', 'item6')
tpl3 = tpl1 + tpl2
print(tpl3)

fruits = ('banana', 'orange', 'mango', 'lemon')
vegetables = ('Tomato', 'Potato', 'Cabbage','Onion', 'Carrot')
fruits_and_vegetables = fruits + vegetables
print(fruits_and_vegetables)

# Deleting Tuples
tpl1 = ('item1', 'item2', 'item3')
del tpl1

# Exercises: Level 1

# 1 Create an empty tuple
empty_tuple = ()

# 2 Create a tuple containing names of your sisters and your brothers (imaginary siblings are fine)
brothers = ('Roko','Marko','Jan')
sisters = ('Marija','Lana','Ana')

# 3 Join brothers and sisters tuples and assign it to siblings
siblings = brothers + sisters
print(siblings)

# 4 How many siblings do you have?
print(len(siblings))

# 5 Modify the siblings tuple and add the name of your father and mother and assign it to family_members
# cannot be done without coverting it to list

siblings = list(siblings)
siblings.insert(0,'Jelena')
siblings.insert(0,'Darijo')
family_members = tuple(siblings)
print(family_members)

# Exercises: Level 2

# 1 Unpack siblings and parents from family_members
parents, siblings1 = family_members[0:2] , family_members[2:]
print(parents)
print(siblings1)

# 2 Create fruits, vegetables and animal products tuples. 
# Join the three tuples and assign it to a variable called food_stuff_tp.

fruits = ('banana', 'orange', 'mango', 'lemon')
vegetables = ('Tomato', 'Potato', 'Cabbage','Onion', 'Carrot')
animal_products = ('Eggs','Milk','Meat','Seafood')
food_stuff_tp = fruits + vegetables + animal_products

# 3 Change the about food_stuff_tp tuple to a food_stuff_lt list
food_stuff_tp = list(food_stuff_tp)

# 4 Slice out the middle item or items from the food_stuff_tp tuple or food_stuff_lt list.
middle_index = len(food_stuff_tp) // 2
print(len(food_stuff_tp))
if len(food_stuff_tp) % 2 == 0:
    print(food_stuff_tp[middle_index - 1 : middle_index + 1])
else:
    print(food_stuff_tp[middle_index : middle_index + 1])

# 5 Slice out the first three items and the last three items from food_stuff_lt list
first_three = food_stuff_tp[0:3]
last_three = food_stuff_tp[-3:]
print(first_three)
print(last_three)

# 6 Delete the food_stuff_tp tuple completely
del food_stuff_tp

# 7 Check if an item exists in tuple:
# Check if 'Estonia' is a nordic country
# Check if 'Iceland' is a nordic country
nordic_countries = ('Denmark', 'Finland','Iceland', 'Norway', 'Sweden')

print('Estonia' in nordic_countries)
print('Iceland' in nordic_countries)

