# Day 07 — Sets

> **Today's Focus:** Working with Python sets – unique collections, set operations (union, intersection, difference, symmetric difference), and practical use cases for de-duplicating and comparing data.  
> **Author:** Luka Marinkovic  

## What I learned

Today I worked with **Python sets**, which are unordered collections of **unique** elements. Sets automatically remove duplicates and support powerful mathematical operations like union, intersection, difference, and symmetric difference. I practiced creating sets, checking membership, adding and removing elements, and using set methods to compare groups of values. I also used sets to analyze a list of ages and to count unique words in a sentence.

## Key Concepts Covered

### 1. Creating sets and basic properties

- I created **empty sets** using `st = set()` and populated sets using literal syntax:  
  ```python
  st = {'item1','item2','item3','item4'}
  fruits = {'banana', 'orange', 'mango', 'lemon'}
  ```
- I used `len(st)` and `len(fruits)` to get the number of elements.  
- Sets are **unordered** and **do not allow duplicates** – if the same element is added twice, it only appears once.

### 2. Membership checks and adding elements

- I checked if an element exists in a set using the `in` operator:  
  ```python
  'item1' in st      # True or False
  'mango' in fruits
  ```
- I added single items using `add()`:
  ```python
  st.add('item5')
  fruits.add('lime')
  ```
- I added **multiple items at once** using `update()`, which accepts any iterable:
  ```python
  st.update(['item6', 'item7', 'item8'])
  vegetables = ('tomato', 'potato', 'cabbage','onion', 'carrot')
  fruits.update(vegetables)
  ```

### 3. Removing, clearing, and deleting sets

- I removed specific items with `remove()`:
  ```python
  st.remove('item2')  # Raises an error if the item does not exist
  ```
- I used `pop()` to remove and return an arbitrary element (since sets are unordered):
  ```python
  fruits = {'banana', 'orange', 'mango', 'lemon'}
  removed_items = fruits.pop()
  ```
- I cleared all elements without deleting the variable using `clear()`:
  ```python
  fruits.clear()
  ```
- I deleted the entire set with `del st`, which removes the name from the current scope.

- I also learned the difference between **`remove` and `discard`**:
  - `remove(x)` → error if `x` is not in the set.  
  - `discard(x)` → does nothing if `x` is missing.  

### 4. Converting between lists and sets

- I converted a list with duplicates to a set to keep only **unique** items:
  ```python
  lst = ['item1', 'item2', 'item3', 'item4', 'item1']
  st = set(lst)  # 'item1' appears only once
  ```
- Later, I converted the `age` list to a set to compare lengths and see how many unique ages there are:
  ```python
  age = [22, 19, 24, 25, 26, 24, 25, 24]
  age_set = set(age)
  len(age)      # full list length
  len(age_set)  # number of unique ages
  ```

### 5. Union and intersection

- I used `union()` and `|` to **join** sets:
  ```python
  st1 = {'item1', 'item2', 'item3', 'item4'}
  st2 = {'item5', 'item6', 'item7', 'item8'}
  st3 = st1.union(st2)
  fruits | vegetables
  ```
- I also used `update()` to merge one set into another in place:
  ```python
  st1.update(st2)
  ```
- To find common elements, I used **intersection**:
  ```python
  st1.intersection(st2)
  st1 & st2
  name1 = {'l','u','k','a'}
  name2 = {'m','a','r','k','o'}
  common_letters = name1.intersection(name2)
  ```

### 6. Subset, superset, and disjoint sets

- I checked if one set is a **subset** of another using `issubset()`:
  ```python
  st2.issubset(st1)
  even_numbers.issubset(whole_numbers)
  ```
- I checked if one set is a **superset** of another using `issuperset()`:
  ```python
  st1.issuperset(st2)
  whole_numbers.issuperset(even_numbers)
  ```
- I used `isdisjoint()` to check if two sets share **no common elements**:
  ```python
  st1.isdisjoint(st2)
  even_numbers.isdisjoint(odd_numbers)
  ```

### 7. Difference and symmetric difference

- The **difference** between sets (`A - B`) returns items that are in `A` but not in `B`:
  ```python
  st1.difference(st2)
  st2.difference(st1)
  whole_numbers.difference(even_numbers)
  ```
- The **symmetric difference** (`A △ B`) returns items that are in either set but not in both:
  ```python
  whole_numbers.symmetric_difference(even_numbers)
  python = {'p', 'y', 't', 'h', 'o','n'}
  dragon = {'d', 'r', 'a', 'g', 'o','n'}
  python.symmetric_difference(dragon)
  ```

### 8. Practical exercises with real data

- With `it_companies`, I:
  - Found the length of the set.  
  - Added `'Twitter'` using `add()`.  
  - Added multiple companies like `'Tesla'`, `'Anthropic'`, `'OpenAI'` using `update()`.  
  - Removed companies using `remove()` and `discard()` and explained their difference.
- With sets `a` and `b`, I:
  - Joined them with `union()`.  
  - Found their intersection.  
  - Checked subset and disjoint relationships.  
  - Calculated the symmetric difference and finally deleted both sets with `del`.

### 9. Unique words in a sentence

- For the sentence:
  ```python
  sentence_string = 'I am a teacher and I love to inspire and teach people'
  ```
  I split it into words using `split()`:
  ```python
  sentence_list = sentence_string.split()
  ```
- Then I used a set to keep only **unique words**:
  ```python
  sentence_set = set(sentence_list)
  len(sentence_set)  # number of unique words
  ```
- This showed how sets are very useful for quick de-duplication and word frequency analysis.

## What I completed

I completed all **Day 7 set exercises**. I created and modified sets of IT companies, practiced adding single and multiple elements, and demonstrated the difference between `remove()` and `discard()`. I worked with numeric sets `a` and `b` to apply union, intersection, subset, superset, disjoint, and symmetric difference operations. I compared a list of ages with its set version to understand how duplicates affect length and confirmed that the list is longer because it allows repeated values. Finally, I used `split()` and `set()` to count how many unique words appear in a sentence, reinforcing how sets help in text analytics and de-duplication tasks.