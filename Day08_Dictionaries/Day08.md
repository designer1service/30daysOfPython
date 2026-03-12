# Day 08 — Dictionaries

> **Today's Focus:** Creating and working with Python dictionaries – key–value storage, nested structures, safe access, updating, and converting dictionaries to other formats.  
> **Author:** Luka Marinkovic  

## What I learned

Today I worked with **Python dictionaries** as key–value mappings, similar to small structured “objects” for storing related data. I practiced creating empty and populated dictionaries, accessing values by key, dealing with missing keys safely using `.get()`, and modifying existing entries. I also used nested dictionaries and lists inside dictionaries, removed items using different methods, and converted dictionaries into lists of keys, values, and `(key, value)` tuples. Finally, I applied these concepts to real examples like a `dog` and a `student` dictionary.

## Key Concepts Covered

### 1. Creating dictionaries and basic structure

- I created an **empty dictionary** with `empty_dict = {}` and a simple one with predefined keys and values:
  ```python
  dct = {'key1':'value1','key2':'value2','key3':'value3'}
  ```
- I built a more complex `person` dictionary with different value types:
  - strings (`'first_name'`), integers (`'age'`), booleans (`'isMarried'`),  
  - a list for `'skills'`,  
  - and a nested dictionary for `'adress'` (with `street` and `zipcode`).  
- I used `len(dct)` and `len(person)` to get the number of key–value pairs in each dictionary.

### 2. Accessing values and nested data

- I accessed values by **key** using square brackets:
  ```python
  dct['key1']
  dct['key3']
  person['age']
  person['skills']
  person['adress']['street']
  ```
- I saw that accessing a non‑existent key like `person['city']` would raise a `KeyError`.  
- To avoid this, I used `.get()`:
  ```python
  person.get('first_name')  # returns 'Luka'
  person.get('city')        # returns None, no error
  ```
- This is useful when I’m not sure if a key exists.

### 3. Adding and modifying dictionary entries

- I added new key–value pairs by simple assignment:
  ```python
  dct['key4'] = 'value4'
  person['job_title'] = 'None'
  ```
- I updated an existing key to a new value:
  ```python
  dct['key1'] = 'value-one'
  ```
- I combined dictionaries with nested structures and lists:
  - Appended a new skill directly to the `skills` list inside `person`:
    ```python
    person['skills'].append('C')
    ```
  - Added a new nested key `city` inside `person['adress']`:
    ```python
    person['adress']['city'] = 'Osijek'
    ```

### 4. Checking for keys

- I used the `in` operator to test if a key exists:
  ```python
  'key1' in dct     # True
  'key11' in dct    # False
  ```
- This helps avoid errors and is often used before accessing or deleting a key.

### 5. Removing items and clearing dictionaries

- I removed specific keys using:
  ```python
  dct.pop('key1')     # removes the key and returns its value
  dct.popitem()       # removes the last inserted key–value pair
  del dct['key2']     # deletes a key without returning its value
  ```
- I did similar operations on `person`, including:
  ```python
  person.pop('first_name')
  person.popitem()
  del person['isMarried']
  ```
- I cleared all items from a dictionary using:
  ```python
  dct.clear()   # dictionary becomes {}
  ```
- I removed the dictionary variable entirely with:
  ```python
  del dct
  ```

### 6. Viewing items, keys, and values

- I used `.items()` to get all key–value pairs:
  ```python
  dct.items()          # dict_items([...])
  list(dct.items())    # list of (key, value) tuples
  ```
- I used `.keys()` to get a view of all keys:
  ```python
  dct.keys()
  ```
- I used `.values()` to get all values:
  ```python
  dct.values()
  ```
- These views can be converted to lists when needed, especially for iteration or exporting.

### 7. Copying dictionaries

- I made a **shallow copy** of a dictionary with:
  ```python
  dct_copy = dct.copy()
  ```
- This creates a new dictionary with the same keys and values, independent from the original at the top level.

### 8. Practical exercises with `dog` and `student`

- For **`dog`**:
  - I first created an empty dictionary and then replaced it with:
    ```python
    dog = {'color':'brown', 'breed':'brown_dog', 'legs':4, 'age':21}
    ```
- For **`student`**:
  - I created a structured dictionary:
    ```python
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
    ```
  - I checked the number of fields with `len(student)`.  
  - I accessed `student['skills']` and confirmed its type is `list`.  
  - I extended the skills with more items:
    ```python
    student['skills'].extend(['C','Python'])
    ```
  - I listed all keys with `student.keys()` and all values with `student.values()`.  
  - I converted the whole dictionary to a list of tuples using `student.items()`.  
  - I removed one field (`city`) using `student.pop('city')`.  
  - Finally, I deleted the `dog` dictionary entirely with `del dog`.

## What I completed

I completed all **Day 8 dictionary exercises**. I created empty and populated dictionaries, then accessed and modified values using both direct indexing and `.get()`. I practiced working with nested data and lists inside dictionaries, updated keys and values, and safely checked for the presence of keys using `in`. I removed entries using `pop()`, `popitem()`, and `del`, cleared dictionaries with `clear()`, and converted dictionaries into lists of key–value tuples, keys, and values.  

Using the `dog` and `student` dictionaries, I simulated real-world structured data, extended skill lists, inspected dictionary structure, and removed specific fields when needed. This solidified my understanding of dictionaries as one of Python’s most important data structures for modeling and organizing related information.