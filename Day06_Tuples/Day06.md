# Day 06 — Tuples

> **Today's Focus:** Deep dive into immutable Python tuples – creation, indexing, slicing, conversion to lists for modification, joining, and membership testing with practical family and food examples.  
> **Author:** Luka Marinkovic  

## What I learned

Today I focused on **Python tuples** as immutable sequences that cannot be changed after creation. I practiced creating empty and populated tuples, accessing elements with positive/negative indexing, slicing operations identical to lists, and converting tuples ↔ lists when modification is needed. I learned tuple concatenation with `+`, complete deletion with `del`, and fast membership checks using `in`. The key insight is that tuples are perfect for **fixed data** like coordinates or categories, while lists are for data that changes.

## Key Concepts Covered

### 1. Creating tuples and basic operations

- Created **empty tuples** using `empty_tuple = ()` or `empty_tuple = tuple()`, both with `len() == 0`.  
- Built **simple tuples** like `fruits = ('banana','orange','mango','lemon')` and **mixed tuples** like `tpl = ('item1','item2','item3')`.  
- Used `len(tpl)` to confirm tuple length works exactly like lists.

### 2. Indexing and slicing (identical to lists)

- **Positive indexing**: `tpl[0]`, `tpl[1]`, `tpl[len(tpl)-1]` for first, middle, last elements.  
- **Negative indexing**: `tpl[-3]`, `tpl[-2]`, `tpl[-1]` to access from the end.  
- **Slicing**: `tpl[0:4]`, `tpl[1:3]` extracts subsets, `all_items = tpl[0:]` grabs everything.  
- For `food_stuff_lt` (list version), calculated **middle index** with `len() // 2` and sliced middle item(s) based on even/odd length.

### 3. Immutability workaround: tuple ↔ list conversion

- **Tuples cannot be modified** – no `insert()`, `append()`, `remove()`, `pop()`.  
- **Solution**: Convert to list, modify, convert back:  
  ```python
  fruits = ('banana','orange','mango','lemon')
  fruits = list(fruits)      # tuple → list
  fruits.insert(0,'Lime')
  fruits.pop(0)
  # fruits is now a list, not tuple
  ```
- For `family_members`:  
  ```python
  siblings = list(siblings)  # Convert to modify
  siblings.insert(0,'Jelena')  # Mother
  siblings.insert(0,'Darijo')  # Father
  family_members = tuple(siblings)  # Back to tuple
  ```

### 4. Joining tuples with `+`

- **Concatenation** creates new tuples:  
  - `tpl3 = tpl1 + tpl2` joins `('item1', 'item2', 'item3')` + `('item4', 'item5', 'item6')`.  
  - `siblings = brothers + sisters`.  
  - `food_stuff_tp = fruits + vegetables + animal_products` (12 items total).  
- Original tuples remain unchanged.

### 5. Deleting tuples completely

- `del tpl1` removes the tuple entirely from memory.  
- For `food_stuff_tp`: converted to list first, then `del food_stuff_tp`.

### 6. Membership testing

- `'item2' in tpl` and `'Estonia' in nordic_countries` return Boolean.  
- **Nordic check**: `'Iceland' in nordic_countries` → `True`, `'Estonia'` → `False`.

### 7. Unpacking and advanced slicing

- Unpacked `family_members`: `parents, siblings1 = family_members[0:2], family_members[2:]`.  
- From `food_stuff_lt`: **first 3** (`[0:3]`), **last 3** (`[-3:]`), **middle** (conditional even/odd logic).

## What I completed

I completed all **Day 6 tuple exercises**. Created empty tuples and family tuples (`brothers = ('Roko','Marko','Jan')`, `sisters = ('Marija','Lana','Ana')`), joined into `siblings`, counted 6 siblings with `len(siblings)`. Converted `siblings` → list to insert parents → back to tuple for `family_members`.

Built `food_stuff_tp` (fruits + vegetables + animal_products), converted to `food_stuff_lt`, sliced **middle items** (handling even/odd length), extracted **first 3** and **last 3**, then deleted original tuple. Validated Nordic countries: confirmed 'Iceland' is Nordic, 'Estonia' is not.

