# Sets

st = set()
st = {'item1','item2','item3','item4'}
fruits = {'banana', 'orange', 'mango', 'lemon'}
print(len(st))
print(len(fruits))

# Checking an item
print('item1' in st)
print('mango' in fruits)

# Adding items to a set
st.add('item5')
fruits.add('lime')
print(st)
print(fruits)

st.update(['item6', 'item7', 'item8'])
print(st)

vegetables = ('tomato', 'potato', 'cabbage','onion', 'carrot')
fruits.update(vegetables)
print(fruits)

# Removing items from a set
st.remove('item2')
print(st)
fruits = {'banana', 'orange', 'mango', 'lemon'}
removed_items = fruits.pop()
print(fruits)
print(removed_items)

# Clearing items in a set
fruits = {'banana', 'orange', 'mango', 'lemon'}
fruits.clear()

# Deleting a set
st = {'item1', 'item2', 'item3', 'item4'}
del st

# Converting a list to a set
lst = ['item1', 'item2', 'item3', 'item4', 'item1']
st = set(lst) # No duplicates

# Joining sets
st1 = {'item1', 'item2', 'item3', 'item4'}
st2 = {'item5', 'item6', 'item7', 'item8'}
st3 = st1.union(st2) # First way
print(st3)
# st4 = st1 + st2 is incorrect

fruits = {'banana', 'orange', 'mango', 'lemon'}
vegetables = {'tomato', 'potato', 'cabbage','onion', 'carrot'}
print(fruits | vegetables) # Second way

st1 = {'item1', 'item2', 'item3', 'item4'}
st2 = {'item5', 'item6', 'item7', 'item8'}
st1.update(st2)
print(st1)

# Finding intersection items
st1 = {'item1', 'item2', 'item3', 'item4'}
st2 = {'item1', 'item2'}
print(st1.intersection(st2)) 
print(st1 & st2)

name1 = {'l','u','k','a'}
name2 = {'m','a','r','k','o'}
print(name1.intersection(name2))

# Checking subset and superset
st1 = {'item1', 'item2', 'item3', 'item4'}
st2 = {'item1', 'item2'}
print(st2.issubset(st1))
print(st1.issuperset(st2))

whole_numbers = {0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10}
even_numbers = {0, 2, 4, 6, 8, 10}
print(even_numbers.issubset(whole_numbers))
print(whole_numbers.issuperset(even_numbers))

# Checking the difference between two sets
st1 = {'item1', 'item2', 'item3', 'item4'}
st2 = {'item2', 'item3'}
print(st1.difference(st2))
print(st2.difference(st1)) # st2 - st1 is empty

whole_numbers = {0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10}
even_numbers = {0, 2, 4, 6, 8, 10}
print(whole_numbers.difference(even_numbers))

# Finding symmetric difference between two sets
# It means (A\B) ∪ (B\A) - returns items that are in either set but not in both

whole_numbers = {0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10}
even_numbers = {0, 2, 4, 6, 8, 10}
whole_numbers.symmetric_difference(even_numbers)

python = {'p', 'y', 't', 'h', 'o','n'}
dragon = {'d', 'r', 'a', 'g', 'o','n'}
print(python.symmetric_difference(dragon))

# Disjoint sets - if they have no common items, the result is True
st1 = {'item1', 'item2', 'item3', 'item4'}
st2 = {'item2', 'item3'}
print(st1.isdisjoint(st2))

even_numbers = {0, 2, 4 ,6, 8}
odd_numbers = {1, 3, 5, 7, 9}
print(even_numbers.isdisjoint(odd_numbers))

# Exercises: Level 1

# Sets
it_companies = {'Facebook', 'Google', 'Microsoft', 'Apple', 'IBM', 'Oracle', 'Amazon'}
a = {19, 22, 24, 20, 25, 26}
b = {19, 22, 20, 25, 26, 24, 28, 27}
age = [22, 19, 24, 25, 26, 24, 25, 24]

# 1 Find the length of the set it_companies
print(len(it_companies))

# 2 Add 'Twitter' to it_companies
it_companies.add('Twitter')
print(it_companies)

# 3 Insert multiple IT companies at once into the set it_companies
it_companies.update(['Tesla','Anthropic','OpenAI'])
print(it_companies)

# 4 Remove one of the companies from the set it_companies
it_companies.remove('Twitter')
print(it_companies)

# 5 What is the difference between remove and discard
# remove - removes the given item from the set and raises an error if the item does not exist
# discard - removes the given item but does not raise an error if the item is not present
it_companies.discard('OpenAI')
print(it_companies)

# Exercises: Level 2

# 1 Join A and B
print(a.union(b))

# 2 Find A intersection B
print(a.intersection(b))

# 3 Is A a subset of B
print(a.issubset(b))

# 4 Are A and B disjoint sets
print(a.isdisjoint(b))

# 5 Join A with B and B with A
print(a.union(b))
print(b.union(a))

# 6 What is the symmetric difference between A and B
print(a.symmetric_difference(b))

# 7 Delete the sets completely
del a,b

# Exercises: Level 3

# 1 Convert the ages to a set and compare the length of the list and the set. Which one is bigger?
print(len(age))
age_set = set(age)
print(len(age_set))
# The list is bigger because it can contain duplicates

# 2 Explain the difference between the following data types: string, list, tuple and set
# string - ordered sequence of characters - immutable
# list - ordered collection of elements - mutable
# tuple - ordered collection of elements - immutable
# set - unordered collection of unique elements - mutable

# 3 I am a teacher and I love to inspire and teach people. 
# How many unique words have been used in the sentence?
# Use the split method and a set to get the unique words.

sentence_string = 'I am a teacher and I love to inspire and teach people'
sentence_list = sentence_string.split()
print(sentence_list)

sentence_set = set(sentence_list)
print(sentence_set)

print(len(sentence_set))
# The answer is 10