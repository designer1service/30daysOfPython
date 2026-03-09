# Day 05 — Lists & List Methods

> **Today's Focus:** Creating, accessing, modifying, slicing, and analyzing lists in Python using real examples with strings, numbers, and mixed data.  
> **Author:** Luka Marinkovic  

## What I learned

Today I worked with **Python lists** as flexible, mutable collections. I practiced creating empty and non‑empty lists, accessing elements using both positive and negative indexing, and unpacking list items into multiple variables. I learned how to slice lists, check membership, and use different ways to add and remove elements. I also applied built‑in list methods to count, search, reverse, and sort elements, and finished with basic statistical operations on a list of ages and some practical tasks with a long list of countries.

## Key Concepts Covered

### 1. Creating lists and basic properties

- I created **empty lists** in two ways: `lst = []` and `lst = list()`, and used `len(lst)` to check their length.  
- I worked with **homogeneous lists** like `fruits`, `components`, and `ages`, and **heterogeneous lists** like `mixed_data_types = ['luka', 21, 180, False, 'fake adress 101']`.  
- I reinforced that the length of a list is the number of elements it contains, and that the last valid index is `len(lst) - 1`.

### 2. Indexing, negative indices, and slicing

- Using **positive indexing** (`fruits[0]`, `fruits[1]`, `fruits[3]`) I accessed the first, middle, and last elements of several lists.  
- With **negative indexing** (`fruits[-1]`, `fruits[-4]`) I accessed items from the end of the list without manually computing `len(lst) - 1`.  
- I practiced **slicing** with expressions like `fruits[0:4]`, `fruits[1:3]`, and `fruits[1:4]` to extract subsets of elements, and used `fruits[::-1]` to create a reversed view of the list.  
- For the long `countries` list I used integer division (`len(countries) // 2`) to find the **middle country**, and `(len(countries) + 1) // 2` to split the list into two halves where the first half gets one extra country when the length is odd.

### 3. Unpacking list items

- I used **unpacking** to assign elements of a list into multiple variables, for example:  
  - `first_item, second_item, third_item, *rest = lst` to capture the first three items and group all remaining items in `rest`.  
  - `first, second, third, *rest, tenth = [1,2,3,4,5,6,7,8,9,10]`, where `rest` holds all elements between the third and last.  
- With the `countries` list, I unpacked the first four countries into separate variables and grouped the Scandinavian countries into `*scandic`, which is helpful when you care about some fixed items and treat the rest as a group.  
- In the task with `specific_countries = ['China', 'Russia', 'USA', 'Finland', 'Sweden', 'Norway', 'Denmark']`, I logically separated the first three countries and the remaining “Scandic” countries using slicing: `specific_countries[:3]` and `specific_countries[3:]`.

### 4. Checking and modifying elements in a list

- I updated elements at specific positions, for example:
  - `fruits[0] = 'avocado'`, changing the first element,  
  - changing the middle element directly by index, and  
  - updating the last element using `last_index = len(fruits) - 1` and `fruits[last_index] = 'lime'`.  
- I used the `in` operator to check membership, such as `'banana' in fruits` or `'OPENAI' in companies`, which returns a Boolean and is useful for validation before modifying a list.  
- With the `companies` list I modified individual company names, inserted a new company in the middle, and converted one name to **uppercase** using `companies[0] = companies[0].upper()`.

### 5. Adding, inserting, and joining lists

- I added single elements at specific positions using `insert(index, value)`, for example:
  - `fruits.insert(2, 'apple')` and `fruits.insert(3, 'lime')` to place new items in the middle,  
  - inserting `'OPENAI'` into an initially empty `it_companies` list.  
- I concatenated several lists with the `+` operator:  
  - `integers = negative_numbers + zero + positive_numbers` to build a continuous range from negative to positive integers.  
- I used `extend()` to append the contents of one list to another:
  - `list1.extend(list2)` to turn `[0,1,2]` and `[3,4,5]` into `[0,1,2,3,4,5]`.  
- With `front_end` and `back_end` I created a `stack` list by joining them, then copied it into `full_stack` and inserted `'Python'` and `'SQL'` immediately after `'Redux'` using `insert(5, 'Python')` and `insert(6, 'SQL')`.  

### 6. Removing elements and clearing lists

- I removed elements **by value** using `remove('banana')`, which deletes the first occurrence of that value from the list.  
- I used `pop()` both without arguments (`fruits.pop()`) to remove the last element and with an index (`fruits.pop(0)`, `companies.pop(3)`) to remove specific positions.  
- With the `del` statement I deleted single elements and slices (`del fruits[0]`, `del fruits[2:4]`), and finally destroyed an entire list using `del it_companies`.  
- I completely emptied a list while keeping the variable using `companies.clear()`, which is useful when you want to reuse the same list object.

### 7. Counting, searching, reversing, and sorting

- I used `count()` to see how many times a value appears in a list, for example `fruits.count('orange')` and `ages.count(24)`.  
- With `index()` I found the position of the first occurrence of a given value, such as `fruits.index('banana')` and `ages.index(25)`, which is helpful before modifying or removing by index.  
- I reversed lists in place using `fruits.reverse()`, which flips the order of all elements.  
- I sorted lists with `sort()`:
  - `fruits.sort()` for alphabetical order and `fruits.sort(reverse=True)` for reverse alphabetical order,  
  - `ages.sort()` and `ages.sort(reverse=True)` to get ascending and descending age lists.  
- I compared `sort()` and `sorted()`:
  - `sort()` modifies the original list in place,  
  - `sorted(fruits)` returns a **new** sorted list and leaves the original unchanged unless I assign it back, as in `fruits = sorted(fruits, reverse=True)`.

### 8. Working with numeric lists and simple statistics

- On the `ages` list I performed several basic statistical operations:
  - After sorting, I found the **minimum** and **maximum** both via indexing and via `min()` and `max()`.  
  - I added the min and max ages again into the list using `insert()`.  
  - I computed the **median age** by averaging the two central values once I knew the list length.  
  - I calculated the **average age** using `average = sum(ages) / len(ages)`.  
  - I found the **range** of ages as `max(ages) - min(ages)`.  
  - I compared how far the minimum and maximum are from the average using `abs(min(ages) - average)` and `abs(max(ages) - average)`, which is a simple way to understand how balanced the data is around the mean.

### 9. Practical tasks with the countries list

- I used a long sorted list of country names to practice real‑world list operations:
  - Found the **middle country** using `middle_index = len(countries) // 2` and `countries[middle_index]`.  
  - Split the list into two nearly equal parts using:
    - `middle_index = (len(countries) + 1) // 2`,  
    - `first_part = countries[:middle_index]`,  
    - `second_part = countries[middle_index:]`,  
    so that the first half gets one extra element when the total number is odd.  
- For the smaller `specific_countries` list, I separated the first three countries and the remaining Scandinavian ones by slicing and printed both parts.

## What I completed

I completed all **Day 5 list exercises**. I declared empty and non‑empty lists, accessed the first, middle, and last elements, and created a mixed‑type list to show that Python lists can hold many different data types at once. I built and modified an `it_companies` list, inserted new companies at the beginning, middle, and end, converted one of the names to uppercase, joined all company names into a single formatted string using `'#; '.join(companies)`, and checked if a specific company existed with the `in` operator.  

I also combined multiple lists of technologies into a `full_stack`, inserted `'Python'` and `'SQL'` in the correct position, and then moved on to numerical analysis with the `ages` list, where I practiced sorting, computing min, max, median, average, range, and comparing distances from the mean using `abs()`. Finally, I applied these list techniques to a large `countries` dataset by finding the middle country, splitting the list into two balanced halves, and logically separating the first three countries from the Scandinavian ones.  
